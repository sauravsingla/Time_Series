# Time Series Forecasting Reference

[![CI](https://github.com/sauravsingla/Time_Series/actions/workflows/ci.yml/badge.svg)](https://github.com/sauravsingla/Time_Series/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue)](pyproject.toml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Reproducible benchmark](https://img.shields.io/badge/benchmark-reproducible-brightgreen)](docs/BENCHMARK_LEADERBOARD.md)

A tested, reproducible reference for learning and applying **classical, statistical and machine-learning time-series forecasting**. It combines historical notebooks with a maintained Python package, open datasets, leakage-safe evaluation, automated tests and a cross-dataset model leaderboard.

> Start with strong baselines, validate chronologically, and adopt a more complex model only when the evidence supports it.

## Navigation

- [Benchmark leaderboard](docs/BENCHMARK_LEADERBOARD.md)
- [Benchmark methodology](docs/BENCHMARK_METHODOLOGY.md)
- [Installation and quick start](#quick-start)
- [Learning path](#recommended-learning-path)
- [Python API example](#python-api-example)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Citation](CITATION.cff)

## Why this repository is useful

Many forecasting repositories contain isolated notebooks without reliable validation or repeatable results. This project provides a stronger reference structure:

- **Traditional and modern progression:** naive baselines, autoregression, exponential smoothing and lag-based machine learning.
- **Open data:** no private files, credentials or manual downloads are required for the maintained benchmark.
- **Leakage-safe evaluation:** chronological splitting and expanding-window backtesting are built into the package.
- **Transparent comparison:** every model is assessed with MAE, RMSE and sMAPE.
- **Reproducibility:** the same command generates raw results and the published Markdown leaderboard.
- **Software quality:** Python packaging, input validation, tests, linting and multi-version CI.

## Implemented coverage

| Layer | Included capability |
|---|---|
| Baselines | Naive, seasonal naive, moving average, drift |
| Classical statistics | Autoregression, Holt-Winters exponential smoothing |
| Machine learning | Regularized lag regression with recursive forecasting |
| Evaluation | Temporal split, expanding-window backtesting, MAE, RMSE, MAPE, sMAPE |
| Data | Sunspots, Mauna Loa CO2 and US real GDP |
| Reproducibility | CLI benchmark, generated leaderboard, tests and CI artifacts |

The original notebooks remain available as historical learning material. The recommended reusable implementation lives in `src/timeseries_reference` and targets Python 3.10+.

## Benchmark leaderboard

The full per-dataset results are published in [`docs/BENCHMARK_LEADERBOARD.md`](docs/BENCHMARK_LEADERBOARD.md).

| Overall rank | Model | Average dataset rank | Dataset wins |
|---:|---|---:|---:|
| 1 | Autoregression | 2.3333 | 1 |
| 2 | Ridge lag regression | 2.6667 | 1 |
| 3 | Exponential smoothing | 3.0000 | 0 |
| 4 | Seasonal naive | 3.3333 | 0 |
| 5 | Naive | 4.3333 | 1 |
| 6 | Drift | 5.3333 | 0 |

Models are ranked by RMSE within each dataset and then by average dataset rank. Raw errors are not averaged across datasets because GDP, CO2 and sunspot values have different scales. The methodology is documented in [`docs/BENCHMARK_METHODOLOGY.md`](docs/BENCHMARK_METHODOLOGY.md).

The naive model winning the real-GDP dataset is intentionally retained. A trustworthy benchmark reports the evidence instead of assuming a more complex model must win.

## Open datasets

All maintained benchmark datasets are loaded through `statsmodels`.

| Dataset | Frequency | Main forecasting challenge | Seasonal period |
|---|---|---|---:|
| Sunspots | Annual | Long cycles and changing amplitude | 11 |
| Mauna Loa CO2 | Weekly | Trend, missing observations and yearly seasonality | 52 |
| US real GDP | Quarterly | Economic trend and structural change | 4 |

These series intentionally represent different behaviours rather than repeating one favourable data pattern.

## Quick start

```bash
git clone https://github.com/sauravsingla/Time_Series.git
cd Time_Series
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e '.[classical,dev]'
```

Run the complete validation suite:

```bash
ruff check src tests
pytest
time-series-benchmark \
  --output benchmark_results.csv \
  --leaderboard docs/BENCHMARK_LEADERBOARD.md
```

Run only one dataset:

```bash
time-series-benchmark \
  --dataset co2 \
  --output co2_results.csv \
  --leaderboard co2_leaderboard.md
```

The command writes a machine-readable CSV and a human-readable Markdown leaderboard. CI repeats the workflow on Python 3.10, 3.11 and 3.12 and uploads both outputs as artifacts.

## Python API example

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

## Recommended learning path

### 1. Understand the signal

Study frequency, missing values, trend, seasonality, cycles, structural breaks and forecast horizon before selecting a model.

### 2. Establish baselines

Run naive, seasonal-naive, moving-average and drift forecasts. These define the minimum standard that advanced approaches should beat.

### 3. Add statistical models

Use autoregression and Holt-Winters when lag dependence, trend or repeated seasonal structure is visible.

### 4. Build leakage-safe machine learning

Create lag features only from past observations. Fit preprocessing exclusively on each training window and use recursive or direct strategies deliberately.

### 5. Evaluate over time

A single holdout is useful for a compact benchmark. Final model selection should use rolling or expanding-window backtesting and inspect residual behaviour.

### 6. Introduce advanced architectures only when justified

LSTM, GRU, N-BEATS, N-HiTS, Temporal Fusion Transformer and PatchTST can be valuable for suitable datasets, but they should be compared against strong simple baselines and evaluated for latency, stability and retraining cost.

## Evaluation principles

1. Never randomly shuffle a forecasting target.
2. Fit transformations and feature generation only on training data.
3. Compare every advanced model with naive and seasonal-naive baselines.
4. Report multiple metrics because no single score captures every error pattern.
5. Use rolling or expanding-window evaluation for final decisions.
6. Record horizon, frequency, runtime and retraining cost alongside accuracy.
7. Surface model failures instead of silently removing them from results.
8. Treat complexity as a cost that must be justified by repeatable improvement.

## Repository structure

```text
.
├── docs/
│   ├── BENCHMARK_LEADERBOARD.md   # generated overall and per-dataset rankings
│   └── BENCHMARK_METHODOLOGY.md   # evaluation and ranking protocol
├── src/timeseries_reference/      # maintained forecasting package
├── tests/                         # unit and integration tests
├── .github/workflows/ci.yml       # lint, tests and benchmark execution
├── *.ipynb                        # historical worked examples
├── CONTRIBUTING.md                # contribution and reproducibility standard
├── SECURITY.md                    # private vulnerability reporting guidance
├── CITATION.cff                   # citation metadata
└── pyproject.toml                 # packaging, dependencies and CLI entry point
```

## Roadmap

The next high-value extensions are:

- ARIMA and SARIMA with order selection and residual diagnostics;
- gradient boosting with calendar and rolling features;
- probabilistic intervals, quantile loss and calibration evaluation;
- multivariate VAR and VECM pipelines;
- intermittent-demand forecasting;
- hierarchical forecasting and reconciliation;
- anomaly detection from forecast residuals;
- carefully benchmarked LSTM, N-BEATS and PatchTST references.

A method should move from roadmap to maintained code only when it has tests, an open dataset, leakage-safe evaluation and reproducible benchmark results.

## Notebook status

Some historical Colab notebooks were created with older library versions and metadata. They are retained for provenance and learning context. The tested package and benchmark are the recommended reference implementation for new work.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a change. Contributions should focus on one clear forecasting problem and include tests, an open dataset or deterministic fixture, baseline comparison and documented limitations.

Community participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Security-sensitive concerns should follow [`SECURITY.md`](SECURITY.md).

## Citation

GitHub can generate citation formats from [`CITATION.cff`](CITATION.cff). Cite the repository when its implementation, benchmark or teaching structure supports published work.

## License

Released under the [MIT License](LICENSE).
