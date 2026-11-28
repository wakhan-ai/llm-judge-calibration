# LLM Judge Calibration — Open Research

Reproducible research across a **synthetic calibration demonstration (Phase I)**, **real-model scientific fact verification (Phase II)**, and a **proposed Phase II+ research agenda**.

## Research articles and evidence

- **Current article:** [Beyond Agreement: What Real LLM Judge Experiments Reveal About Evidence, Verification and Risk](phase-2-scifact/articles/BEYOND-AGREEMENT.md) — [LinkedIn article](https://www.linkedin.com/pulse/beyond-agreement-what-real-llm-judge-experiments-reveal-waheed-abbas-lyfne/) · [Illustrated announcement](https://www.linkedin.com/feed/update/urn:li:share:7532260344161902592/).
- **Next experimental direction:** [VARE Research Phase II+ — Completing the Missing Evidence Before Publication](phase-2-scifact/articles/VARE-PHASE-II-PLUS.md) — explicit untested hypotheses, controls, evaluation gates and reproducibility requirements.
- **Research implementation and results:** [SciFact Phase II](phase-2-scifact/README.md); [study protocol](phase-2-scifact/PROTOCOL.md); [dataset provenance and licences](phase-2-scifact/DATA.md); [experiment evidence](phase-2-scifact/evidence/).

## Phase I — Synthetic evaluator-calibration demonstration

*Who Judges the AI Judge? A Computational Study of LLM Evaluator Calibration and Risk-Sensitive Review.*

The computational demonstration uses **600 synthetic assessment records**, split into 300 development and 300 held-out records. It illustrates agreement, probability calibration and selective review. **It contains no real LLM calls, qualified human judgments, or pharmaceutical review outcomes.**

```sh
python -m pip install -r requirements.txt
python simulate.py
```

The fixed-seed script writes `synthetic_cases.csv` and `simulation_results.csv`.

## Phase II — Public SciFact evidence and real-model inference

The [Phase II research folder](phase-2-scifact/README.md) contains the SciFact provenance, retrieval code and experimental evidence from **real API-based** judging and verification. It includes a 30-claim pilot, 15-claim follow-up, 41-claim document-disjoint evaluation and 97-claim contradiction stress test.

**Scope of evidence:** Retrieval and exploratory judge–verifier results have been recorded. The experiments **do not validate** a complete deterministic verifier, genuinely held-out probability calibration, independently assessed severity costs, evidence-removal stability or generalisable superiority of VARE. Model outputs and routing failures must not be conflated with semantic correctness.

## LinkedIn publication cross-links

- Earlier article, *Who Judges the AI Judge?* — confirm its published URL before adding here.
- Current article, *Beyond Agreement* — manuscript at [articles/BEYOND-AGREEMENT.md](phase-2-scifact/articles/BEYOND-AGREEMENT.md).
- Next article, *VARE Phase II+* — an **experimental agenda** at [articles/VARE-PHASE-II-PLUS.md](phase-2-scifact/articles/VARE-PHASE-II-PLUS.md), not a completed empirical result.

**Transparency principle:** Report what was measured, note negative results, and clearly distinguish research hypotheses from proven benefits. Read source licences in [DATA.md](phase-2-scifact/DATA.md).
