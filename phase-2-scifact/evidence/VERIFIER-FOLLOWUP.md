# SciFact verifier follow-up

Fifteen fresh development claims, balanced across the three reference labels. Review budget: three claims per condition. GPT-4.1 Mini was the judge. The verifier variants crossed GPT-4.1 Mini and Gemini 2.5 Flash with cited sentences and full retrieved abstracts.

Neither baseline accepted a reference non-support claim before review. All six conditions ended at 0 false acceptances out of 10 reference non-support claims. The rubric and all four verifier variants selected the same three claims because invalid rubric citations consumed the review budget. The plain arm retained one automatic true acceptance and the rubric-based arms retained three, out of five reference support claims.

All 42 calls returned without HTTP errors. Under the original parser, the plain arm had one invalid citation, the rubric had three, and the six Gemini outputs failed strict JSON parsing. An exploratory offline check stripped the enclosing Markdown fences and all six Gemini responses validated against their evidence packets. This check did not change the recorded run. In one case, Gemini changed from insufficient evidence on cited sentences to support on full evidence. That case was reference support, and neither arm selected it for review in the recorded run. Reported cost: $0.0325492.

This development sample did not test whether the verifier detects false acceptances present in baseline scores. A grouped holdout with enough baseline errors to evaluate routing is still pending.
