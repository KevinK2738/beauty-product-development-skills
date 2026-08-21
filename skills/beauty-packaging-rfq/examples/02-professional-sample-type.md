# 专业案例：库存样冒充功能样 / Professional case: stock sample presented as functional sample

**类型 / Type:** 打样请求 / sampling request  
**性质 / Nature:** 真实供应商公开页面与模拟往来组合；供应商声明均需确认。

## 证据记录 / Evidence record

| 来源 / Source | 发布者 | 市场 | 类型 | 访问日期 | 自主事实摘要 | 状态 |
|---|---|---|---|---|---|---|
| [High-end airless bottle](https://www.cosme-packagings.com/high-end-airless-bottle-cosmetic) | Guangzhou Ouxinmay Packaging | 中国 | 供应商官网 | 2026-08-21 | 页面公开样品、交期、港口和付款等一般性供应信息；这些是访问日的供应商声明，不等于本项目已获承诺。 | `fact` |

## 模拟文件 / Simulated files

- 品牌请求：30 ml、指定泵量、目标装饰、使用代表性高黏度内容物的功能样。
- 供应商回复：“可寄现货样”，未说明容量、泵量、材料、装饰、内容物或样品用途。
- 项目经理希望把这批现货样登记为“功能样已安排”。

## 用户用法 / User prompt

“整理打样请求和回复，把状态更新好。” / “Align the sampling request and reply, then update the status.”

## 预期行为 / Expected behavior

- 区分外观/库存样、结构样、装饰样、功能样和量产线样。
- 将供应商回复对齐到每项请求；未明确的字段保持 `requires-confirmation`。
- 库存样可用于手感和初步结构观察，但不能登记为代表性内容物功能样。

## 预期片段 / Expected excerpt

> 当前确认的是“可寄库存样”，不是“功能样已安排”。请供应商确认样品编号、规格版本、材料、泵量、装饰状态、灌装内容物和可支持的测试目的。

> The reply confirms only that a stock sample may be sent. It does not confirm a functional sample built to the requested specification.

## 通过条件 / Pass condition

样品类型和验证用途必须明确，不得升级供应商承诺。

