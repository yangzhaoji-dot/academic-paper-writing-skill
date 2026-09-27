# Procedure: Editorial Distillation

Goal: remove specification-like completeness from drafted prose while preserving the scientific contract.

Run after a Section Writer produces a complete draft and before final section verification.

This procedure asks **why an object still deserves space**, not whether it is technically correct.

## Inputs

Use:

- drafted section;
- Main Result Spine;
- Section Contract;
- Formal Method / Technical State when needed;
- Manuscript Maturity;
- representation responsibilities;
- adjacent finalized sections when duplication is possible.

## Unit decisions

For each paragraph, subsection, displayed equation block, figure/table explanation, or algorithm, choose exactly one primary action:

```text
KEEP
COMPRESS
MERGE
RELOCATE
APPENDIX
DELETE
```

## Decision tests

### 1. Spine test

What part of the Main Result Spine does this unit serve?

If none, it needs a strong prerequisite/reproducibility reason to remain.

### 2. Removal-cost test

Ask:

> If this unit disappears from the main body, what does the first-pass reader lose?

Classify loss as:

- blocking understanding;
- important interpretation;
- verification detail;
- convenience only;
- nothing.

### 3. Resolution test

Could the same scientific object be represented at lower resolution here and fully elsewhere?

Typical pattern:

```text
Abstract -> role
Introduction -> intuition / mechanism class
Method -> exact mechanics
Appendix -> derivation / implementation detail
```

### 4. Redundancy test

Check whether prose merely restates:

- a figure;
- a table;
- an equation;
- an earlier paragraph;
- an internal planning artifact.

Keep the primary carrier and only the interpretation needed around it.

### 5. Workflow-leakage test

Remove author-side process language such as:

- primary evidence surface;
- this experiment discharges obligation X;
- the next check is;
- to validate contribution 2 we;
- pending values;
- writer/audit/pass terminology.

Replace it with reader-facing scientific content, or delete it when it carries no science.

### 6. Maturity test

At `pre_results`, remove fake final-result surfaces. Keep experimental protocol and planned comparisons, but do not build tables full of TBD/pending cells.

## Safety invariant

Distillation may reduce surface area but may not:

- delete the only definition of a required technical prerequisite;
- weaken reproducibility beyond the chosen main-body/appendix split;
- invent evidence;
- strengthen claims;
- hide a material limitation.

If removing content would violate the Section Contract, repair the architecture/resolution decision rather than forcing deletion.

## Output

Return:

1. a compact decision ledger;
2. the distilled section;
3. any relocation/appendix obligations;
4. any upstream issue discovered.

Do not expose the decision ledger in the final manuscript.
