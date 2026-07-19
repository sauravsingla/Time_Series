# Time-Series Forecasting in Python: Practical Guide

This guide explains how to build, evaluate and compare time-series forecasting models in Python without data leakage. It complements the reusable code, benchmark CLI and notebooks in this repository.

## What is time-series forecasting?

Time-series forecasting estimates future values from observations ordered over time. Common applications include demand forecasting, sales forecasting, financial forecasting, traffic prediction, energy-load forecasting, capacity planning, inventory planning and anomaly detection.

A forecasting workflow should define:

- target variable;
- sampling frequency;
- forecast horizon;
- seasonal period;
- missing-value policy;
- retraining frequency;
- evaluation metric;
- operational acceptance threshold.

## Start with forecasting baselines

Simple baselines are essential because they reveal whether a complex model adds real value.

### Naive forecast

The next value is predicted as the latest observed value. This is often competitive for random-walk-like series.

### Seasonal naive forecast

The forecast repeats the value from the previous seasonal cycle. It is a strong baseline for weekly, monthly, quarterly and annual seasonal data.

### Drift forecast

The model extends the average historical slope into the future.

### Moving-average forecast

The forecast uses a recent rolling average to smooth local noise.

## Classical statistical forecasting

### Autoregression

Autoregressive models predict future values from lagged observations. They are useful when recent values contain predictive information and the series is sufficiently stable.

### Exponential smoothing and Holt-Winters

Exponential-smoothing models are effective for level, trend and repeated seasonality. Holt-Winters forecasting can model additive or multiplicative seasonal patterns.

### ARIMA and SARIMA

ARIMA combines autoregression, differencing and moving-average errors. SARIMA extends ARIMA with seasonal terms. These models should be selected with residual diagnostics, chronological validation and explicit seasonal assumptions.

## Machine-learning forecasting

Machine-learning models convert a time series into supervised learning features such as:

- lagged values;
- rolling means and standard deviations;
- calendar features;
- trend indicators;
- holiday and event variables;
- external regressors.

The repository currently includes regularized lag regression. Future extensions may include gradient boosting and other tabular forecasting models.

## Deep-learning forecasting

LSTM, GRU, N-BEATS, N-HiTS, Temporal Fusion Transformer and PatchTST can be useful for large or multivariate datasets. They should still be compared with strong simple baselines and evaluated for latency, stability, retraining cost and reproducibility.

## Leakage-safe time-series validation

Random train-test splitting is inappropriate for forecasting because it allows future observations to influence training.

Use one of these approaches:

### Chronological holdout

Train on the earliest observations and test on the most recent block.

### Walk-forward validation

Repeatedly train on past data and evaluate on the next forecast window.

### Expanding-window backtesting

The training window grows over time while the test horizon moves forward.

### Rolling-window backtesting

A fixed-length training window moves through time, which is useful when older data becomes less relevant.

## Forecast accuracy metrics

### MAE

Mean absolute error is easy to interpret and less sensitive to large errors than RMSE.

### RMSE

Root mean squared error penalizes large misses more heavily.

### MAPE

Mean absolute percentage error is intuitive but unstable when actual values are zero or close to zero.

### sMAPE

Symmetric mean absolute percentage error reduces some MAPE asymmetry and is useful for comparing relative errors.

No single metric is sufficient for every forecasting problem.

## Probabilistic forecasting

Point forecasts do not communicate uncertainty. Production systems should often include prediction intervals, quantile forecasts, calibration analysis and coverage metrics.

## Forecast-based anomaly detection

Anomalies can be identified when observed values fall outside expected forecast intervals or produce unusually large residuals. Thresholds should account for seasonality, changing variance and business impact.

## Recommended workflow

1. Understand frequency, horizon, trend, seasonality and missing values.
2. Establish naive and seasonal-naive baselines.
3. Add autoregression or exponential smoothing.
4. Add leakage-safe lag-based machine learning.
5. Evaluate through walk-forward or expanding-window backtesting.
6. Compare MAE, RMSE and sMAPE.
7. Inspect residuals and failure periods.
8. Introduce advanced models only when they produce repeatable improvement.

## Repository resources

- [`../README.md`](../README.md) — project overview and quick start.
- [`BENCHMARK_LEADERBOARD.md`](BENCHMARK_LEADERBOARD.md) — cross-dataset model rankings.
- [`BENCHMARK_METHODOLOGY.md`](BENCHMARK_METHODOLOGY.md) — evaluation protocol.
- [`FAQ.md`](FAQ.md) — common forecasting questions.
- [`GLOSSARY.md`](GLOSSARY.md) — forecasting terminology.
- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) — installation and runtime help.

## Search topics covered

This guide is relevant to Python time-series forecasting, forecasting backtesting, walk-forward validation, rolling-origin evaluation, ARIMA, SARIMA, Holt-Winters, autoregression, machine-learning forecasting, LSTM forecasting, GRU forecasting, N-BEATS, PatchTST, demand forecasting, probabilistic forecasting and forecast-based anomaly detection.