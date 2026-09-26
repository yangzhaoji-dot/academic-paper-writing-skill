# Pass 04 — Formal Method Builder

## Responsibility

Construct the complete mathematical / algorithmic method specification that the manuscript must explain.

This pass owns the \`formal_method\` part of the Frozen Paper Spec.

It does **not** optimize prose or page count.

## Inputs

Use:

- Scientific Spec;
- Packaging Spec;
- Technical State;
- Citation Map for baseline attribution;
- Convention Profile for formula-exposition priors only.

## Convention boundary

Use the Convention Profile only to check **exposition completeness**, for example whether a methods paper normally needs:

- baseline formulation before the method delta;
- variables defined before use;
- the exact optimized update in the main body;
- correction terms after forced / off-policy sampling;
- limiting or degenerate cases when they clarify the method.

Convention evidence may change **what must be explained visibly**, but it may not change the mathematical method itself.

## Required construction

### 1. Baseline formulation first

Write the mathematical object being modified before the proposed method.

Required when applicable:

- policy / factorization;
- trajectory or action notation;
- reward / return;
- policy ratio;
- baseline advantage estimator;
- baseline objective;
- baseline credit assignment rule.

For an RL paper, "everyone knows GRPO/PPO" is not a reason to omit the baseline object from the formal method state.

### 2. Expose the mismatch mathematically

Show precisely where the baseline object fails to represent the distinction highlighted by the packaging thesis.

Example pattern:

\`\`\`text
baseline:
A_i -> all generated tokens

method setting:
prefix -> invocation -> conditional execution

missing distinction:
one A_i cannot separately identify those roles
\`\`\`

### 3. Define the proposed estimator

Every new quantity must have:

- operational meaning;
- prerequisites;
- equation;
- interpretation.

### 4. Map estimator to optimized units

Explicitly define where each credit signal applies:

- token;
- action;
- segment;
- branch;
- route;
- module.

Do not leave this mapping implicit.

### 5. Give the exact update objective

This is a hard requirement.

The final formal specification must show how the proposed credit is inserted into the actual policy update.

A generic pattern is:

\`\`\`text
baseline clipped objective
+ proposed token/action advantage assignment
+ behavior / importance weighting when sampling changed
+ KL or regularization term
\`\`\`

If the paper proposes a new advantage but never writes the actual policy-update equation, the pass is blocked.

### 6. Sampling corrections

If rollouts are forced, stratified, branched, replayed, or otherwise off the baseline sampling distribution, define the weighting/correction and state whether alternative aggregation forms are equivalent.

### 7. Training schedule and edge cases

Formalize only schedules or special cases that materially change the objective.

Examples:

- warm-up masks;
- coefficient schedule;
- \`K=1\` fallback;
- deterministic/cached external feedback assumption.

### 8. Metric definitions

Provide formulas/protocols for method-specific experiment metrics required by Scientific Spec.

## Formal-method completeness test

A technically competent reader should be able to answer:

1. What is the baseline update?
2. What exact mathematical object changes?
3. Which generated units receive which signal?
4. What is the final proposed update?
5. What sampling correction is applied?
6. What assumptions are required?
7. Which metrics directly test the new distinction?

## Exit criteria

Block if any of the above is missing.

Do not solve missing equations with explanatory prose.

## Issue routing

Missing baseline or undefined scientific quantity -> Pass 01.

Unverified attribution -> Pass 02.

Packaging / terminology inconsistency -> Pass 03.
