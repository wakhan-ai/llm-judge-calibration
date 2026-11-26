# Proposed experiment protocol

## Question

Does an explicit evidence rubric, with an independent verification layer and a review policy, reduce acceptance of unsupported or contradicted claims at the same review budget? Which components contribute to the result?

## Inputs and split

Use SciFact first. Keep claim IDs, document IDs, annotated verdicts and evidence references in the scoring pipeline. Send claim and evidence text to the judge without gold labels or gold rationale positions. Use the exact same model, evidence packet and decoding parameters for paired prompt conditions. Use independent stateless requests and log the prompt version, configured model, provider metadata where returned, raw response, latency, and parsing status. Treat timeouts and invalid output as separately reported failures.

Reserve grouped partitions for prompt development, calibration and final evaluation. Build groups from connected components of claims and cited or annotated evidence documents, then verify there is no overlap. Report class counts and any imbalance before freezing the split. Avoid fitting or tuning on final evaluation labels. One case is a format check. A 30-claim paired pilot can establish operational feasibility. A larger holdout is required for calibration and uncertainty estimates.

## Comparisons

1. Plain judge with a fixed output schema.
2. Same judge with an explicit rubric for entailment, contradiction, and insufficient evidence, including population, endpoint, units and time.
3. Rubric judge with an independent verifier. Report deterministic checks alone and hybrid results. Treat a mismatch as grounds for review unless the verifier has enough context to establish contradiction. Include paired valid and altered numerical claims and irrelevant-evidence removal controls.
4. Calibration fit on the calibration partition. Request probabilities for SUPPORT, CONTRADICT and INSUFFICIENT_EVIDENCE and validate the schema and probability sum. Score uncalibrated and calibrated outputs on the frozen holdout.
5. Selective review with common and category-specific thresholds at matched review budgets. Freeze categories and costs before final scoring and report sensitivity to those costs.
6. Remove each component in turn. Compare retrieved top-k evidence with an oracle evidence condition for claims with annotated evidence. Compute paired comparisons on identical claims. Include no-evidence claims in retrieved-condition classification and report them separately.
7. Repeat external evaluations on FEVER and FEVEROUS once acquired. FEVEROUS supports both table and sentence evidence.

## Outputs and interpretation

Report confusion matrices, the count and rate of non-SUPPORT gold claims accepted as SUPPORT, and the count and rate of contradicted claims missed. Distinguish refusal or review from an automatic acceptance. Report false rejection and automation coverage alongside error rates. Add multiclass Brier score, reliability plots, calibration error with stated bins, risk-coverage curves, and paired document-group bootstrap intervals. Define minimum meaningful gains and review budgets before the full run. Preserve negative results and report any unsupported categories. Public fact-verification benchmarks do not supply regulatory severity or qualified MLR decisions.

## Run status

Dataset integrity and lexical retrieval were verified. The inference service was smoke-tested in chat. Pending work includes the paired benchmark runner, judge inference, independent verification, held-out calibration, and external benchmark validation.

## Implementation details to freeze before collecting holdout predictions

- Commit a split manifest with claim ID, document-component ID, partition and reference-label counts. A component follows every cited and annotated document edge, including edges for claims with no annotated evidence. If a large component prevents a usable split, document the imbalance and designate a separate validation dataset before tuning.
- Use three explicit verdicts: `SUPPORT`, `CONTRADICT`, and `INSUFFICIENT_EVIDENCE`. The shared JSON schema contains the verdict, probabilities for all three labels summing to 1 within a stated tolerance, and an evidence list of document and zero-based sentence IDs drawn from the packet. Validate all IDs and require evidence for a definitive verdict. A structurally valid citation still requires semantic verification.
- For the VARE condition, first validate schema and citations, then run an independent evidence check against the cited text. Log deterministic validation and the independent verdict separately. A malformed response or unresolved disagreement sends a claim to review. Keep this condition paired with the rubric-only condition on the same claim, evidence and model settings.
- At each prespecified review budget, calculate false acceptance as automatic SUPPORT decisions on gold non-SUPPORT claims divided by all gold non-SUPPORT claims. Also report errors among automatically accepted claims and the fraction resolved automatically. Report the count sent to review and the count of failed requests. Fit calibration only on its designated partition and compute uncertainty over document components with each claim's paired results kept intact.
