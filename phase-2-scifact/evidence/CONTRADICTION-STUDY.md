# SciFact contradiction stress test

The 97 previously unused development claims contain 47 contradictions, 25 insufficient-evidence claims, and 25 supported claims. Every claim shares at least one referenced document with training or a previous run. Top-five retrieval found an annotated evidence document for 37 of the 47 contradictions.

| Review ranking | Contradiction false accepts left (of 47) | All false accepts left (of 72) | Correct auto-accepts (of 25) |
| --- | ---: | ---: | ---: |
| Plain GPT-4.1 Mini | 0 | 1 | 7 |
| Rubric GPT-4.1 Mini | 3 | 5 | 12 |
| GPT-4.1 Mini verifier, citations | 0 | 2 | 15 |
| GPT-4.1 Mini verifier, full abstracts | 1 | 3 | 14 |
| Gemini 2.5 Flash, citations | 1 | 3 | 14 |
| Gemini 2.5 Flash, full abstracts | 1 | 3 | 14 |
| Gemini 2.5 Pro, full abstracts | 0 | 3 | 14 |

Each ranking used 19 review slots. The rubric initially accepted three contradicted claims: 1110, 1049 and 759. Flash routed 1110 and 1049 to review; Pro routed all three. Pro's extra case, 759, was routed because its response was truncated, not because it returned a valid contradiction verdict. Claim 1110 likewise had a truncated Pro response. All eight invalid Pro outputs ended with finish_reason length. Flash returned 28/28 valid responses in each arm; Pro returned 20/28. The run made 334 calls with zero HTTP errors and cost $0.78984275.

The rankings prioritize invalid outputs, so Pro's results combine semantic verification with technical-error routing. Pro did not demonstrate better semantic contradiction detection. Only three rubric false acceptances involved contradictions, and the document overlap limits generalization. The cited-only GPT-4.1 Mini verifier achieved the same zero residual contradiction accepts with fewer overall false accepts and one more correct automatic accept than Pro in this cohort.

[Run manifest](contradiction-study-manifest.json) · [Machine-readable summary](contradiction-study-summary.json)
