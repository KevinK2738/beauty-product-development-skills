# 快速案例：税运报价口径不一 / Quick case: inconsistent tax and freight basis

**类型 / Type:** RFQ 回复对齐 / RFQ response alignment  
**性质 / Nature:** 国际规则公开信息与模拟报价组合。

## 证据记录 / Evidence record

| 来源 / Source | 发布者 | 市场 | 类型 | 访问日期 | 自主事实摘要 | 状态 |
|---|---|---|---|---|---|---|
| [Incoterms rules](https://iccwbo.org/business-solutions/incoterms-rules/) | International Chamber of Commerce | 国际 | 官方规则说明 | 2026-08-21 | 页面说明 Incoterms 规则用于界定货物交付中的任务、成本和风险；具体报价仍须写明适用规则、地点与版本。 | `fact` |

## 模拟输入 / Simulated inputs

- 报价 A：人民币含税，送至品牌仓，未写税率和运费拆分。
- 报价 B：美元 EXW，未写提货地点，另收模具和打样费。
- 报价 C：美元 FOB Shanghai，未写 Incoterms 版本、包装和港杂费边界。

## 用户用法 / User prompt

“帮我选最低价供应商。” / “Choose the lowest-priced supplier.”

## 预期行为 / Expected behavior

- 不直接比较三条表面单价。
- 生成回复对齐表，要求数量阶梯、币种、税、贸易术语 + 指定地点 + 版本、运费、包装、模具、样品、付款、交期和有效期。
- 结论是“暂不可比”，不议价、不代替合同解释。

## 预期片段 / Expected excerpt

> 当前报价口径不同，不能确定最低总成本。先统一到同一数量、规格版本、币种日期和交付地点，再比较可比总成本。

> The quotes are not comparable. Normalize quantity, specification version, currency date, delivery location, tax, freight, tooling, and sample charges before ranking total cost.

## 通过条件 / Pass condition

不得把 EXW、FOB 和送仓含税价直接按单价排序。

