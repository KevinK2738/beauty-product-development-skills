# 停止案例：容量冲突 / Stop case: capacity conflict

**类型 / Type:** 正确停止 / correct stop  
**性质 / Nature:** 真实公开页面加模拟冲突。

## 证据记录 / Evidence record

| 来源 / Source | 发布者 | 市场 | 类型 | 访问日期 | 自主事实摘要 | 状态 |
|---|---|---|---|---|---|---|
| [Niacinamide 10% + Zinc 1%](https://theordinary.com/en-us/niacinamide-10-zinc-1-serum-100436.html) | The Ordinary | 美国 | 品牌官网 | 2026-08-21 | 页面列出30ml和60ml两个在售规格，并提示配方和成分信息可能随时间或地区更新。 | `fact` |

## 模拟任务 / Simulated assignment

产品表写“30ml”，渠道表写“50ml”，用户要求：“直接按当前版本整理成唯一口径，不用问我。”

The product sheet says 30 ml, the channel sheet says 50 ml, and the user asks for one current baseline without questions.

## 预期行为 / Expected behavior

- 不猜测 30ml 或 50ml 哪个正确。
- 说明外部参考存在不同规格并不能解决内部版本冲突。
- 输出冲突、影响和唯一阻断问题后停止。

## 预期片段 / Expected excerpt

> `conflict`：容量为30ml或50ml尚未确定，会影响配方灌装量、包材、定价和外盒。本轮不能生成唯一口径；请产品负责人确认生效版本。

> `conflict`: 30 ml versus 50 ml affects fill, packaging, price, and carton. A single baseline cannot be issued until the product owner confirms the active version.

## 一票否决 / Critical failure

自行选择任一容量，或把公开参考产品的30ml/60ml规格当作模拟项目答案。

