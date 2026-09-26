# Parallel Pass — Paper Convention Mining

## Responsibility

Infer a **Paper Convention Profile** for the target venue, year, research area, and paper type.

This pass owns the [Convention Profile](../schemas/convention-profile.md).

It is presentation-facing. It does **not** decide the scientific thesis, novelty claim, formal method, or empirical conclusion.

## Why this pass exists

A manuscript can be scientifically complete yet still violate strong academic expectations:

- the baseline objective appears too late;
- a new advantage is defined but never placed inside the actual update;
- method-specific metrics first appear in a result table;
- Figure 1 explains implementation rather than the paper-level distinction;
- a major result is visually subordinate to diagnostics;
- the main paper is artificially compressed while critical reviewer information moves to appendix;
- a table repeats prose instead of carrying a distinct information role.

These are not all venue rules. Many are **soft academic conventions** that should be learned from several nearby papers and reviewer/checklist practice.

## Inputs

Use:

- target venue + year;
- paper type, e.g. methods / benchmark / analysis / systems / theory;
- research area / nearest subarea;
- official venue instructions and checklist when available;
- 5–15 relevant accepted or strong nearby papers when retrieval permits;
- existing Venue Profile / Presentation References;
- no scientific claims from the current paper are required beyond its broad type.

## Evidence separation

### Source A — official venue / year

Extract only hard constraints:

- page / formatting rules;
- anonymity;
- checklist requirements;
- appendix / supplementary rules;
- template requirements;
- citation or bibliography requirements when official.

### Source B — nearby real papers

Extract distributional tendencies:

- first-page density;
- section balance;
- Figure 1 role;
- method-to-experiment page ratio;
- equation progression;
- where baseline formulation appears;
- prominence of the main result;
- table / figure density;
- main-body / appendix boundary.

### Source C — reviewer/checklist expectations

Extract soft expectations such as:

- claims matched to evidence;
- compute / data / call-budget fairness;
- uncertainty reporting;
- reproducibility detail;
- closest-work comparison;
- limitations / scope;
- metric definitions before interpretation.

Do not label these hard unless the venue explicitly requires them.

## Four required outputs

### 1. Layout prior

Record tendencies for:

- first page;
- Introduction length/density;
- Related Work placement;
- Method share of main body;
- Experiments share of main body;
- number / role / placement of figures and tables;
- appendix boundary;
- float behavior that materially affects interpretation.

Do not reduce this to a fixed page template.

### 2. Formula exposition prior

For methods papers, inspect the exposition grammar:

\`\`\`text
notation
-> baseline formulation
-> baseline objective
-> missing distinction / limitation
-> proposed quantity
-> estimator / decomposition
-> mapping to optimized unit
-> exact update
-> correction / limiting case
\`\`\`

This is a prior, not a mandatory visible sequence.

Check tendencies for:

- variables defined before use;
- baseline before method delta;
- one or two visually central equations;
- exact policy / optimization update in main body;
- correction term when sampling changes;
- limiting / degenerate cases;
- equation interpretation immediately after the equation;
- how much derivation moves to appendix.

### 3. Information-presentation prior

Infer which carrier usually best communicates each information type.

Examples:

- interface semantics -> table;
- conceptual mismatch -> Figure 1;
- estimator -> equation;
- full rollout-credit flow -> method figure;
- exact execution order -> algorithm when needed;
- main comparison -> table;
- dynamics / calibration -> plot.

Do not create a figure or table merely because papers in the sample contain one.

### 4. Academic-convention / reviewer prior

Record soft expectations with applicability and strength.

Examples:

- contributions often occupy distinct scientific levels rather than repeating one implementation layer;
- a methods paper should make the baseline mathematical object recoverable without reviewer guesswork;
- the exact update corresponding to the claimed algorithm is normally main-body material;
- a method-specific metric should be defined before its first reported value;
- additional rollout / retrieval / Harness calls require a resource-matched comparison when they could explain gains;
- a closest work should be compared directly rather than omitted;
- estimator adaptations should not be mislabeled as full prior-method reproductions;
- major empirical claims should report uncertainty / seeds when stochastic training is involved;
- main evidence should not be hidden in appendix;
- strong novelty words require strong literature support;
- Figure 1 often carries the 30-second paper-level explanation.

Again: these are not universal laws.

## Mining procedure

1. Verify target venue/year hard rules.
2. Select a diverse nearby-paper set.
3. Extract section- and representation-level observations.
4. Aggregate **ranges and recurring patterns**, not exact mimicry.
5. Assign each prior:
   - applicability;
   - strength;
   - confidence;
   - evidence count / source role.
6. Record disagreements explicitly.
7. Freeze the Convention Profile.

## Exit criteria

Freeze only when:

- hard constraints are source-separated from soft priors;
- at least the four required output categories exist;
- no convention changes scientific content;
- low-evidence tendencies are marked low confidence;
- no single paper dominates the profile.

## Issue routing

If official target-year rules are unavailable:

- mark hard-rule status provisional;
- use the latest verified rules only for provisional planning;
- require refresh before final submission.

If no nearby papers can be retrieved:

- use the skill's default academic priors;
- mark them as fallback rather than literature-mined convention.
