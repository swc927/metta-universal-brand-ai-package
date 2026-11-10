# Project Handover

## Purpose and current state

This project consolidates Metta’s identity, language, universal-design and AI-use guidance into a shareable Markdown-first package. Version 0.11 is a researched draft ready for Community Partnership review, not an adopted organisation-wide policy. The recovery repository is `https://github.com/swc927/metta-universal-brand-ai-package`, public, branch `main`.

## Architecture

- `INSTALL.md` is the public beginner installation entry point. Stable brand-only ZIP links use GitHub's latest-release download route. Compatible installers can use the exact public skill folder link; ordinary ChatGPT uses the manual reference-file route.

- `METTA_UNIVERSAL_BRAND_GUIDE.md` is the canonical human standard.
- `START_HERE.md`, `BEGINNER_PROMPTS.md` and `EMPLOYEE_QUICK_GUIDE.md` provide guided beginner and daily-use routes.
- `PLATFORM_SETUP.md` explains how each supported AI environment consumes the package.
- `metta-brand-tokens.json` provides machine-readable values and status labels.
- `AI_PROMPT_PACK.md` provides reusable prompts.
- `templates/` contains practical communication and approval templates.
- `skill/metta-universal-brand/` is the Codex/OpenAI skill package.
- `adapters/` contains minimal instructions for other AI platforms.
- `assets/` contains current Metta logo masters.
- `SOURCE_REGISTER.md` records evidence and unresolved decisions.
- `scripts/validate_package.py` and `.github/workflows/validate.yml` protect integrity.

## Completed verification

- Reviewed all pages of the 2024 Communication and Publicity Handbook.
- Reviewed all pages of the 2008 Corporate Identity Manual and Publicity Guideline.
- Reviewed the current 2026 volunteer handbook and relevant communication/confidentiality sections of the employee handbook.
- Reviewed the 2025/26 annual report and current official Metta web pages.
- Inspected current official SVG logo masters and extracted their embedded colour values.
- Reviewed WCAG 2.2, PDPC photography guidance and Charity Portal communication/fundraising requirements.
- Validated the Codex skill structure with the bundled skill validator.
- Validated JSON syntax, internal links/paths and logo checksums.
- Clarified, based on a complete search of the reviewed identity sources, that no blanket rule prohibits bottom or footer logo placement.
- Added employee quick-start materials, platform setup and six practical templates.
- Added copy-and-paste beginner prompts that ask one simple question at a time and preserve unknown facts as verification items.
- Added page-level source evidence and deterministic continuous validation.

## Important decisions

- Approved identity rules are separated from observed campaign practice and recommendations.
- Pantone/CMYK remain the print authority; website hex values are implementation tokens only.
- The legacy tagline is not declared universally current pending owner confirmation.
- AI is draft-only and cannot approve, publish, send, invent facts or alter the logo.
- The package contains no confidential HR provisions, client data, donor data, credentials or session material.
- Bottom/footer logo placement is permitted when the complete logo remains legible, meets clear-space and minimum-size requirements and follows the approved template.

## Known issues

See the open decisions in `SOURCE_REGISTER.md`. Community Partnership review is required before version 1.0.

## Next actions

1. Confirm the seven open decisions with Community Partnership and relevant service owners.
2. Replace draft status with approval metadata and a review date.
3. Test the start page, beginner prompts, quick guide and templates with staff from at least one centre in each service pillar.
4. Publish controlled logo assets and bilingual glossary in a stable internal location.
5. Publish a `v0.11-draft` release, then after Community Partnership approval tag version 1.0 and record the approval date and review owner.

## Resume prompt

“Open `PROJECT_HANDOVER.md` in the Metta universal brand package, review the open decisions with the latest owner evidence, and prepare the next verified milestone without changing approved identity rules.”
