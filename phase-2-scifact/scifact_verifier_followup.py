"""Compare SciFact review rankings on fresh development claims."""
import argparse
from collections import Counter
import getpass
import json
import os
from pathlib import Path
from types import SimpleNamespace

import scifact_webui_pilot as pilot
from scifact_retrieval_pilot import index_documents, load_data, retrieve

VERIFIER = ("Assess whether the supplied evidence supports, contradicts, or is insufficient "
            "for the claim. Check direction, population and endpoint. Assess each citation in context.")
TUNING_IDS = {100, 598, 800}


def compare(rows, budget):
    output = {}
    for name in ("plain", "rubric", "same_cited", "same_full", "other_cited", "other_full"):
        def priority(row):
            calls = row["calls"]
            base = calls["plain" if name == "plain" else "rubric"].get("parsed", {})
            if not base:
                return (-2, row["claim_id"])
            if base["verdict"] != "SUPPORT":
                return (1, row["claim_id"])
            result = calls[name].get("parsed", {})
            return (result.get("probabilities", {}).get("SUPPORT", -1), row["claim_id"])
        reviewed = {row["claim_id"] for row in sorted(rows, key=priority)[:budget]}
        auto = [r for r in rows if r["claim_id"] not in reviewed]
        base = "plain" if name == "plain" else "rubric"
        counts = Counter((r["gold"], r["calls"][base].get("parsed", {}).get("verdict", "UNRESOLVED"))
                         for r in auto)
        output[name] = {"reviewed_ids": sorted(reviewed),
                        "false_accepts": sum(counts[label, "SUPPORT"] for label in pilot.LABELS[1:]),
                        "gold_non_support": sum(r["gold"] != "SUPPORT" for r in rows),
                        "true_accepts": counts["SUPPORT", "SUPPORT"],
                        "unresolved_outside_budget": sum(counts[label, "UNRESOLVED"] for label in pilot.LABELS)}
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("--pilot", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--verifier-model", required=True)
    parser.add_argument("--per-label", type=int, default=5)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    judge = "openai/gpt-4.1-mini"
    if args.verifier_model == judge or args.per_label < 1:
        parser.error("provide a distinct verifier and a positive sample size")
    previous = [json.loads(line) for line in args.pilot.read_text(encoding="utf-8").splitlines()]
    excluded = TUNING_IDS | {row["claim_id"] for row in previous}
    corpus, train, dev = load_data(args.archive)
    selected = pilot.sample_dev(train, [r for r in dev if r["id"] not in excluded],
                                args.per_label, 20261128)
    manifest = {"judge": judge, "verifier": args.verifier_model, "seed": 20261128,
                "claim_ids": [r["id"] for r in selected], "excluded_ids": sorted(excluded),
                "review_budget": len(selected) // 5, "max_tokens": 1024}
    if args.dry_run:
        print(pilot.canonical(manifest))
        return
    key = os.getenv("OPEN_WEBUI_API_KEY") or getpass.getpass("Local Open WebUI API key: ").strip()
    base = "http://127.0.0.1:8080/api/v1"
    models = {r["id"] for r in pilot.request(base, key, "/models")["data"]}
    if not {judge, args.verifier_model} <= models:
        parser.error("Both fixed model IDs must be visible in Open WebUI")
    primary = SimpleNamespace(base_url=base, model=judge, max_tokens=1024)
    alternate = SimpleNamespace(base_url=base, model=args.verifier_model, max_tokens=1024)
    index = index_documents(corpus, True)
    docs = {d["doc_id"]: d for d in corpus}
    args.out.mkdir(parents=True)
    (args.out / "manifest.json").write_text(pilot.canonical(manifest), encoding="utf-8")
    rows = []
    with (args.out / "responses.jsonl").open("w", encoding="utf-8") as output:
        for claim in selected:
            evidence = [{"doc_id": i, "title": docs[i]["title"],
                         "sentences": list(enumerate(docs[i]["abstract"]))}
                        for i in retrieve(claim["claim"], *index)[:5]]
            calls = {name: pilot.call(primary, key, name, prompt, claim["claim"], evidence)
                     for name, prompt in pilot.PROMPTS.items()}
            rubric = calls["rubric"].get("parsed", {})
            if rubric.get("verdict") == "SUPPORT":
                ids = {tuple(pair) for pair in rubric["evidence"]}
                cited = [{**doc, "sentences": [s for s in doc["sentences"] if (doc["doc_id"], s[0]) in ids]}
                         for doc in evidence if any(i == doc["doc_id"] for i, _ in ids)]
                for name, model, packet in (("same_cited", primary, cited), ("same_full", primary, evidence),
                                            ("other_cited", alternate, cited), ("other_full", alternate, evidence)):
                    calls[name] = pilot.call(model, key, name, VERIFIER, claim["claim"], packet)
            row = {"claim_id": claim["id"], "gold": pilot.gold_label(claim), "calls": calls}
            print(pilot.canonical(row), file=output, flush=True)
            if any(c.get("http_status") == 429 for c in calls.values()):
                raise SystemExit("Provider throttled the run. Partial responses were saved.")
            rows.append(row)
            print(f"{len(rows)}/{len(selected)}: claim {claim['id']}", flush=True)
    summary = {"n": len(rows), "conditions": compare(rows, manifest["review_budget"])}
    (args.out / "summary.json").write_text(pilot.canonical(summary), encoding="utf-8")


if __name__ == "__main__":
    main()
