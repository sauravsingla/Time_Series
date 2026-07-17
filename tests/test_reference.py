import numpy as np
import pandas as pd
import pytest

from timeseries_reference import (
    DriftForecaster,
    NaiveForecaster,
    SeasonalNaiveForecaster,
    expanding_window_backtest,
    mae,
    rmse,
    smape,
    temporal_train_test_split,
)
from timeseries_reference.leaderboard import rank_results, render_leaderboard


def test_metrics_return_expected_values() -> None:
    actual = [1.0, 2.0, 3.0]
    predicted = [1.0, 2.0, 5.0]
    assert mae(actual, predicted) == pytest.approx(2 / 3)
    assert rmse(actual, predicted) == pytest.approx(np.sqrt(4 / 3))
    assert smape(actual, actual) == 0.0


def test_temporal_split_preserves_order_and_gap() -> None:
    series = pd.Series(range(10))
    train, test = temporal_train_test_split(series, test_size=2, gap=1)
    assert train.tolist() == list(range(7))
    assert test.tolist() == [8, 9]


def test_baselines_forecast_expected_values() -> None:
    np.testing.assert_array_equal(NaiveForecaster().fit([1, 2, 3]).predict(2), [3, 3])
    np.testing.assert_array_equal(
        SeasonalNaiveForecaster(2).fit([1, 2, 3, 4]).predict(5), [3, 4, 3, 4, 3]
    )
    np.testing.assert_array_equal(DriftForecaster().fit([1, 2, 3]).predict(2), [4, 5])


def test_expanding_window_backtest_is_leakage_free() -> None:
    result = expanding_window_backtest(
        [1, 2, 3, 4, 5, 6],
        NaiveForecaster,
        initial_train_size=3,
    )
    np.testing.assert_array_equal(result.actual, [4, 5, 6])
    np.testing.assert_array_equal(result.predicted, [3, 4, 5])
    assert result.folds == 3
    assert result.mae == 1.0


def test_leaderboard_uses_scale_independent_dataset_ranks() -> None:
    results = pd.DataFrame(
        [
            {"dataset": "small", "model": "a", "mae": 1.0, "rmse": 1.0, "smape": 10.0},
            {"dataset": "small", "model": "b", "mae": 2.0, "rmse": 2.0, "smape": 20.0},
            {"dataset": "large", "model": "a", "mae": 200.0, "rmse": 200.0, "smape": 20.0},
            {"dataset": "large", "model": "b", "mae": 100.0, "rmse": 100.0, "smape": 10.0},
        ]
    )
    ranked, overall = rank_results(results)
    assert ranked.groupby("dataset")["rank"].min().eq(1).all()
    assert overall["average_rank"].tolist() == [1.5, 1.5]
    assert set(overall["model"]) == {"a", "b"}


def test_leaderboard_markdown_contains_overall_and_dataset_sections() -> None:
    results = pd.DataFrame(
        [
            {"dataset": "demo", "model": "naive", "mae": 2.0, "rmse": 3.0, "smape": 4.0},
            {"dataset": "demo", "model": "drift", "mae": 1.0, "rmse": 2.0, "smape": 3.0},
        ]
    )
    markdown = render_leaderboard(results)
    assert "# Benchmark Leaderboard" in markdown
    assert "## Overall leaderboard" in markdown
    assert "## demo" in markdown
    assert "drift" in markdown


def test_invalid_inputs_raise_clear_errors() -> None:
    with pytest.raises(ValueError):
        mae([], [])
    with pytest.raises(ValueError):
        temporal_train_test_split(pd.Series([1, 2]), test_size=1, gap=1)
    with pytest.raises(RuntimeError):
        NaiveForecaster().predict(1)
    with pytest.raises(ValueError):
        rank_results(pd.DataFrame())
