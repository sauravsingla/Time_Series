# Time-Series Forecasting Model Selection and Use Cases

This guide helps practitioners choose a forecasting approach by data pattern, business problem, forecast horizon and validation requirement. It complements the maintained benchmark in this repository.

## Common forecasting use cases

| Use case | Typical frequency | Important challenges | Good starting models |
|---|---|---|---|
| Retail sales forecasting | Daily or weekly | promotions, holidays, stockouts, seasonality | seasonal naive, Holt-Winters, lag regression |
| Demand forecasting | Hourly, daily or weekly | intermittent demand, calendar effects, changing trends | seasonal naive, exponential smoothing, gradient boosting |
| Financial time-series forecasting | Daily or intraday | non-stationarity, regime shifts, weak signal | naive, drift, autoregression with strict backtesting |
| Energy-load forecasting | Hourly or daily | weather effects, multiple seasonalities, peaks | seasonal baselines, regression with exogenous variables, deep learning when justified |
| Traffic and capacity forecasting | Minute, hourly or daily | spikes, missing data, operational constraints | moving average, autoregression, lag regression |
| Economic forecasting | Monthly or quarterly | structural breaks, revisions, long horizons | drift, autoregression, ARIMA, VAR |
| Inventory planning | Daily or weekly | intermittent demand, service levels, lead time | seasonal naive, Croston-family methods, probabilistic forecasting |
| Forecast-based anomaly detection | Any regular frequency | changing baseline, alert thresholds, uncertainty | residuals from validated forecasting models |

## Model selection by signal pattern

### Stable level without seasonality

Start with naive, moving-average and simple exponential-smoothing models. More complex models should demonstrate repeatable gains in rolling-origin evaluation.

### Trend without seasonality

Compare drift and Holt-style trend models. Autoregression or lag regression can help when recent changes contain predictive information.

### Strong repeated seasonality

Use seasonal naive as the minimum benchmark. Holt-Winters or SARIMA may be appropriate when seasonal structure is stable and there is enough history.

### Multiple seasonalities

Hourly and sub-daily series may contain daily, weekly and annual cycles. Consider calendar features, Fourier terms, dynamic regression or carefully benchmarked neural models.

### Intermittent demand

Ordinary percentage metrics can become unstable when many targets are zero. Use suitable intermittent-demand methods and evaluate operational outcomes such as stock availability and inventory cost.

### Multivariate forecasting

When related variables provide predictive value, consider dynamic regression, VAR/VECM, gradient boosting or sequence models. Exogenous features must be available at prediction time.

## Classical forecasting models

### Naive and seasonal naive

These are essential baselines. A production candidate that cannot consistently beat them should not be selected because of complexity alone.

### Autoregression

Useful when recent lags predict future values. Lag order should be selected inside training data rather than using the test set.

### Exponential smoothing and Holt-Winters

Appropriate for level, trend and stable seasonality. They are fast, interpretable and often competitive for business forecasting.

### ARIMA and SARIMA

ARIMA models autocorrelation and differencing. SARIMA adds seasonal terms. Both require residual diagnostics and chronological evaluation.

## Machine-learning and deep-learning forecasting

Lag-based ridge regression is maintained in this repository as a transparent machine-learning reference. Tree-based models can incorporate calendar, rolling and exogenous features but must avoid leakage.

LSTM, GRU, N-BEATS, N-HiTS, Temporal Fusion Transformer and PatchTST can help on larger or multi-series datasets. They should be compared with strong statistical baselines and evaluated for runtime, stability, retraining cost and deployment complexity.

## Backtesting and validation

Forecasting validation must preserve time order.

- Use a chronological holdout for a simple first comparison.
- Use expanding-window backtesting when all historical data remains relevant.
- Use rolling-window backtesting when older observations become less representative.
- Match the validation horizon to the real operational forecast horizon.
- Refit transformations and features inside every training window.

Random train/test splitting is usually invalid for forecasting because it allows future information to influence training.

## Forecast accuracy metrics

| Metric | Best use | Limitation |
|---|---|---|
| MAE | interpretable error in original units | does not penalize large misses as strongly as RMSE |
| RMSE | emphasizes large errors | scale dependent and sensitive to outliers |
| MAPE | familiar percentage interpretation | unstable near zero |
| sMAPE | bounded percentage-style comparison | can still behave unexpectedly around zero |
| MASE | comparison across differently scaled series | requires a defined scaling baseline |
| Pinball loss | probabilistic quantile forecasts | must be interpreted per quantile |

Use several metrics and inspect errors by horizon, season and business segment.

## Production checklist

Before deploying a model, document:

1. target, frequency and forecast horizon;
2. data availability and publication delay;
3. baseline models;
4. rolling-origin validation design;
5. accuracy, runtime and retraining cost;
6. prediction intervals or quantiles;
7. monitoring and retraining triggers;
8. fallback behaviour when data is missing;
9. domain acceptance thresholds;
10. model and data lineage.

## Repository resources

- [Project overview](../README.md)
- [Forecasting guide](time-series-forecasting-guide.md)
- [Benchmark leaderboard](BENCHMARK_LEADERBOARD.md)
- [Benchmark methodology](BENCHMARK_METHODOLOGY.md)
- [Forecasting glossary](GLOSSARY.md)
- [Frequently asked questions](FAQ.md)
