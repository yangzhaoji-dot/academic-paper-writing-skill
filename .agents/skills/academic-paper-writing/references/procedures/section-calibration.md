# Procedure: Section calibration

Goal: make each section **complete, selective, and calibrated** before final prose realization.

Section calibration is an internal check inside **Write Sections**. It does not create a new user-facing phase.

It combines four questions:

1. **Completeness** — what must this section establish?
2. **Information resolution** — what must be explained now, previewed, or deferred?
3. **Representation allocation** — which information belongs primarily in prose, equation, table, figure, or algorithm?
4. **Discourse calibration** — how do strong papers in the same area/venue usually organize this kind of section?

## Inputs

Use, as needed:

- Paper Core;
- Technical State;
- Claim Graph;
- Experimental Obligations;
- Section Contract;
- prior sections;
- section-matched Discourse References;
- section-matched real-paper references.

## 1. Completeness

Start from the Section Contract.

Confirm:

- every technical prerequisite has a reader-visible home;
- downstream variables are defined before use;
- no central equation depends on an omitted interface, state, token, transition, or mask;
- no central empirical claim lacks its required evidence.

This is a hard gate.

## 2. Information resolution

Not every true fact belongs at full detail in the current section.

Classify section-relevant information into:

\`\`\`text
must_explain_now
preview_only
defer_to_later_section
defer_to_appendix
omit_from_main_paper
\`\`\`

Use reader dependency, not information availability, to choose the level.

### Introduction

Typical resolution:

- **must explain now**: concrete problem, key distinction, why current formulation is insufficient, high-level method idea, evidence preview;
- **preview only**: mechanism names, broad empirical findings;
- **defer**: exact token grammar, estimator equations, optimization details, training schedules.

Do not let the Introduction become a compressed version of the whole paper.

### Method

Typical resolution:

- **must explain now**: definitions required for central equations/algorithm, operational semantics, core mechanism, objective;
- **defer**: serialization details, full schemas, routine derivations, engineering specifics.

### Experiments

Typical resolution:

- **must explain now**: empirical question, controlled comparison, direct metric, main result, interpretation boundary;
- **defer**: exhaustive per-seed tables, secondary sweeps, non-decisive diagnostics.

## 3. Representation allocation

For every important fact or concept, choose one **primary carrier**:

\`\`\`yaml
fact_or_concept:
primary_carrier: prose | figure | table | equation | algorithm
secondary_mentions: []
\`\`\`

Do not fully explain the same fact in prose, table, and figure unless each representation serves a distinct role.

Examples:

- Harness suite semantics -> compact table as primary carrier;
- candidate-conditioned Verification exception -> prose as primary carrier;
- credit decomposition -> equation as primary carrier;
- full rollout/credit flow -> method figure as primary carrier;
- algorithm execution order -> pseudocode only if prose + figure remain ambiguous.

Run a **representation redundancy check**:

- is a table repeating prose row by row?
- is a figure decorative rather than carrying unique information?
- is an equation restated in sentences without adding interpretation?
- is an algorithm duplicating the Method subsection line by line?

If yes, remove or compress the weaker carrier.

## 4. Visual obligations

Some concepts should be assigned a visual role during section planning rather than discovered during final typesetting.

Record only when useful:

\`\`\`yaml
concept:
role:
required_information:
best_form: figure | table | plot | equation | algorithm
\`\`\`

A visual is justified when it reduces reader memory load, exposes a structure, or makes a decisive comparison interpretable.

Examples:

- Introduction: conceptual ambiguity -> Figure 1;
- Method: full rollout + credit map -> overview figure;
- Experiments: decisive same-data comparison -> main table;
- training dynamics claim -> plot.

Do not create a visual solely because the section "needs a figure."

## 5. Discourse calibration

Use 3–8 relevant papers when available.

Extract only abstract tendencies:

- how quickly the section reaches its core question;
- how much technical detail appears before the main idea;
- how equations are motivated;
- how experiment subsections connect to claims;
- how much interpretation follows a result.

Do not match one paper's sentence sequence.

The current paper's own dependencies dominate.

## Section-specific calibration questions

### Introduction

- How many conceptual moves occur before the concrete problem?
- Is method detail appearing before the reader understands the need?
- Are later-section details consuming first-page attention?
- Does Figure 1 explain the paper's problem rather than the implementation?

### Method

- Are all technical prerequisites present?
- Is each equation motivated by a reader-visible question?
- Are prose, table, and figure responsibilities non-redundant?
- Does the overview figure carry enough structure to reduce prose?
- Are exceptions and non-uniform protocols explained where they matter?

### Experiments

- Is the decisive claim given the most visual and textual prominence?
- Does each major subsection answer an empirical question?
- Are compute / data / interaction confounds controlled where required?
- Are ablations tied to explanatory alternatives rather than listed as component deletions?

## Exit condition

A section is ready for final discourse realization only when it is:

- **complete** — no missing prerequisite;
- **selective** — no unnecessary early detail;
- **non-redundant** — each representation has a primary role;
- **calibrated** — its information density and reveal order are plausible relative to strong real papers.

Do not expose this checklist in the finished paper.
