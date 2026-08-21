# Beauty Product Development Skills

[简体中文](README.md)

An open-source collection of Agent Skills for practical beauty product, packaging, and supplier work. The skills turn fragmented inputs into reviewable, traceable, and actionable artifacts. They do not replace formulation engineering, regulatory review, supplier commitments, or mass-production release.

Maintained by **K-Beauty** and licensed under the [Apache License 2.0](LICENSE); see the [Apache Software Foundation guidance](https://www.apache.org/legal/apply-license.html) and the [OSI license directory](https://opensource.org/licenses). This is an independent open-source project and is not affiliated with, sponsored by, or endorsed by any brand, supplier, or platform mentioned in its examples.

**Current status: release candidate.** The skills, cases, and templates are in place, but the 96 real runs across four platforms are not complete. This repository must not yet be tagged or promoted as `v1.0.0`, and it does not claim compatibility with untested platforms. See [`validation/RELEASE_CHECKLIST.md`](validation/RELEASE_CHECKLIST.md) for the current gate snapshot.

## Skills

| Skill | Use case | Default artifact |
|---|---|---|
| [`beauty-product-intake`](skills/beauty-product-intake/) | Review early product ideas and mixed materials; separate facts, claims, constraints, conflicts, and unknowns | New Product Intake Clarification |
| [`beauty-competitor-opportunity`](skills/beauty-competitor-opportunity/) | Research competitors, user problems, and product or packaging opportunities for a defined decision | Competitor and Opportunity Brief |
| [`beauty-product-brief`](skills/beauty-product-brief/) | Turn product goals and constraints into a cross-functional definition | Beauty Product Development Brief |
| [`beauty-packaging-requirements`](skills/beauty-packaging-requirements/) | Translate formula, experience, channel, and commercial needs into packaging requirements and validation work | Beauty Packaging Requirements |
| [`beauty-packaging-candidate-review`](skills/beauty-packaging-candidate-review/) | Review user-provided catalogs, drawings, links, and commercial data | Packaging Candidate Review |
| [`beauty-packaging-directions`](skills/beauty-packaging-directions/) | Create reviewable packaging directions grounded in real structures and strategic tension | Packaging Design Directions |
| [`beauty-packaging-specification`](skills/beauty-packaging-specification/) | Organize packaging information for inquiry, sampling, confirmation, or change states | Beauty Packaging Technical Specification |
| [`beauty-packaging-rfq`](skills/beauty-packaging-rfq/) | Prepare an RFI, RFQ, sampling request, or align supplier responses | Inquiry and Response Alignment Pack |

Each skill is independently installable and usable. No fixed end-to-end sequence is required, and a skill must not invoke another merely to complete a workflow.

## Usage

Each directory is a standard Agent Skill package. Install only the skill folders you need, then ask in natural language. For example:

> Review the attached product manual, communications brief, and brand guidelines. Separate confirmed facts, marketing claims, creative constraints, and version conflicts, then prepare a new product intake clarification.

See [`platforms/`](platforms/) for installation notes and [`COMPATIBILITY.en.md`](COMPATIBILITY.en.md) for evidence-based compatibility status.

`beauty-packaging-specification` and `beauty-packaging-rfq` also include bilingual `.xlsx` blank templates, and the RFQ Skill includes bilingual plain-text email templates. Spreadsheet application test results are recorded in [`validation/spreadsheet-compatibility.md`](validation/spreadsheet-compatibility.md).

## Editable assets

| Use | Chinese | English |
|---|---|---|
| Packaging technical specification | [Excel template](skills/beauty-packaging-specification/assets/beauty-packaging-specification-template.zh-CN.xlsx) | [Excel template](skills/beauty-packaging-specification/assets/beauty-packaging-specification-template.en.xlsx) |
| RFI / RFQ / sampling / response alignment | [Excel template](skills/beauty-packaging-rfq/assets/beauty-packaging-rfq-template.zh-CN.xlsx) · [Email templates](skills/beauty-packaging-rfq/assets/email-templates.zh-CN.txt) | [Excel template](skills/beauty-packaging-rfq/assets/beauty-packaging-rfq-template.en.xlsx) · [Email templates](skills/beauty-packaging-rfq/assets/email-templates.en.txt) |

## Shared evidence states

- `confirmed-input`: explicitly provided by the user.
- `public-evidence`: supported by a traceable public source.
- `recommendation`: a professional recommendation generated from available evidence.
- `requires-confirmation`: requires confirmation by the brand, supplier, test owner, or regulatory professional.
- `conflict`: sources, versions, or fields disagree.

## Examples and sources

Examples are simulated assignments grounded in real public evidence. They do not claim to reproduce any brand's internal decision process. The repository stores only independently written minimum fact summaries, source links, and access dates—not third-party logos, images, full webpages, or long excerpts. See [`SOURCE_POLICY.en.md`](SOURCE_POLICY.en.md).

## Quality boundary

This repository provides practice-oriented professional tools; it is not an industry certification. Outputs still require review by the appropriate accountable party, especially for formulation, claims, regulatory status, packaging testing, supplier commercials, engineering drawings, contracts, and production release.

## Contributing

Issues and pull requests are welcome. Contributors must disclose sources, rights status, and applicability and must not submit confidential client, employer, or supplier information. See [`CONTRIBUTING.en.md`](CONTRIBUTING.en.md).
