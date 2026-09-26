# Academic Paper Writing Skill

A portable Agent Skill for constructing academic papers from research facts rather than generating prose in one shot.

The core pipeline is:

```text
Research State
  -> Claim & Framing
  -> Global Narrative
  -> Section / Rhetorical Modules
  -> Semantic Draft
  -> Discourse Composition
  -> Natural Language Realization
  -> Global Review
```

The repository is designed around one source of truth:

```text
.agents/skills/academic-paper-writing/
```

That directory contains the actual Skill. The rest of the repository provides packaging, validation, examples, and repository-level guidance.

## Design principles

1. **Ground before writing.** Research facts, results, and limitations are separated from presentation.
2. **Claims are typed and evidence-linked.** A broader implication must not silently become a demonstrated result.
3. **Narrative is planned before prose.** The system first decides what story the paper tells.
4. **Modules are rhetorical functions, not paragraphs.** Multiple modules may be merged into one paragraph and one module may span multiple paragraphs.
5. **Semantic drafting and naturalization are separate.** The naturalizer may reorganize prose but may not invent facts or strengthen claims.
6. **The core workflow is runtime-independent.** Scripts are optional enhancements, not prerequisites.

## Current MVP

The first release fully specifies the pipeline for **Introduction writing**. The same state, claim, narrative, and realization layers are intended to extend to Method, Experiments, Related Work, and Conclusion.

Included Introduction modules:

- context
- existing paradigm
- limitation
- consequence
- core insight
- method overview
- evidence preview
- contributions

Included narrative patterns:

- limitation-driven
- principle-driven
- discovery-driven

## Codex

This repository stores the skill in the repo-local Codex convention:

```text
.agents/skills/academic-paper-writing/SKILL.md
```

When this repository is the active workspace, ask Codex to use the `academic-paper-writing` skill for paper framing, drafting, revising, or reviewing.

To use the skill in another repository, copy the directory:

```bash
cp -r .agents/skills/academic-paper-writing /path/to/other-repo/.agents/skills/
```

## ChatGPT / API packaging

Create a portable zip with a single top-level skill folder:

```bash
python scripts/package_skill.py
```

Output:

```text
dist/academic-paper-writing.zip
```

The zip is structured for surfaces that accept an uploaded Skill bundle. Product availability and installation UI can differ by ChatGPT account/workspace.

## Validate

```bash
python scripts/validate_skill.py
```

The validator checks front matter, required files, and local Markdown links in the skill package.

## Repository structure

```text
.
├── AGENTS.md
├── README.md
├── .agents/
│   └── skills/
│       └── academic-paper-writing/
│           ├── SKILL.md
│           ├── references/
│           ├── modules/
│           ├── narratives/
│           ├── styles/
│           ├── schemas/
│           └── assets/
├── examples/
└── scripts/
```

## Status

MVP v0.1: architecture and Introduction pipeline.
