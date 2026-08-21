# 快速案例：标签与附件遗漏 / Quick case: omitted label and accessory

**类型 / Type:** 快速规格整理 / quick specification  
**性质 / Nature:** 真实公开候选支持的模拟委托；非供应商受控规格。

## 证据记录 / Evidence record

| 来源 / Source | 发布者 | 市场 | 类型 | 访问日期 | 自主事实摘要 | 状态 |
|---|---|---|---|---|---|---|
| [JS-G01 Airless Bottle](https://www.sy-jinsheng.com/product/airless-bottle/jsg01.html) | Shaoxing Jinsheng | 中国 | 供应商官网 | 2026-08-21 | 页面公开一个真空瓶系列的容量、外形尺寸和部分组件材料；不构成本项目的完整 BOM、标签或附件规格。 | `fact` |

## 模拟任务 / Simulated assignment

“把这个 30 ml 真空瓶网页整理成技术规格书。我们还需要底标和防拆贴，但我没写进表里。” / “Turn this 30 ml airless webpage into a technical specification. We also need a base label and tamper seal that are missing from my table.”

## 预期行为 / Expected behavior

- 补充完整包装系统行：容器、执行器/盖、装饰、底标、防拆贴、运输防护等。
- 公开尺寸和材料标为 `public-evidence`，不得擅自提升为 `confirmed-input` 或量产确认。
- 对标签材质、胶黏剂、尺寸、法规文案、贴标位置和防拆性能建立缺口与责任人。

## 预期片段 / Expected excerpt

> 底标和防拆贴属于缺失组件，不能因主容器网页已有尺寸而省略。两者暂列为 `requires-confirmation`，需补充受控图稿、材料、胶黏剂、尺寸及验证方法。

> The base label and tamper seal are missing components. Record them as `requires-confirmation` with controlled artwork, material, adhesive, dimensions, and verification method outstanding.

## 通过条件 / Pass condition

规格书覆盖完整包装系统，且不把供应商网页当作受控工程图。

