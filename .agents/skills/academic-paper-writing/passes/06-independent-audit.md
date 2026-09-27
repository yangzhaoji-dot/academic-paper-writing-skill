# Pass 06 — Independent Paper Audit

## Responsibility

Audit the drafted manuscript from a fresh context after section writers have produced prose.

This pass should not receive the writers' private planning rationale.

It owns issues, not the upstream scientific state.

## Inputs

Use:

- draft manuscript;
- Frozen Paper Spec;
- Scientific Spec;
- Citation Map;
- Main Result Spine;
- Manuscript Maturity;
- relevant research sources;
- venue profile;
- optionally 3–5 manuscript references.

## Audit dimensions

### 1. Scientific completeness

Check whether the manuscript actually contains:

- problem formulation;
- baseline mathematical object;
- required equations;
- exact method delta;
- exact update;
- assumptions;
- metric definitions;
- evidence status.

Do not assume presence because these existed in the Paper Spec.

### 2. Main-result visibility and selectivity

Without reading internal planning, answer:

- What is the single central question?
- What is the one-sentence answer?
- Which method objects are core versus supporting?
- Does any supporting machinery visually/rhetorically compete with the core?
- Could any paragraph/subsection/equation disappear from the main body without harming first-pass understanding?

Flag a manuscript that is scientifically complete but presents all technical objects at equal resolution.

### 3. Packaging visibility

Without reading internal planning, answer:

- What is the paper's thesis?
- What are its contributions?
- What is the core scientific distinction?
- What should Figure 1 make memorable?
- What is the core equation?
- What is the main empirical evidence?

If these answers are unclear, report a packaging/manuscript issue.

### 4. Citation integrity

Check:

- citation exists where a literature-dependent claim is made;
- metadata / labels match Citation Map;
- no adaptation is mislabeled as a full prior method;
- no stale or invented bibliographic entry entered through prose writing.

### 5. Method audit

Check:

- baseline before delta;
- variables defined before equations;
- new advantage/estimator mapped to optimized units;
- final update objective present;
- sampling correction present;
- no required technical prerequisite moved to appendix.

### 6. Experiment and maturity audit

Check:

- manuscript surfaces match Manuscript Maturity;
- at pre_results, no fake final-result table is filled with pending/TBD cells;
- at pre_results, planned evidence is not described as an observed finding;
- metrics defined;
- main comparison matches evidence obligation;
- compute / rollout / Harness-call confounds controlled when required;
- end-to-end baselines separated from estimator adaptations;
- main result visually and rhetorically prominent;
- interpretation does not exceed the comparison.

### 7. Editorial / discourse audit

Check:

- every substantial section has survived Editorial Distillation;
- Reverse Outline reveals one cumulative argument rather than duplicated paragraph functions;
- no workflow scaffold leakage;
- subsection structure is not one-to-one with internal nodes;
- terminology is stable;
- prose reads as scientific argument rather than an explanation of paper organization.

### 8. Venue / rendered-manuscript audit

When PDF exists, additionally inspect:

- official template;
- float ownership / no table before its section;
- page density;
- equation/table readability;
- main-body vs appendix boundary.

## Issue format

Every issue must include:

\`\`\`yaml
severity:
owner_pass:
location:
problem:
why_it_matters:
required_fix:
downstream_outputs_to_invalidate: []
\`\`\`

## Independence rule

Do not rationalize an omission using the writer's intent.

Judge the manuscript that exists.

## Exit criteria

A paper can proceed to final typesetting / calibration only when no blocking issue remains.
