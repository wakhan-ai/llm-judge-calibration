# Phase II — SciFact scientific-claim evaluation

**Research article:** [Beyond Agreement: What Real LLM Judge Experiments Reveal About Evidence, Verification and Risk](articles/BEYOND-AGREEMENT.md)  
**Proposed next experiments:** [VARE Research Phase II+](articles/VARE-PHASE-II-PLUS.md)  
**Source and licences:** [DATA.md](DATA.md) · **Experimental protocol:** [PROTOCOL.md](PROTOCOL.md)

This package documents the public SciFact dataset, reproducible lexical retrieval, actual LLM judging and second-verifier experiments, and limitations that motivate the next phase. **It does not establish a validated risk-sensitive regulatory decision system.**

## Reproduce the retrieval baseline

Run from this directory in Python 3.10+ (standard library):

```sh
python scifact_retrieval_pilot.py data/scifact-data.tar.gz
```

The original SciFact archive contains **5,183 abstracts, 809 labelled training claims, 300 labelled development claims and 300 test claims with withheld labels**. Development includes 124 SUPPORT, 64 CONTRADICT and 112 without annotated evidence. Of 188 evidence-bearing development claims, title-only top-five TF-IDF retrieved an annotated document for **115**, versus **168** for title plus abstract (**+28.2 percentage points**); see [retrieval-results.json](evidence/retrieval-results.json). Retrieval hit rates do **not** measure judge accuracy.

## Recorded model-based experiments

| Experiment | Subset | Main observation | Evidence |
|---|---|---|---|
| Initial pilot | 30 balanced development claims | Plain, rubric and same-model verifier retained 3/20 false automatic accepts; verifier increased review to 17/30 | [Paired pilot](evidence/PAIRED-PILOT.md) |
| Cross-verifier follow-up | 15 development claims | All arms had zero non-support false accepts; unable to test correction of those errors | [Follow-up](evidence/VERIFIER-FOLLOWUP.md) |
| Document-disjoint evaluation | 41 claims, 8 review slots | Rubric 2/20 false accepts; Gemini Flash with full abstracts 1/20, a one-case difference | [Holdout](evidence/VERIFIER-HOLDOUT.md) |
| Contradiction stress test | 97 development claims, 19 review slots | Rubric retained 3/47 contradiction false accepts; same-model cited verifier retained 0/47, but the plain judge also retained 0/47 | [Stress test](evidence/CONTRADICTION-STUDY.md) |

The 41-claim document-disjoint subset contains just **one contradicted reference claim**. The 97-claim stress subset **shares evidence-document relationships** with earlier data; it is not a pristine final holdout. Model truncation, JSON failures and citation failures can cause human deferrals without semantic error detection. Neither these samples nor their decision policies prove general superiority.

## Executable tools and study details

- [Lexical retrieval runner](scifact_retrieval_pilot.py)
- [LLM pilot runner](scifact_webui_pilot.py)
- [Verifier follow-up runner](scifact_verifier_followup.py)
- [Windows/Open WebUI/OpenRouter setup](OPEN-WEBUI.md)
- [Machine-readable summaries and manifests](evidence/)
- [Dataset provenance and licensing](DATA.md)
- [Research protocol](PROTOCOL.md)

## Pending — the Phase II+ agenda

Actual deterministic number/endpoint/unit checks; controlled evidence-removal and redundancy experiments; independent severity rating; grouped calibration and cost-sensitive review; strong paired ablation and external FEVEROUS evaluation remain uncompleted. The [Phase II+ document](articles/VARE-PHASE-II-PLUS.md) records the required controls and publication decision gates.

## LinkedIn research linkage

Published on LinkedIn: [LinkedIn article](https://www.linkedin.com/pulse/beyond-agreement-what-real-llm-judge-experiments-reveal-waheed-abbas-lyfne/) · [LinkedIn announcement](https://www.linkedin.com/feed/update/urn:li:ugcPost:7532259796884975616/). The Phase II+ roadmap describes planned experiments.
