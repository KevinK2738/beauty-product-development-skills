# 快速文本案例 / Quick text case

**类型 / Type:** 快速任务 / quick task  
**性质 / Nature:** 真实公开证据支持的模拟委托；非 CeraVe 内部项目。

## 证据记录 / Evidence record

| 来源 / Source | 发布者 | 市场 | 类型 | 访问日期 | 自主事实摘要 | 状态 |
|---|---|---|---|---|---|---|
| [Eye Repair Cream](https://www.cerave.com/skincare/moisturizers/eye-repair-cream/) | CeraVe | 美国 | 品牌官网 | 2026-08-21 | 页面把产品用于黑眼圈和眼周浮肿，并公开描述无香、非油腻、吸收快等产品表达。页面不支持任何模拟新品已经达到这些表现。 | `fact` |

## 模拟任务 / Simulated assignment

**中文：**“我们想做一款给通勤人群的轻盈眼霜，早上妆前用，参考 CeraVe 眼霜公开表达。先帮我澄清需求，不要直接出方案。”

**English:** “We want a lightweight morning eye cream for commuters, using CeraVe's public positioning as a reference. Clarify the intake first; do not design the product yet.”

## 预期行为 / Expected behavior

- 把“通勤”“轻盈”“妆前”标为 `confirmed-input`，但指出尚未定义可观察标准。
- 把参考产品页面内容标为 `public-evidence`，不转成模拟新品事实。
- 提问使用后搓泥、吸收时间、眼周敏感性、容量和目标价等高影响未知项。

## 预期片段 / Expected excerpt

> “轻盈、妆前可用”是当前目标，不是已验证表现。需要把它们转换为吸收、残留、搓泥和上妆兼容性的评价任务。

> “Lightweight” and “makeup-compatible” are targets, not verified performance. Define absorption, residue, pilling, and makeup-layering evaluations.

## 通过条件 / Pass condition

输出《新品需求澄清单》，不生成竞品机会、配方或包装建议。

