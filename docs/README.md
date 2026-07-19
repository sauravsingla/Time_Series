# Time-Series Forecasting Documentation Hub

Use this page as the entry point for maintained Python time-series forecasting documentation, benchmark results, leakage-safe evaluation guidance, business use cases and model-comparison resources.

## Start here

- [Project overview](../README.md)
- [Forecasting methods and evaluation index](FORECASTING_METHODS_INDEX.md)
- [Practical time-series forecasting guide](time-series-forecasting-guide.md)
- [Model selection and business use cases](model-selection-and-use-cases.md)
- [Benchmark leaderboard](BENCHMARK_LEADERBOARD.md)
- [Benchmark methodology](BENCHMARK_METHODOLOGY.md)
- [Reproducibility standard](REPRODUCIBILITY.md)
- [Frequently asked questions](FAQ.md)
- [Troubleshooting](TROUBLESHOOTING.md)
- [Forecasting glossary](GLOSSARY.md)

## Find guidance by problem

| Problem | Recommended page |
|---|---|
| Search for a forecasting model, metric or validation method | [Forecasting methods and evaluation index](FORECASTING_METHODS_INDEX.md) |
| Sales or demand forecasting | [Model selection and business use cases](model-selection-and-use-cases.md) |
| ARIMA, SARIMA, Holt-Winters or autoregression | [Practical forecasting guide](time-series-forecasting-guide.md) |
| Walk-forward validation or rolling-origin evaluation | [Benchmark methodology](BENCHMARK_METHODOLOGY.md) |
| Comparing MAE, RMSE, MAPE, sMAPE and MASE | [Forecasting methods and evaluation index](FORECASTING_METHODS_INDEX.md) |
| Reproducing model rankings | [Benchmark leaderboard](BENCHMARK_LEADERBOARD.md) |
| Avoiding data leakage | [Reproducibility standard](REPRODUCIBILITY.md) |
| Forecast-based anomaly detection | [Model selection and business use cases](model-selection-and-use-cases.md) |
| Installation and runtime errors | [Troubleshooting](TROUBLESHOOTING.md) |

## Topics covered

The documentation covers:

- Python time-series forecasting;
- sales, demand, energy, traffic and economic forecasting;
- naive, seasonal-naive, moving-average and drift baselines;
- autoregression and Holt-Winters exponential smoothing;
- ARIMA and SARIMA concepts;
- lag-based machine-learning forecasting;
- recursive multi-step forecasting;
- LSTM, GRU, N-BEATS, N-HiTS, TFT and PatchTST evaluation principles;
- chronological train-test splitting;
- time-series cross-validation;
- walk-forward validation and rolling-origin evaluation;
- expanding-window and rolling-window backtesting;
- MAE, RMSE, MAPE, sMAPE and MASE;
- probabilistic forecasting and prediction intervals;
- intermittent-demand forecasting;
- forecast-based anomaly detection.

## Contributing and governance

- [Contribution guide](../CONTRIBUTING.md)
- [Code of conduct](../CODE_OF_CONDUCT.md)
- [Security policy](../SECURITY.md)
- [Changelog](../CHANGELOG.md)
- [Release checklist](RELEASE_CHECKLIST.md)
- [Citation metadata](../CITATION.cff)

## Recommended learning order

1. Use the [forecasting methods index](FORECASTING_METHODS_INDEX.md) to locate the relevant method, metric or validation approach.
2. Read the [practical forecasting guide](time-series-forecasting-guide.md).
3. Use the [model-selection guide](model-selection-and-use-cases.md) to map methods to a real problem.
4. Run the naive and seasonal-naive baselines.
5. Inspect chronological train/test splitting.
6. Run the complete open-dataset benchmark.
7. Compare per-dataset results instead of trusting only the overall rank.
8. Re-run the benchmark with a different holdout horizon.
9. Add a new model only after confirming it beats a simple baseline on at least one appropriate dataset.

## Documentation standard

Maintained documentation should be executable, specific and honest. Commands must match the current package, benchmark claims must be reproducible, and limitations must be stated alongside results.
