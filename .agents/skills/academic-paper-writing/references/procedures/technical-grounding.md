# Procedure: Technical grounding

Goal: preserve the technical objects, interfaces, state transitions, action semantics, optimization masks, and dependencies required to understand or reproduce the method.

The Technical State is parallel to the Paper Core:

- **Paper Core** answers: what is this paper fundamentally about?
- **Technical State** answers: what must remain technically defined for the method to be well-formed?

Do not compress implementation-defining semantics merely because they are not part of the paper's conceptual thesis.

## Inputs

Use all research sources that may define the method, including:

- method specifications;
- interface / API documents;
- loss and objective specifications;
- environment adapters;
- training protocols;
- architecture notes;
- implementation constraints;
- experiment protocols;
- open design decisions.

Do not assume that the repository's README or primary method document contains the full technical definition.

## Research Source Coverage

Before constructing the Technical State, inventory the available research sources by role:

\`\`\`text
idea / claims
method
interfaces / action space
state and transitions
training objective / loss
environment / data
experiments
implementation constraints
limitations / open questions
\`\`\`

For each role, record:

- which source(s) were inspected;
- whether coverage is complete, partial, or unknown;
- unresolved conflicts between sources;
- technical files or notes that have not yet been read.

If a source is likely to define a core method object but has not been inspected, mark technical grounding incomplete.

## Extract the Technical State

Record only method-defining information supported by the research sources.

Useful categories include:

### Objects and variables

- policy variables;
- latent / explicit decisions;
- state variables;
- action variables;
- rewards / utilities;
- baselines and advantages;
- persistent external state.

### Representation

- special tokens;
- tokenizer assumptions;
- action grammar;
- structured outputs;
- masks;
- model-visible vs hidden state.

### Interfaces

For every tool, Harness, module, or external component:

- state it reads;
- state it writes;
- actor-facing API;
- call timing;
- return type;
- cost;
- allowed information boundary;
- deterministic / stochastic behavior.

### Transition semantics

For each important decision:

\`\`\`text
pre-state
-> decision / action
-> external computation or state mutation
-> observation / return
-> next actor state
\`\`\`

### Optimization semantics

Record:

- which generated regions receive loss;
- which observations / external outputs are masked;
- where different advantages are applied;
- behavior-policy corrections;
- schedules or stage-dependent masks.

### Protocol variants and exceptions

Do not erase a real exception merely to make the method look uniform.

If one component has a different decision boundary, action timing, or state dependency, record it explicitly.

### Sampling and branching semantics

When relevant, distinguish:

- where a decision exists;
- where extra samples are collected;
- what is forced vs naturally sampled;
- which state is restored;
- which random variables are held fixed;
- which groups are compared.

## Dependency graph

Construct semantic prerequisites among technical objects.

Example:

\`\`\`text
action interface
-> meaning of decision variable
-> branch semantics
-> return groups
-> credit estimator
-> optimization objective
\`\`\`

A downstream equation or algorithm may not be treated as reader-ready while a required upstream object remains undefined.

## Completeness test

Another model should be able to answer, when applicable:

1. What can the policy choose at each relevant step?
2. How is that choice represented?
3. What state does each external component read or mutate?
4. What exactly happens under each branch / mode?
5. Which outputs become context and which receive gradient?
6. Which decisions exist everywhere and which are sampled only at selected locations?
7. What does each central variable in the equations correspond to operationally?
8. Which protocol exceptions matter?

If these questions cannot be answered from the Technical State, do not proceed to final Method prose.

## Output

Use the [Technical State schema](../../schemas/technical-state.md).

Technical State is author-side state. It is not a requirement to expose every field verbatim in the paper. Section Contracts decide what a reader needs in each section.
