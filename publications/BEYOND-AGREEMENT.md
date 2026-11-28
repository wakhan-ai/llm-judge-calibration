# Beyond Agreement: What Real LLM Judge Experiments Reveal About Evidence, Verification and Risk

**Status:** Public experimental research report; not a validated deployment system  
**Research programme:** LLM Judge Calibration — Phase II / SciFact  
**Date:** 27 November 2026  
**Repository:** https://github.com/wakhan-ai/llm-judge-calibration  
**Next research iteration:** [VARE Research Phase II+ — Completing the Missing Evidence Before Publication](../research/VARE-PHASE-II-PLUS.md)

## Abstract

Can a second language model make an AI evaluator more reliable? Does a more explicit rubric prevent false acceptance of unsupported scientific claims? Can review decisions be improved without sending too many correct claims to humans?

Following a Phase I **simulation** of calibration and review, we tested actual model calls on publicly labelled SciFact scientific claims. Our work spans an evidence-retrieval comparison, a 30-claim judge feasibility pilot, a 15-claim verifier follow-up, a 41-claim document-disjoint evaluation and a 97-claim contradiction-focused development stress test.

The evidence is mixed. Including abstracts alongside titles increased annotated-document retrieval@5 from 115/188 to 168/188. In the 30-claim pilot, a same-model verifier **did not** reduce three false acceptances and increased review from two rubric cases to seventeen. In a 41-claim document-disjoint cohort with eight review slots per condition, a Gemini 2.5 Flash full-evidence verifier reduced remaining false accepts from two (rubric) to one, a result hinging on one case. In a contradiction-enriched 97-claim development sample, different verifier strategies produced distinct trade-offs; invalid/truncated responses were sometimes routed to review rather than correctly semantically classified.

The results do **not** establish a universally superior hybrid architecture. They motivate controlled numerical verification, evidence-removal controls, true held-out calibration, category-sensitive review and stronger external validation.

## 1. Why move beyond aggregate agreement?

An AI judge can agree frequently with references while accepting an important unsupported statement. Three connected concerns motivate this phase:

- **Consequence:** a wrong scientific number may matter more than a stylistic error; public SciFact labels do not establish those consequences.
- **Mechanism:** two judges may share the same error; a second LLM is not equivalent to a deterministic fact checker.
- **Decision quality:** reducing automatic false acceptance by reviewing many more claims may be undesirable unless review budgets and false alarms are measured.

We therefore distinguish **reference-label agreement**, **false acceptance**, **technical/format failures**, **review allocation** and **cost**. No result below should be interpreted as pharmaceutical MLR validation.

## 2. Benchmark and reproducible materials

