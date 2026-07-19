# Time-Series Forecasting Documentation Hub

Use this page as the entry point for maintained Python time-series forecasting documentation, benchmark results, leakage-safe evaluation guidance and model-comparison resources.

## Start here

- [Project overview](../README.md)
- [Practical time-series forecasting guide](time-series-forecasting-guide.md)
- [Benchmark leaderboard](BENCHMARK_LEADERBOARD.md)
- [Benchmark methodology](BENCHMARK_METHODOLOGY.md)
- [Frequently asked questions](FAQ.md)
- [Troubleshooting](TROUBLESHOOTING.md)
- [Forecasting glossary](GLOSSARY.md)

## Topics covered

The documentation covers:

- Python time-series forecasting;
- naive and seasonal-naive baselines;
- autoregression and Holt-Winters exponential smoothing;
- ARIMA and SARIMA concepts;
- lag-based machine-learning forecasting;
- LSTM, GRU, N-BEATS and PatchTST evaluation principles;
- chronological train-test splitting;
- walk-forward validation and rolling-origin evaluation;
- expanding-window and rolling-window backtesting;
- MAE, RMSE, MAPE and sMAPE;
- probabilistic forecasting and prediction intervals;
- demand forecasting and forecast-based anomaly detection.

## Contributing and governance

- [Contribution guide](../CONTRIBUTING.md)
- [Code of conduct](../CODE_OF_CONDUCT.md)
- [Security policy](../SECURITY.md)
- [Changelog](../CHANGELOG.md)
- [Citation metadata](../CITATION.cff)

## Recommended learning order

1. Read the [practical forecasting guide](time-series-forecasting-guide.md).
2. Run the naive and seasonal-naive baselines.
3. Inspect chronological train/test splitting.
4. Run the complete open-dataset benchmark.
5. Compare per-dataset results instead of trusting only the overall rank.
6. Re-run the benchmark with a different holdout horizon.
7. Add a new model only after confirming it beats a simple baseline on at least one appropriate dataset.

## Documentation standard

Maintained documentation should be executable, specific and honest. Commands must match the current package, benchmark claims must be reproducible, and limitations must be stated alongside results.