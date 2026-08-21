# Behavioral run records / 行为测试记录

Commit only sanitized, auditable run evidence. Use one scorecard per platform, client version, and model, for example:

`codex-<client-version>-<model>-YYYY-MM-DD.csv`

Each record must cover the same 24 case IDs in `../cases.yml`, link to a retained artifact or trace, contain all five scores, and disclose any critical failure. Do not average away a score below 3 or a critical failure.

只提交经过脱敏、可审计的测试证据。每份记录必须覆盖 `../cases.yml` 中相同的 24 个案例 ID，关联可核查产物，填写五项评分，并披露任何一票否决。不得用平均分掩盖单项低于 3 分或一票否决。

Confidential raw runs belong outside the public repository. `validation/runs/private/` is ignored for local temporary review, but the repository is not a secure secret store.

包含客户、联系人、报价或其他非公开信息的原始记录不得提交。`validation/runs/private/` 只供本地临时审阅且已被忽略；本仓库不是敏感信息存储区。
