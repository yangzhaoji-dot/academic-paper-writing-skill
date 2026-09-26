# Procedure: Section Contract and prerequisite check

Goal: define what a section must accomplish semantically before prose optimization or page compression can begin.

A Section Contract sits between global paper planning and section drafting.

It prevents two failures:

1. a rhetorically smooth section that omits technical prerequisites;
2. a venue-compressed section that moves necessary definitions out of the main paper.

## Inputs

Use:

- Paper Core;
- Claim Graph;
- Technical State;
- Experimental Obligations;
- Reader Path;
- Narrative;
- section role;
- prior sections and what they have already established.

## Build the Section Contract

For each section, record:

### Must establish

Facts, definitions, distinctions, claims, equations, or empirical questions that the reader must understand before leaving the section.

### Must define before use

Terms, symbols, interfaces, state variables, action semantics, and protocol assumptions whose downstream use depends on them.

### Must not claim

Unsupported, premature, or out-of-scope conclusions.

### May reference as established

Concepts already defined earlier and safe to reuse without full re-explanation.

### Information resolution

For section-relevant information, classify the required resolution:

- **must explain now** — required for this section's reader task;
- **preview only** — useful orientation, but detailed explanation belongs later;
- **defer to later section** — needed in the main paper, but not yet;
- **defer to appendix** — not required for first-pass understanding/evaluation;
- **omit from main paper** — true but unnecessary for the paper argument.

This prevents a technically complete section from becoming overfull.

### Representation responsibility

For important facts or concepts, identify a primary carrier when useful:

- prose;
- figure;
- table;
- equation;
- algorithm.

Secondary mentions should add interpretation rather than duplicate the primary carrier.

### May defer

Details that can move later or to appendix without breaking understanding or evaluation.

### Dependencies

Represent reader-visible prerequisites as a directed graph.

Example:

\`\`\`text
Harness interface
-> USE / NO-HARNESS semantics
-> routing variable g
-> paired branch
-> mode means
-> gate advantage
\`\`\`

The graph is semantic, not necessarily the final paragraph order.

## Method Contract

For Method, explicitly check, when relevant:

- decision / action space;
- representation of each decision;
- exact decision boundary;
- state and interface semantics;
- transition under each mode;
- model-visible observations;
- optimization / loss masks;
- sampling or branching semantics;
- meaning of every central mathematical variable;
- protocol exceptions;
- objective and training schedule.

Do not treat interface semantics as appendix-only implementation detail when the method's equations depend on them.

## Experiment Contract

For Experiments, ensure:

- each major experiment maps to a central claim or obligation;
- the competing explanation is visible;
- controlled and independent variables are defined;
- direct metrics are identified;
- compute / interaction matching is explicit when causally necessary;
- interpretation and falsifier remain within the comparison's scope.

## Calibration hook

After the contract is built, run [Section calibration](section-calibration.md) when the section is substantial enough to benefit from real-paper comparison or representation planning.

Section calibration checks:

- completeness;
- information resolution;
- representation redundancy;
- visual obligations;
- discourse calibration against real papers.

## Contract gate

A section may proceed from Semantic Draft to Discourse Composition only if:

- every \`must_establish\` item is covered;
- every downstream-used prerequisite is defined or explicitly inherited;
- no dependency edge points to an undefined node;
- deferred items are genuinely non-essential for first-pass understanding;
- no unsupported claim is required to make the section coherent.

If the gate fails, repair Technical State, Section Contract, or Semantic Draft first. Do not use naturalization to hide the omission.

## Presentation gate

Before moving content from main paper to appendix, re-run the Section Contract.

Classify content as:

- **core claim**;
- **technical prerequisite**;
- **supporting detail**;
- **appendix candidate**;
- **removable**.

Technical prerequisites default to the main paper unless they were already established elsewhere or can be compressed without losing the dependency.

## Output

Use the [Section Contract schema](../../schemas/section-contract.md).
