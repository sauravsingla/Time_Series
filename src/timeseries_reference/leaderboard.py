"""Create reproducible per-dataset and overall benchmark leaderboards."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

_REQUIRED_COLUMNS = {"dataset", "model", "mae", "rmse", "smape"}


def rank_results(results: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return per-dataset rankings and a scale-independent overall leaderboard."""
    missing = _REQUIRED_COLUMNS.difference(results.columns)
    if missing:
        raise ValueError(f"benchmark results are missing columns: {sorted(missing)}")
    if results.empty:
        raise ValueError("benchmark results must not be empty")

    ranked = results.copy()
    ranked["rank"] = ranked.groupby("dataset")["rmse"].rank(method="min").astype(int)
    ranked = ranked.sort_values(["dataset", "rank", "mae", "model"], ignore_index=True)

    overall = (
        ranked.groupby("model", as_index=False)
        .agg(
            average_rank=("rank", "mean"),
            dataset_wins=("rank", lambda values: int((values == 1).sum())),
            average_smape=("smape", "mean"),
            datasets=("dataset", "nunique"),
        )
        .sort_values(["average_rank", "average_smape", "model"], ignore_index=True)
    )
    overall.insert(0, "overall_rank", range(1, len(overall) + 1))
    return ranked, overall


def _markdown_table(frame: pd.DataFrame, decimals: int = 4) -> str:
    display = frame.copy()
    numeric = display.select_dtypes(include="number").columns
    display[numeric] = display[numeric].round(decimals)
    headers = [str(column) for column in display.columns]
    rows = [[str(value) for value in row] for row in display.itertuples(index=False, name=None)]
    separator = ["---"] * len(headers)
    return "\n".join(
        [
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join(separator) + " |",
            *("| " + " | ".join(row) + " |" for row in rows),
        ]
    )


def render_leaderboard(results: pd.DataFrame) -> str:
    """Render a complete Markdown leaderboard from raw benchmark results."""
    ranked, overall = rank_results(results)
    sections = [
        "# Benchmark Leaderboard",
        "",
        "Generated from chronological holdout forecasts. Lower RMSE, MAE, sMAPE and "
        "average rank are better. Overall rank uses each model's average RMSE rank across "
        "datasets so differently scaled datasets remain comparable.",
        "",
        "## Overall leaderboard",
        "",
        _markdown_table(overall),
    ]

    for dataset, group in ranked.groupby("dataset", sort=True):
        columns = ["rank", "model", "rmse", "mae", "smape", "train_size", "test_size"]
        available = [column for column in columns if column in group.columns]
        sections.extend(["", f"## {dataset}", "", _markdown_table(group[available])])

    sections.extend(
        [
            "",
            "## Reproduce",
            "",
            "```bash",
            "pip install -e '.[classical,dev]'",
            "time-series-benchmark --output benchmark_results.csv --leaderboard docs/BENCHMARK_LEADERBOARD.md",
            "```",
            "",
        ]
    )
    return "\n".join(sections)


def write_leaderboard(results: pd.DataFrame, output: str | Path) -> Path:
    """Write the rendered leaderboard and return its path."""
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_leaderboard(results), encoding="utf-8")
    return path
