"""Reproduce the SciFact evidence retrieval pilot using Python 3."""
import argparse
from collections import Counter
import hashlib
import heapq
import json
import math
from pathlib import Path
import random
import re
import tarfile

EXPECTED_SHA = "11c621288d41ac144d29b13b0f8503b3820b7d6e8b1f6ff24dff335c196d76be"


def load_data(path):
    if hashlib.sha256(path.read_bytes()).hexdigest() != EXPECTED_SHA:
        raise ValueError("SciFact archive checksum differs from the published release")
    with tarfile.open(path) as archive:
        return [
            [json.loads(line) for line in archive.extractfile(f"data/{name}.jsonl")]
            for name in ("corpus", "claims_train", "claims_dev")
        ]


def referenced_docs(claims):
    return {
        int(doc_id)
        for claim in claims
        for doc_id in [*claim["cited_doc_ids"], *claim["evidence"]]
    }


def tokens(text):
    return re.findall(r"\b\w+\b", text.lower())


def weighted_terms(text, idf):
    weighted = {
        term: (1 + math.log(count)) * idf[term]
        for term, count in Counter(tokens(text)).items()
        if term in idf
    }
    norm = math.sqrt(sum(value ** 2 for value in weighted.values())) or 1
    return {term: value / norm for term, value in weighted.items()}


def index_documents(corpus, include_abstracts):
    texts = {
        row["doc_id"]: " ".join([row["title"], *row["abstract"]])
        if include_abstracts else row["title"]
        for row in corpus
    }
    frequencies = Counter(term for text in texts.values() for term in set(tokens(text)))
    idf = {term: 1 + math.log((1 + len(texts)) / (1 + n)) for term, n in frequencies.items()}
    index = {}
    for doc_id, text in texts.items():
        for term, weight in weighted_terms(text, idf).items():
            index.setdefault(term, []).append((doc_id, weight))
    return idf, index


def retrieve(claim, idf, index):
    scores = Counter()
    for term, weight in weighted_terms(claim, idf).items():
        for doc_id, doc_weight in index[term]:
            scores[doc_id] += weight * doc_weight
    return heapq.nsmallest(10, scores, key=lambda doc_id: (-scores[doc_id], doc_id))


def evaluate(corpus, dev, clean_ids, include_abstracts):
    idf, index = index_documents(corpus, include_abstracts)
    records = []
    for claim in dev:
        if claim["evidence"]:
            gold = set(map(int, claim["evidence"]))
            ranking = retrieve(claim["claim"], idf, index)
            label = next(iter({group["label"] for groups in claim["evidence"].values() for group in groups}))
            records.append({
                "id": claim["id"], "label": label, "gold_count": len(gold),
                "disjoint": claim["id"] in clean_ids,
                "hit": {k: bool(gold.intersection(ranking[:k])) for k in (1, 5, 10)},
            })
    return records


def summarize(records, corpus_size):
    return {
        "n": len(records),
        "hits": {k: sum(row["hit"][k] for row in records) for k in (1, 5, 10)},
        "expected_random_hit_at_5": round(sum(
            1 - math.comb(corpus_size - row["gold_count"], 5) / math.comb(corpus_size, 5)
            for row in records
        ), 4)
    }


def paired_interval(first, second):
    outcomes = [int(b["hit"][5]) - int(a["hit"][5]) for a, b in zip(first, second, strict=True)]
    rng = random.Random(20261125)
    draws = sorted(sum(rng.choices(outcomes, k=len(outcomes))) / len(outcomes) for _ in range(5000))
    return {"gain": sum(outcomes) / len(outcomes), "claim_bootstrap_95": [draws[125], draws[4874]]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    args = parser.parse_args()
    corpus, train, dev = load_data(args.archive)
    train_docs = referenced_docs(train)
    clean_ids = {claim["id"] for claim in dev if referenced_docs([claim]).isdisjoint(train_docs)}
    title = evaluate(corpus, dev, clean_ids, False)
    full = evaluate(corpus, dev, clean_ids, True)
    result = {
        "corpus": len(corpus),
        "dev": len(dev),
        "dev_document_disjoint_from_train": len(clean_ids),
        "shared_train_dev_docs": len(train_docs & referenced_docs(dev)),
        "paired_full_minus_title": paired_interval(title, full),
    }
    for name, records in (("title", title), ("title_and_abstract", full)):
        result[name] = {
            "all": summarize(records, len(corpus)),
            "disjoint": summarize([r for r in records if r["disjoint"]], len(corpus)),
            "by_label": {
                label: summarize([r for r in records if r["label"] == label], len(corpus))
                for label in ("SUPPORT", "CONTRADICT")
            },
        }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
