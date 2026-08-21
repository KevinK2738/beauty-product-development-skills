# Codex 安装适配 / Codex installation

> 测试状态：待完成。本文只说明安装方式，不构成兼容性声明。

## 中文

本仓库中的每个 `skills/<skill-name>/` 都是独立源包。将所需目录复制或链接到 Codex 的 Skills 目录，并保持 `SKILL.md`、`references/`、`examples/` 与可选 `assets/` 的相对路径不变。重启或刷新客户端后，用该 Skill 的自然语言触发语义进行测试。

建议只安装实际需要的 Skill；8 个 Skill 不要求整套启用，也不依赖固定先后顺序。不要修改源包正文来适配客户端，平台差异应记录在本文或测试记录中。

Codex 的 Skills 概念与最新使用方式以 [OpenAI Skills 官方资料](https://openai.com/academy/skills/) 为准。客户端版本、模型、日期和运行结果必须写入 `validation/runs/`，通过门槛见根目录 `COMPATIBILITY.md`。

## English

Each `skills/<skill-name>/` directory is a standalone canonical package. Copy or link only the required package into the Codex skills location while preserving relative paths for `SKILL.md`, `references/`, `examples/`, and optional `assets/`. Refresh the client, then test with the natural-language trigger intent.

The eight skills are independently installable and have no mandatory sequence. Keep client-specific notes outside the canonical skill instructions. Refer to [OpenAI's official Skills material](https://openai.com/academy/skills/) for current product behavior, and record the tested client version, model, date, and result under `validation/runs/`.

