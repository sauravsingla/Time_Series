# Benchmark Methodology

This document defines how forecasting results in this repository are produced and interpreted.

## Objective

The benchmark is designed to answer a practical question: which model performs consistently across time series with different scales and structures while remaining reproducible and leakage-safe?

It is not intended to claim universal state-of-the-art performance.

## Datasets

The maintained benchmark currently uses three open datasets distributed through `statsmodels`:

| Dataset | Frequency | Target pattern | Seasonal period |
|---|---|---|---:|
| Sunspots | Annual | Cycles with changing amplitude | 11 |
| Mauna Loa CO2 | Weekly | Trend and yearly seasonality | 52 |
| US real GDP | Quarterly | Macroeconomic trend and structural change | 4 |

Each dataset is loaded through code, converted to finite numeric values and checked for sufficient history.

## Models

The benchmark compares several model families:

- naive last-value forecast;
- seasonal-naive forecast;
- drift forecast;
- autoregression;
- Holt-Winters exponential smoothing;
- ridge regression over lag features.

Simple models are deliberately included because advanced methods should not be considered useful unless they improve on appropriate baselines.

## Evaluation protocol

1. Observations retain their original order.
2. The final chronological block is held out for evaluation.
3. No test observation is used during fitting or feature generation.
4. Every model predicts the same horizon for a dataset.
5. Failures should surface in CI rather than being silently removed from the leaderboard.

The default horizon is based on the seasonal period and available history. This keeps evaluation meaningful across frequencies while avoiding excessively small training windows.

## Metrics

### MAE

Mean absolute error reports the average absolute forecast error in the original unit. It is easy to interpret but cannot be averaged fairly across differently scaled datasets.

### RMSE

Root mean squared error penalizes larger misses more strongly. RMSE is the primary metric used to rank models within each dataset.

### sMAPE

Symmetric mean absolute percentage error provides an additional scale-normalized view. It is reported as supporting evidence and used as a tie-breaker in the overall leaderboard.

## Overall leaderboard

Raw errors from different datasets are not averaged. GDP values are numerically much larger than CO2 or sunspot values, so averaging RMSE would make the largest-scale series dominate.

Instead:

1. models receive an RMSE rank within each dataset;
2. those per-dataset ranks are averaged;
3. lower average rank is better;
4. dataset wins and average sMAPE provide additional context.

This is a transparent, scale-independent comparison. It rewards consistency rather than one exceptional result on a single series.

## Reproducing results

```bash
pip install -e '.[classical,dev]'
time-series-benchmark \
  --output benchmark_results.csv \
  --leaderboard docs/BENCHMARK_LEADERBOARD.md
```

The CSV contains complete numerical results. The Markdown file contains the human-readable leaderboard.

## Interpretation cautions

- A leaderboard winner is not automatically the best production model.
- Operational latency, retraining cost, forecast horizon and uncertainty requirements also matter.
- A single holdout is useful for a compact reference benchmark, but final model selection should use rolling or expanding-window backtesting.
- Hyperparameter tuning must be performed inside the training period, never against the final test block.
- Results can change when dependency versions, model defaults or dataset preprocessing change; such changes should be documented.

## Extending the benchmark

A new model should be deterministic, tested, documented and evaluated on every supported dataset. A new dataset should add a genuinely different forecasting challenge and include clear source, frequency, target and seasonal metadata.
