"""Time-aware validation helpers."""

from __future__ import annotations

from typing import TypeVar

import pandas as pd

FrameOrSeries = TypeVar("FrameOrSeries", pd.DataFrame, pd.Series)


def temporal_train_test_split(
    data: FrameOrSeries,
    *,
    test_size: int | float,
    gap: int = 0,
) -> tuple[FrameOrSeries, FrameOrSeries]:
    """Split ordered observations without shuffling.

    ``test_size`` may be an integer number of rows or a fraction in ``(0, 1)``.
    ``gap`` removes observations between train and test to reduce leakage when
    features use lagged or rolling windows.
    """
    n_rows = len(data)
    if n_rows < 2:
        raise ValueError("data must contain at least two rows")
    if gap < 0:
        raise ValueError("gap must be non-negative")

    if isinstance(test_size, float):
        if not 0 < test_size < 1:
            raise ValueError("float test_size must be between 0 and 1")
        n_test = max(1, int(round(n_rows * test_size)))
    else:
        n_test = test_size

    if n_test < 1 or n_test + gap >= n_rows:
        raise ValueError("test_size and gap leave no training observations")

    train_end = n_rows - n_test - gap
    train = data.iloc[:train_end].copy()
    test = data.iloc[n_rows - n_test :].copy()
    return train, test
