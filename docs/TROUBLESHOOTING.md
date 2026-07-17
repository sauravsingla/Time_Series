# Troubleshooting

## Installation fails while building dependencies

Upgrade packaging tools and retry inside a fresh virtual environment:

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -e '.[classical,dev]'
```

Use one of the supported Python versions: 3.10, 3.11 or 3.12.

## `time-series-benchmark` is not found

Confirm the editable install completed in the active environment:

```bash
python -m pip show time-series-reference
python -m timeseries_reference.benchmark --help
```

The module command is a useful fallback when the console-script path has not refreshed.

## A dataset cannot be loaded

The maintained datasets are supplied through `statsmodels`. Confirm the optional classical dependencies are installed and that the dataset name is one reported by the CLI help.

## A model fails on a short series

Statistical and lag-based models require enough observations for the configured lag and seasonal period. Reduce the lag, use a smaller seasonal period only when scientifically justified, or begin with naive and drift baselines.

## Metrics contain `NaN` or infinite values

Check the input series and predictions for missing or non-finite values. Do not silently fill future targets. Imputation rules must be fitted using training data only.

## Results differ from the published leaderboard

Check:

1. Python and dependency versions.
2. Dataset name and holdout horizon.
3. Whether source files have uncommitted changes.
4. Whether the complete dependency group was installed.
5. Whether the benchmark was run from the intended branch.

Regenerate both artifacts with:

```bash
time-series-benchmark \
  --output benchmark_results.csv \
  --leaderboard docs/BENCHMARK_LEADERBOARD.md
```

## CI passes locally but fails on GitHub Actions

Run the same commands used by CI:

```bash
ruff check src tests
pytest

time-series-benchmark --output benchmark_results.csv --leaderboard generated_leaderboard.md
```

Also verify that no test relies on local files, notebook state, credentials or a machine-specific path.

## The advanced model is worse than naive

Do not hide the result. Investigate horizon choice, seasonality, structural breaks, lag selection and recursive error accumulation. A simple model may genuinely be the better operational choice.
