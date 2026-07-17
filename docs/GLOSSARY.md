# Time-series glossary

**Autocorrelation** — correlation between a series and a lagged version of itself.

**Backtesting** — simulating historical forecasts using only information available before each forecast origin.

**Baseline** — a simple reference forecast that an advanced model should improve upon.

**Drift forecast** — extrapolation of the average change observed between the first and last training values.

**Expanding window** — evaluation where the training set grows as the forecast origin moves forward.

**Forecast horizon** — number of future periods predicted.

**Lag** — a past observation used to explain or predict a later value.

**Leakage** — use of information during training that would not be available at prediction time.

**MAE** — mean absolute error; average absolute distance between actual and predicted values.

**RMSE** — root mean squared error; penalizes larger errors more strongly than MAE.

**Seasonal naive** — forecast that repeats the most recent observed seasonal cycle.

**Seasonal period** — number of observations in one repeating cycle, such as 12 for monthly annual seasonality.

**sMAPE** — symmetric mean absolute percentage error; a scale-relative percentage-style metric.

**Temporal holdout** — final chronological portion of a series reserved for evaluation.

**Walk-forward validation** — repeated forecasting from successive historical origins while preserving temporal order.
