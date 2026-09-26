# Procedure: Discourse grounding from real papers

Goal: learn reusable reader-facing communication patterns from relevant academic papers without copying their wording, factual content, or paper-specific claims.

This procedure provides positive examples of how strong papers communicate. It does not establish scientific novelty or evidence; use [Literature grounding](literature-grounding.md) for that.

## Core transformation

Always abstract before reuse:

```text
paper text
-> rhetorical / discourse observation
-> section-level discourse reference
-> new realization from our own semantic content
```

Never use:

```text
paper text
-> close paraphrase
```

Do not preserve distinctive phrases, sentence skeletons, metaphors, or unusual wording from a source.

## Reference set

Prefer several relevant papers rather than one imitation target.

A useful set is typically 3–8 papers selected for one or more of:

- close technical area;
- similar type of contribution;
- same target section;
- strong venue fit;
- clear exposition.

Section matching matters. Introduction references should primarily inform Introduction discourse; Method references should inform Method exposition; experiment-writing references should inform experiment questions and result interpretation.

## What to extract

Extract abstract discourse properties, not quotations.

### Section level

Record:

- entry strategy;
- time to the actual research problem;
- ordering of problem, distinction, requirement, and method;
- when the method name first appears;
- how evidence is previewed;
- how contribution statements are scoped.

### Paragraph level

Record:

- local rhetorical purpose;
- relation to the previous paragraph;
- number of conceptual moves combined in one paragraph;
- whether the paragraph leads with example, observation, definition, contrast, question, or claim;
- how paragraph endings create the next information need.

### Sentence level

Record patterns such as:

- contrast between two decision roles;
- concrete ambiguity followed by its learning consequence;
- condition -> consequence;
- definition after phenomenon;
- motivation before equation;
- experimental question before table/result;
- qualification attached directly to a claim.

Represent these as semantic moves, not reusable sentences.

## Section-specific profiles

Do not use one prose profile for the whole paper.

### Introduction

Focus on:

- entry point and abstraction level;
- problem reveal;
- how quickly a concrete difficulty appears;
- how the key distinction is taught;
- method-entry timing;
- contribution scope.

### Method

Focus on:

- the unresolved estimation, optimization, or modeling question before each mechanism;
- definition placement;
- how the paper creates a need for a mathematical object before defining it;
- equation introduction and immediate interpretation;
- whether equations answer reader-visible questions rather than merely documenting components;
- dependency between components;
- transitions between intuition and formalization;
- edge cases or limiting cases used to motivate objective design.

Treat WHY -> WHAT -> HOW as an internal semantic check, not a mandatory visible ordering. A stronger Method discourse pattern is often:

```text
question / ambiguity
-> required quantity
-> definition or equation
-> what the equation measures
-> remaining ambiguity
-> next quantity
```

This lets equations participate in the argument instead of appearing after a prose description of each component.

### Experiments

Focus on:

- research-question-first vs result-first organization;
- how baselines and controls are motivated;
- separation of observation from interpretation;
- qualification of negative or mixed results;
- how ablations connect back to claims.

### Related Work

Focus on:

- comparison axes;
- grouping strategy;
- distinction between shared mechanism and different research problem;
- avoidance of citation-by-catalog.

## Build a Discourse Reference

Use the [Discourse Reference schema](../../schemas/discourse-reference.md).

A reference should describe tendencies such as:

```yaml
section: introduction
entry_strategy: concrete-problem-first
problem_reveal: contrastive
method_naming: delayed_until_requirement_visible
paragraph_flow:
  - situation_to_ambiguity
  - ambiguity_to_distinction
  - distinction_to_solution_requirement
claim_style: conservative
transition_style: semantic_not_marker_heavy
```

Do not encode arbitrary numeric style targets unless they are genuinely useful. The goal is discourse control, not imitation by statistics.

## Applying references

During Reader-facing Discourse Composition:

1. start from our Reader Path and Semantic Draft;
2. choose only discourse patterns compatible with our scientific content;
3. combine patterns from multiple references rather than cloning one source;
4. preserve our terminology and Paper Core;
5. allow paragraph and sentence boundaries to change;
6. prefer natural causal, contrastive, and prerequisite relations over explicit scaffold labels.

A discourse reference may influence organization and realization, but it may not:

- add a fact;
- add or remove a limitation;
- strengthen a claim;
- introduce a citation not scientifically needed;
- import another paper's motivation;
- force our paper into another paper's narrative.

## Failure checks

Reject a realization if:

- its paragraph sequence mirrors one reference paper too closely;
- it contains distinctive wording from a source;
- it adopts a prior paper's problem statement instead of our own;
- the prose is smoother only because claim scope became broader;
- stylistic imitation overrides reader dependency or technical precision.

## No-retrieval fallback

If real paper text is unavailable, use the default academic profile and the skill's reader-first rules. Do not hallucinate a literature-derived discourse profile.
