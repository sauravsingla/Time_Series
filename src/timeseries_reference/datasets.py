"""Reproducible open time-series datasets bundled with statsmodels."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class Dataset:
    """A named univariate time series and its forecasting metadata."""

    name: str
    values: np.ndarray
    frequency: str
    seasonal_period: int
    description: str


def _clean(values: pd.Series) -> np.ndarray:
    series = pd.to_numeric(values, errors="coerce").interpolate(limit_direction="both")
    result = series.to_numpy(dtype=float)
    if result.size < 24 or not np.all(np.isfinite(result)):
        raise ValueError("dataset must contain at least 24 finite observations")
    return result


def load_sunspots() -> Dataset:
    """Annual sunspot activity from 1700 to 2008."""
    from statsmodels.datasets import sunspots

    frame = sunspots.load_pandas().data
    return Dataset(
        name="sunspots",
        values=_clean(frame["SUNACTIVITY"]),
        frequency="annual",
        seasonal_period=11,
        description="Annual mean sunspot activity, useful for cyclic forecasting.",
    )


def load_co2() -> Dataset:
    """Weekly atmospheric CO2 measurements from Mauna Loa."""
    from statsmodels.datasets import co2

    frame = co2.load_pandas().data
    return Dataset(
        name="co2",
        values=_clean(frame["co2"]),
        frequency="weekly",
        seasonal_period=52,
        description="Weekly atmospheric CO2 concentration with trend and seasonality.",
    )


def load_macrodata() -> Dataset:
    """Quarterly US real GDP from the statsmodels macroeconomic dataset."""
    from statsmodels.datasets import macrodata

    frame = macrodata.load_pandas().data
    return Dataset(
        name="real_gdp",
        values=_clean(frame["realgdp"]),
        frequency="quarterly",
        seasonal_period=4,
        description="Quarterly US real GDP, useful for trend-dominated forecasting.",
    )


_LOADERS: dict[str, Callable[[], Dataset]] = {
    "sunspots": load_sunspots,
    "co2": load_co2,
    "real_gdp": load_macrodata,
}


def available_datasets() -> tuple[str, ...]:
    """Return stable dataset identifiers supported by the benchmark suite."""
    return tuple(_LOADERS)


def load_dataset(name: str) -> Dataset:
    """Load one supported open dataset by name."""
    try:
        return _LOADERS[name]()
    except KeyError as exc:
        choices = ", ".join(available_datasets())
        raise ValueError(f"unknown dataset {name!r}; choose from: {choices}") from exc
