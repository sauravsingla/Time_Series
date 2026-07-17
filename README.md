# Time Series Forecasting Reference

A practical collection of **traditional and modern time-series methods**, organized so that students and practitioners can use the repository as a reliable reference rather than a set of disconnected notebooks.

## What this repository covers

| Problem | Recommended starting point | Advanced direction |
|---|---|---|
| Univariate forecasting | Naive, seasonal naive, moving average, drift | ARIMA/SARIMA, Prophet, gradient boosting, N-BEATS |
| Multivariate forecasting | VAR/VECM | LSTM/GRU, Temporal Fusion Transformer, PatchTST |
| Irregular demand | Seasonal baseline, Croston-style methods | Probabilistic and hierarchical forecasting |
| Anomaly detection | Rolling statistics and residual thresholds | Autoencoders, isolation methods, transformer embeddings |
| Model evaluation | Temporal split and walk-forward backtesting | Nested temporal validation and probabilistic scoring |

The original notebooks remain available as historical learning material. The reusable `timeseries_reference` package adds tested Python 3 implementations for the foundations every forecasting project needs.

## Repository structure

```text
.
├── src/timeseries_reference/   # reusable forecasting utilities
├── tests/                      # deterministic unit tests
├── .github/workflows/ci.yml    # linting and tests on Python 3.10-3.12
├── *.ipynb                     # original worked examples
└── pyproject.toml              # modern packaging and dependencies
```

## Quick start

```bash
git clone https://github.com/sauravsingla/Time_Series.git
cd Time_Series
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -e '.[dev,classical]'
pytest
```

## Minimal forecasting example

```python
from timeseries_reference import (
    NaiveForecaster,
    SeasonalNaiveForecaster,
    expanding_window_backtest,
)

values = [120, 128, 133, 121, 130, 136, 124, 132, 139]

result = expanding_window_backtest(
    values,
    model_factory=lambda: SeasonalNaiveForecaster(season_length=3),
    initial_train_size=6,
)

print(result.mae, result.rmse)

model = NaiveForecaster().fit(values)
print(model.predict(horizon=3))
```

## Evaluation principles

1. Never randomly shuffle time-series observations.
2. Fit preprocessing only on the training window.
3. Compare every advanced model against naive and seasonal-naive baselines.
4. Report more than one metric; MAE/RMSE measure scale-dependent error while sMAPE helps comparison across series.
5. Use rolling or expanding-window backtests instead of judging a model on one convenient split.
6. Track forecast horizon, data frequency, latency and retraining cost alongside accuracy.

## Traditional-to-modern roadmap

### Foundations

- Missing-value treatment and resampling
- Trend, seasonality and decomposition
- Stationarity, ACF/PACF and differencing
- Exponential smoothing, ARIMA/SARIMA and VAR
- Leakage-safe validation and residual diagnostics

### Machine learning

- Lag, rolling and calendar features
- Regularized linear models
- Random forest and gradient boosting
- Direct, recursive and multi-output forecasting strategies

### Deep learning and current architectures

- LSTM and GRU sequence models
- Temporal convolutional networks
- N-BEATS/N-HiTS
- Temporal Fusion Transformer
- PatchTST and transformer-based long-horizon forecasting
- Probabilistic forecasting with quantiles or full predictive distributions

Advanced models are intentionally listed as directions rather than presented as universally better choices. Dataset size, horizon, seasonality, operational cost and baseline performance should determine the model.

## Quality checks

```bash
ruff check src tests
pytest
```

CI runs these checks on Python 3.10, 3.11 and 3.12 for each pull request.

## Notebook status

Some original Colab notebooks were created with older library versions and may need small API updates before execution. New reusable code targets Python 3.10+ and avoids deprecated notebook-only patterns. Future notebook modernization should preserve the original learning intent while adding reproducible data loading, fixed random seeds, baseline comparison and walk-forward validation.

## Contributing

Focused contributions are welcome: one problem, one clear implementation, tests, a reproducible example and a short explanation of when the method should or should not be used.

## License

This project is available under the MIT License.
