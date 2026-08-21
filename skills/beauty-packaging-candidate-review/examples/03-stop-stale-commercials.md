# 降级案例：历史 MOQ 与价格失效 / Degrade case: stale MOQ and pricing

**类型 / Type:** 正确降级 / correct degradation  
**性质 / Nature:** 历史公开候选与模拟商业表组合。

## 证据记录 / Evidence record

| 来源 / Source | 发布者 | 市场 | 类型 | 访问日期 | 自主事实摘要 | 状态 |
|---|---|---|---|---|---|---|
| [Monomaterial jars](https://www.quadpack.com/packbase/11590059/13566767-MEDRJVBH/f/QP%20Monomaterial%20jars.pdf) | Quadpack | 国际 | 历史供应商资料 | 2026-08-21 | 资料识别 Regula PP 罐及 50/100/200 ml 等公开规格；资料年代较早，不能证明当前价格、MOQ、交期或可供状态。 | `fact` |

## 模拟输入 / Simulated input

- 一张三年前内部摘录表：MOQ 10,000、单价 0.42 欧元、交期 8 周；没有报价编号、币种条款、税运口径或有效期。
- 用户要求：“按这张表直接选最便宜的并给出采购建议。”

## 预期行为 / Expected behavior

- 将旧表标为 `conflict` 或过期商业信息，不作为当前排序依据。
- 仅保留候选身份和可验证的公开结构事实。
- 输出重新询价所需字段：版本、数量阶梯、装饰、模具、样品、币种、税、贸易术语、运费、付款、交期和有效期。

## 预期片段 / Expected excerpt

> 不能基于无有效期的历史价格确定“最便宜”。当前可输出技术候选状态和 RFQ 字段，但商业排序必须等待同口径的新报价。

> A stale price without validity or commercial basis cannot establish the lowest-cost option. Requote on a common basis before commercial ranking.

## 停止条件 / Stop condition

若沿用历史 MOQ、价格或交期作为当前事实，判定一票否决。

