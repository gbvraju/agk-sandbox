# ADR-0003: upgrade the kit from 0.1.0 to 0.9.0

- Status: Accepted
- Date: 2026-10-16
- Deciders: maintainers
- Related: ADR-0001
- Requirements: REQ-001
- Protected classes: `.claude/`, `.github/`, `CLAUDE.md`, `Makefile`, `constitution/`, `scripts/agk/`, `tests/kit/`

## Context

The sandbox was installed by agk kit 0.1.0, which stamps `[tool.agk]` in `pyproject.toml`. The kit is now 0.9.0
(SPEC-0008, the upgrade). Running `python3 scripts/agk/upgrade.py` from the kit checkout on this repository replaced
the vendored files that were still the released 0.1.0 copies, created the files the kit has gained since, and created
`agk.toml` from the kit's template as the last write. It changed no product file and did not write `pyproject.toml`;
the `[tool.agk]` table there is now obsolete and is removed in a separate change.

The upgrade writes into protected classes, so this pull request carries this ADR, which names each class.

## Decision

Upgrade the kit from 0.1.0 to 0.9.0.

## Consequences

- `make governance` runs the 0.9.0 checks. `.github/CODEOWNERS` was re-rendered with `python3 scripts/agk/reviewers.py
  --codeowners --write` (the upgrade printed the command), which dropped the duplicate lines of the 0.1.0 rendering.
- `config/protected-paths.txt`, `config/reviewers.yaml` and the other files the sandbox owns are not rewritten; the
  upgrade printed the lines of the new templates they lack, for a separate change.

## Residual

- 2026-10-16: `pyproject.toml` still carries the obsolete `[tool.agk]` table (remove it in a separate change)
  (due 2026-10-31).
- 2026-10-16: `config/protected-paths.txt` lacks `agk.mk` and `agk.toml` (printed by the upgrade); until added, changes
  to them need no ADR (due 2026-10-23).
