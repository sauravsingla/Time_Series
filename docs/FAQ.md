# Frequently asked questions

## Is the overall leaderboard the only result that matters?

No. It is a compact cross-dataset summary. Model selection should still use the dataset-level metrics, forecast horizon, operational constraints and failure costs relevant to the real problem.

## Why rank models within each dataset?

Raw RMSE values are not comparable across series with different units and scales. Ranking within each dataset prevents a numerically large series from dominating the overall result.

## Why can a naive model beat a more advanced model?

Many time series are locally persistent, short, noisy or structurally unstable. A simple last-value forecast can therefore be difficult to beat. This is useful evidence, not a benchmark defect.

## Why not randomly split the data?

Random splitting allows future observations to influence training and creates optimistic estimates. Forecasting evaluation must preserve temporal order.

## Are the historical notebooks maintained?

They are retained as learning material and provenance. The package under `src/timeseries_reference` is the tested, maintained implementation.

## Does the repository include deep-learning models?

Not yet in the maintained benchmark. Neural models should be added only with reproducible training, deterministic tests where practical, resource documentation and evidence that they improve an appropriate baseline.

## Can I use my own dataset?

Yes. Use a chronologically ordered one-dimensional series, define an appropriate seasonal period, reserve a future holdout window and compare against naive baselines before interpreting advanced-model results.

## Which metric should I optimize?

Use a metric aligned with the business cost. RMSE emphasizes large errors, MAE is easier to interpret in the original unit, and sMAPE offers a scale-relative view but has its own edge cases near zero.

## Are benchmark results guaranteed to be identical on every machine?

The deterministic algorithms should be highly stable, but small floating-point differences can occur across dependency versions and platforms. Record Python and package versions when publishing results.

## Is the package production ready?

It is a reference implementation and evaluation foundation. Production use still requires monitoring, retraining policy, data validation, feature pipelines, prediction intervals, alerting and domain-specific acceptance thresholds.
