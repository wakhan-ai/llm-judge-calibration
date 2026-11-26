# Phase II SciFact evaluation

This package records the verified benchmark source, completed retrieval experiment, and proposed judge experiment. Run the retrieval baseline from this directory with Python 3.10 or later. The retrieval script uses only the standard library.

```sh
python scifact_retrieval_pilot.py data/scifact-data.tar.gz
```

See [PROTOCOL.md](PROTOCOL.md) for the comparison design and [DATA.md](DATA.md) for provenance. See [OPEN-WEBUI.md](OPEN-WEBUI.md) for the Windows setup, observed provider smoke test, and path to a repeatable API run. Machine-readable retrieval results are in [evidence/retrieval-results.json](evidence/retrieval-results.json).

## Observed evidence

- The archive contained 5,183 abstracts, 809 labelled training claims, 300 labelled development claims, and 300 test claims without public reference labels.
- The development set contains 124 supported claims, 64 contradicted claims, and 112 claims with no annotated evidence.
- Among the 188 development claims with annotated evidence, title-only TF-IDF returned at least one annotated document in the top five for 115 claims. Title plus abstract did so for 168 claims, a gain of 28.2 percentage points. The paired claim-bootstrap interval is 21.8 to 35.1 points. That interval assumes claim-level resampling and may be too narrow when claims share a document.
- Title plus abstract retrieved an annotated document for 53 of 64 contradicted claims. The retrieval experiment used all abstracts as the search index and used no supervised training.
- Training and development share 181 cited or annotated evidence documents. Of the 300 development claims, 104 have no such overlap with training, including 64 of the 188 evidence-bearing claims.
- Open WebUI on Windows returned "OpenRouter connection works" from inclusionAI Ling 3.2 Flash (free) in response to a short test prompt. This is an observed connectivity check. No SciFact verdicts, calibration fits, or VARE comparisons were run.

The retrieval hit rates concern annotated document retrieval. They measure neither sentence-level evidence selection nor verifier accuracy. The 112 claims with no annotated evidence are outside the retrieval hit-rate denominator.
