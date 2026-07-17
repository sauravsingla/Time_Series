# Security Policy

## Supported code

Security reports should concern the maintained Python package, automation or repository configuration on the default branch. Historical notebooks are retained for learning and provenance and may contain older dependency references.

## Reporting a vulnerability

Please do not open a public issue for a vulnerability that could expose credentials, private data or arbitrary code execution.

Use GitHub's private vulnerability reporting feature when it is available for this repository. Include:

- the affected file and version or commit;
- a clear reproduction procedure;
- the expected and observed behaviour;
- the potential impact;
- a proposed mitigation, when known.

Do not include real credentials, private datasets, payment information or personally identifiable information in a report or test case.

## Data safety

This project uses public example datasets. Contributions must not contain confidential business data, production extracts, API tokens or personal information. Use public or deterministic synthetic data for demonstrations and tests.

## Dependency concerns

Dependency vulnerabilities should identify the affected package and explain whether the vulnerable functionality is reachable through this project. Automated alerts are useful signals, but upgrades should still be validated with the full test and benchmark suite.
