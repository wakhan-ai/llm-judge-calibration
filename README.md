# LLM Judge Calibration

Reproducibility files for *Who Judges the AI Judge? A Computational Study of LLM Evaluator Calibration and Risk-Sensitive Review*.

This computational demonstration uses 600 synthetic assessment records, split into 300 development and 300 held-out records. It illustrates agreement, probability calibration, and selective human review. It contains no actual LLM calls, human reviewer judgments, or pharmaceutical review outcomes.

## Reproduce the results

Run these commands from the repository root in a Python environment:

```sh
python -m pip install -r requirements.txt
python simulate.py
```

The script uses a fixed random seed and writes `synthetic_cases.csv` and `simulation_results.csv` to the current directory.
