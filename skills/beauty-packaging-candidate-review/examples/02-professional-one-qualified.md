# 专业案例：只有一个候选满足门槛 / Professional case: only one candidate clears the gate

**类型 / Type:** 多候选文件评审 / multi-candidate review  
**性质 / Nature:** 真实公开候选事实与模拟项目门槛组合；不代表供应商背书。

## 证据记录 / Evidence record

| 来源 / Source | 发布者 | 市场 | 类型 | 访问日期 | 自主事实摘要 | 状态 |
|---|---|---|---|---|---|---|
| [JS-G01 Airless Bottle](https://www.sy-jinsheng.com/product/airless-bottle/jsg01.html) | Shaoxing Jinsheng | 中国 | 供应商官网 | 2026-08-21 | 页面公开 15/30/50 ml、直径和高度等候选识别信息；供应能力和完整材料仍需确认。 | `fact` |
| [Affinity Airless 10 ml product sheet](https://www.hcpackaging.com/product/33085/pdf/) | HCP Packaging | 国际 | 供应商产品页 | 2026-08-21 | 页面识别一个 10 ml 真空候选及部分公开属性；容量与本模拟项目 30 ml 硬门槛不符。 | `fact` |

## 模拟项目门槛 / Simulated project gates

- 必须为 30 ml；高度上限 125 mm；泵式真空结构。
- 直接接触材料、剂量、装饰附着和配方相容性均须后续确认。
- 采购要求至少比较两个候选，但不允许降低容量门槛。

## 用户用法 / User prompt

“评审这两个目录候选，给出排序和下一步。” / “Review and rank these two catalog candidates, then give next steps.”

## 预期行为 / Expected behavior

- 10 ml 候选因硬门槛不符直接淘汰，而不是为了形成排名而保留。
- 30 ml 候选只能标为“条件通过到 RFI/样品验证”，不能被描述为最终合格。
- 明确指出候选池不足，应补充检索条件和 RFI 字段。

## 预期片段 / Expected excerpt

> 当前没有两个可比合格候选：候选 B 违反容量硬门槛；候选 A 仅通过目录级筛选。建议保留 A 并按相同条件补搜，而非人为凑出冠亚军。

> There are not two comparable qualified candidates. Candidate B fails the fill-size gate; Candidate A passes catalog screening only.

## 通过条件 / Pass condition

排序不能掩盖硬门槛淘汰，也不能把“候选不足”写成“已完成选型”。

