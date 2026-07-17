"""Classical forecasting baselines that every advanced model should beat."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def _series(values: list[float] | np.ndarray) -> np.ndarray:
    data = np.asarray(values, dtype=float).reshape(-1)
    if data.size == 0 or not np.all(np.isfinite(data)):
        raise ValueError("values must contain at least one finite observation")
    return data


@dataclass
class NaiveForecaster:
    last_value_: float | None = None

    def fit(self, values: list[float] | np.ndarray) -> "NaiveForecaster":
        self.last_value_ = float(_series(values)[-1])
        return self

    def predict(self, horizon: int) -> np.ndarray:
        if self.last_value_ is None:
            raise RuntimeError("fit must be called before predict")
        if horizon < 1:
            raise ValueError("horizon must be positive")
        return np.full(horizon, self.last_value_)


@dataclass
class SeasonalNaiveForecaster:
    season_length: int
    season_: np.ndarray | None = None

    def fit(self, values: list[float] | np.ndarray) -> "SeasonalNaiveForecaster":
        data = _series(values)
        if self.season_length < 1 or data.size < self.season_length:
            raise ValueError("season_length must be positive and no larger than the series")
        self.season_ = data[-self.season_length :].copy()
        return self

    def predict(self, horizon: int) -> np.ndarray:
        if self.season_ is None:
            raise RuntimeError("fit must be called before predict")
        if horizon < 1:
            raise ValueError("horizon must be positive")
        return np.resize(self.season_, horizon)


@dataclass
class MovingAverageForecaster:
    window: int
    mean_: float | None = None

    def fit(self, values: list[float] | np.ndarray) -> "MovingAverageForecaster":
        data = _series(values)
        if self.window < 1 or data.size < self.window:
            raise ValueError("window must be positive and no larger than the series")
        self.mean_ = float(np.mean(data[-self.window :]))
        return self

    def predict(self, horizon: int) -> np.ndarray:
        if self.mean_ is None:
            raise RuntimeError("fit must be called before predict")
        if horizon < 1:
            raise ValueError("horizon must be positive")
        return np.full(horizon, self.mean_)


@dataclass
class DriftForecaster:
    first_: float | None = None
    last_: float | None = None
    observations_: int = 0

    def fit(self, values: list[float] | np.ndarray) -> "DriftForecaster":
        data = _series(values)
        if data.size < 2:
            raise ValueError("drift forecasting requires at least two observations")
        self.first_, self.last_, self.observations_ = float(data[0]), float(data[-1]), data.size
        return self

    def predict(self, horizon: int) -> np.ndarray:
        if self.first_ is None or self.last_ is None:
            raise RuntimeError("fit must be called before predict")
        if horizon < 1:
            raise ValueError("horizon must be positive")
        slope = (self.last_ - self.first_) / (self.observations_ - 1)
        return self.last_ + slope * np.arange(1, horizon + 1)
