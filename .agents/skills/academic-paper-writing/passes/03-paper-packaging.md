# Pass 03 — Paper Packaging

## Responsibility

Decide the paper-level scientific identity before section writing.

This pass owns:

- title direction;
- one-sentence thesis;
- contribution structure;
- paper-level problem framing;
- canonical terminology;
- Figure 1 message;
- core-equation message;
- empirical story;
- novelty boundary.

It consumes scientific and literature state but does **not** alter them.

## Inputs

Use:

- frozen or sufficiently stable Scientific Spec;
- Citation Map / closest-work boundary;
- Paper Core / framing candidates;
- evidence status.

## Packaging questions

### 1. What is the one-sentence thesis?

It must express a scientific relation, not a workflow description.

A useful form is:

\`\`\`text
change in setting / structure
-> mismatch or missing distinction
-> required method property
\`\`\`

### 2. What is the paper's core object?

The title, Figure 1, Introduction, Method, and Experiments should all make the same object visible.

### 3. What are the contributions?

Do not force exactly three bullets, but prefer **distinct scientific layers** rather than several bullets at one implementation layer.

Common structure for methods papers:

\`\`\`text
problem / formulation
method / estimator / algorithm
evidence / empirical finding
\`\`\`

A third empirical contribution may remain unresolved until real evidence exists.

Do not count "claim-driven evaluation" or paper-organization choices as scientific contributions.

### 4. What is the core visual message?

Figure 1 should communicate the paper-level insight, not merely draw the pipeline.

### 5. What is the core equation message?

Decide what mathematical contrast should remain in the reader's memory.

Examples:

\`\`\`text
one trajectory advantage everywhere
-> token / segment-specific credit

single action group
-> nested between-mode and within-mode comparisons
\`\`\`

### 6. Canonical terminology

Freeze a compact active vocabulary.

Avoid multiple primary names for one concept.

### 7. Title audit

A title should usually expose enough of:

- method identity;
- scientific problem;
- research setting;
- mechanism type.

Avoid titles that describe only a local operation when the paper claims a broader scientific object.

## Exit criteria

Freeze packaging only when:

- thesis is one sentence;
- contributions occupy distinct scientific layers;
- Figure 1 and core equation reinforce the thesis;
- title and terminology are aligned;
- claims stay within Citation Map / Scientific Spec boundaries.

## Issue routing

If packaging requires a stronger scientific claim than the evidence/spec supports, return the issue upstream instead of inflating the story.
