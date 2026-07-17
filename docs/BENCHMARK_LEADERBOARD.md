# Benchmark Leaderboard

Generated from chronological holdout forecasts. Lower RMSE, MAE, sMAPE and average rank are better. Overall rank uses each model's average RMSE rank across datasets so differently scaled datasets remain comparable.

## Overall leaderboard

| overall_rank | model | average_rank | dataset_wins | average_smape | datasets |
| --- | --- | --- | --- | --- | --- |
| 1 | autoregression | 2.3333 | 1 | 12.5732 | 3 |
| 2 | ridge_lag_regression | 2.6667 | 1 | 12.3251 | 3 |
| 3 | exponential_smoothing | 3.0 | 0 | 26.6081 | 3 |
| 4 | seasonal_naive | 3.3333 | 0 | 13.73 | 3 |
| 5 | naive | 4.3333 | 1 | 34.5397 | 3 |
| 6 | drift | 5.3333 | 0 | 34.8213 | 3 |

## co2

| rank | model | rmse | mae | smape | train_size | test_size |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | autoregression | 0.3706 | 0.3017 | 0.0814 | 2232 | 52 |
| 2 | ridge_lag_regression | 0.4568 | 0.369 | 0.0997 | 2232 | 52 |
| 3 | exponential_smoothing | 0.5861 | 0.4848 | 0.1308 | 2232 | 52 |
| 4 | seasonal_naive | 1.567 | 1.4962 | 0.4041 | 2232 | 52 |
| 5 | drift | 2.1273 | 1.8359 | 0.4952 | 2232 | 52 |
| 6 | naive | 2.1658 | 1.85 | 0.4991 | 2232 | 52 |

## real_gdp

| rank | model | rmse | mae | smape | train_size | test_size |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | naive | 347.6579 | 334.8063 | 2.5472 | 199 | 4 |
| 2 | exponential_smoothing | 356.6863 | 343.0245 | 2.6089 | 199 | 4 |
| 3 | seasonal_naive | 397.721 | 384.7012 | 2.9206 | 199 | 4 |
| 4 | autoregression | 449.4155 | 430.9589 | 3.2652 | 199 | 4 |
| 5 | ridge_lag_regression | 475.7528 | 455.3003 | 3.4459 | 199 | 4 |
| 6 | drift | 488.4405 | 468.8246 | 3.5467 | 199 | 4 |

## sunspots

| rank | model | rmse | mae | smape | train_size | test_size |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ridge_lag_regression | 13.661 | 8.8456 | 33.4296 | 298 | 11 |
| 2 | autoregression | 16.5401 | 11.5087 | 34.3729 | 298 | 11 |
| 3 | seasonal_naive | 25.1135 | 20.0 | 37.8653 | 298 | 11 |
| 4 | exponential_smoothing | 38.9681 | 33.8324 | 77.0845 | 298 | 11 |
| 5 | drift | 55.6553 | 44.7879 | 100.422 | 298 | 11 |
| 6 | naive | 55.7721 | 44.8182 | 100.5729 | 298 | 11 |

## Reproduce

```bash
pip install -e '.[classical,dev]'
time-series-benchmark --output benchmark_results.csv --leaderboard docs/BENCHMARK_LEADERBOARD.md
```

Results were reproduced independently with the same package versions and benchmark logic. CI regenerates this file on every pull request and fails when the committed leaderboard becomes stale.
