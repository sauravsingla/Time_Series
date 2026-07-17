## Summary

Describe the forecasting problem and the change in a few sentences.

## Why this change is needed

Explain the user, teaching or research value. State why the existing implementation is insufficient.

## Validation

- [ ] `ruff check src tests`
- [ ] `pytest`
- [ ] Relevant open-dataset benchmark executed
- [ ] No random shuffling or future-data leakage
- [ ] New behaviour has tests
- [ ] Assumptions and limitations are documented

## Benchmark impact

Include before/after results when the change affects forecasts. Compare against naive and seasonal-naive baselines and specify dataset, horizon and metrics.

## Reproducibility

Provide the exact command needed to reproduce the result. Confirm that no private data, credentials or manually modified files are required.

## Scope

List anything intentionally left for a follow-up pull request.
