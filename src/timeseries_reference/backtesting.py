"""Walk-forward evaluation for forecasting models."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Protocol

import numpy as np

from .metrics import mae, rmse


class Forecaster(Protocol):
    def fit(self, values: list[float] | np.ndarray) -> "Forecaster": ...
    def predict(self, horizon: int) -> np.ndarray: ...


@dataclass(frozen=True)
class BacktestResult:
    actual: np.ndarray
    predicted: np.ndarray
    mae: float
    rmse: float
    folds: int


def expanding_window_backtest(
    values: list[float] | np.ndarray,
    model_factory: Callable[[], Forecaster],
    *,
    initial_train_size: int,
    horizon: int = 1,
    step: int = 1,
) -> BacktestResult:
    """Evaluate a fresh model on sequential, expanding training windows."""
    data = np.asarray(values, dtype=float).reshape(-1)
    if not np.all(np.isfinite(data)):
        raise ValueError("values must contain only finite observations")
    if initial_train_size < 2:
        raise ValueError("initial_train_size must be at least 2")
    if horizon < 1 or step < 1:
        raise ValueError("horizon and step must be positive")
    if initial_train_size + horizon > data.size:
        raise ValueError("series is too short for the requested backtest")

    actual_parts: list[np.ndarray] = []
    predicted_parts: list[np.ndarray] = []
    for train_end in range(initial_train_size, data.size - horizon + 1, step):
        model = model_factory().fit(data[:train_end])
        prediction = np.asarray(model.predict(horizon), dtype=float).reshape(-1)
        if prediction.size != horizon:
            raise ValueError("model returned a prediction with the wrong horizon")
        actual_parts.append(data[train_end : train_end + horizon])
        predicted_parts.append(prediction)

    actual = np.concatenate(actual_parts)
    predicted = np.concatenate(predicted_parts)
    return BacktestResult(
        actual=actual,
        predicted=predicted,
        mae=mae(actual, predicted),
        rmse=rmse(actual, predicted),
        folds=len(actual_parts),
    )
