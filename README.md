# Python Time-Series Forecasting Benchmark with Walk-Forward Backtesting

[![CI](https://github.com/sauravsingla/Time_Series/actions/workflows/ci.yml/badge.svg)](https://github.com/sauravsingla/Time_Series/actions/workflows/ci.yml)
[![Link check](https://github.com/sauravsingla/Time_Series/actions/workflows/link-check.yml/badge.svg)](https://github.com/sauravsingla/Time_Series/actions/workflows/link-check.yml)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue)](pyproject.toml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Reproducible benchmark](https://img.shields.io/badge/benchmark-reproducible-brightgreen)](docs/BENCHMARK_LEADERBOARD.md)

A tested and reproducible reference for **Python time-series forecasting with walk-forward validation**, **forecasting backtesting**, **rolling-origin evaluation**, **statistical forecasting**, and **machine-learning model comparison**.

The repository combines a maintained Python package, open datasets, leakage-safe chronological validation, automated tests and a cross-dataset forecasting benchmark. It is relevant to sales forecasting, demand forecasting, economic forecasting, energy-load forecasting, traffic forecasting, capacity planning and forecast-based anomaly detection.

> Start with strong baselines, validate chronologically, and adopt a more complex model only when the evidence supports it.

## Find the right forecasting resource

| Goal | Start here |
|---|---|
| Search forecasting models, metrics or validation methods | [Forecasting methods and evaluation index](docs/FORECASTING_METHODS_INDEX.md) |
| Learn Python time-series forecasting | [Practical forecasting guide](docs/time-series-forecasting-guide.md) |
| Choose a model for sales, demand or economic forecasting | [Model selection and use cases](docs/model-selection-and-use-cases.md) |
| Compare forecasting models | [Benchmark leaderboard](docs/BENCHMARK_LEADERBOARD.md) |
| Understand walk-forward validation and backtesting | [Benchmark methodology](docs/BENCHMARK_METHODOLOGY.md) |
| Reproduce a result correctly | [Reproducibility standard](docs/REPRODUCIBILITY.md) |
| Resolve common forecasting questions | [FAQ](docs/FAQ.md) |
| Fix installation or runtime issues | [Troubleshooting](docs/TROUBLESHOOTING.md) |
| Learn forecasting terminology | [Glossary](docs/GLOSSARY.md) |
| Browse all documentation | [Documentation hub](docs/README.md) |

## Forecasting use cases

| Use case | Typical challenges | Suitable starting points |
|---|---|---|
| Sales forecasting | promotions, holidays, changing demand | seasonal naive, Holt-Winters, lag regression |
| Demand forecasting | calendar effects, stockouts, intermittent demand | seasonal baselines, exponential smoothing, machine learning |
| Financial forecasting | non-stationarity, regime changes, weak signal | naive, drift, autoregression, strict backtesting |
| Energy-load forecasting | weather effects, peaks, multiple seasonalities | seasonal baselines, exogenous regression, neural models when justified |
| Traffic and capacity forecasting | spikes, missing data, operational constraints | moving average, autoregression, lag regression |
| Economic forecasting | structural breaks, revisions, long horizons | drift, autoregression, ARIMA, VAR |
| Inventory forecasting | intermittent demand, service levels, lead time | seasonal naive, Croston-family methods, probabilistic forecasts |
| Anomaly detection | changing baseline and threshold calibration | residuals from validated forecasting models |

## Why this repository is useful

Many forecasting repositories contain isolated notebooks without reliable validation or repeatable results. This project provides:

- **Traditional-to-modern progression:** naive baselines, autoregression, exponential smoothing and lag-based machine learning.
- **Open data:** no private files, credentials or manual downloads are required for the maintained benchmark.
- **Leakage-safe evaluation:** chronological splitting and expanding-window backtesting are built into the package.
- **Transparent comparison:** every model is assessed with MAE, RMSE and sMAPE.
- **Reproducibility:** one command generates raw results and the published Markdown leaderboard.
- **Software quality:** Python packaging, input validation, tests, linting and multi-version CI.
- **Honest reporting:** weak models and simple-model wins remain visible rather than being removed.

## Implemented forecasting coverage

| Layer | Included capability |
|---|---|
| Baselines | Naive, seasonal naive, moving average, drift |
| Classical statistics | Autoregression, Holt-Winters exponential smoothing |
| Machine learning | Regularized lag regression with recursive forecasting |
| Evaluation | Temporal split, expanding-window backtesting, MAE, RMSE, MAPE, sMAPE |
| Open datasets | Sunspots, Mauna Loa CO2 and US real GDP |
| Reproducibility | CLI benchmark, generated leaderboard, tests and CI artifacts |

The recommended reusable implementation lives in `src/timeseries_reference` and targets Python 3.10+.

## Benchmark leaderboard

The complete overall and per-dataset results are published in [`docs/BENCHMARK_LEADERBOARD.md`](docs/BENCHMARK_LEADERBOARD.md).

| Overall rank | Model | Average dataset rank | Dataset wins |
|---:|---|---:|---:|
| 1 | Autoregression | 2.3333 | 1 |
| 2 | Ridge lag regression | 2.6667 | 1 |
| 3 | Exponential smoothing | 3.0000 | 0 |
| 4 | Seasonal naive | 3.3333 | 0 |
| 5 | Naive | 4.3333 | 1 |
| 6 | Drift | 5.3333 | 0 |

Models are ranked by RMSE within each dataset and then by average dataset rank. Raw errors are not averaged across datasets because GDP, CO2 and sunspot values have different scales.

The naive model winning the real-GDP dataset is intentionally retained. A trustworthy benchmark reports evidence instead of assuming a more complex model must win.

## Open forecasting datasets

All maintained benchmark datasets are loaded through `statsmodels`.

| Dataset | Frequency | Main forecasting challenge | Seasonal period |
|---|---|---|---:|
| Sunspots | Annual | Long cycles and changing amplitude | 11 |
| Mauna Loa CO2 | Weekly | Trend, missing observations and yearly seasonality | 52 |
| US real GDP | Quarterly | Economic trend and structural change | 4 |

## Quick start

```bash
git clone https://github.com/sauravsingla/Time_Series.git
cd Time_Series
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e '.[classical,dev]'
```

Run the complete validation and benchmark workflow:

```bash
ruff check src tests
pytest
time-series-benchmark \
  --output benchmark_results.csv \
  --leaderboard docs/BENCHMARK_LEADERBOARD.md
```

Run one dataset:

```bash
time-series-benchmark \
  --dataset co2 \
  --output co2_results.csv \
  --leaderboard co2_leaderboard.md
```

The command writes a machine-readable CSV and a human-readable Markdown leaderboard. CI repeats the workflow on Python 3.10, 3.11 and 3.12.

## Python forecasting API example

```python
from timeseries_reference.benchmark import benchmark_dataset
from timeseries_reference.datasets import load_dataset
from timeseries_reference.leaderboard import render_leaderboard
from timeseries_reference.ml import LagRegressionForecaster

sunspots = load_dataset("sunspots")
train = sunspots.values[:-12]

model = LagRegressionForecaster(lags=11).fit(train)
forecast = model.predict(horizon=12)
print(forecast)

comparison = benchmark_dataset("sunspots")
print(comparison[["model", "rmse", "smape"]])
print(render_leaderboard(comparison))
```

## Model-selection path

1. Understand frequency, missing values, trend, seasonality, cycles, structural breaks and forecast horizon.
2. Establish naive, seasonal-naive, moving-average and drift baselines.
3. Add autoregression and Holt-Winters where lag dependence, trend or stable seasonality exists.
4. Build leakage-safe machine-learning features using only past information.
5. Evaluate with chronological holdouts and rolling or expanding-window backtesting.
6. Introduce LSTM, GRU, N-BEATS, N-HiTS, Temporal Fusion Transformer or PatchTST only when justified by data scale and repeatable improvement.

## Evaluation principles

1. Never randomly shuffle a forecasting target.
2. Fit transformations and feature generation only on training data.
3. Compare advanced models with naive and seasonal-naive baselines.
4. Report several metrics because no single score captures every error pattern.
5. Match the validation horizon to the real operational forecast horizon.
6. Record runtime, retraining cost and stability alongside accuracy.
7. Surface model failures instead of silently removing them.
8. Treat complexity as a cost that must be justified by repeatable improvement.

## Search topics covered

This repository is relevant to:

- walk-forward validation for Python time-series forecasting;
- Python time-series forecasting examples and benchmarks;
- forecasting backtesting and rolling-origin evaluation;
- expanding-window evaluation and time-series cross-validation;
- leakage-safe and chronological forecasting validation;
- autoregression and Holt-Winters exponential smoothing;
- ARIMA and SARIMA model-selection concepts;
- machine-learning forecasting with lag features;
- recursive multi-step forecasting;
- LSTM, GRU, N-BEATS, N-HiTS, TFT and PatchTST evaluation;
- sales, demand, inventory and energy forecasting;
- economic and financial time-series forecasting;
- probabilistic forecasting and prediction intervals;
- intermittent-demand forecasting;
- forecast-based anomaly detection;
- forecast accuracy metrics including MAE, RMSE, MAPE, sMAPE and MASE.

## Roadmap

High-value future extensions include:

- ARIMA and SARIMA with residual diagnostics;
- gradient boosting with calendar and rolling features;
- probabilistic intervals, quantile loss and calibration;
- multivariate VAR and VECM pipelines;
- intermittent-demand forecasting;
- hierarchical forecasting and reconciliation;
- anomaly detection from forecast residuals;
- carefully benchmarked LSTM, N-BEATS and PatchTST references.

A method should move from roadmap to maintained code only when it has tests, an open dataset, leakage-safe evaluation and reproducible benchmark results.

## Project status

This is a reference and teaching implementation, not a turnkey production forecasting service. Production systems additionally require data contracts, monitoring, retraining policy, prediction intervals, alerting, rollback, access controls and domain-specific acceptance thresholds.

Historical Colab notebooks remain available for provenance and learning context, while the tested package and benchmark are the recommended path for new work.

## Contributing, citation and license

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a change. Use [`SUPPORT.md`](SUPPORT.md) for help and [`SECURITY.md`](SECURITY.md) for security-sensitive concerns.

GitHub can generate citation formats from [`CITATION.cff`](CITATION.cff). Cite the repository when its implementation, benchmark or teaching structure supports published work.

Released under the [MIT License](LICENSE).