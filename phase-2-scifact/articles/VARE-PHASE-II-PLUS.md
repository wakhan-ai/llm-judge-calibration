# VARE Research Phase II+ — Completing the Missing Evidence Before Publication

**Status:** Proposed and testable follow-up experiments — not completed findings.  
**Companion empirical article:** [Beyond Agreement](BEYOND-AGREEMENT.md)  
**Related earlier work:** [Phase I synthetic calibration](../../README.md) · [Phase II SciFact](../README.md)

## Motivation: convert expert concerns into falsifiable tests

| Concern raised in discussion | Required test | Primary failure mode to report |
|---|---|---|
| Judge agrees on average yet accepts wrong claims | Paired valid/invalid examples; targeted contradiction cohorts | Non-SUPPORT automatically accepted as SUPPORT |
| Errors carry different consequences | Independently rated severity and matched-budget threshold policies | Cost-sensitive misses and false alarms |
| Numerical accuracy needs independent checks | Deterministic verifier with population, endpoint, time, quantity, denominator and unit | Wrong value or context passes checks |
| Evidence removal may trigger unhelpful hesitancy | Remove one of two adequate sources, the last adequate source, and irrelevant sources | Wrong revision **and** wrong stability |
| Same-family judges can share errors | Same-model, different-model and deterministic comparisons | Joint wrong agreement, not just mean accuracy |
| Review and formatting can camouflage failure | Track semantic verdict, invalid JSON/citation, truncation, timeout, escalation separately | Spurious improvements from abstention |

## Research question and primary endpoint

At equal human-review budget, does a hybrid evidence verification architecture reduce **non-SUPPORT false automatic acceptance** compared with the strongest simple baseline on a fresh, document-grouped holdout? Secondary endpoints: contradiction-specific false accepts; correct automatic support; false rejection; review and invalid-output rates; accuracy–coverage/risk–coverage curves; latency and cost.

Public SciFact labels **do not define regulatory severity**. Until external severity adjudication, call the primary metric 'non-SUPPORT false acceptance', not a validated measure of consequential or MLR risk.

Define FAR = (# non-SUPPORT claims automatically accepted as SUPPORT)/(# reference non-SUPPORT claims), and report separately the error fraction among automatic SUPPORT decisions and automatic coverage. Human review is not counted as correct automatic judgment.

## Work packages and prespecified controls

### WP1. Dataset lineage and untouched evaluation

- Use [SciFact provenance](../DATA.md) and preserve exact source and archive hashes.
- Partition by connected components of shared claim–evidence document IDs and adversarial family IDs, not random record rows.
- Treat all cases used to refine the current prompts as development data. The 41-claim and 97-claim cohorts have already been inspected; **do not rebrand them as a new untouched confirmatory holdout**.
- Run a fresh grouped evaluation; add a genuinely external dataset (FEVEROUS for table-plus-text evidence) when licences and labels are validated.
- Precompute cohort composition and a minimum effect/power or precision target. Report class counts and dependence.

### WP2. Grounded deterministic numeric/context verifier

- Create text-grounded source records with study, cohort, endpoint, numerator, denominator, time, units, value, provenance offsets and version.
- Check equations, denominators, normalised units, temporal and population matching; audit semantic extraction separately.
- **Oracle-structure condition:** rules receive gold structured fields.
- **End-to-end condition:** rules receive parser/LLM-extracted fields with extraction errors measured.
- Include valid controls, subtle substitutions, missing values, misleading but numerically matching claims and source ambiguity; treat unsupported parsing as REVIEW, never silent PASS.
- Compare rules-only, judge-only, LLM-verifier and combined approaches.

### WP3. Counterfactual evidence sensitivity **and stability**

For each eligible claim build a provenance-controlled family:
1. Original sufficient evidence.
2. Remove one of two genuinely independent adequate sources: expected SUPPORT stays SUPPORT.
3. Remove the last sufficient source: expected verdict changes to INSUFFICIENT_EVIDENCE, unless remaining evidence contradicts it.
4. Remove irrelevant retrieved text: expected verdict remains unchanged.
5. Insert a conflicting/replaced source: expected response respects relevance, source quality and disagreement.

Annotate expected outcome independently; ensure 'two sources' are not merely duplicates of the same study. Report appropriate stability, appropriate revision, unhelpful abstention and false confidence separately. Do not treat **any** answer change as success.

### WP4. Calibration and severity

- Obtain per-class model probabilities with a validated JSON schema and track invalid outputs.
- Fit calibrators on a **separate grouped calibration cohort** and evaluate on fresh grouped test data; report multiclass Brier score, reliability diagrams and documented calibration binning.
- Obtain severity ratings from multiple suitably qualified reviewers with an adjudication procedure; publish their agreement and uncertainty.
- Compare common thresholds, severity-stratified thresholds and an expected-cost policy under **identical review quotas**. Publish multiple plausible cost weight schemes and sensitivity analyses.
- Never imply synthetic severity weights are established real-world patient, legal or regulatory costs.

### WP5. Independence, ablation and operations

- Same-model versus different-provider model versus deterministic-only; quantify pairwise joint errors and disagreement resolution.
- Hold claim, retrieved packet, prompt version, decoding and review budget fixed wherever comparing paired arms.
- Ablate rubric, rules, independent verifier, calibrated risk, evidence stability gating.
- Distinguish semantically correct rejection from refusal, formatting errors, invalid IDs, length truncation, rate limits and human review.
- Record model id, provider route, UTC time, cost, tokens, prompt+packet hash, raw responses and exceptions without committing secrets.

### WP6. Statistics and reproducibility

- Report matched-claim paired counts and confidence intervals from bootstrap resampling over independent document/case-family components; use exact paired tests where suitable.
- State null hypothesis, single primary endpoint, minimum practical gain and review budgets before final scoring; treat exploratory comparisons as such.
- Publish metric computation code, frozen manifests, requirements/environment lock, checksums, raw predictions permitted by provider terms, plots and negative findings.
- Re-run from a clean environment; where APIs are stochastic, disclose repeatability limits.

## Candidate output figures

1. False acceptance and correct automatic acceptance by architecture with paired uncertainty.
2. Risk–coverage curve at matched review budgets.
3. Per-class calibration reliability and Brier scores.
4. Oracle vs end-to-end numeric verifier confusion matrices.
5. Evidence-removal stability/revision matrix.
6. Joint model failure and verifier-ablation breakdown.
7. Token cost, latency and review workload per accepted claim.

## Decision gates for a results publication

A claims-based VARE superiority paper is appropriate **only if** an untouched grouped evaluation demonstrates improvement over the strongest simpler baseline at equal review budgets, with uncertainty, false alarms and cost reported. Where results are mixed, publish them as mixed. Unvalidated deterministic checks, synthetic severity and informal expert opinion must not be described as verified improvements.

## Links to LinkedIn research articles

- Earlier LinkedIn article: *Who Judges the AI Judge?* — add its actual URL when confirmed.
- Current article: [Beyond Agreement: What Real LLM Judge Experiments Reveal About Evidence, Verification and Risk](https://www.linkedin.com/pulse/beyond-agreement-what-real-llm-judge-experiments-reveal-waheed-abbas-lyfne/).
- Proposed subsequent article: *VARE Research Phase II+ — Completing the Missing Evidence Before Publication* — this is a **research programme**, not a completed experimental report. Update with measured findings and the eventual article URL after experiments.

