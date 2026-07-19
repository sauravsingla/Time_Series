# Release checklist

Use this checklist for every tagged release of `time-series-reference`.

## 1. Validate the release scope

- Confirm that every user-visible change is recorded in `CHANGELOG.md`.
- Confirm that benchmark claims are reproducible from committed code and open datasets.
- Confirm that newly added models include baseline comparisons, tests and documented limitations.
- Confirm that no private data, credentials, tokens or generated secrets are committed.

## 2. Run local quality checks

```bash
python -m pip install --upgrade pip
pip install -e '.[classical,dev]'
ruff check src tests
ruff format --check src tests
mypy src/timeseries_reference
pytest --cov=timeseries_reference --cov-report=term-missing
time-series-benchmark \
  --output benchmark_results.csv \
  --leaderboard generated/BENCHMARK_LEADERBOARD.md
```

Review benchmark changes rather than accepting them automatically. Unexpected ranking changes may indicate a regression, changed dependency behaviour or an evaluation mistake.

## 3. Validate package metadata

Update the version in `pyproject.toml`, then build and inspect the distributions:

```bash
rm -rf build dist *.egg-info
python -m build
twine check dist/*
```

Verify that the source distribution and wheel contain the package, README, licence and expected metadata.

## 4. Review documentation

- Verify README installation and CLI commands.
- Verify documentation links.
- Verify the published benchmark leaderboard against freshly generated output.
- Verify that roadmap items are not described as implemented features.
- Verify the package version and changelog entry agree.

## 5. Create the release

1. Commit the version and changelog updates.
2. Wait for CI and CodeQL to pass.
3. Create an annotated tag such as `v0.3.0`.
4. Push the tag.
5. Create a GitHub Release using the matching changelog section.
6. Publish to PyPI through the protected `pypi` GitHub environment and Trusted Publishing workflow.

## 6. Post-release verification

Install the published artifact in a clean environment:

```bash
python -m venv release-check
source release-check/bin/activate
python -m pip install --upgrade pip
pip install time-series-reference
python -c "import timeseries_reference; print('import successful')"
time-series-benchmark --help
```

Confirm that the GitHub Release, PyPI project page, documentation links and citation metadata point to the intended version.

## Release principles

- Do not publish from an unreviewed working tree.
- Do not bypass failing tests, security checks or distribution validation.
- Do not change benchmark methodology silently.
- Do not claim support for models that exist only in roadmap documentation.
- Prefer a delayed release over an unreproducible release.
