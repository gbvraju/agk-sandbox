# Requirements

Each requirement is a `### REQ-nnn` section with a `- Status:` line (planned | in-progress | done).
Only the Status line may change without an ADR. `done` requires at least one test marker `REQ-nnn` in a
`test_*.py` file under `tests/`.

`REQ-001`..`REQ-099` are reserved for requirements defined by the kit. Add this project's requirements from
`REQ-101`.

### REQ-001 — Protected paths change only with an ADR in the same PR

- Acceptance: AC1 check fails without an ADR that names the path class; AC2 Status-only change in requirements exempt; AC3 message names the path class
- Status: planned

### REQ-002 — Agents never merge or bypass checks

- Acceptance: AC1 branch rules documented in ADR-0001; AC2 settings deny force-push and hard reset; AC3 stop hook blocks on red governance
- Status: planned

### REQ-003 — Every requirement is traceable to tests

- Acceptance: AC1 matrix generated; AC2 done requires a marker; AC3 matrix never committed
- Status: planned

### REQ-101 — Count words

- Acceptance: AC1 prints the count of whitespace-separated words on stdin; AC2 empty input prints `0`
- Status: planned

### REQ-102 — Refuse non-UTF-8 input

- Acceptance: AC1 exit code 2 and a message naming the input encoding setting, never the bytes
- Status: planned
