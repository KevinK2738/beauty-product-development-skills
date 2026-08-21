# Compatibility

[简体中文](COMPATIBILITY.md)

The project maintains one canonical Agent Skills source. The table lists only platforms on which installation, triggering, and output behavior have actually been validated. Untested platforms are not claimed as compatible.

| Platform | Status | Tested version | Test date | Cases passed | Notes |
|---|---|---|---|---:|---|
| Codex | Full test pending | To record | — | 0/24 | Repository-level static validation only |
| WorkBuddy | Untested | — | — | 0/24 | Client installation and login required |
| TRAE Work | Untested | — | — | 0/24 | TRAE Work must be tested separately from TRAE IDE |
| Doubao Office Tasks | Untested | — | — | 0/24 | Client installation and login required |

The `v1.0.0` release gate is 96/96 passing scenarios. See [`validation/README.md`](validation/README.md) for the run record format. Until the gate is met, repository content is a release candidate and must not be tagged v1.0.0.

