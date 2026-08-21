#!/usr/bin/env python3
"""Static release-candidate checks for this repository."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "beauty-product-intake",
    "beauty-competitor-opportunity",
    "beauty-product-brief",
    "beauty-packaging-requirements",
    "beauty-packaging-candidate-review",
    "beauty-packaging-directions",
    "beauty-packaging-specification",
    "beauty-packaging-rfq",
)
REQUIRED_REFS = (
    "instructions.zh-CN.md",
    "instructions.en.md",
    "result-format.zh-CN.md",
    "result-format.en.md",
)
REQUIRED_ASSETS = (
    "skills/beauty-packaging-specification/assets/beauty-packaging-specification-template.zh-CN.xlsx",
    "skills/beauty-packaging-specification/assets/beauty-packaging-specification-template.en.xlsx",
    "skills/beauty-packaging-rfq/assets/beauty-packaging-rfq-template.zh-CN.xlsx",
    "skills/beauty-packaging-rfq/assets/beauty-packaging-rfq-template.en.xlsx",
    "skills/beauty-packaging-rfq/assets/email-templates.zh-CN.txt",
    "skills/beauty-packaging-rfq/assets/email-templates.en.txt",
)
REQUIRED_REPOSITORY_FILES = (
    "README.md",
    "README.en.md",
    "CONTRIBUTING.md",
    "CONTRIBUTING.en.md",
    "SOURCE_POLICY.md",
    "SOURCE_POLICY.en.md",
    "COMPATIBILITY.md",
    "COMPATIBILITY.en.md",
    "SECURITY.md",
    "SECURITY.en.md",
    "CITATION.cff",
    "LICENSE",
    "NOTICE",
    "platforms/codex.md",
    "platforms/workbuddy.md",
    "platforms/trae-work.md",
    "platforms/doubao.md",
    "validation/README.md",
    "validation/RELEASE_CHECKLIST.md",
    "validation/scorecard-template.csv",
    "validation/spreadsheet-compatibility.md",
    "validation/runs/README.md",
)
EXPECTED_WORKBOOK_SHEETS = {
    "beauty-packaging-specification-template.zh-CN.xlsx": ("Control", "Components", "Verification", "Change Log"),
    "beauty-packaging-specification-template.en.xlsx": ("Control", "Components", "Verification", "Change Log"),
    "beauty-packaging-rfq-template.zh-CN.xlsx": ("Control", "Items", "Commercial", "Samples", "Alignment"),
    "beauty-packaging-rfq-template.en.xlsx": ("Control", "Items", "Commercial", "Samples", "Alignment"),
}
BANNED = (
    "Pack" + "Agent",
    "Reali" + "box",
    "/" + "Users" + "/" + "kevin",
    "屠" + "总",
    "launch" + "BriefSchema",
    "Product" + "Intent",
    "Packaging" + "CandidateSet",
    "Supplier" + "InquiryPack",
    "Pack" + "Agent Catalog",
    "珀" + "莱雅",
    "PRO" + "YA",
    "Pro" + "ya",
)
PLACEHOLDERS = re.compile(r"\b(?:" + "|".join(("TO" + "DO", "T" + "BD", "FIX" + "ME", "X" + "XX", "OWN" + "ER")) + r")\b")
LOCAL_LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    closing = text.find("\n---\n", 4)
    if closing < 0:
        return {}
    block = text[4:closing]
    result: dict[str, str] = {}
    active = ""
    for line in block.splitlines():
        match = re.match(r"^([a-z_-]+):\s*(.*)$", line)
        if match:
            active = match.group(1)
            result[active] = match.group(2).strip().strip('"')
        elif active and line.startswith("  "):
            result[active] += " " + line.strip()
    return result


def text_files() -> list[Path]:
    suffixes = {".md", ".yml", ".yaml", ".cff", ".csv", ".py", ".mjs", ".txt"}
    return [p for p in ROOT.rglob("*") if p.is_file() and p.suffix.lower() in suffixes and ".git" not in p.parts]


def main() -> int:
    errors: list[str] = []
    actual = sorted(p.name for p in (ROOT / "skills").iterdir() if p.is_dir())
    if actual != sorted(SKILLS):
        errors.append(f"skill set mismatch: {actual}")

    for required_file in REQUIRED_REPOSITORY_FILES:
        if not (ROOT / required_file).is_file():
            errors.append(f"missing required repository file: {required_file}")

    for required_asset in REQUIRED_ASSETS:
        if not (ROOT / required_asset).is_file():
            errors.append(f"missing required asset: {required_asset}")

    cases_path = ROOT / "validation" / "cases.yml"
    case_rows: list[tuple[str, str, str, str]] = []
    if cases_path.is_file():
        case_rows = re.findall(
            r"\{id:\s*([^,]+),\s*skill:\s*([^,]+),\s*type:\s*([^,]+),\s*example:\s*([^,]+),",
            cases_path.read_text(encoding="utf-8"),
        )
        if len(case_rows) != 24:
            errors.append(f"expected 24 validation cases, found {len(case_rows)}")
        if len({row[0].strip() for row in case_rows}) != len(case_rows):
            errors.append("duplicate validation case id")
        for _, skill, case_type, example in case_rows:
            skill = skill.strip()
            case_type = case_type.strip()
            example = example.strip()
            if skill not in SKILLS:
                errors.append(f"unknown validation skill: {skill}")
                continue
            if case_type not in {"quick", "professional", "stop"}:
                errors.append(f"unknown validation case type: {case_type}")
            if not (ROOT / "skills" / skill / example).is_file():
                errors.append(f"validation example not found: {skill}/{example}")
        for skill in SKILLS:
            types = sorted(row[2].strip() for row in case_rows if row[1].strip() == skill)
            if types != ["professional", "quick", "stop"]:
                errors.append(f"validation case coverage mismatch: {skill} -> {types}")
    else:
        errors.append("missing validation/cases.yml")

    for skill in SKILLS:
        base = ROOT / "skills" / skill
        entry = base / "SKILL.md"
        if not entry.exists():
            errors.append(f"missing {entry.relative_to(ROOT)}")
            continue
        metadata = parse_frontmatter(entry.read_text(encoding="utf-8"))
        if metadata.get("name") != skill:
            errors.append(f"frontmatter name mismatch: {skill}")
        description = metadata.get("description", "")
        if not description or not re.search(r"[\u4e00-\u9fff]", description) or not re.search(r"[A-Za-z]", description):
            errors.append(f"description is not bilingual: {skill}")
        for ref in REQUIRED_REFS:
            if not (base / "references" / ref).is_file():
                errors.append(f"missing reference: {skill}/{ref}")
        examples = sorted((base / "examples").glob("*.md"))
        if len(examples) != 3:
            errors.append(f"expected 3 examples for {skill}, found {len(examples)}")
        for example in examples:
            body = example.read_text(encoding="utf-8")
            for heading in ("证据记录 / Evidence record", "预期"):
                if heading not in body:
                    errors.append(f"missing example marker '{heading}': {example.relative_to(ROOT)}")
            if "http://" not in body and "https://" not in body:
                errors.append(f"example has no public source URL: {example.relative_to(ROOT)}")
            if not any(marker in body for marker in ("模拟", "Simulated", "simulation")):
                errors.append(f"example is not marked as simulated: {example.relative_to(ROOT)}")
            if not any(marker in body for marker in ("Pass condition", "Stop condition", "Critical failure")):
                errors.append(f"missing pass or stop condition: {example.relative_to(ROOT)}")

    for path in text_files():
        body = path.read_text(encoding="utf-8")
        for term in BANNED:
            if term in body:
                errors.append(f"banned term '{term}': {path.relative_to(ROOT)}")
        if PLACEHOLDERS.search(body):
            errors.append(f"unfinished placeholder: {path.relative_to(ROOT)}")
        for raw_target in LOCAL_LINK.findall(body):
            target = raw_target.split("#", 1)[0].strip()
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"broken local link '{raw_target}': {path.relative_to(ROOT)}")

    for workbook in ROOT.rglob("*.xlsx"):
        try:
            with zipfile.ZipFile(workbook) as archive:
                names = archive.namelist()
                metadata = "\n".join(
                    archive.read(name).decode("utf-8", errors="ignore")
                    for name in names
                    if name.startswith("docProps/")
                )
                workbook_xml = archive.read("xl/workbook.xml").decode("utf-8", errors="ignore")
                worksheet_xml = "\n".join(
                    archive.read(name).decode("utf-8", errors="ignore")
                    for name in names
                    if name.startswith("xl/worksheets/sheet") and name.endswith(".xml")
                )
        except (OSError, zipfile.BadZipFile) as exc:
            errors.append(f"invalid workbook {workbook.relative_to(ROOT)}: {exc}")
            continue
        if any(name.endswith("vbaProject.bin") for name in names):
            errors.append(f"macro found: {workbook.relative_to(ROOT)}")
        if any(name.startswith("xl/externalLinks/") for name in names):
            errors.append(f"external workbook link found: {workbook.relative_to(ROOT)}")
        if "dataValidation" not in worksheet_xml:
            errors.append(f"no list validation found: {workbook.relative_to(ROOT)}")
        if "COUNTIF(" not in worksheet_xml:
            errors.append(f"expected portable COUNTIF formula missing: {workbook.relative_to(ROOT)}")
        if re.search(r"(?:_xlfn\.|MINIFS\(|MAXIFS\()", worksheet_xml, flags=re.IGNORECASE):
            errors.append(f"fragile formula found: {workbook.relative_to(ROOT)}")
        if re.search(r"#(?:REF!|VALUE!|NAME\?|DIV/0!|N/A)", worksheet_xml, flags=re.IGNORECASE):
            errors.append(f"formula error marker found: {workbook.relative_to(ROOT)}")
        for sheet_name in EXPECTED_WORKBOOK_SHEETS.get(workbook.name, ()):
            if f'name="{sheet_name}"' not in workbook_xml:
                errors.append(f"missing sheet '{sheet_name}': {workbook.relative_to(ROOT)}")
        for term in BANNED:
            if term in metadata:
                errors.append(f"workbook metadata contains '{term}': {workbook.relative_to(ROOT)}")
        if PLACEHOLDERS.search(metadata):
            errors.append(f"workbook metadata contains placeholder: {workbook.relative_to(ROOT)}")

    if errors:
        print("STATIC VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"STATIC VALIDATION PASSED: {len(SKILLS)} skills, 24 examples")
    return 0


if __name__ == "__main__":
    sys.exit(main())
