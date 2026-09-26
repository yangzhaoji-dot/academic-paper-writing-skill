# Academic Paper Writing Skill

A portable Agent Skill for constructing academic papers from research facts rather than generating prose in one shot.

The v0.5 pipeline is:

```text
Research State
  -> Candidate Framing
       <-> Literature Challenge
  -> Claim Graph
       <-> Claim-Literature Matrix
  -> Paper Core
       <-> Novelty Boundary Check
       |\
       | -> Experimental Obligations
       |       <-> Literature-grounded baselines / metrics / protocols
       v
     Narrative
       -> Reader Path
       -> Section / Rhetorical Modules
       -> Semantic Draft
       +  Discourse References from real papers
       -> Reader-facing Discourse Composition
       -> Natural Language Realization
       -> Venue Resolver (conference + year)
       -> Page / Figure / Table / Equation Planning
       -> Official Template Realization
       -> Rendered PDF Review
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

The v0.5 pipeline adds venue-aware presentation to the literature-grounded paper-construction core:

- **Paper Core**: every major section tells the same story at a different level of detail.
- **Reader Path**: internal framing is compressed into the shortest conceptual path a reader needs.
- **Experimental Obligations**: central claims determine the evidence, controls, metrics, baselines, and falsifiers required from experiments.
- **Literature Grounding**: external work challenges framing, constrains novelty claims, and grounds baselines/metrics/protocols.
- **Discourse Grounding**: real papers provide section-specific rhetorical patterns for composition without donating scientific claims or copied wording.
- **Venue Profile**: official conference + year rules define hard submission constraints.
- **Presentation Reference**: recent papers provide soft layout tendencies without being treated as official rules.
- **Rendered PDF Review**: page-level defects are inspected after typesetting, not inferred from LaTeX source alone.

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
9. **Scientific literature evidence and writing references are separate.** A paper may inform both, but the two evidence roles must never be conflated.
10. **Learn discourse, not wording.** Real papers may provide abstract section/paragraph/sentence moves; distinctive phrases and close sentence skeletons must not be transferred.
11. **Semantic drafting, discourse composition, and naturalization are separate.** Surface realization may reorganize prose but may not invent facts or strengthen claims.
12. **Venue rules are year-specific and official-source-first.** An older venue profile may guide planning but cannot define a later year's submission requirements.
13. **Presentation follows scientific priority.** Page pressure should move or redesign information before it weakens claims, controls, or limitations.
14. **The core workflow is runtime-independent.** Retrieval, rendering, and scripts are optional backends, not prerequisites.

## Current MVP

The current release focuses on **Introduction construction and paper-level story formation**, with literature-grounded framing/novelty/experiment checks and literature-grounded discourse composition. The same state, framing, core, reader-path, literature, and realization layers are intended to extend to Method, Experiments, Related Work, Abstract, and Conclusion.

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

MVP v0.5: literature-grounded paper construction, discourse realization, and venue-aware presentation with rendered-PDF review.
