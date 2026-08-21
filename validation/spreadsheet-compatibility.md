# Spreadsheet compatibility record

Test date: 2026-08-21

This record is separate from Agent Skills platform compatibility. It covers only the four `.xlsx` templates shipped with this repository.

| Application | Version | Scope | Result |
|---|---|---|---|
| WPS Office for macOS | 12.1.26046 | Opened the Chinese packaging-specification template, displayed all four worksheets and styles, edited a cell, saved an `.xlsx` copy, reopened the package structure, and confirmed the edit plus data-validation rule remained present | Pass for open/edit/save smoke test |
| Microsoft Excel | Not installed | No run performed | Untested |
| LibreOffice Calc | Broken local launcher; application bundle absent | No run performed | Untested |

## Static workbook checks

All four distributed templates are checked for:

- a valid ZIP/OOXML container;
- expected worksheet names;
- formulas without macros or external workbook links;
- list data-validation rules on controlled status fields;
- absence of internal names, local paths, and unfinished placeholders in Office metadata;
- successful rendering of every worksheet during generation.

The WPS smoke test does not claim pixel-identical rendering across applications. Excel and LibreOffice remain untested until a working installation is available.
