# Academic Paper Writing Skill

A portable Agent Skill for constructing academic papers from research facts rather than generating prose in one shot.

The v0.12 user-facing execution surface remains compact, but substantial paper work is now maturity-aware, selective, convention-aware, and layout-contract aware:

```text
1. Understand
   -> Research State + Technical State

2. Position
   -> Literature / Framing / Claims
   -> Paper Core

3. Design Evidence
   -> Experimental Obligations
   -> Baselines / Metrics / Controls

4. Write Sections
   -> Main Result Spine
   -> Section Planning / Writer
   -> Editorial Distillation
   -> Reverse Outline
   -> Final Prose Realization

5. Present
   -> Layout Contracts / Page Composition
   -> Official Template / LaTeX / PDF
   -> Rendered Layout Verifier
   -> Final Manuscript Calibration
```

The richer schemas remain available internally, but they are not five more user-visible stages. For example, Section Planning may internally use Reader Path, modules, a Section Contract, and dependency checks without serializing each one as a separate artifact.

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

Internally, full-paper work is no longer one large generation. v0.12 keeps the v0.11 convention/layout machinery and adds **Manuscript Maturity**, a **Main Result Spine**, **Editorial Distillation**, and **Reverse Outline** that carry semantic page-flow constraints alongside the scientific and literature state:

```text
Research Sources                     Convention Sources
   |                                      |
   +--> 01 Scientific Audit               +--> Convention Mining
   |
   +--> 02 Literature Audit
          \          /                    /
           +-------- frozen state --------+
                         |
                   03 Paper Packaging
                         |
                   04 Formal Method
                         |
                   05 Paper Architecture
                         |
                  Frozen Paper Spec
                         |
                Section Writer Calls
                         |
                  06 Independent Audit
                         |
                   Repair / Present
```

The existing procedures remain the toolbox used inside these calls.

Key v0.12 rules:

- **One pass, one decision responsibility.** Scientific formalization, literature verification, packaging, writing, and review do not share one call by default.
- **Frozen handoffs.** Scientific Spec, Citation Map, Convention Profile, and Frozen Paper Spec are explicit interfaces between calls.
- **Hard-vs-soft convention separation.** Official venue rules are hard constraints; layout/formula/information/reviewer patterns mined from real papers are soft priors with evidence and confidence.
- **No silent downstream mutation.** A writer that discovers a missing equation or citation raises an issue to the owning pass instead of patching the scientific story locally.
- **Fresh independent review.** The audit call judges the manuscript that exists and should not inherit the writer's private planning rationale.
- **Targeted invalidation.** A changed upstream decision reruns only downstream outputs that depend on it.
- **Maturity before manuscript surface.** Pre-results drafts may define protocols and evidence slots but may not impersonate finished Results with pending/TBD tables.
- **One central answer before section allocation.** The Main Result Spine ranks core, prerequisite, supporting, appendix, and omit-level material before Architecture spends page budget.
- **Complete drafts are not automatically accepted.** Editorial Distillation explicitly chooses KEEP / COMPRESS / MERGE / RELOCATE / APPENDIX / DELETE.
- **Verify the prose backwards.** Reverse Outline reconstructs paragraph functions from the final draft and catches duplicated or orphaned functions.
- **Semantic layout before physical floats.** High-impact figures/tables carry Layout Contracts that specify owner section, prerequisites, first textual reference, forbidden regions, reading-order dependencies, and fallback placement.
- **Rendered layout is audited semantically.** A PDF can fail even with no overfull boxes if a float drifts across a section boundary or creates a reading-order inversion.

The convention layer captures four explicit prior families:

- **Layout prior**: first-page density, section balance, Figure 1 role, table/figure prominence, appendix boundary.
- **Formula prior**: notation, baseline-before-delta, exact-update visibility, correction terms, limiting cases, equation density.
- **Information-presentation prior**: which scientific objects are best carried by prose, equation, figure, table, algorithm, or plot.
- **Academic/reviewer prior**: closest-work comparison, compute/call fairness, uncertainty reporting, metric-definition order, contribution structure, and other strong but non-universal expectations.

The layout layer adds an explicit compiler state between representation planning and LaTeX:

- **Layout Contract**: who owns a float, what must be read before it, where its first reference lives, where it may not appear, and what reading-order constraints must hold.
- **Page Composition**: converts Layout Contracts into float-placement constraints.
- **Rendered Layout Verifier**: checks semantic float drift, section-boundary integrity, two-column reading order, heading integrity, and attention competition.

The previous calibration and synthesis mechanisms remain active inside the new execution model:

- **Paper Convention Profile**: separates official hard rules from evidence-weighted soft priors for layout, formulas, information carriers, and reviewer expectations.
- **Authorial Synthesis**: internal claims, modules, obligations, and technical nodes are compressed into a smaller author-facing structure by removing workflow commentary, merging concepts/subsections, stabilizing terminology, and preserving concrete anchors.
- **Section Calibration**: each section is checked for completeness, information resolution, representation redundancy, visual obligations, and discourse calibration.
- **Final Manuscript Calibration**: the rendered paper is compared against a small distribution of nearby real papers for narrative density, visual hierarchy, and section balance.
- **Technical State**: method-defining tokens, interfaces, action/state semantics, loss masks, sampling rules, and protocol exceptions survive story compression.
- **Section Contract**: every section declares what must be established, defined before use, inherited, or safely deferred.
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
14. **Technical prerequisites are not implementation trivia.** If a central equation, algorithm, or result depends on an interface, token, transition, or state definition, that prerequisite must remain reader-visible.
15. **Complete is not enough.** Sections must also be selective about when detail appears and calibrated against real-paper discourse.
16. **Real-paper calibration is distributional, not imitation.** Compare against several papers and repair only clear reader-cost or presentation defects.
17. **Internal structure is not manuscript structure.** Claim graphs, obligations, contracts, and modules may guide writing but should not appear as visible prose or one-to-one subsection structure.
18. **Use a compact active vocabulary.** Do not multiply terms unless they encode distinct scientific objects.
19. **Separate incompatible reasoning jobs.** Do not ask one call to verify literature, formalize the baseline, package contributions, write prose, and approve its own result.
20. **Freeze upstream decisions before writing.** Section writers consume Paper Spec; they do not redefine it.
21. **Independent audit is issue-producing, not self-justifying.** Review from fresh context and route defects to their owning pass.
22. **Conventions are evidence-weighted priors, not laws.** Official venue rules may be hard; accepted-paper patterns and reviewer expectations remain soft and contextual.
23. **Semantic placement is part of correctness.** A figure/table that appears before its prerequisites or outside its owner section is a layout defect even if LaTeX permits it.
24. **The core workflow is runtime-independent.** Retrieval, rendering, and scripts are optional backends, not prerequisites.

## Current MVP

The current release covers paper-level framing plus **Introduction, Method, experiment planning, technical-completeness checking, discourse realization, and venue-aware presentation**. Related Work, Abstract, Conclusion, and additional section-specific modules can reuse the same Research State, Technical State, Section Contract, literature, discourse, and presentation layers.

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

MVP v0.12: maturity-aware paper construction with Scientific Spec / Citation Map / Convention Profile / Main Result Spine / Layout Contracts / Paper Spec handoffs, editorial distillation, reverse outlining, semantic page-flow verification, independent manuscript audit, and exact final-artifact calibration.
