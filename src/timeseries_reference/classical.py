"""Classical statistical forecasting adapters."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class AutoRegressiveForecaster:
    """Autoregression with a configurable lag order."""

    lags: int = 12
    trend: str = "ct"

    def fit(self, values: list[float] | np.ndarray) -> "AutoRegressiveForecaster":
        from statsmodels.tsa.ar_model import AutoReg

        data = np.asarray(values, dtype=float).reshape(-1)
        if data.size <= self.lags + 2:
            raise ValueError("series is too short for the requested lag order")
        self._result = AutoReg(data, lags=self.lags, trend=self.trend, old_names=False).fit()
        self._size = data.size
        return self

    def predict(self, horizon: int) -> np.ndarray:
        if horizon < 1:
            raise ValueError("horizon must be positive")
        if not hasattr(self, "_result"):
            raise RuntimeError("fit must be called before predict")
        return np.asarray(self._result.predict(start=self._size, end=self._size + horizon - 1), dtype=float)


@dataclass
class ExponentialSmoothingForecaster:
    """Holt-Winters forecasting for level, trend and seasonality."""

    seasonal_periods: int | None = None
    trend: str | None = "add"
    seasonal: str | None = None
    damped_trend: bool = True

    def fit(self, values: list[float] | np.ndarray) -> "ExponentialSmoothingForecaster":
        from statsmodels.tsa.holtwinters import ExponentialSmoothing

        data = np.asarray(values, dtype=float).reshape(-1)
        if data.size < 8:
            raise ValueError("at least eight observations are required")
        if self.seasonal and not self.seasonal_periods:
            raise ValueError("seasonal_periods is required for a seasonal model")
        self._result = ExponentialSmoothing(
            data,
            trend=self.trend,
            seasonal=self.seasonal,
            seasonal_periods=self.seasonal_periods,
            damped_trend=self.damped_trend and self.trend is not None,
            initialization_method="estimated",
        ).fit(optimized=True)
        return self

    def predict(self, horizon: int) -> np.ndarray:
        if horizon < 1:
            raise ValueError("horizon must be positive")
        if not hasattr(self, "_result"):
            raise RuntimeError("fit must be called before predict")
        return np.asarray(self._result.forecast(horizon), dtype=float)
