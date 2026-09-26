# Academic Paper Writing Skill

A portable Agent Skill for constructing academic papers from research facts rather than generating prose in one shot.

The v0.3 pipeline is:

```text
Research State
  -> Problem Construction / Framing
  -> Claim Graph
  -> Paper Core
       |\
       | -> Experimental Obligations
       v
     Narrative
       -> Reader Path
       -> Section / Rhetorical Modules
       -> Semantic Draft
       -> Reader-facing Discourse
       -> Natural Language Realization
       -> Global Review
```

The framing layer explicitly separates:

```text
Original Idea
-> Research Setting
-> Structural Change
-> Structural Mismatch
-> Research Problem
-> Method Role
-> Technical Mechanism
```

The v0.3 reader-facing layer adds three controls:

- **Paper Core**: every major section tells the same story at a different level of detail.
- **Reader Path**: internal framing is compressed into the shortest conceptual path a reader needs.
- **Experimental Obligations**: central claims determine the evidence, controls, metrics, baselines, and falsifiers required from experiments.

Method writing additionally follows a semantic **WHY -> WHAT -> HOW** check before prose realization.

## Reader-first inspiration

The reader-facing additions adapt high-level principles from [wmd3i/Some-tips-for-writing-an-AI-ML-paper](https://github.com/wmd3i/Some-tips-for-writing-an-AI-ML-paper): keep a consistent story across sections, reduce reader/reviewer effort, explain why before mechanics, and align experiments with claims. This repository operationalizes those principles as explicit intermediate representations rather than copying the source wording.

## Design principles

1. **Ground before writing.** Research facts, results, and limitations are separated from presentation.
2. **Construct the problem structurally.** Broader framing comes from identifying the setting, changed decision/system structure, and any real mismatch—not from promotional language.
3. **Keep one Paper Core.** Abstract, Introduction, Method, Experiments, and Conclusion must remain views of the same research story.
4. **Optimize for the reader.** Internal planning schemas must not leak mechanically into final prose.
5. **Claims are typed and evidence-linked.** A broader implication must not silently become a demonstrated result.
6. **Claims create experimental obligations.** Experiments should test the thesis and eliminate competing explanations.
7. **Explain why before what/how.** Method components should be motivated by an unresolved need before their mechanics are presented.
8. **Modules are rhetorical functions, not paragraphs.**
9. **Semantic drafting and naturalization are separate.** The naturalizer may reorganize prose but may not invent facts or strengthen claims.
10. **The core workflow is runtime-independent.** Scripts are optional enhancements, not prerequisites.

## Current MVP

The current release focuses on **Introduction construction and paper-level story formation**, while also defining the bridge from claims to experiment design. The same state, framing, core, reader-path, and realization layers are intended to extend to Method, Experiments, Related Work, Abstract, and Conclusion.

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

When this repository is the active workspace, ask Codex to use the `academic-paper-writing` skill for paper framing, drafting, revising, experiment-story alignment, or reviewing.

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

MVP v0.3: reader-first paper construction, one-core-story consistency, and claim-driven experimental obligations.
