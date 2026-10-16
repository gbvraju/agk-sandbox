# ADR-0004: protect agk.mk and agk.toml; remove the obsolete [tool.agk] table

- Status: Accepted
- Date: 2026-10-16
- Deciders: maintainers
- Related: ADR-0003
- Requirements: REQ-001
- Protected classes: `config/`, `pyproject.toml`, `.github/`

## Context

ADR-0003 upgraded the kit from 0.1.0 to 0.9.0. The upgrade created `agk.mk` (the commands the `Makefile` and the CI
workflow call) and `agk.toml` (the kit's configuration and version stamp), and printed that the kit's current protected
list also names them. Until they are in `config/protected-paths.txt`, a change to either needs no ADR. The upgrade also
left the obsolete `[tool.agk]` table in `pyproject.toml`, since `agk.toml` replaced it; both ADR-0003 residuals name
these two changes.

## Decision

1. Add `agk.mk` and `agk.toml` to `config/protected-paths.txt`, and to the `protected` and `kit` classes of
   `config/reviewers.yaml` (`reviewers.py --check` requires the two lists to be equal); re-render `.github/CODEOWNERS`
   with `python3 scripts/agk/reviewers.py --codeowners --write`.
2. Remove the `[tool.agk]` table from `pyproject.toml`. `agk.toml` carries the same settings (`version`, `installed`,
   `test_dirs`); no other line of `pyproject.toml` changes.

## Consequences

- A change to `agk.mk` or `agk.toml` now needs an ADR that names its class, and is owned by the maintainers in CODEOWNERS.
- The ADR-0003 residuals (due 2026-10-23 and 2026-10-31) are closed by this change.

## Residual

- None.
