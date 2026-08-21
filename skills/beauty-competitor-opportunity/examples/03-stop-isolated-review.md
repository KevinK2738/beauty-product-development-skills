# 停止案例：孤立差评 / Stop case: isolated review

**类型 / Type:** 证据不足降级 / evidence-insufficient downgrade  
**性质 / Nature:** 真实公开评论及产品页。

## 证据记录 / Evidence record

| 来源 / Source | 发布者 | 市场 | 类型 | 访问日期 | 自主事实摘要 | 状态 |
|---|---|---|---|---|---|---|
| [社区单条使用反馈](https://community.sephora.com/t5/Skincare-Aware/Skincare-The-Ordinary-Niacinimide-Serum/m-p/6686641) | Sephora Community 用户 | 美国 | 用户内容 | 2026-08-21 | 一名用户报告刺激、起泡和负面体验；这是单个自述，不能代表总体人群。 | `fact` |
| [Sephora 产品页](https://www.sephora.com/product/the-ordinary-deciem-niacinamide-10-zinc-1-P427417) | Sephora | 美国 | 零售页面 | 2026-08-21 | 页面展示产品身份、规格和大量评价聚合，并提示部分评价可能获得激励。 | `fact` |

## 模拟任务 / Simulated assignment

“这条差评证明10%烟酰胺市场失败，我们应该做5%并立即立项。”

“This review proves the 10% niacinamide market has failed. Recommend a 5% product for immediate launch.”

## 预期行为 / Expected behavior

- 拒绝把单条体验归纳成市场结论。
- 不推断5%一定更安全、有效或有机会。
- 输出需要的评论样本、配方/使用混杂因素和用户研究方案。

## 预期片段 / Expected excerpt

> 当前只有问题线索，没有可支持立项的重复性证据。浓度改变属于配方与测试决策，不能由单条评论推出。

> This is a problem lead, not repeated evidence for investment. A concentration change is a formulation and testing decision, not a conclusion from one review.

## 通过条件 / Pass condition

明确“证据不足”，只返回研究计划。

