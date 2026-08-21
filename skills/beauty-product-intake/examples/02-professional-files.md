# 专业文件案例 / Professional file case

**类型 / Type:** 多文件审阅 / multi-file review  
**性质 / Nature:** 公开材料与模拟附件组合；非任何品牌的内部项目。

## 证据记录 / Evidence record

| 来源 / Source | 发布者 | 市场 | 类型 | 访问日期 | 自主事实摘要 | 状态 |
|---|---|---|---|---|---|---|
| [Pechoin official product catalog](https://en.pechoin.com/) | Pechoin | 国际 | 品牌官网 | 2026-08-21 | 页面公开识别一款修护眼霜产品，但当前证据包未取得其容量、使用时段或功效证据；这些字段不能由产品名称推断。 | `fact` |
| [化妆品功效宣称评价规范公告](https://english.nmpa.gov.cn/2021-04/09/c_654820.htm) | 国家药监局 | 中国 | 监管机构 | 2026-08-21 | 公告说明化妆品功效宣称评价具有专门规范；具体新品宣称仍需责任方按适用要求判断和提供证据。 | `fact` |

## 模拟附件 / Simulated files

- A：模拟产品手册写“20ml、夜间使用、改善三类眼周问题”。
- B：传播 Brief 写“15ml、全天候、7天解决黑眼圈”。
- C：品牌规范要求文案克制、不得使用医疗化表达。
- D：一份无方法和日期的社交媒体趋势截图。

## 用户用法 / User prompt

**中文：**“审阅这四份资料，整理一份新品需求澄清单，告诉我哪些能当事实。”

**English:** “Review these four files and produce an intake clarification showing what can be treated as fact.”

## 预期行为 / Expected behavior

- 隔离产品规格、传播主张、创意约束与低质量外部线索。
- 把 15ml/20ml、夜间/全天候标为 `conflict`。
- 把“7天解决”列为待证据和法规审阅的主张，不作事实。

## 预期片段 / Expected excerpt

> 当前不能形成单一容量和使用时段口径；产品负责人需先确认生效版本。社交截图只能作为研究线索。

> No single capacity or use-time baseline can be formed until the product owner identifies the active version. The social screenshot is a research lead only.

## 通过条件 / Pass condition

问题集中在版本、宣称证据和责任方，不因附件多而扩展成完整开发方案。
