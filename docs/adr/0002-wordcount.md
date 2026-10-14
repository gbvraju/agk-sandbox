# ADR-0002: the sandbox product is a wordcount CLI

- Status: Proposed
- Date: 2026-10-14
- Deciders: maintainers
- Related: ADR-0001
- Requirements: REQ-101, REQ-102
- Protected classes: docs/requirements.md

## Context

The sandbox needs a first product requirement that exercises the governance kit end to end: a protected path
change that needs an ADR, tests that carry requirement markers, and a PR body that passes the checks.

## Decision

1. The sandbox's product is a tiny CLI `wordcount` (`src/wordcount.py`, standard library only) that reads UTF-8
   text on stdin and prints the number of words.
2. A word is a maximal run of non-whitespace characters; empty input prints `0` (REQ-101).
3. Input that is not valid UTF-8 is refused with exit code 2 and a message naming the input encoding setting,
   never the bytes (REQ-102).
4. `docs/requirements.md` gains REQ-101 and REQ-102 with Status `planned`. Maintainers change the Status lines.

## Consequences

- Adding the requirements changes a protected path, so this ADR names its class (`docs/requirements.md`).
- Tests run the CLI as a subprocess, so no import-path or `pyproject.toml` change is needed.

## Residual

- 2026-10-14: no packaging or entry point; the CLI is run as `python3 src/wordcount.py`.
