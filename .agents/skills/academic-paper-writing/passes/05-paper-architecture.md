# Pass 05 — Paper Architecture

## Responsibility

Map the frozen science, packaging, formal method, evidence obligations, real-paper references, and venue rules into a complete manuscript architecture.

This is the first pass allowed to assign page budget.

It does **not** remove required scientific objects merely to fit a page target.

## Inputs

Use:

- Scientific Spec;
- Citation Map;
- Packaging Spec;
- Formal Method;
- Main Result Spine;
- Manuscript Maturity;
- Experimental Obligations;
- Convention Profile;
- venue profile;
- 3–5 nearby real manuscript references when useful.

## Convention use

Apply hard venue rules as constraints.

Apply soft Convention Profile priors as **calibration**, not law. In particular use them to assess:

- section balance;
- where baseline / preliminaries normally become necessary;
- Figure 1 role;
- method-equation density;
- table / figure prominence;
- main-body / appendix boundary;
- reviewer expectations around fairness, uncertainty, and closest-work comparison.

If the current paper has a scientifically justified reason to deviate, preserve the deviation and record it.

Before assigning section space, build or load the [Main Result Spine](../schemas/main-result-spine.md) using [Main Result Spine](../references/procedures/main-result-spine.md).

The spine determines presentation priority. Scientific completeness remains upstream in Formal Method; Architecture decides how much of that science the first-pass reader needs to see.

## Architecture decisions

### 1. Section structure

Choose the minimum structure that gives required scientific objects a natural home.

For a methods paper, explicitly consider whether readers need:

- Preliminaries;
- Problem Formulation;
- Method;
- Experiments;
- Discussion / Limitations;
- Conclusion.

Do not omit Preliminaries simply because the proposed method can be described informally.

### 2. Required-content placement and resolution

Every required equation, definition, citation group, metric, contribution, and assumption must have a section location.

Also classify each substantial object as:

- core;
- prerequisite;
- supporting;
- appendix candidate;
- omit-from-manuscript.

Assign main-body resolution separately from scientific necessity.

No required object may remain "implicitly known", but not every scientifically valid object requires full main-body exposition.

### 3. Section contracts

For each section record:

- scientific role;
- must include;
- may defer;
- equations;
- citations;
- visuals;
- page target.

### 4. Visual architecture

Plan visuals by scientific responsibility:

- Figure 1 -> paper-level insight;
- method overview -> mechanism / credit map;
- main table -> central evidence;
- diagnostics -> secondary evidence.

Do not make sampling mechanics the visual center if the contribution is a credit estimator.

For every high-impact visual/table/algorithm, also construct a [Layout Contract](../schemas/layout-contract.md) using [Layout Contract Construction](../references/procedures/layout-contract.md).

At minimum record:

- owner section;
- prerequisites that must appear first;
- first textual reference / anchor;
- forbidden regions;
- single- vs double-column preference;
- reading-order dependencies;
- heading-integrity requirement;
- repair owner if the final float drifts.

### 5. Maturity-aware experiment surfaces

Apply Manuscript Maturity before planning result surfaces.

At `pre_results`, plan protocols, metrics, baselines, and evidence slots, but do not create full pending/TBD result tables or prose that simulates observed findings.

At `evidence_ready` or later, verified result artifacts may become main tables/plots and empirical claims.

### 6. Experiment hierarchy

Separate:

- end-to-end method comparisons;
- controlled same-data / same-rollout estimator comparisons;
- mechanism ablations;
- diagnostic metrics;
- robustness / scope.

Baseline naming must follow Citation Map distinctions.

### 7. Page budget

Only after required content is placed, assign page targets.

Do not optimize a methods paper toward an arbitrary short preview if the venue permits more room and the missing content affects reviewer judgment.

### 8. Appendix boundary

Move reproducibility detail, extended derivations, prompts, adapters, and secondary sweeps only after confirming the main paper retains what is necessary to evaluate the claim.

## Real-paper calibration

Prefer the already-mined Convention Profile when available. Do not independently rediscover a second incompatible set of conventions inside this pass.



Use several papers to check whether the architecture is plausible, not to copy one outline.

Ask:

- where do nearby methods papers establish their baseline formulation?
- how much main-body space is allocated to the core method?
- where are metric definitions placed?
- how prominent is the main result?
- which technical details remain in the main body?

## Exit criteria

The architecture is ready to freeze when:

- every required scientific object has a location;
- the paper thesis is visible across sections;
- the central method has enough main-body space;
- experiments have a clear evidence hierarchy;
- page budget follows scientific need;
- appendix moves do not break reviewer understanding;
- high-impact figures/tables have frozen Layout Contracts.

## Output

Assemble the [Frozen Paper Spec](../schemas/paper-spec.md) from Pass 1–5 outputs.

Set \`status: frozen\` only when cross-pass contradictions are resolved.
