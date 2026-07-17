"""Machine-learning forecasting with leakage-safe lag features."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class LagRegressionForecaster:
    """Recursive forecasting with a regularized linear lag model."""

    lags: int = 12
    alpha: float = 1.0

    def fit(self, values: list[float] | np.ndarray) -> "LagRegressionForecaster":
        from sklearn.linear_model import Ridge

        data = np.asarray(values, dtype=float).reshape(-1)
        if data.size <= self.lags:
            raise ValueError("series is too short for the requested lag order")
        if self.lags < 1 or self.alpha < 0:
            raise ValueError("lags must be positive and alpha must be non-negative")
        features = np.vstack([data[i - self.lags : i] for i in range(self.lags, data.size)])
        self._model = Ridge(alpha=self.alpha).fit(features, data[self.lags :])
        self._history = data.tolist()
        return self

    def predict(self, horizon: int) -> np.ndarray:
        if horizon < 1:
            raise ValueError("horizon must be positive")
        if not hasattr(self, "_model"):
            raise RuntimeError("fit must be called before predict")
        history = self._history.copy()
        predictions: list[float] = []
        for _ in range(horizon):
            feature = np.asarray(history[-self.lags :], dtype=float).reshape(1, -1)
            prediction = float(self._model.predict(feature)[0])
            predictions.append(prediction)
            history.append(prediction)
        return np.asarray(predictions)
