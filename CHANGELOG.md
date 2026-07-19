# Changelog

All notable changes to the maintained reference implementation are documented here. The project follows the spirit of Keep a Changelog and semantic versioning once releases begin.

## Unreleased

### Added

- Reusable `timeseries_reference` Python package.
- Naive, seasonal-naive, drift and moving-average baselines.
- Autoregression and Holt-Winters classical models.
- Ridge lag-regression forecasting.
- Leakage-safe chronological splitting and expanding-window backtesting.
- MAE, RMSE, MAPE and sMAPE metrics.
- Open benchmark datasets for sunspots, Mauna Loa CO2 and US real GDP.
- Command-line benchmark execution.
- Per-dataset and scale-independent overall leaderboard.
- Python 3.10–3.12 continuous integration.
- Deterministic unit and integration tests.
- Documentation hub, methodology, FAQ, troubleshooting and glossary.
- Practical forecasting and model-selection guides covering real-world use cases.
- Contribution, security, conduct, citation and pull-request guidance.
- Dependabot configuration for Python and GitHub Actions dependencies.
- CodeQL security analysis.
- Pre-commit checks for Ruff, formatting and repository hygiene.
- PyPI Trusted Publishing workflow.
- Repository code ownership rules.
- Reproducible release checklist.
- Coverage configuration with an 85% minimum.
- CI package-build and distribution validation.

### Changed

- Replaced the minimal landing page with a structured reference-quality README.
- Reframed legacy notebooks as historical learning material while directing users to the tested package.
- Expanded package metadata and search keywords for forecasting methods and business use cases.
- Strengthened CI with formatting checks, static type checking, branch coverage and package validation.
- Enabled strict pytest configuration to catch unknown markers and invalid settings.

### Notes

The initial reference release intentionally prioritizes transparent baselines and reproducible evaluation over adding many unvalidated model families.
