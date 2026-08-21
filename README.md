# 美妆产品开发 Skills

[English](README.en.md)

一组面向美妆产品、包装与供应链实务的开源 Agent Skills。它们帮助从业者把零散输入整理成可审阅、可追溯、可继续协作的结果物，而不是替代配方工程、法规判断、供应商承诺或量产放行。

本项目由 **K-Beauty** 维护，采用 [Apache License 2.0](LICENSE)；许可使用说明可参阅 [Apache Software Foundation](https://www.apache.org/legal/apply-license.html) 与 [OSI 许可证目录](https://opensource.org/licenses)。项目为独立开源作品，与案例中提到的品牌、供应商及平台无隶属、合作或背书关系。

**当前状态：发布候选。** Skill 内容、案例和模板已经建立；四个平台的 96 次真实运行尚未完成，因此当前仓库不应标记或宣传为 `v1.0.0`，也不声称未经测试的平台兼容。当前门槛快照见 [`validation/RELEASE_CHECKLIST.md`](validation/RELEASE_CHECKLIST.md)。

## 能力

| Skill | 适用任务 | 默认结果物 |
|---|---|---|
| [`beauty-product-intake`](skills/beauty-product-intake/) | 审阅新品想法与混合资料，隔离事实、主张、约束、冲突和未知项 | 《新品需求澄清单》 |
| [`beauty-competitor-opportunity`](skills/beauty-competitor-opportunity/) | 围绕明确决策问题研究竞品、用户问题及产品与包装机会 | 《竞品与产品包装机会简报》 |
| [`beauty-product-brief`](skills/beauty-product-brief/) | 将新品目标和约束转成跨职能可评审的定义 | 《新品开发 Brief》 |
| [`beauty-packaging-requirements`](skills/beauty-packaging-requirements/) | 把内容物、体验、渠道和商业条件转成包装要求与验证计划 | 《美妆包装开发需求书》 |
| [`beauty-packaging-candidate-review`](skills/beauty-packaging-candidate-review/) | 审阅用户提供的包材目录、图纸、链接和商务数据 | 《包材候选评审》 |
| [`beauty-packaging-directions`](skills/beauty-packaging-directions/) | 基于真实结构和策略张力形成可评审的包装设计方向 | 《包装设计方向提案》 |
| [`beauty-packaging-specification`](skills/beauty-packaging-specification/) | 整理询价、打样、确认或变更状态下的包材技术信息 | 《美妆包材技术规格书》 |
| [`beauty-packaging-rfq`](skills/beauty-packaging-rfq/) | 准备 RFI、RFQ、打样请求，或对齐供应商回复 | 《询盘与回复对齐包》 |

这些 Skill 可以独立安装、独立调用。它们不要求按固定顺序执行，也不会为了补齐流程自动调用另一个 Skill。

## 使用方式

每个目录都是一个标准 Skill 包。把需要的目录安装到支持 Agent Skills 的产品中，然后用自然语言描述任务。例如：

> 请审阅附件里的产品手册、传播 Brief 和品牌规范，区分已确认事实、宣传主张、创意约束与版本冲突，生成新品需求澄清单。

平台安装入口见 [`platforms/`](platforms/)。兼容性只按真实测试结果公布，见 [`COMPATIBILITY.md`](COMPATIBILITY.md)。

`beauty-packaging-specification` 和 `beauty-packaging-rfq` 另含中英文 `.xlsx` 空白模板，RFQ Skill 还含中英文纯文本邮件模板。表格应用实测记录见 [`validation/spreadsheet-compatibility.md`](validation/spreadsheet-compatibility.md)。

## 可编辑资产

| 用途 | 中文 | English |
|---|---|---|
| 包材技术规格书 | [Excel 模板](skills/beauty-packaging-specification/assets/beauty-packaging-specification-template.zh-CN.xlsx) | [Excel template](skills/beauty-packaging-specification/assets/beauty-packaging-specification-template.en.xlsx) |
| RFI / RFQ / 打样 / 回复对齐 | [Excel 模板](skills/beauty-packaging-rfq/assets/beauty-packaging-rfq-template.zh-CN.xlsx) · [邮件模板](skills/beauty-packaging-rfq/assets/email-templates.zh-CN.txt) | [Excel template](skills/beauty-packaging-rfq/assets/beauty-packaging-rfq-template.en.xlsx) · [Email templates](skills/beauty-packaging-rfq/assets/email-templates.en.txt) |

## 共同证据状态

所有 Skill 使用同一组状态，防止建议被误写成事实：

- `confirmed-input`：用户明确提供的信息。
- `public-evidence`：有可追溯公开来源支持的事实。
- `recommendation`：Skill 基于现有信息提出的建议。
- `requires-confirmation`：需品牌方、供应商、测试或法规专业人员确认。
- `conflict`：来源、版本或字段之间存在冲突。

## 案例与证据

案例使用真实公开资料支持的模拟委托，不声称复原任何品牌的内部决策。仓库只保存自主改写的最小事实摘要、来源链接和访问日期，不保存第三方 Logo、图片、整页网页或长篇原文。完整规则见 [`SOURCE_POLICY.md`](SOURCE_POLICY.md)。

## 质量边界

本仓库定位为专业实务型工具，不代表行业认证。任何输出仍需由相应责任方确认，尤其是：

- 配方比例、生产工艺和功效证据；
- 法规、备案、注册和宣称结论；
- 包材相容性、密封、跌落、耐磨和量产测试；
- MOQ、价格、产能、库存和交期；
- 工程图、公差、合同、采购准入和量产放行。

## 贡献

欢迎提交 Issue 和 Pull Request。贡献者必须说明来源、授权状态、适用边界，并确保不包含客户、雇主、供应商或其他主体的非公开信息。见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。