The [SciFact dataset](https://github.com/allenai/scifact) and [original paper](https://aclanthology.org/2020.emnlp-main.609/) provide scientific claims, abstracts and evidence annotations. The downloaded archive contains 5,183 abstracts, 809 labelled training claims, 300 labelled development claims and 300 official test claims without public labels. The development set includes 124 support, 64 contradiction and 112 claims without annotated evidence. We use the available labelled development claims for the experiments described here; the official test set is not reported as a labelled test set.

Data provenance, upstream attribution and licence notices: [DATA.md](../phase-2-scifact/DATA.md). Dataset and analysis code: [Phase II package](../phase-2-scifact/README.md). Research comparison protocol: [PROTOCOL.md](../phase-2-scifact/PROTOCOL.md).

### 2.1 Evidence retrieval

Among 188 development claims with annotated evidence:

| Top-k annotated-document retrieval | Title only | Title + abstract |
|---|---:|---:|
| k=1 | 70/188 | 122/188 |
| k=5 | 115/188 | 168/188 |
| k=10 | 132/188 | 173/188 |

Retrieval@5 increased **28.2 percentage points** (61.2% to 89.4%). A paired claim bootstrap reported a 95% interval of **21.8 to 35.1 percentage points**, although shared evidence documents may make claim-level intervals too narrow. These metrics test finding *an annotated document*, not selecting the right rationale sentence or judging the claim correctly.

[Machine-readable retrieval results](../phase-2-scifact/evidence/retrieval-results.json).

## 3. Actual LLM judge and verifier experiments

### 3.1 Balanced 30-claim feasibility pilot

The 26 November 2026 pilot used **GPT-4.1 Mini** with ten cases from each reference label. The VARE feasibility arm called the *same underlying model* again to assess rubric-cited evidence.

| Arm | False accepts among 20 non-support cases | Review | Automatic coverage |
|---|---:|---:|---:|
| Plain | 3 | 0/30 | 100% |
| Rubric | 3 | 2/30 | 93.3% |
| Same-model VARE feasibility | 3 | 17/30 | 43.3% |

All three arms accepted the same three reference non-support claims. The additional verifier therefore **failed to reduce false acceptance** and substantially increased review. Of 80 model calls, 73 passed output validation; this was a feasibility sample, not a matched-review-budget generalisation estimate.

[Detailed pilot report](../phase-2-scifact/evidence/PAIRED-PILOT.md) · [Summary JSON](../phase-2-scifact/evidence/paired-pilot-summary.json).

### 3.2 Fifteen-claim follow-up

A fresh, label-balanced development sample compared same-model and Gemini 2.5 Flash verifiers given cited sentences or full abstracts, at a budget of three reviews. None of the baseline arms accepted a non-support case before review; thus this experiment **could not test rescue of actual false acceptances**. Strict JSON parsing rejected some fenced Gemini responses, which illustrates the need to separate output-format failures from semantic judgments.

[Follow-up report](../phase-2-scifact/evidence/VERIFIER-FOLLOWUP.md).

### 3.3 Forty-one-claim document-disjoint evaluation

This subset shared no cited or annotated evidence documents with training or earlier experimental claims. It comprised **21 SUPPORT, 19 INSUFFICIENT_EVIDENCE and only 1 CONTRADICT** reference labels. Each method received **eight** review slots.

| Arm | False accepts remaining among 20 reference non-support cases | Correct automatic accepts among 21 reference-support cases |
|---|---:|---:|
| Plain GPT-4.1 Mini | 2 | 13 |
| Rubric GPT-4.1 Mini | 2 | 17 |
| GPT-4.1 Mini, cited verifier | 2 | 17 |
| GPT-4.1 Mini, full-evidence verifier | 2 | 17 |
| Gemini 2.5 Flash, cited verifier | 2 | 17 |
| Gemini 2.5 Flash, full-evidence verifier | **1** | **18** |

The full-evidence Gemini configuration improved the rubric comparison **by one residual false acceptance**, with the same review budget. This is an observed result on a small cohort, not evidence of reliable superiority or robust contradiction detection. The one contradiction in the cohort is a major limitation. The retrieval index remained the common abstract corpus.

[Document-disjoint report](../phase-2-scifact/evidence/VERIFIER-HOLDOUT.md) · [Run manifest](../phase-2-scifact/evidence/verifier-holdout-manifest.json) · [Summary JSON](../phase-2-scifact/evidence/verifier-holdout-summary.json).

### 3.4 Ninety-seven-claim contradiction-focused stress test

This previously unused *development* subset contained **47 CONTRADICT, 25 INSUFFICIENT_EVIDENCE and 25 SUPPORT** labels. Every case shared at least one document relationship with training or previous runs, so it is **not document-disjoint**. Each condition used **19** review slots.

| Arm | Contradiction false accepts remaining /47 | All false accepts remaining /72 | Correct automatic accepts /25 |
|---|---:|---:|---:|
| Plain GPT-4.1 Mini | 0 | 1 | 7 |
| Rubric GPT-4.1 Mini | 3 | 5 | 12 |
| Same-model, cited verifier | 0 | 2 | 15 |
| Same-model, full verifier | 1 | 3 | 14 |
| Gemini 2.5 Flash, cited verifier | 1 | 3 | 14 |
| Gemini 2.5 Flash, full verifier | 1 | 3 | 14 |
| Gemini 2.5 Pro, full verifier | 0 | 3 | 14 |

The rubric condition was not universally better than the plain baseline. Some Gemini Pro responses were truncated and then routed to review as invalid outputs; this can suppress unsafe automatic acceptance **without proving successful semantic contradiction detection**. The experiment supports analysis of review-policy and verifier trade-offs, not a claim that the strongest model reasoned best.

[Stress-test report](../phase-2-scifact/evidence/CONTRADICTION-STUDY.md) · [Summary JSON](../phase-2-scifact/evidence/contradiction-study-summary.json).

## 4. What these findings actually establish

1. **Retrieval matters.** More complete lexical evidence materially improved annotated-document hit rates in this benchmark.
2. **Another LLM is not an independent fact oracle.** In the initial pilot it left the same false acceptances and dramatically increased review.
3. **Verifier evidence scope and model choice can change allocation.** A cross-model full-evidence verifier improved one small document-disjoint comparison by one case.
4. **Output invalidity is a distinct safety mechanism.** Routing malformed or truncated outputs may be appropriate, but it must not be counted as semantic error detection.
5. **Matched review budgets are essential.** Automation coverage, false alarms and correct acceptances must accompany any false-acceptance metric.

The results **do not** validate the final VARE architecture, a production-ready regulatory reviewer or performance on unseen error-severity categories.

## 5. Important remaining research gaps and the Phase II+ agenda

The next experiments are documented in [**VARE Research Phase II+ — Completing the Missing Evidence Before Publication**](../research/VARE-PHASE-II-PLUS.md). They address objections that the current dataset and model comparisons cannot settle:

- **Independent deterministic checks:** parse and verify quantities, units, study population, endpoint, denominator and time, measuring extraction separately from rule validation.
- **Evidence-removal controls:** remove irrelevant evidence, one redundant source or the last sufficient source and measure appropriate verdict *stability* and *revision*.
- **Cost-sensitive review:** validate severity categories and explicit costs, calibrate confidence on a separate split, and evaluate at equal review budgets.
- **Shared failure analysis:** compare same-model, different-model and deterministic validators on matched cases while separating parsing, truncation and semantic failures.
- **Fresh grouped holdout and external benchmarks:** evaluate source-disjoint cohorts and FEVEROUS-style tabular evidence with uncertainty analysis and ablations.
- **Expert reference standards:** SciFact support labels are not measurements of clinical or regulatory error severity; those require independently justified domain review.

The next contribution should be assessed against **strong simple baselines**. If a lightweight check plus well-designed deferral performs as well as a complicated architecture, that negative result is scientifically useful.

## 6. Limits and integrity

These results reflect saved experimental reports and machine-readable summaries in this repository; they have not been independently reproduced as part of this publication preparation. The 30-claim pilot is label-balanced, the 41-claim cohort is very small and contradiction-sparse, and the 97-claim stress test is development data with document overlap. Additional model calls can be stochastic or affected by provider/model-version changes. The first 600-row study was synthetic: it contained no real LLM or expert-review decisions. Some recorded verification arms are **separate LLM calls**, not completed deterministic numerical-rule engines. Held-out calibration, validated severity costs and external benchmark testing are still pending.

## 7. Reproduce and inspect

Start at [repository README](../README.md), [Phase II README](../phase-2-scifact/README.md), [SciFact data provenance](../phase-2-scifact/DATA.md), [protocol](../phase-2-scifact/PROTOCOL.md) and [model runner instructions](../phase-2-scifact/OPEN-WEBUI.md). See the four [evidence experiment reports](../phase-2-scifact/evidence/) and source files for archived results and settings.

## References

- Wadden et al. (2020), *Fact or Fiction: Verifying Scientific Claims*, EMNLP. https://aclanthology.org/2020.emnlp-main.609/
- Allen Institute for AI, SciFact benchmark. https://github.com/allenai/scifact
- Gu et al., *A Survey on LLM-as-a-Judge*. https://arxiv.org/abs/2411.15594
- Shankar et al., *Who Validates the Validators?* https://arxiv.org/abs/2404.12272
- Project research protocol, dataset provenance, source code and reports: https://github.com/wakhan-ai/llm-judge-calibration

**Author note:** Independent exploratory research using public data. No organisation, medical or regulatory approval is implied. Results should be read with their sample, evidence and review-policy limitations.
