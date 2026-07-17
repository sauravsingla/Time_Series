"""Forecast error metrics with consistent validation."""

from __future__ import annotations

import numpy as np

ArrayLike = np.ndarray | list[float] | tuple[float, ...]


def _validated_arrays(actual: ArrayLike, predicted: ArrayLike) -> tuple[np.ndarray, np.ndarray]:
    y_true = np.asarray(actual, dtype=float)
    y_pred = np.asarray(predicted, dtype=float)
    if y_true.shape != y_pred.shape:
        raise ValueError("actual and predicted must have the same shape")
    if y_true.size == 0:
        raise ValueError("actual and predicted must not be empty")
    if not np.all(np.isfinite(y_true)) or not np.all(np.isfinite(y_pred)):
        raise ValueError("actual and predicted must contain only finite values")
    return y_true, y_pred


def mae(actual: ArrayLike, predicted: ArrayLike) -> float:
    """Return mean absolute error."""
    y_true, y_pred = _validated_arrays(actual, predicted)
    return float(np.mean(np.abs(y_true - y_pred)))


def rmse(actual: ArrayLike, predicted: ArrayLike) -> float:
    """Return root mean squared error."""
    y_true, y_pred = _validated_arrays(actual, predicted)
    return float(np.sqrt(np.mean(np.square(y_true - y_pred))))


def mape(actual: ArrayLike, predicted: ArrayLike, *, epsilon: float = 1e-8) -> float:
    """Return mean absolute percentage error in percent.

    Values whose absolute actual value is below ``epsilon`` are excluded because
    percentage errors are undefined at zero.
    """
    y_true, y_pred = _validated_arrays(actual, predicted)
    mask = np.abs(y_true) > epsilon
    if not np.any(mask):
        raise ValueError("MAPE is undefined when all actual values are zero")
    return float(np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100)


def smape(actual: ArrayLike, predicted: ArrayLike, *, epsilon: float = 1e-8) -> float:
    """Return symmetric mean absolute percentage error in percent."""
    y_true, y_pred = _validated_arrays(actual, predicted)
    denominator = np.abs(y_true) + np.abs(y_pred)
    ratio = np.divide(
        2.0 * np.abs(y_true - y_pred),
        denominator,
        out=np.zeros_like(denominator),
        where=denominator > epsilon,
    )
    return float(np.mean(ratio) * 100)
