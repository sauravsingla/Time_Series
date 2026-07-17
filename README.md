# Time Series Forecasting Reference

A practical, tested collection of **traditional, statistical and machine-learning time-series methods**. The repository is designed as an outside-world reference: reproducible datasets, leakage-safe evaluation, strong baselines, reusable Python code and CI-generated benchmark results.

## Implemented coverage

| Layer | Included methods |
|---|---|
| Baselines | Naive, seasonal naive, moving average, drift |
| Classical statistics | Autoregression, Holt-Winters exponential smoothing |
| Machine learning | Regularized lag regression with recursive forecasting |
| Evaluation | Temporal split, expanding-window backtesting, MAE, RMSE, MAPE, sMAPE |
| Reproducibility | Open datasets, command-line benchmark, tests and CI artifacts |

The original notebooks remain as historical learning material. New maintained code lives in `src/timeseries_reference` and targets Python 3.10+.

## Open datasets

The benchmark uses datasets distributed through `statsmodels`, so no private data, credentials or manual downloads are required.

| Dataset | Frequency | Main pattern | Default seasonality |
|---|---:|---|---:|
| Sunspots | Annual | Long cycles and changing amplitude | 11 |
| Mauna Loa CO2 | Weekly | Strong trend and yearly seasonality | 52 |
| US real GDP | Quarterly | Economic trend and structural change | 4 |

These datasets exercise different forecasting problems rather than repeatedly testing models on one convenient series.

## Repository structure

```text
.
├── src/timeseries_reference/   # reusable forecasting package
├── tests/                      # deterministic unit and integration tests
├── .github/workflows/ci.yml    # lint, tests and benchmark execution
├── *.ipynb                     # original worked examples
└── pyproject.toml              # packaging, dependencies and CLI entry point
```

## Quick start

```bash
git clone https://github.com/sauravsingla/Time_Series.git
cd Time_Series
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -e '.[classical,dev]'
ruff check src tests
pytest
time-series-benchmark --output benchmark_results.csv
```

Run one dataset only:

```bash
time-series-benchmark --dataset co2 --output co2_results.csv
```

The output is a sorted CSV with dataset, frequency, model, train/test size, MAE, RMSE and sMAPE. CI runs the full benchmark on Python 3.10, 3.11 and 3.12 and uploads the result files as workflow artifacts.

## Python example

```python
from timeseries_reference.benchmark import benchmark_dataset
from timeseries_reference.datasets import load_dataset
from timeseries_reference.ml import LagRegressionForecaster

sunspots = load_dataset("sunspots")
model = LagRegressionForecaster(lags=11).fit(sunspots.values[:-12])
forecast = model.predict(horizon=12)
print(forecast)

comparison = benchmark_dataset("sunspots")
print(comparison[["model", "rmse", "smape"]])
```

## Evaluation principles

1. Never randomly shuffle time-series observations.
2. Fit preprocessing only on the training window.
3. Compare every advanced model against naive and seasonal-naive baselines.
4. Report multiple metrics because no single score explains every forecast failure.
5. Prefer rolling or expanding-window evaluation for final model selection.
6. Record horizon, frequency, latency and retraining cost alongside accuracy.
7. Treat an advanced model as useful only when it consistently beats a simple baseline.

## Traditional-to-modern roadmap

### Implemented now

- Missing-value validation and chronological splitting
- Naive, seasonal, moving-average and drift baselines
- Autoregression and Holt-Winters forecasting
- Lag-feature machine learning
- Walk-forward backtesting
- Multi-dataset benchmark execution

### Extension path

- ARIMA/SARIMA with order selection and residual diagnostics
- Gradient boosting with calendar and rolling features
- Probabilistic prediction intervals and quantile losses
- Multivariate VAR/VECM reference pipelines
- LSTM/GRU, N-BEATS and PatchTST examples
- Hierarchical forecasting and anomaly detection

Modern methods are not automatically better. Dataset size, forecast horizon, seasonality, operational cost and baseline performance should determine the final model.

## Quality standard

Every maintained implementation should include:

- explicit input validation;
- no future-data leakage;
- a simple baseline comparison;
- deterministic tests;
- an open reproducible dataset;
- documented assumptions and failure modes;
- compatibility with the supported Python versions.

## Notebook status

Some original Colab notebooks were created with older library versions, including legacy kernel metadata. They are retained for provenance, while the tested package provides the recommended reference implementation. Notebook modernization can continue as focused follow-up commits without weakening the stable package.

## Contributing

Keep contributions focused: one forecasting problem, one clear implementation, tests, a reproducible dataset and a short explanation of when the method should or should not be used.

## License

This project is available under the MIT License.
