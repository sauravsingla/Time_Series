"""Command-line benchmark across open datasets and model families."""

from __future__ import annotations

import argparse
from collections.abc import Callable
from pathlib import Path

import pandas as pd

from .baselines import DriftForecaster, NaiveForecaster, SeasonalNaiveForecaster
from .classical import AutoRegressiveForecaster, ExponentialSmoothingForecaster
from .datasets import available_datasets, load_dataset
from .metrics import mae, rmse, smape
from .ml import LagRegressionForecaster


def benchmark_dataset(name: str, test_size: int | None = None) -> pd.DataFrame:
    """Evaluate representative model families on one chronological holdout."""
    dataset = load_dataset(name)
    horizon = test_size or min(dataset.seasonal_period, max(4, len(dataset.values) // 10))
    train, test = dataset.values[:-horizon], dataset.values[-horizon:]
    lag = min(dataset.seasonal_period, max(2, len(train) // 8))

    factories: dict[str, Callable[[], object]] = {
        "naive": NaiveForecaster,
        "seasonal_naive": lambda: SeasonalNaiveForecaster(dataset.seasonal_period),
        "drift": DriftForecaster,
        "autoregression": lambda: AutoRegressiveForecaster(lags=lag),
        "exponential_smoothing": lambda: ExponentialSmoothingForecaster(
            seasonal_periods=dataset.seasonal_period,
            seasonal="add" if len(train) >= 2 * dataset.seasonal_period else None,
        ),
        "ridge_lag_regression": lambda: LagRegressionForecaster(lags=lag),
    }

    rows: list[dict[str, float | str | int]] = []
    for model_name, factory in factories.items():
        model = factory()
        prediction = model.fit(train).predict(horizon)  # type: ignore[attr-defined]
        rows.append(
            {
                "dataset": dataset.name,
                "frequency": dataset.frequency,
                "model": model_name,
                "train_size": len(train),
                "test_size": horizon,
                "mae": mae(test, prediction),
                "rmse": rmse(test, prediction),
                "smape": smape(test, prediction),
            }
        )
    return pd.DataFrame(rows).sort_values(["rmse", "mae"], ignore_index=True)


def run_benchmarks(names: tuple[str, ...] | None = None) -> pd.DataFrame:
    """Run all configured models across several open datasets."""
    selected = names or available_datasets()
    return pd.concat([benchmark_dataset(name) for name in selected], ignore_index=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", choices=available_datasets(), action="append")
    parser.add_argument("--output", type=Path, default=Path("benchmark_results.csv"))
    args = parser.parse_args()
    results = run_benchmarks(tuple(args.dataset) if args.dataset else None)
    results.to_csv(args.output, index=False)
    print(results.to_string(index=False))
    print(f"\nSaved benchmark results to {args.output}")


if __name__ == "__main__":
    main()
