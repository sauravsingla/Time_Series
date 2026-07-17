import numpy as np

from timeseries_reference.benchmark import benchmark_dataset
from timeseries_reference.classical import AutoRegressiveForecaster, ExponentialSmoothingForecaster
from timeseries_reference.datasets import available_datasets, load_dataset
from timeseries_reference.ml import LagRegressionForecaster


def test_open_datasets_are_finite_and_documented():
    assert set(available_datasets()) == {"sunspots", "co2", "real_gdp"}
    for name in available_datasets():
        dataset = load_dataset(name)
        assert dataset.name == name
        assert dataset.values.ndim == 1
        assert len(dataset.values) >= 24
        assert np.all(np.isfinite(dataset.values))
        assert dataset.seasonal_period > 0
        assert dataset.description


def test_model_families_forecast_requested_horizon():
    values = 10 + 0.2 * np.arange(80) + np.sin(np.arange(80) * 2 * np.pi / 12)
    models = [
        AutoRegressiveForecaster(lags=12),
        ExponentialSmoothingForecaster(seasonal_periods=12, seasonal="add"),
        LagRegressionForecaster(lags=12),
    ]
    for model in models:
        prediction = model.fit(values).predict(6)
        assert prediction.shape == (6,)
        assert np.all(np.isfinite(prediction))


def test_benchmark_runs_all_model_families():
    result = benchmark_dataset("sunspots", test_size=6)
    assert len(result) == 6
    assert set(result["model"]) == {
        "naive",
        "seasonal_naive",
        "drift",
        "autoregression",
        "exponential_smoothing",
        "ridge_lag_regression",
    }
    assert np.all(np.isfinite(result[["mae", "rmse", "smape"]].to_numpy()))
