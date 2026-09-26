# Repository instructions

For academic paper framing, planning, drafting, rewriting, or reviewing tasks, read and follow:

`.agents/skills/academic-paper-writing/SKILL.md`

Treat that directory as the canonical skill implementation. Do not duplicate its instructions elsewhere.

When developing the skill itself:

1. Keep the portable core instruction-first; do not make scripts mandatory for normal execution.
2. Keep `SKILL.md` concise and use progressive disclosure through linked reference files.
3. Preserve the separation between research facts, claims, narrative, semantic content, and surface prose.
4. Run `python scripts/validate_skill.py` after structural edits.
5. Run `python scripts/package_skill.py` after a release-worthy change.
