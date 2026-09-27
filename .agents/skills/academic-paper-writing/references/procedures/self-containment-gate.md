# Procedure: Self-Containment Gate

Goal: ensure Editorial Distillation does not remove definitions needed to understand or verify the core method from the main paper.

Run after Editorial Distillation and before Reverse Outline.

## Inputs

Use:

- distilled section;
- Main Result Spine;
- Formal Method;
- Technical State;
- Section Contract;
- appendix relocation decisions.

## Core-equation closure

For every core equation or algorithm retained in the main body:

1. list every nonstandard symbol, loss term, estimator, state, operator, and correction it references;
2. identify where each dependency is defined;
3. classify the dependency as:
   - locally defined;
   - defined earlier in the main body;
   - conventional and safely assumed;
   - appendix-only;
   - undefined;
4. reject the distilled section if a dependency required to interpret the core equation is appendix-only or undefined.

The appendix may hold derivations, alternate forms, implementation schedules, and expanded algebra. It must not hold the only operational meaning of a term used by a core main-body objective.

## Verification-chain test

A technically capable reader should be able to answer from the main paper:

- What is optimized?
- Which tokens / actions / policy regions receive each signal?
- How is each central advantage / score computed?
- How are forced or biased samples corrected?
- Which baseline or normalization the core estimator depends on?
- What changes relative to the stated baseline?

If one of these answers requires an appendix, restore a compact exact definition to the main body.

## Compression ladder

When the gate fails, restore the smallest representation that closes the dependency:

~~~text
full derivation in appendix
+
compact exact main-body definition
~~~

Prefer this over moving the entire derivation back.

Example:

~~~text
main body:
B_x = exact compact definition
regional losses = compact exact definitions

appendix:
expanded target-weighted sigma_x^2
alternate flat-sample correction derivation
training-schedule detail
~~~

## Core vs supporting rule

Self-containment applies most strongly to objects classified as core or prerequisite by the Main Result Spine.

Supporting objects may remain appendix-only when the main paper does not reference their undefined symbols or rely on them to interpret the central update.

## Exit condition

PASS only when all core main-body equations have dependency closure inside the main paper.

Possible failures:

~~~text
undefined_core_term
appendix_only_core_dependency
missing_optimization_semantics
missing_sampling_correction_semantics
missing_policy_region_mapping
~~~

Route failures to Editorial Distillation / Paper Architecture rather than silently expanding prose everywhere.
