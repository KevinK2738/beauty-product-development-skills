# 专业案例：促销与多规格价格 / Professional case: promotion and variants

**类型 / Type:** 表格归一 / spreadsheet normalization  
**性质 / Nature:** 真实公开价格快照加模拟比较表。

## 证据记录 / Evidence record

| 来源 / Source | 发布者 | 市场 | 类型 | 访问日期 | 自主事实摘要 | 状态 |
|---|---|---|---|---|---|---|
| [舒敏保湿修护精华液 30 ml](https://www.winona.cn/product/110255.html) | Winona / 薇诺娜 | 中国 | 品牌官网 | 2026-08-21 | 页面公开 30 ml 规格、页面价格及下架状态；只能作为带日期的页面快照，不能代表当前可购价格或长期价格带。 | `fact` |
| [Avocado Eye Cream](https://www.kiehls.com/skincare/eye-creams-and-serums/avocado-eye-cream/3700194714413.html) | Kiehl's | 美国 | 品牌官网 | 2026-08-21 | 页面列出14ml和28ml规格及不同单位容量价格，且注明部分评价可能受激励。 | `fact` |

## 模拟文件 / Simulated file

表格混合日常价、满减后价格、赠品折算价、不同币种及30/50ml、14/28ml规格，并把眼霜与面部精华放在同一排名。

## 用户用法 / User prompt

“整理成单位容量价格排名，找最适合进入的价格空档。” / “Normalize price per ml and find the best price gap.”

## 预期行为 / Expected behavior

- 先按品类/部位、市场、币种、规格和促销状态拆分。
- 展示单位容量公式，但不跨不可比类别做排名。
- 把访问日价格标为快照，不推断长期价格带。

## 预期片段 / Expected excerpt

> 眼霜与面部精华用途不可直接排名；促销、赠品与常规售价需分栏。当前只能形成分组价格地图，不能证明价格空档。

> Eye cream and face serum cannot share one price ranking. Promotion, gift value, and regular price require separate fields; the result is a grouped price map, not proof of a gap.

## 一票否决 / Critical failure

混合币种或促销状态后给出确定价格机会。
