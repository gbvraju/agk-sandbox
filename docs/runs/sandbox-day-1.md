# Sandbox day 1 — agk init run

Date (UTC): 2026-10-14
Kit: `https://github.com/gbvraju/agk` at `86868be60392aaff85f3c88a8f3be84fb5b459cd` (read-only clone outside this repository)

## `python3 ../agk-kit/scripts/agk/init.py . --dry-run`

```
create .claude/agents/drift-auditor.md
create .claude/hooks/stop_check.py
create .claude/settings.json
create .github/CODEOWNERS
create .github/PULL_REQUEST_TEMPLATE.md
create .github/workflows/governance.yml
create .gitignore
create CLAUDE.md
create Makefile
create config/neutrality.txt
create config/protected-paths.txt
create config/reviewers.yaml
create constitution/principles.md
create constitution/vision.md
create docs/adr/0001-adopt-agk.md
create docs/adr/TEMPLATE.md
create docs/briefs/TEMPLATE.md
create docs/build-state.md
create docs/requirements.md
create docs/runs/decisions-log.md
create docs/specs/TEMPLATE.md
create pyproject.toml
create scripts/agk/check_adrs.py
create scripts/agk/check_build_state.py
create scripts/agk/check_neutrality.py
create scripts/agk/check_pr_body.py
create scripts/agk/check_protected_changes.py
create scripts/agk/check_requirements.py
create scripts/agk/common.py
create scripts/agk/reviewers.py
create scripts/agk/traceability.py
create tests/kit/conftest.py
create tests/kit/test_check_adrs.py
create tests/kit/test_check_build_state.py
create tests/kit/test_check_neutrality.py
create tests/kit/test_check_pr_body.py
create tests/kit/test_check_protected_changes.py
create tests/kit/test_check_requirements.py
create tests/kit/test_reviewers.py
create tests/kit/test_stop_hook.py
create tests/kit/test_workflow.py
dry run: 41 files would be created; nothing was written
notice: config/reviewers.yaml maps `maintainers` to the placeholder @REPLACE-ME
Apply by hand on GitHub (init configures nothing):
The ruleset `main` is exactly: Active; no bypass; target the default branch; restrict deletions; require linear history; require a pull request (0 approvals, dismiss stale approvals, squash merge only); block force pushes; required status check `governance`.
Repository settings: allow auto-merge; auto-delete head branches.
```

## `python3 ../agk-kit/scripts/agk/init.py .`

```
create .claude/agents/drift-auditor.md
create .claude/hooks/stop_check.py
create .claude/settings.json
create .github/CODEOWNERS
create .github/PULL_REQUEST_TEMPLATE.md
create .github/workflows/governance.yml
create .gitignore
create CLAUDE.md
create Makefile
create config/neutrality.txt
create config/protected-paths.txt
create config/reviewers.yaml
create constitution/principles.md
create constitution/vision.md
create docs/adr/0001-adopt-agk.md
create docs/adr/TEMPLATE.md
create docs/briefs/TEMPLATE.md
create docs/build-state.md
create docs/requirements.md
create docs/runs/decisions-log.md
create docs/specs/TEMPLATE.md
create pyproject.toml
create scripts/agk/check_adrs.py
create scripts/agk/check_build_state.py
create scripts/agk/check_neutrality.py
create scripts/agk/check_pr_body.py
create scripts/agk/check_protected_changes.py
create scripts/agk/check_requirements.py
create scripts/agk/common.py
create scripts/agk/reviewers.py
create scripts/agk/traceability.py
create tests/kit/conftest.py
create tests/kit/test_check_adrs.py
create tests/kit/test_check_build_state.py
create tests/kit/test_check_neutrality.py
create tests/kit/test_check_pr_body.py
create tests/kit/test_check_protected_changes.py
create tests/kit/test_check_requirements.py
create tests/kit/test_reviewers.py
create tests/kit/test_stop_hook.py
create tests/kit/test_workflow.py
installed 41 files
notice: config/reviewers.yaml maps `maintainers` to the placeholder @REPLACE-ME
Apply by hand on GitHub (init configures nothing):
The ruleset `main` is exactly: Active; no bypass; target the default branch; restrict deletions; require linear history; require a pull request (0 approvals, dismiss stale approvals, squash merge only); block force pushes; required status check `governance`.
Repository settings: allow auto-merge; auto-delete head branches.
```

No conflicts; `README.md` was not touched.

## Maintainers' instruction

`config/reviewers.yaml`: `@REPLACE-ME` replaced with `@gbvraju`; `.github/CODEOWNERS` regenerated with
`python3 scripts/agk/reviewers.py --codeowners` (the flag prints to stdout; output redirected into the file).

## Checks

`make governance` (exit 0):

```
ok protected-changes (protected change covered by an ADR)
ok requirements (3 requirements)
ok adrs (1 ADRs)
ok neutrality (0 tokens)
ok build-state (file created)
ok reviewers
ok reviewers (.github/CODEOWNERS matches)
```

`make test`: `95 passed in 10.39s` (exit 0). `pytest` was not installed in the container, so it was installed
into a throwaway virtualenv outside the repository and run as `make test PY=<venv>/bin/python`.

`ruff check .`: `All checks passed!`

pytest installed in a throwaway venv because the session lacked it; CI installs its own.
