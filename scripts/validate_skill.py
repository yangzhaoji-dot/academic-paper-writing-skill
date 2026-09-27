#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / ".agents" / "skills" / "academic-paper-writing"
SKILL_MD = SKILL_ROOT / "SKILL.md"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    if not SKILL_MD.exists():
        fail(f"missing {SKILL_MD}")

    text = SKILL_MD.read_text(encoding="utf-8")
    fm = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not fm:
        fail("SKILL.md must start with YAML front matter")

    front = fm.group(1)
    if not re.search(r"(?m)^name:\s*academic-paper-writing\s*$", front):
        fail("front matter must contain name: academic-paper-writing")
    if not re.search(r"(?m)^description:\s*\S.+$", front):
        fail("front matter must contain a non-empty description")

    required = [
        "references/workflow.md",
        "references/execution.md",
        "references/multi-pass-execution.md",
        "references/portability.md",
        "references/reader-first-principles.md",
        "references/procedures/grounding.md",
        "references/procedures/technical-grounding.md",
        "references/procedures/section-contract.md",
        "references/procedures/section-calibration.md",
        "references/procedures/authorial-synthesis.md",
        "references/procedures/manuscript-calibration.md",
        "references/procedures/layout-contract.md",
        "references/procedures/rendered-layout-verifier.md",
        "references/procedures/framing.md",
        "references/procedures/paper-core.md",
        "references/procedures/experimental-obligations.md",
        "references/procedures/literature-grounding.md",
        "references/procedures/discourse-grounding.md",
        "references/procedures/venue-presentation.md",
        "references/procedures/narrative.md",
        "references/procedures/reader-path.md",
        "references/procedures/module-planning.md",
        "references/procedures/semantic-writing.md",
        "references/procedures/naturalization.md",
        "references/procedures/review.md",
        "schemas/scientific-spec.md",
        "schemas/citation-map.md",
        "schemas/convention-profile.md",
        "schemas/layout-contract.md",
        "schemas/paper-spec.md",
        "schemas/research-state.md",
        "schemas/technical-state.md",
        "schemas/section-contract.md",
        "schemas/framing.md",
        "schemas/claim.md",
        "schemas/paper-core.md",
        "schemas/reader-path.md",
        "schemas/experimental-obligation.md",
        "schemas/literature-map.md",
        "schemas/discourse-reference.md",
        "schemas/venue-profile.md",
        "schemas/presentation-reference.md",
        "schemas/module.md",
        "schemas/paper-state.md",
        "passes/README.md",
        "passes/01-scientific-audit.md",
        "passes/02-literature-citation-audit.md",
        "passes/convention-mining.md",
        "passes/03-paper-packaging.md",
        "passes/04-formal-method.md",
        "passes/05-paper-architecture.md",
        "passes/06-independent-audit.md",
        "passes/section-writer.md",
    ]
    for rel in required:
        if not (SKILL_ROOT / rel).exists():
            fail(f"missing required file: {rel}")

    link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    errors = []
    for md in SKILL_ROOT.rglob("*.md"):
        body = md.read_text(encoding="utf-8")
        for target in link_re.findall(body):
            target = target.strip()
            if not target or target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            candidate = (md.parent / target).resolve()
            try:
                candidate.relative_to(SKILL_ROOT.resolve())
            except ValueError:
                errors.append(f"{md.relative_to(SKILL_ROOT)} -> link escapes skill root: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{md.relative_to(SKILL_ROOT)} -> missing link target: {target}")

    if errors:
        for e in errors:
            print("ERROR:", e)
        raise SystemExit(1)

    print("Skill validation passed.")


if __name__ == "__main__":
    main()
