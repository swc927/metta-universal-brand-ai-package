#!/usr/bin/env python3
"""Validate the portable Metta brand package without third-party dependencies."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "START_HERE.md",
    "EMPLOYEE_QUICK_GUIDE.md",
    "PLATFORM_SETUP.md",
    "METTA_UNIVERSAL_BRAND_GUIDE.md",
    "AI_PROMPT_PACK.md",
    "metta-brand-tokens.json",
    "SOURCE_REGISTER.md",
    "PROJECT_HANDOVER.md",
    "CHANGELOG.md",
    "templates/README.md",
    "templates/communication-brief.md",
    "templates/email.md",
    "templates/social-media.md",
    "templates/event-poster-brief.md",
    "templates/bilingual-announcement.md",
    "templates/final-artwork-review.md",
    "skill/metta-universal-brand/SKILL.md",
    "skill/metta-universal-brand/agents/openai.yaml",
]

EXPECTED_HASHES = {
    "assets/metta-logo-official-master.svg": "dcb3ae7e05b82849607ca90f0bb77313ea75ffb3fe081f000ba604b2dfe392a9",
    "assets/metta-logo-official-master.png": "9d659560e632fa5521b825bf0e39bbfbe166cf893107967d6f6e902e60cb5ac4",
}

SECRET_PATTERN = re.compile(
    r"BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY|"
    r"(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*[^\s{]|"
    r"gh[opsu]_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}",
    re.IGNORECASE,
)

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


for relative in REQUIRED:
    if not (ROOT / relative).is_file():
        fail(f"required file missing: {relative}")

tokens = json.loads((ROOT / "metta-brand-tokens.json").read_text(encoding="utf-8"))
if tokens["meta"]["version"] != "0.10.0-draft":
    fail("token version is not 0.10.0-draft")
if tokens["logoRules"].get("bottomPlacementProhibited") is not False:
    fail("logo bottom-placement rule is missing or incorrect")

copies = [
    ("METTA_UNIVERSAL_BRAND_GUIDE.md", "skill/metta-universal-brand/references/metta-universal-brand-guide.md"),
    ("SOURCE_REGISTER.md", "skill/metta-universal-brand/references/source-register.md"),
    ("EMPLOYEE_QUICK_GUIDE.md", "skill/metta-universal-brand/references/employee-quick-guide.md"),
    ("assets/metta-logo-official-master.svg", "skill/metta-universal-brand/assets/metta-logo-official-master.svg"),
    ("assets/metta-logo-official-master.png", "skill/metta-universal-brand/assets/metta-logo-official-master.png"),
]
for canonical, packaged in copies:
    if (ROOT / canonical).read_bytes() != (ROOT / packaged).read_bytes():
        fail(f"packaged copy differs from canonical file: {packaged}")

for relative, expected in EXPECTED_HASHES.items():
    actual = sha256(ROOT / relative)
    if actual != expected:
        fail(f"official asset checksum changed: {relative}")

for path in ROOT.rglob("*"):
    if path.resolve() == Path(__file__).resolve():
        continue
    if not path.is_file() or ".git" in path.parts or path.suffix.lower() in {".png"}:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    relative = path.relative_to(ROOT)
    if "/Users/" in text or "file://" in text:
        fail(f"private local path found in {relative}")
    if SECRET_PATTERN.search(text):
        fail(f"secret-like content found in {relative}")
    if path.suffix.lower() == ".md":
        for target in MARKDOWN_LINK.findall(text):
            target = target.strip().split("#", 1)[0]
            if not target or re.match(r"^(?:https?://|mailto:)", target):
                continue
            if not (path.parent / target).resolve().exists():
                fail(f"broken local link in {relative}: {target}")

skill_text = (ROOT / "skill/metta-universal-brand/SKILL.md").read_text(encoding="utf-8")
if not skill_text.startswith("---\n") or "name: metta-universal-brand" not in skill_text:
    fail("skill frontmatter is invalid")
if "[TODO" in skill_text or "CHANGEME" in skill_text:
    fail("unfinished skill scaffold found")

print("Metta brand package validation passed.")
