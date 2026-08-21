# Release gate snapshot / 发布门槛快照

Snapshot date / 快照日期: 2026-08-21

| Gate | Current evidence | Status |
|---|---|---|
| 8 canonical Skill packages | Frontmatter, bilingual instructions, bilingual result formats | Pass |
| 24 fixed cases | 8 skills × quick, professional, stop/degrade | Pass |
| Required editable assets | 4 `.xlsx` templates and 2 plain-text email template sets | Pass |
| Static repository validation | `python3 scripts/validate_repo.py` | Pass |
| Public URL check | `python3 scripts/check_links.py`; 32 unique URLs reachable on snapshot date, including sites that returned access-limiting HTTP responses | Pass |
| Skill package validation | Eight packages pass the Skill Creator validator | Pass |
| Spreadsheet application smoke test | WPS Office for macOS 12.1.26046 passed one open/edit/save test; Excel and LibreOffice untested | Partial |
| Codex behavioral runs | 0/24 recorded | Pending |
| WorkBuddy behavioral runs | 0/24 recorded; client absent | Pending |
| TRAE Work behavioral runs | 0/24 recorded; client absent | Pending |
| Doubao Office Tasks behavioral runs | 0/24 recorded; client absent | Pending |
| GitHub publication | Local repository initialized; no remote and no authenticated GitHub CLI session | Pending |

`v1.0.0` must not be tagged or published until all 96 behavioral runs meet the scoring threshold with no critical failure. This snapshot records a release candidate, not an industry certification or four-platform compatibility claim.

在 96 次行为测试全部达到评分门槛且没有一票否决之前，不得创建或发布 `v1.0.0`。本快照只代表发布候选状态，不代表行业认证或四端兼容声明。
