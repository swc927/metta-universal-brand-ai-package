# AI Platform Setup

The package can be used as project knowledge in general AI tools and as an installable skill in compatible Codex environments. These are different setup methods.

## ChatGPT Project or custom GPT

1. Download the repository ZIP and extract it.
2. Upload `METTA_UNIVERSAL_BRAND_GUIDE.md`, `EMPLOYEE_QUICK_GUIDE.md`, `AI_PROMPT_PACK.md` and the relevant template.
3. Add the universal system instruction from `AI_PROMPT_PACK.md` to the Project or GPT instructions.
4. Upload the approved logo only when the task needs it.
5. Start each task with current approved facts.

Pasting only the GitHub URL may let ChatGPT read the public repository, but it does not permanently install the package into ordinary ChatGPT.

## Claude Project

1. Add the same guide and quick-guide files to Project Knowledge.
2. Use `adapters/CLAUDE.md` as the Project instruction.
3. Provide task-specific facts in each conversation.

## Gemini Gem

1. Add the guide and quick-guide files as Gem knowledge where supported.
2. Use `adapters/GEMINI.md` as the Gem instruction.
3. Require verification and human approval before release.

## Codex-compatible skill

Copy the complete `skill/metta-universal-brand/` directory to the environment’s skills directory. Keep the folder name unchanged. Invoke it with:

```text
Use $metta-universal-brand to create a Metta-branded [DELIVERABLE] for [AUDIENCE] using the attached approved information.
```

Installing the skill provides reusable instructions; it does not grant authority to publish, send or modify live systems.

## GitHub Copilot

Copy `adapters/copilot-instructions.md` to `.github/copilot-instructions.md` in the target repository. Keep the brand guide and tokens in the repository or provide stable paths to them.

## Minimum files for any AI tool

- `METTA_UNIVERSAL_BRAND_GUIDE.md`
- The current approved facts for the task
- Relevant template from `templates/`
- Approved logo master only when needed
