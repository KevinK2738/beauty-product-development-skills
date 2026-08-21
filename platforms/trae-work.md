# TRAE Work 安装适配 / TRAE Work installation

> 测试状态：当前机器未安装 TRAE Work，且尚未确认其当前版本对该源包结构的完整导入行为。

## 中文

本仓库不把 TRAE Work 的产品介绍等同于 Agent Skills 格式兼容。官方产品入口可用于确认客户端与功能范围：[TRAE Work 官方介绍](https://www.trae.ai/blog/trae_work_0609)。

测试人员应在真实 TRAE Work 客户端中确认：

1. 是否能导入或稳定调用完整目录，而非只读取单个提示词；
2. 是否按任务语言加载正确的双语参考文件；
3. 是否能读取案例和 Excel/邮件资产；
4. 停止/降级边界是否在实际模型中生效；
5. 产物是否可以保存并回溯到输入证据。

若客户端需要不同清单或包格式，只新增薄适配文件，不复制或分叉 8 套能力正文。未完成 24 次真实运行前，`COMPATIBILITY.md` 必须保持“待测试”。

## English

This repository does not treat a product introduction as proof of Agent Skills package compatibility. Validate the complete package in a real TRAE Work client: directory import, language routing, reference and asset access, stopping behavior, and artifact traceability.

If a future client version requires a manifest or wrapper, add a thin adapter without forking the eight canonical instruction sets. Keep compatibility marked as pending until all 24 platform runs pass.

