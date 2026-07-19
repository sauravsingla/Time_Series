# Forecasting Methods and Evaluation Index

This index helps readers find Python time-series forecasting methods, evaluation techniques, datasets, metrics and business use cases covered by this repository.

## Implemented forecasting models

| Search topic | Repository coverage | Where to start |
|---|---|---|
| Naive forecasting | Last-observation baseline | [`src/timeseries_reference`](../src/timeseries_reference) and [benchmark leaderboard](BENCHMARK_LEADERBOARD.md) |
| Seasonal naive forecasting | Seasonal baseline using the previous seasonal cycle | [Benchmark methodology](BENCHMARK_METHODOLOGY.md) |
| Drift forecasting | Linear drift baseline | [Benchmark leaderboard](BENCHMARK_LEADERBOARD.md) |
| Moving-average forecasting | Rolling historical-average baseline | [Practical forecasting guide](time-series-forecasting-guide.md) |
| Autoregressive forecasting | Lag-based statistical autoregression | [Benchmark leaderboard](BENCHMARK_LEADERBOARD.md) |
| Holt-Winters forecasting | Exponential smoothing with trend and seasonality | [Practical forecasting guide](time-series-forecasting-guide.md) |
| Machine-learning time-series forecasting | Ridge regression using leakage-safe lag features | [Model selection and use cases](model-selection-and-use-cases.md) |
| Recursive multi-step forecasting | Forecasts generated one step at a time using prior predictions | [Python API example](../README.md#python-forecasting-api-example) |

## Forecasting methods discussed or planned

The following methods are covered as model-selection concepts or roadmap items. They are not yet part of the maintained benchmark unless explicitly stated otherwise.

| Search topic | Current status | Guidance |
|---|---|---|
| ARIMA forecasting | Concept and roadmap | [Practical forecasting guide](time-series-forecasting-guide.md) |
| SARIMA forecasting | Concept and roadmap | [Practical forecasting guide](time-series-forecasting-guide.md) |
| VAR and VECM | Roadmap for multivariate forecasting | [Model selection and use cases](model-selection-and-use-cases.md) |
| Croston intermittent-demand forecasting | Use-case guidance and roadmap | [Model selection and use cases](model-selection-and-use-cases.md) |
| Probabilistic forecasting | Guidance and roadmap | [Model selection and use cases](model-selection-and-use-cases.md) |
| LSTM and GRU forecasting | Evaluation guidance; not benchmarked yet | [Practical forecasting guide](time-series-forecasting-guide.md) |
| N-BEATS and N-HiTS | Evaluation guidance; not benchmarked yet | [Practical forecasting guide](time-series-forecasting-guide.md) |
| Temporal Fusion Transformer | Evaluation guidance; not benchmarked yet | [Model selection and use cases](model-selection-and-use-cases.md) |
| PatchTST | Evaluation guidance; not benchmarked yet | [Practical forecasting guide](time-series-forecasting-guide.md) |

## Backtesting and validation

| Search topic | What it means here | Documentation |
|---|---|---|
| Time-series train-test split | Training observations always precede test observations | [Benchmark methodology](BENCHMARK_METHODOLOGY.md) |
| Walk-forward validation | Repeated chronological training and forecasting | [Benchmark methodology](BENCHMARK_METHODOLOGY.md) |
| Rolling-origin evaluation | Forecast origin advances through time | [Benchmark methodology](BENCHMARK_METHODOLOGY.md) |
| Expanding-window backtesting | Training history grows at each evaluation step | [Benchmark methodology](BENCHMARK_METHODOLOGY.md) |
| Rolling-window backtesting | Fixed-length training window moves through time | [Practical forecasting guide](time-series-forecasting-guide.md) |
| Leakage-safe feature engineering | Lag and preprocessing features use past data only | [Reproducibility standard](REPRODUCIBILITY.md) |
| Forecast-horizon selection | Validation horizon should match operational use | [Model selection and use cases](model-selection-and-use-cases.md) |

## Forecast accuracy metrics

| Metric | Typical interpretation | Repository use |
|---|---|---|
| MAE | Average absolute forecast error | Maintained benchmark |
| RMSE | Error metric that penalizes large misses more heavily | Maintained benchmark and model ranking |
| MAPE | Percentage error; problematic near zero | Maintained package |
| sMAPE | Symmetric percentage error | Maintained benchmark |
| MASE | Scale-free error relative to a naive baseline | Documentation guidance |

See the [forecasting glossary](GLOSSARY.md) and [practical forecasting guide](time-series-forecasting-guide.md) for definitions and limitations.

## Open time-series datasets

| Dataset | Frequency | Typical search intent |
|---|---|---|
| Sunspots | Annual | cyclical time-series forecasting, long-cycle forecasting |
| Mauna Loa CO2 | Weekly | seasonal forecasting, missing-data time series, trend forecasting |
| US real GDP | Quarterly | economic forecasting, structural breaks, quarterly time series |

## Business forecasting use cases

The repository provides model-selection guidance for:

- sales forecasting;
- retail and product-demand forecasting;
- inventory and intermittent-demand forecasting;
- financial and economic forecasting;
- energy-load forecasting;
- traffic and capacity forecasting;
- forecast-residual anomaly detection;
- probabilistic forecasting and prediction intervals.

Use the [model-selection and business use-case guide](model-selection-and-use-cases.md) for the recommended starting point, validation design and cautions for each problem.

## Reproducibility requirements

A forecasting result should record the dataset source, frequency, time boundaries, horizon, seasonal period, preprocessing, hyperparameters, metrics, runtime environment and raw outputs. See [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) for the complete standard.
