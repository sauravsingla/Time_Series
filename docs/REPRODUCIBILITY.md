# Forecasting Reproducibility Guide

This guide defines the minimum information required to reproduce a time-series forecasting result from this repository.

## Reproducibility checklist

Record the following for every benchmark, experiment or published comparison:

1. Dataset name, source and version.
2. Observation frequency and timestamp timezone, when applicable.
3. Missing-value handling and resampling rules.
4. Forecast horizon and seasonal period.
5. Exact chronological train, validation and test boundaries.
6. Backtesting design: holdout, expanding window or rolling window.
7. Model name, implementation and hyperparameters.
8. Random seed for every stochastic component.
9. Software environment, Python version and dependency versions.
10. Metrics, aggregation rules and treatment of zero-valued targets.
11. Runtime environment and approximate execution time.
12. Generated artifacts, including raw predictions and benchmark tables.

## Recommended commands

Create an isolated environment and install the maintained implementation:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e '.[classical,dev]'
```

Run validation and regenerate the benchmark outputs:

```bash
ruff check src tests
ruff format --check src tests
mypy src/timeseries_reference
pytest --cov=timeseries_reference --cov-report=term-missing
time-series-benchmark \
  --output benchmark_results.csv \
  --leaderboard generated/BENCHMARK_LEADERBOARD.md
```

## Avoiding leakage

A reproducible result is not necessarily a valid result. Ensure that:

- timestamps remain ordered;
- future target values are never used to create training features;
- transformations are fitted only on each training window;
- hyperparameter selection does not use the final test period;
- missing-value treatment does not use future observations unless explicitly justified;
- recursive forecasts use only information available at each forecast origin.

## Benchmark artifact policy

Keep machine-readable predictions or metrics alongside the human-readable summary. A leaderboard alone is insufficient because it hides row-level errors, failed model runs and aggregation choices.

For a material benchmark change, document:

- why the protocol changed;
- which historical results are no longer directly comparable;
- whether model rankings changed;
- the command used to regenerate the published artifacts.

## Environment capture

For archival experiments, save an environment snapshot:

```bash
python --version
python -m pip freeze > environment.txt
```

When GPU-based models are introduced, also record CUDA, driver, accelerator and framework versions. Do not claim GPU reproducibility from CPU-only validation.

## Reporting failures

Do not silently remove models that fail on a dataset. Record the model, dataset, error category and any fallback behaviour. Transparent failures are part of a trustworthy forecasting benchmark.
