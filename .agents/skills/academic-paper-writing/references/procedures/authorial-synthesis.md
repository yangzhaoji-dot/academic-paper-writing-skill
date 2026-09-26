# Procedure: Authorial synthesis

Goal: convert a semantically complete section plan into an **author-shaped exposition** before paragraph-level discourse realization.

Authorial synthesis is an internal step inside **Write Sections**. It does not add a user-facing phase and should not be serialized unless it helps diagnose or iteratively revise a section.

The central rule is:

> Internal research and writing structure must not become the visible structure of the manuscript by default.

A paper may internally use Claim Graphs, Experimental Obligations, Reader Paths, Section Contracts, modules, dependency graphs, and evidence priorities. The final manuscript should expose the science, not the workflow that organized it.

## Position in the pipeline

\`\`\`text
Section Planning
-> Section Calibration
-> Semantic Draft
-> Authorial Synthesis
-> Discourse Realization
-> Naturalization
\`\`\`

Section Calibration decides **what belongs** and **at what resolution**.

Semantic Draft guarantees **scientific completeness**.

Authorial Synthesis decides **what an author would actually foreground, merge, name, and carry forward**.

Discourse Realization then turns that synthesized structure into paragraphs and sentences.

## Inputs

Use only what is needed from:

- Semantic Draft;
- Section Contract;
- Paper Core;
- Technical State;
- section-specific Claim / Experimental Obligation information;
- prior section prose;
- section-matched Discourse References.

## Four synthesis checks

### 1. Scaffold removal

Identify sentences, headings, or transitions whose primary function is to explain the paper-writing process rather than the science.

Common warning patterns include:

- "the paper's central claim";
- "the decisive experiment";
- "the primary result";
- "our question is narrower";
- "this experiment is designed to";
- "this comparison isolates";
- "this metric matters because";
- "we therefore separate the evaluation into";
- "the following section validates";
- "to test our claim";
- "the experimental obligation is";
- "the contribution of this experiment is".

These phrases are not universally forbidden. Reject them only when their meaning can be carried more directly by the scientific observation, comparison, or interpretation.

Prefer transformations such as:

\`\`\`text
workflow statement
-> scientific setup / observation / interpretation
\`\`\`

Example:

Bad:
> The decisive experiment holds branch data fixed and changes only the credit rule.

Prefer:
> We reuse the same restored states, suffixes, and rewards across credit estimators, so differences in learning arise from the assigned credit rather than additional exploration.

Better when results exist:
> With identical branch trajectories and rewards, H-PAIR improves success while reducing invocation regret relative to branch-based credit baselines.

The goal is not to delete experimental rationale. It is to express the rationale as part of the scientific comparison rather than as commentary on paper organization.

### 2. Concept and subsection compression

Internal concepts are finer-grained than manuscript concepts.

Before preserving a heading or named component, ask:

> Does the reader need this concept as an independently reusable scientific object, or is it only an internal planning distinction?

Merge adjacent internal nodes when they form one continuous reader-facing idea.

For example, an internal Method plan may contain:

\`\`\`text
decision protocol
Harness semantics
branch-point selection
state restoration
conditional sampling
\`\`\`

but the visible paper may need only:

\`\`\`text
Harness Decisions and Paired Rollouts
\`\`\`

Similarly:

\`\`\`text
route mean
gate value
prefix credit
gate credit
within-mode residual
\`\`\`

may belong under one visible subsection:

\`\`\`text
Paired Credit Assignment
\`\`\`

#### Heading test

Keep a subsection heading only if at least one is true:

- the concept is a reusable scientific object referenced later;
- the subsection answers a distinct reader question;
- the subsection contains a substantial derivation, algorithmic stage, or experimental unit;
- collapsing it would make navigation materially harder.

Do not create headings merely because an internal schema has a named field.

### 3. Terminology compression

Maintain a small **canonical vocabulary** for each paper.

Create, implicitly or explicitly, a map:

\`\`\`yaml
canonical_terms:
  concept:
    preferred_term:
    allowed_variants: []
    avoid_as_primary: []
\`\`\`

Rules:

- one scientific distinction should normally have one primary name;
- a new term must introduce a real new distinction;
- internal schema names do not automatically become paper terminology;
- avoid alternating between near-synonyms merely for stylistic variety;
- abbreviations should reduce burden rather than create another vocabulary layer.

For H-PAIR, for example, a compact active vocabulary may prefer:

- Harness decision;
- use / skip;
- paired rollout;
- invocation credit;
- execution credit.

Terms such as \`gate\`, \`routing decision\`, \`mode\`, \`semantic route\`, and \`decision boundary\` should not all behave as independent names unless the method genuinely requires those distinctions.

#### Terminology test

For each paragraph, ask:

- how many new technical nouns are introduced?
- are two names referring to the same thing?
- does changing the term help precision, or merely vary wording?
- can an internal label disappear entirely after its equation or role is understood?

### 4. Concrete-anchor continuity

Each major section should give the reader a concrete object, state, example, comparison, or trajectory that can carry abstractions forward.

Ask:

> What is the reader mentally following through this section?

A useful anchor can be:

- one candidate action;
- one trajectory;
- one restored state;
- one failure case;
- one table comparison;
- one running mathematical object.

For H-PAIR, a Verification example can carry the Introduction and early Method:

\`\`\`text
candidate action
-> verify or skip
-> continuation
-> task outcome
\`\`\`

The abstract distinction then grows from that anchor:

\`\`\`text
verify vs skip
-> invocation difference

multiple verified continuations
-> execution difference
\`\`\`

Do not force one example across the entire paper. Preserve an anchor only while it reduces abstraction cost.

## Section-specific synthesis

### Introduction

Prefer:

\`\`\`text
concrete situation / ambiguity
-> consequence for learning
-> missing distinction
-> method idea
-> evidence preview
\`\`\`

Avoid turning the Introduction into a visible sequence of:

\`\`\`text
setting
-> gap
-> claim
-> contribution
-> experimental obligation
\`\`\`

even if those states exist internally.

Contribution bullets should describe what the research contributes, not how the paper validates itself.

### Method

Prefer a few scientifically meaningful subsections over one subsection per internal component.

Definitions should appear where they become necessary.

Do not name every intermediate quantity in prose if the equation and immediate interpretation are sufficient.

A strong visible organization often looks like:

\`\`\`text
operational setup
-> core comparison / estimator
-> optimization / training
\`\`\`

while retaining many more internal dependencies.

### Experiments

Do not translate Experimental Obligations directly into prose.

Prefer:

\`\`\`text
comparison setup
-> observation
-> interpretation
-> boundary / exception
\`\`\`

over:

\`\`\`text
claim
-> why this experiment tests the claim
-> why this metric matters
-> table
-> restatement of the result
\`\`\`

The experiment design can remain explicit when causal control requires it, but it should read as scientific setup rather than workflow commentary.

### Related Work

Do not expose the literature matrix as a catalog.

Group papers by scientific relation and state differences directly.

## Synthesis output

The output is not polished prose. It is a compressed author-facing structure such as:

\`\`\`yaml
section_surface_outline:
  - ...
canonical_terms:
  - ...
concrete_anchor:
  ...
merge_decisions:
  - ...
scaffold_to_remove:
  - ...
\`\`\`

This representation is optional. In ordinary drafting, perform these transformations implicitly and pass the result directly to Discourse Realization.

## Hard preservation rules

Authorial synthesis may:

- merge internal modules;
- remove internal labels;
- rename concepts to canonical terms;
- reorder locally when dependencies remain valid;
- replace workflow commentary with direct scientific statements;
- carry one concrete example across several paragraphs;
- reduce subsection count.

It may not:

- remove a technical prerequisite required by the Section Contract;
- strengthen or weaken a claim;
- invent a result;
- erase a limitation;
- alter an equation's meaning;
- hide a protocol exception;
- change the evidence hierarchy established by Experimental Obligations.

## Exit condition

A section is ready for Discourse Realization when:

- internal workflow language is no longer carrying the argument;
- visible concepts are coarser than internal planning nodes where appropriate;
- terminology is stable and compact;
- the reader has a concrete anchor when abstraction would otherwise become costly;
- technical completeness survives the compression.

The desired result should feel **authored from the science**, not assembled from the writing workflow.
