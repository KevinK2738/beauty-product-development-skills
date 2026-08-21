# 豆包安装适配 / Doubao installation

> 测试状态：当前机器未安装目标豆包客户端；尚无本仓库可据以声明兼容的真机结果。

## 中文

豆包不同产品形态和版本可能具有不同的智能体、文件或知识导入能力。本仓库暂不假定它们原生支持 Agent Skills 目录。

测试时应记录确切产品名称、客户端版本、模型与导入方式。如果只能粘贴单个提示词、不能稳定读取 `references/` 和 `assets/`，则该方式不算完整兼容。可以为该客户端增加薄适配说明，但不得把正文复制成独立分支后声称同等能力。

逐个 Skill 完成快速文本、专业文件、停止/降级三类任务，并保留产物和评分。24 次运行全部达标后再更新兼容表。

## English

Different Doubao products and versions may expose different agent, file, or knowledge-import capabilities. Do not assume native support for an Agent Skills directory.

Record the exact product, client version, model, and import method. A prompt-only setup that cannot reliably access `references/` and `assets/` is not full compatibility. Run all three fixed scenarios per skill and publish compatibility only after all 24 runs pass.

