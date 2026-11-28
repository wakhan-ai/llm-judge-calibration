# VARE Research Phase II+ — Completing the Missing Evidence Before Publication

**Status: planned experiments, not completed results.**  
**Preceding article:** [Beyond Agreement: What Real LLM Judge Experiments Reveal About Evidence, Verification and Risk](../publications/BEYOND-AGREEMENT.md)  
**Baseline research:** [Phase II SciFact evidence](../phase-2-scifact/evidence/) · [Current protocol](../phase-2-scifact/PROTOCOL.md)

## Purpose

The preceding real-model studies exposed inconsistent gains from adding verification, shared evaluator failures, response-format problems and dependence on review allocation. This phase seeks to establish **under what conditions** verification, calibration and severity-sensitive routing reduce unsupported automatic acceptance without unacceptable false alarms, workload or cost.

A specific scientific hypothesis: **a source-grounded deterministic verifier plus a calibrated, category-aware review policy can outperform the strongest matched-budget simpler baseline on held-out, materially altered scientific claims.** This is untested.

## Reviewers' concern → falsifiable experiment

| Concern | Required controls | Primary measure |
|---|---|---|
| Serious mistakes hidden by average agreement | Paired correct/incorrect claims, contradiction-rich fresh source groups | False acceptance by error category |
| Numerical mistakes should be machine-checkable | Oracle parsed values versus LLM-extracted values; unit/endpoint/date/denominator swaps | Detection recall and false flags |
| Equal error costs are unrealistic | Independently justified severity rubric, multiple cost schedules | Expected loss at matched reviews |
| Common thresholds ignore context | Frozen common versus category-specific thresholds | Risk–coverage comparison |
| A second judge can repeat errors | Same-model, cross-model, deterministic, plus disagreement analysis | Joint-error rate and incremental rescues |
| Evidence removal may cause false hesitation | Remove irrelevant, redundant, last adequate evidence; add contradictory source | Stability and appropriate revision |
| Performance may not generalise | Grouped source-disjoint holdout and external scientific/table benchmark | Paired confidence intervals and transfer |

## Study design

1. **Freeze versioned research protocol:** label mapping, claim-pair definitions, exact evidence packets, exclusions, error-cost sensitivity scenarios, outcome calculations, sample-size/power target, review budgets and adjudication rules. Do not tune on the final test set.
2. **Construct source-grouped cases:** preserve all variants from an originating claim, document and evidence pair in a single partition. Create factual controls and single-error mutations affecting value, unit, denominator, population, endpoint, timeframe and unsupported generalisation.
3. **Test extraction separately:** evaluate rule engine with oracle structured source records before end-to-end testing with model-extracted records. Track undecidable/missing fields; exact numeric-match alone must not mean the claim is supported.
4. **Counterfactual evidence test:** unchanged verdict after irrelevant evidence removed; unchanged verdict when one of two *independently sufficient* sources is removed; appropriate abstention when last adequate evidence is removed. Check changes for overconfidence and underconfidence.
5. **Independent validators:** compare deterministic rules and same-/cross-model semantic verification; score technical invalidity and semantic disagreement separately.
6. **Real probability calibration:** fit on a fixed calibration partition, not the holdout. Report multiclass Brier score, reliability plots, log loss, and how review choices change at matched coverage.
7. **Severity study:** use independent reviewers or a clearly labelled research proxy; do not infer clinical/regulatory cost from SciFact labels. Show sensitivity across competing cost matrices and adjudicate disagreements.
8. **Confirmation:** use a fresh, source-grouped holdout; run FEVEROUS or another appropriately licensed tabular evidence benchmark for external validation. Paired/bootstrap confidence intervals must cluster by originating source or claim family.
9. **Ablations and engineering:** compare plain, rubric, deterministic-only, calibrated-only, simple deferral, semantic verifier, full VARE; measure accuracy, false acceptance, false rejection, review, latency, token cost, failure rates and reproducibility.

## Primary estimand

At each prespecified human-review budget, report:

```text
FAR = count(gold non-SUPPORT claims automatically accepted as SUPPORT)
      / count(all gold non-SUPPORT claims)
```

Alongside false rejection, correct automatic accepts, review coverage, cost and semantic-versus-technical failure accounting. For "consequential" false acceptance, define and validate severity **before** measuring that endpoint.

## Required release artifacts

- Dataset lineage, checksum, data licences, generation scripts and frozen split manifests.
- Model/prompt/version metadata, temperatures, retrieved evidence packet IDs, parsed JSON and raw output logs without secrets.
- Deterministic validator unit tests and paired counterfactual cases.
- Calibration fits, policy parameters and cost-sensitivity results.
- Matched-budget results, error attribution, source-group clustered uncertainty estimates, negative results and reproducing commands.
- Independent review rubric, disagreements, limitations, and a release suitable for academic and professional peer feedback.

## Publication gate

**Do not claim full VARE validation** until the new deterministic-verification and risk-aware policies have been compared against strong baselines on fresh holdout cases; external benchmark generalisation remains a further prerequisite for general claims. Continue to publish negative results. A simpler system achieving equivalent performance at lower cost is a meaningful finding.

## Links to earlier work

- [Phase I synthetic demonstration](../README.md)
- [Phase II real-model research article](../publications/BEYOND-AGREEMENT.md)
- [SciFact protocol](../phase-2-scifact/PROTOCOL.md)
- [SciFact experiment results](../phase-2-scifact/evidence/)
