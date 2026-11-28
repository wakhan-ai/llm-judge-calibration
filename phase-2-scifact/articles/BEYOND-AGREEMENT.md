# Beyond Agreement: What Real LLM Judge Experiments Reveal About Evidence, Verification and Risk

**Status:** Public research article manuscript — evidence-backed experimental update; not an assertion that VARE is validated.  
**Publication:** LinkedIn URL to be added after publication (do not substitute a guessed URL).  
**Companion:** [VARE Research Phase II+ — Completing the Missing Evidence Before Publication](VARE-PHASE-II-PLUS.md)  
**Repository:** [LLM Judge Calibration](https://github.com/wakhan-ai/llm-judge-calibration) · [SciFact experiments](../README.md)  
**Dataset:** [SciFact](https://github.com/allenai/scifact); see [dataset provenance](../DATA.md).

## Abstract

An LLM evaluating another LLM can produce a confident verdict without reliably detecting the errors that matter. Following a synthetic calibration study, this research moves to real model judgments on the public SciFact scientific-claim benchmark. We evaluated lexical evidence retrieval, judge prompts, same-model and cross-model verification, evidence scope and selective routing for human review. Results were mixed: adding abstracts substantially improved retrieval of annotated evidence; a separate verifier sometimes improved review allocation; but verification often increased deferrals without preventing false acceptance. The work establishes observable failure modes and a repeatable empirical baseline, **not** a validated superiority claim for a complete hybrid architecture.

## Why this study

The first study illustrated calibration and selective review using **600 synthetic records**, not real LLM outputs or qualified human regulatory judgments ([Phase I](../../README.md)). Subsequent technical feedback raised four questions:

1. Can a judge miss deliberately incorrect claims while showing reasonable aggregate agreement?
2. Are error costs and review thresholds appropriate when mistakes have different consequences?
3. Would numerical, temporal and contextual checks be more dependable as independently tested rules than as another LLM verdict?
4. Can an evaluator reward **appropriate stability** (removing irrelevant or redundant evidence) as well as **appropriate revision** (removing the last sufficient source)?

The completed experiments directly examine the first question in limited public-benchmark settings and explore extra semantic verification. They **do not yet** establish empirical category costs, a separately tested deterministic verifier, held-out calibration or evidence-removal stability. Those are explicitly scoped in the [Phase II+ protocol](VARE-PHASE-II-PLUS.md).

## Benchmark and reproducibility

The archived SciFact release contains **5,183 abstracts**, **809 labelled training claims**, **300 labelled development claims** and **300 unlabelled official test claims**. The development set has **124 SUPPORT**, **64 CONTRADICT** and **112 claims without annotated evidence**. These labels are about claim–evidence relationships; they are **not** pharmaceutical MLR severity labels. See [DATA.md](../DATA.md), [PROTOCOL.md](../PROTOCOL.md) and the [runner](../scifact_webui_pilot.py).

The published evidence describes real API inference with **GPT-4.1 Mini** and verifier configurations involving **Gemini 2.5 Flash** and **Gemini 2.5 Pro**, as distinct from the earlier synthetic calibration records. Provider and model changes can affect reproduction. Metrics below are taken from the versioned GitHub evidence files; this manuscript does not claim fresh independent reruns.

## Experiment 1 — Getting adequate evidence to the judge

Among **188** development claims with annotated evidence:

| Retrieval top-k | Title-only TF-IDF | Title + abstract TF-IDF |
|---|---:|---:|
| Top 1 | 70/188 | 122/188 |
| Top 5 | 115/188 (61.2%) | 168/188 (89.4%) |
| Top 10 | 132/188 | 173/188 |

The **top-five gain was 28.2 percentage points** (paired claim-level bootstrap 95% interval **21.8–35.1 points**). This interval does not fully account for shared evidence documents. These are **annotated-document retrieval hits**, not sentence-level grounding, judge accuracy or end-to-end proof of correctness. See [retrieval results](../evidence/retrieval-results.json).

## Experiment 2 — A second call did not solve the first judge's mistakes

A balanced **30-claim development feasibility pilot** compared a plain judge, rubric judge and a separate same-model cited-sentence verifier:

| Arm | False automatic SUPPORT on 20 non-SUPPORT claims | Review cases / 30 | Automatic coverage |
|---|---:|---:|---:|
| Plain GPT-4.1 Mini | 3 | 0 | 100% |
| Rubric GPT-4.1 Mini | 3 | 2 | 93.3% |
| Same-model VARE feasibility | 3 | 17 | 43.3% |

All three arms retained the **same three false acceptances**. Extra verification markedly increased review burden without improving the target error count. The VARE arm reviewed **8 of 10** reference-supported claims. **73 of 80** model outputs passed structural validation. This label-balanced pilot is not a deployment-prevalence estimate and review rates were not matched across arms. See [paired pilot report](../evidence/PAIRED-PILOT.md).

A **15-claim development follow-up** crossed same-model/different-model verifiers and cited/full-abstract evidence at a fixed three-case review budget. It contained **no baseline false acceptance** on non-SUPPORT claims, so it could not demonstrate whether the added verifier corrected that error class. JSON fences and evidence-scope effects exposed parser/format confounds. See [follow-up report](../evidence/VERIFIER-FOLLOWUP.md).

## Experiment 3 — Document-disjoint evaluation under a matched budget

A **41-claim** subset shared no cited or annotated documents with training or previous experimental claims (the retrieval index itself still contained the shared public corpus). It included **21 SUPPORT**, **19 INSUFFICIENT_EVIDENCE**, and **1 CONTRADICT**. All arms were allocated **eight review slots**.

| Arm | Non-SUPPORT false accepts remaining (of 20) | Correct automatic SUPPORT (of 21) |
|---|---:|---:|
| Plain GPT-4.1 Mini | 2 | 13 |
| Rubric GPT-4.1 Mini | 2 | 17 |
| Same-model verifier, cited evidence | 2 | 17 |
| Same-model verifier, full abstracts | 2 | 17 |
| Gemini 2.5 Flash, cited evidence | 2 | 17 |
| Gemini 2.5 Flash, full abstracts | **1** | **18** |

The full-abstract Gemini arm improved by **one false acceptance** relative to the rubric arm under the same review budget, while retaining one more correct automatic acceptance. This is a fragile, small-sample result, not established superiority. Only **one reference contradiction** was present, preventing a meaningful contradiction-performance conclusion. See [document-disjoint report](../evidence/VERIFIER-HOLDOUT.md), [manifest](../evidence/verifier-holdout-manifest.json) and [summary](../evidence/verifier-holdout-summary.json).

## Experiment 4 — A contradiction stress test revealed an important confound

A previously unused **97-claim development subset** included **47 CONTRADICT**, **25 INSUFFICIENT_EVIDENCE**, and **25 SUPPORT** claims. Each ranking had **19 review slots**.

| Arm | Contradictions falsely accepted after review (of 47) | All non-SUPPORT false accepts (of 72) |
|---|---:|---:|
| Plain GPT-4.1 Mini | 0 | 1 |
| Rubric GPT-4.1 Mini | 3 | 5 |
| Same-model verifier, cited evidence | 0 | 2 |
| Same-model verifier, full abstracts | 1 | 3 |
| Gemini 2.5 Flash, full abstracts | 1 | 3 |
| Gemini 2.5 Pro, full abstracts | 0 | 3 |

The plain judge was strong under this particular routing policy; a more explicit rubric was **not automatically better**. The same-model cited verifier corrected some rubric-arm errors but did not outperform the plain arm on all false accepts. Gemini Pro's zero residual contradiction accepts **must not** be interpreted as purely semantic success: some flagged cases arose from **truncated responses** routed to review. The subset had evidence-document overlap with training or earlier runs and is **not a clean independent confirmation set**. See [contradiction report](../evidence/CONTRADICTION-STUDY.md) and [manifest](../evidence/contradiction-study-manifest.json).

## What these results mean

1. **Retrieval is part of evaluator reliability.** Finding relevant abstracts improved substantially; correct interpretation remains separately unproved.
2. **A second LLM is not independent ground truth.** It can agree with a wrong verdict, increase reviews, or be sensitive to how much evidence it receives.
3. **Technical failure is not semantic detection.** Invalid JSON, citations or truncated output can trigger safe review, but they must be reported separately from recognizing a contradiction.
4. **Match review budgets before comparing safety.** Sending more claims to people is not automatically a better automatic judge.
5. **Report negative results.** They reveal which improvements may be illusory and motivate strong ablation tests.

## What is not yet demonstrated

These SciFact runs do **not** establish: qualified pharmaceutical MLR outcomes; severity-weighted error costs; a deterministic verification engine validated on numerical/endpoint/population/unit errors; evidence-removal/redundancy controls; calibrated error probabilities on a fresh grouped holdout; generalisation to FEVEROUS; or conclusive statistical superiority of VARE. The official SciFact test labels are not public in the archive.

These are not footnotes to hide. They are the **testable agenda for Phase II+**, described in [VARE Research Phase II+](VARE-PHASE-II-PLUS.md).

## Next research question

**Can a system combining real source-grounded semantic judgment, independently tested deterministic checks, calibrated error risk and fixed-budget escalation reduce consequential false acceptance on fresh, document-disjoint claims without unacceptable false alarms, workload or cost?**

The next evaluation will compare simpler baselines against the full system; test evidence removal with redundant and irrelevant sources; distinguish oracle extraction from end-to-end numerical checks; study shared model failures; and preregister thresholds, partitions and decision criteria before final test scoring.

A negative result remains publishable and scientifically useful. The aim is not to defend a particular architecture but to establish **which verification mechanisms work, when, and at what cost**.

## Sources and reproducibility

- Wadden et al. (2020), [*Fact or Fiction: Verifying Scientific Claims*](https://aclanthology.org/2020.emnlp-main.609/), and the [SciFact dataset](https://github.com/allenai/scifact).
- Gu et al., [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594).
- Shankar et al., [*Who Validates the Validators?*](https://arxiv.org/abs/2404.12272).
- [Experimental protocol](../PROTOCOL.md), [dataset provenance](../DATA.md), [inference setup](../OPEN-WEBUI.md), [machine-readable evidence](../evidence/).
- [Phase II+ research roadmap](VARE-PHASE-II-PLUS.md).

**Research boundary:** Independent public-benchmark research, not organisational endorsement or regulatory approval. Repo results are reported as archived; no fresh independent rerun is asserted here.
