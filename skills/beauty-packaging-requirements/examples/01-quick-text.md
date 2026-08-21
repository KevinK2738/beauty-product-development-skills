# 快速文本案例：光氧敏感精华 / Quick text case: light- and oxygen-sensitive serum

**类型 / Type:** 快速任务 / quick task  
**性质 / Nature:** 真实公开参考支持的模拟委托；非 SkinCeuticals 内部项目。

## 证据记录 / Evidence record

| 来源 / Source | 发布者 | 市场 | 类型 | 访问日期 | 自主事实摘要 | 状态 |
|---|---|---|---|---|---|---|
| [C E Ferulic](https://www.skinceuticals.com/skincare/vitamin-c-serums/c-e-ferulic-with-15-l-ascorbic-acid/S17.html) | SkinCeuticals | 美国 | 品牌官网 | 2026-08-21 | 页面公开 30 ml 规格、配方成分表达和使用方式；页面本身不构成模拟产品的稳定性结论。 | `fact` |
| [Provisions for Cosmetics Production and Operation](https://english.nmpa.gov.cn/2022-10/25/c_961745.htm) | 国家药监局 / NMPA | 中国 | 官方法规信息 | 2026-08-21 | 公开条文涉及与化妆品直接接触的包装材料管理、标签和可追溯要求；具体项目适用性仍需法规人员确认。 | `fact` |

## 模拟任务 / Simulated assignment

**中文：**“做一款 30 ml 精华，内容物团队确认对光和氧敏感。请写包装开发需求，不要替供应商填技术参数。”

**English:** “Develop packaging requirements for a 30 ml serum. The formula team confirms light and oxygen sensitivity. Do not invent supplier parameters.”

## 预期行为 / Expected behavior

- 将光氧敏感性标为 `confirmed-input`，将公开产品信息仅作为 `public-evidence`。
- 覆盖初级容器、泵/滴管、密封、装饰、标签、附件和运输包装，而非只写瓶子。
- 把遮光、氧暴露、残留量、相容性和运输完整性写成验证任务，不编造透过率、泄漏阈值或寿命。

## 预期片段 / Expected excerpt

> 遮光与低氧暴露是设计目标；验收阈值应由内容物稳定性方案、风险评估与供应商可实现能力共同确认。

> Light protection and low oxygen exposure are design objectives. Acceptance thresholds require confirmation through stability planning, risk assessment, and supplier capability.

## 通过条件 / Pass condition

产出完整包装系统需求和验证矩阵，未知工程数值保持 `requires-confirmation`。

