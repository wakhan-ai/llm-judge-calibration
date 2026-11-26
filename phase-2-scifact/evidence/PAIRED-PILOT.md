# SciFact 30-claim feasibility pilot

Run on 26 November 2026 with GPT-4.1 Mini through Open WebUI and OpenRouter. The fixed-seed development sample contained 10 claims per reference label and excluded the three claims used to refine the prompt. Each claim used up to five retrieved abstracts. The verifier was a separate call to the same model over rubric-cited sentences.

| Condition | False accepts / reference non-support | Reviewed | Automatic coverage |
| --- | ---: | ---: | ---: |
| Plain | 3/20 | 0/30 | 100% |
| Rubric | 3/20 | 2/30 | 93.3% |
| VARE | 3/20 | 17/30 | 43.3% |

All three accepted the same three non-support claims (268, 847, 879). The verifier allowed those decisions to stand. VARE reviewed eight of ten gold-supported claims. Across 80 calls, 73 outputs passed validation. The rubric had two invalid evidence citations and the verifier returned five invalid JSON outputs. There were zero HTTP errors. Reported inference cost totalled $0.060362.

The pilot found no reduction in false acceptance and a substantial increase in review. The policy sends rubric abstentions to review by construction. A larger evaluation needs calibrated comparisons at matched review budgets and a verifier with a different source of evidence or error. The label-balanced sample supports feasibility analysis. Its rates should not be used as deployment estimates.

[Machine-readable summary](paired-pilot-summary.json)
