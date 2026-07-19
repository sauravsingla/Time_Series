# Time-Series Forecasting Documentation Hub

Use this page as the entry point for maintained Python time-series forecasting documentation, benchmark results, leakage-safe evaluation guidance, business use cases and model-comparison resources.

## Start here

- [Project overview](../README.md)
- [Practical time-series forecasting guide](time-series-forecasting-guide.md)
- [Model selection and business use cases](model-selection-and-use-cases.md)
- [Benchmark leaderboard](BENCHMARK_LEADERBOARD.md)
- [Benchmark methodology](BENCHMARK_METHODOLOGY.md)
- [Frequently asked questions](FAQ.md)
- [Troubleshooting](TROUBLESHOOTING.md)
- [Forecasting glossary](GLOSSARY.md)

## Find guidance by problem

| Problem | Recommended page |
|---|---|
| Sales or demand forecasting | [Model selection and business use cases](model-selection-and-use-cases.md) |
| ARIMA, SARIMA, Holt-Winters or autoregression | [Practical forecasting guide](time-series-forecasting-guide.md) |
| Walk-forward validation or rolling-origin evaluation | [Benchmark methodology](BENCHMARK_METHODOLOGY.md) |
| Comparing MAE, RMSE, MAPE and sMAPE | [Practical forecasting guide](time-series-forecasting-guide.md) |
| Reproducing model rankings | [Benchmark leaderboard](BENCHMARK_LEADERBOARD.md) |
| Forecast-based anomaly detection | [Model selection and business use cases](model-selection-and-use-cases.md) |
| Installation and runtime errors | [Troubleshooting](TROUBLESHOOTING.md) |

## Topics covered

The documentation covers:

- Python time-series forecasting;
- sales, demand, energy, traffic and economic forecasting;
- naive and seasonal-naive baselines;
- autoregression and Holt-Winters exponential smoothing;
- ARIMA and SARIMA concepts;
- lag-based machine-learning forecasting;
- LSTM, GRU, N-BEATS, N-HiTS, TFT and PatchTST evaluation principles;
- chronological train-test splitting;
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
- [Citation metadata](../CITATION.cff)

## Recommended learning order

1. Read the [practical forecasting guide](time-series-forecasting-guide.md).
2. Use the [model-selection guide](model-selection-and-use-cases.md) to map methods to a real problem.
3. Run the naive and seasonal-naive baselines.
4. Inspect chronological train/test splitting.
5. Run the complete open-dataset benchmark.
6. Compare per-dataset results instead of trusting only the overall rank.
7. Re-run the benchmark with a different holdout horizon.
8. Add a new model only after confirming it beats a simple baseline on at least one appropriate dataset.

## Documentation standard

Maintained documentation should be executable, specific and honest. Commands must match the current package, benchmark claims must be reproducible, and limitations must be stated alongside results.
