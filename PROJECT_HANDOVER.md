# Project Handover

## Purpose and current state

This project consolidates Metta’s identity, language, universal-design and AI-use guidance into a shareable Markdown-first package. Version 0.9 is a researched draft ready for Community Partnership review, not an adopted organisation-wide policy. The recovery repository is `https://github.com/swc927/metta-universal-brand-ai-package`, public, branch `main`.

## Architecture

- `METTA_UNIVERSAL_BRAND_GUIDE.md` is the canonical human standard.
- `metta-brand-tokens.json` provides machine-readable values and status labels.
- `AI_PROMPT_PACK.md` provides reusable prompts.
- `skill/metta-universal-brand/` is the Codex/OpenAI skill package.
- `adapters/` contains minimal instructions for other AI platforms.
- `assets/` contains current Metta logo masters.
- `SOURCE_REGISTER.md` records evidence and unresolved decisions.

## Completed verification

- Reviewed all pages of the 2024 Communication and Publicity Handbook.
- Reviewed all pages of the 2008 Corporate Identity Manual and Publicity Guideline.
- Reviewed the current 2026 volunteer handbook and relevant communication/confidentiality sections of the employee handbook.
- Reviewed the 2025/26 annual report and current official Metta web pages.
- Inspected current official SVG logo masters and extracted their embedded colour values.
- Reviewed WCAG 2.2, PDPC photography guidance and Charity Portal communication/fundraising requirements.
- Validated the Codex skill structure with the bundled skill validator.
- Validated JSON syntax, internal links/paths and logo checksums.

## Important decisions

- Approved identity rules are separated from observed campaign practice and recommendations.
- Pantone/CMYK remain the print authority; website hex values are implementation tokens only.
- The legacy tagline is not declared universally current pending owner confirmation.
- AI is draft-only and cannot approve, publish, send, invent facts or alter the logo.
- The package contains no confidential HR provisions, client data, donor data, credentials or session material.

## Known issues

See the open decisions in `SOURCE_REGISTER.md`. Community Partnership review is required before version 1.0.

## Next actions

1. Confirm the seven open decisions with Community Partnership and relevant service owners.
2. Replace draft status with approval metadata and a review date.
3. Test templates with staff from at least one centre in each service pillar.
4. Publish controlled logo assets and bilingual glossary in a stable internal location.
5. After Community Partnership approval, tag a version 1.0 release and record the approval date and review owner.

## Resume prompt

“Open `PROJECT_HANDOVER.md` in the Metta universal brand package, review the open decisions with the latest owner evidence, and prepare the next verified milestone without changing approved identity rules.”
