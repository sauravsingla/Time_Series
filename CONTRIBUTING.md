# Contributing

Thank you for helping improve this forecasting reference.

## Contribution standard

A contribution should solve one clearly defined time-series problem and include:

- a reproducible open dataset or a deterministic synthetic fixture;
- a simple baseline that the proposed method must beat or explain;
- chronological validation with no future-data leakage;
- tests covering expected behaviour and invalid inputs;
- documentation describing assumptions, limitations and appropriate use;
- compatibility with the supported Python versions.

## Development setup

```bash
git clone https://github.com/sauravsingla/Time_Series.git
cd Time_Series
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e '.[classical,dev]'
```

Run the quality checks before opening a pull request:

```bash
ruff check src tests
pytest
time-series-benchmark \
  --output benchmark_results.csv \
  --leaderboard docs/BENCHMARK_LEADERBOARD.md
```

## Adding a forecasting model

1. Implement a small estimator with `fit(values)` and `predict(horizon)` methods.
2. Validate dimensions, finite values, minimum history and model parameters.
3. Add it to the benchmark only when it can run deterministically on every supported Python version.
4. Add focused tests and compare it with naive and seasonal-naive forecasts.
5. Explain where the method is likely to fail.

## Adding a dataset

Datasets must be public, redistributable or loaded from a stable public Python package. Document the source, frequency, target variable, seasonal period, preprocessing and licence constraints. Never commit credentials, private transaction data or personally identifiable information.

## Pull-request scope

Keep pull requests reviewable. Prefer one model, dataset, evaluation feature or documentation improvement per pull request. Avoid mixing notebook formatting changes with production-code changes.

## Commit style

Use short, descriptive commits such as:

- `add seasonal MASE metric`
- `benchmark gradient boosting`
- `document rolling validation`

## Reproducibility checklist

Before requesting review, confirm that:

- random seeds are fixed where relevant;
- data are split chronologically;
- preprocessing is fitted only on training data;
- reported scores can be regenerated from a command;
- benchmark failures are visible rather than silently skipped;
- new public APIs have docstrings and tests.
