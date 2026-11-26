# SciFact document-disjoint evaluation

The 41-claim subset excludes prior experimental claims and shares no cited or annotated documents with training or earlier experimental claims. Retrieval still searches the shared abstract corpus. The subset contains 21 support, 19 insufficient-evidence and one contradiction reference label.

Each method receives eight review slots. Correct accepts are gold-support claims accepted automatically.

| Method | False accepts after review (of 20) | Correct accepts (of 21) |
| --- | ---: | ---: |
| Plain GPT-4.1 Mini | 2 | 13 |
| Rubric GPT-4.1 Mini | 2 | 17 |
| GPT-4.1 Mini verifier, citations | 2 | 17 |
| GPT-4.1 Mini verifier, full abstracts | 2 | 17 |
| Gemini 2.5 Flash verifier, citations | 2 | 17 |
| Gemini 2.5 Flash verifier, full abstracts | 1 | 18 |

The rubric accepted two reference non-support claims before review. The full-evidence Gemini arm routed claim 507 to review and missed claim 1226. Both were labelled insufficient evidence. The plain arm also flagged 507, while leaving a different second false acceptance. Relative to rubric alone, the full-evidence Gemini arm reviewed one fewer correct acceptance at the same eight-slot budget. Six rubric outputs, two cited-only GPT verifier outputs, and two cited-only Gemini outputs failed validation. There were 166 model calls, zero HTTP errors, and $0.1246193 in reported cost.

The matched-budget result rests on one changed false acceptance relative to rubric alone. With one reference contradiction, the cohort does not establish contradiction-detection performance.

[Run manifest](verifier-holdout-manifest.json) · [Machine-readable summary](verifier-holdout-summary.json)
