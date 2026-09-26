---
name: academic-paper-writing
description: Construct, draft, revise, or review academic research papers from research ideas, evidence, experiments, and notes using explicit problem construction, claim framing, paper-core extraction, reader-path planning, rhetorical modules, semantic drafting, natural-language realization, experimental obligations, and claim-evidence review. Use for paper introductions, section planning, research framing, contribution positioning, prose naturalization, experiment-story alignment, and full-paper consistency review; do not invent missing research facts or citations.
---

# Academic Paper Writing

Use this skill to turn research content into a paper through explicit intermediate representations rather than a single prose-generation step.

## Core invariant

Separate **what is true**, **what the paper is about**, and **how the reader encounters it**.

Never introduce a factual result, comparison, citation, method component, dataset property, or literature claim that is not supported by the supplied research material or a source the user explicitly authorizes you to retrieve.

## Operating modes

Infer the narrowest mode that satisfies the request:

- **Ground**: organize ideas, methods, experiments, literature notes, and limitations into a Research State.
- **Frame**: construct the broader research setting, structural change, mismatch, research problem, method role, and defensible claims.
- **Core**: compress the selected framing and claims into one stable Paper Core that every major section must express at an appropriate level of detail.
- **Plan**: choose a narrative, derive the shortest Reader Path, and map it into section-level rhetorical modules.
- **Draft**: create semantic content and then reader-facing natural prose.
- **Experiment**: derive experimental obligations from central claims before planning result tables or benchmark sweeps.
- **Revise**: update an existing section while preserving verified claims, the Paper Core, and evidence.
- **Review**: inspect claim strength, evidence coverage, cross-section story consistency, reader effort, repetition, and naturalness.

Do not rerun earlier stages unnecessarily when a usable state already exists.

## Workflow

Read [references/workflow.md](references/workflow.md) for the end-to-end process. The default order is:

1. Ground the research.
2. Construct the paper-level problem and select a framing.
3. Build the Claim Graph under that framing.
4. Extract the Paper Core.
5. Derive experimental obligations from central claims.
6. Select a global narrative.
7. Convert the internal narrative into a Reader Path.
8. Plan section modules.
9. Fill modules semantically.
10. Compose reader-facing discourse across module boundaries.
11. Realize natural academic prose.
12. Review globally and repair only the failing layer.

For runtime-specific behavior, read [references/portability.md](references/portability.md).

## Reader-first principles

Read [references/reader-first-principles.md](references/reader-first-principles.md) when planning or revising prose.

The key rules are:

- the abstract, introduction, method, experiments, and conclusion must describe the same Paper Core at different levels of resolution;
- minimize the conceptual work required from the reader;
- explain why a nontrivial method component is needed before describing what it is or how it works;
- derive experiments from paper claims and competing explanations, not from a desire to accumulate benchmark numbers.

## State model

Use the schemas in `schemas/` as logical representations, not mandatory serialization formats:

- [Research State](schemas/research-state.md)
- [Framing](schemas/framing.md)
- [Claim](schemas/claim.md)
- [Paper Core](schemas/paper-core.md)
- [Reader Path](schemas/reader-path.md)
- [Experimental Obligation](schemas/experimental-obligation.md)
- [Module](schemas/module.md)
- [Paper State](schemas/paper-state.md)

In chat-only environments, keep the state conceptually in conversation context. In repository workflows, it may be persisted if useful. Do not require a state file to perform the workflow.

## Procedure selection

Read only the procedure files needed for the current request:

- [Research grounding](references/procedures/grounding.md)
- [Problem construction and claim framing](references/procedures/framing.md)
- [Paper Core](references/procedures/paper-core.md)
- [Experimental obligations](references/procedures/experimental-obligations.md)
- [Narrative planning](references/procedures/narrative.md)
- [Reader Path](references/procedures/reader-path.md)
- [Module planning](references/procedures/module-planning.md)
- [Semantic writing](references/procedures/semantic-writing.md)
- [Naturalization](references/procedures/naturalization.md)
- [Review](references/procedures/review.md)

## Framing invariant

Do not enlarge an idea by adding rhetorical importance. Enlarge it by identifying the broader setting in which the idea is structurally meaningful.

The default framing path is:

```text
Original Idea
-> Research Setting
-> Structural Change
-> Structural Mismatch
-> Research Problem
-> Method Role
-> Technical Mechanism
```

This path is diagnostic, not mandatory. Skip a node if it cannot be supported. Do not invent a field merely to produce a grander story.

## Paper Core invariant

The Paper Core is the smallest stable statement of what the paper is actually about. It should survive changes in section length, prose style, venue, and local ordering.

A Paper Core normally contains:

- the concrete problem or ambiguity;
- the key distinction or insight;
- the central thesis;
- the conceptual role of the method;
- the technical mechanism at one-line resolution;
- the evidence required to make the thesis credible;
- the claims the paper must not make.

Every major section should instantiate this same core at a different zoom level rather than inventing a new motivation or contribution.

## Reader Path invariant

Internal representations are scaffolding, not prose.

Do not verbalize labels such as "research setting", "structural mismatch", "method role", or "broader implication" merely because they exist internally. Convert them into the shortest reader-facing argument that makes the method necessary.

Prefer:

```text
concrete situation
-> concrete ambiguity or difficulty
-> distinction the reader must notice
-> missing capability in the current training/model
-> required property of a solution
-> proposed method
```

over a paragraph-by-paragraph translation of the internal schema.

## Method explanation invariant

For every nontrivial method component, establish:

```text
WHY -> WHAT -> HOW
```

- **WHY**: what unresolved need requires this component?
- **WHAT**: what conceptual operation does it perform?
- **HOW**: what algorithm, equation, or implementation realizes it?

These are semantic roles, not mandatory headings.

## Experimental obligation invariant

For each central claim, ask:

1. What observation would directly support the claim?
2. What alternative explanation could produce the same headline result?
3. What control, ablation, or matched comparison rules out that explanation?
4. What metric measures the claimed effect most directly?
5. What baseline represents the strongest competing explanation?
6. What result would falsify or materially weaken the claim?

Major experiments should discharge one or more explicit obligations.

## Natural-language constraint

Naturalization is a **semantics-preserving, scaffold-hiding transformation**. It may:

- merge or split sentences and paragraphs;
- reorder local material when the logic remains intact;
- compress several internal nodes into one concrete reader-facing observation;
- replace explicit transitions with implicit causal or contrastive structure;
- remove semantic repetition and unnecessary explanation;
- introduce a concrete example when it clarifies an abstract distinction without adding facts;
- improve reference chains and information flow;
- match an author profile.

It may not:

- add a new research fact or citation;
- strengthen a claim category;
- turn an interpretation into a demonstrated result;
- change numerical results;
- hide an important limitation;
- manufacture consensus in the literature.

Default prose guidance is in [styles/default-academic.md](styles/default-academic.md). If the user supplies their own writing, derive an author profile using [styles/author-profile-template.md](styles/author-profile-template.md) without copying distinctive phrases verbatim.

## Review rule

When review detects a problem, repair the earliest responsible layer:

- factual error -> Research State;
- artificial or inflated problem -> Framing;
- unstable or inconsistent story -> Paper Core;
- overclaim -> Framing or Claim Graph;
- experiment does not test the thesis -> Experimental Obligations;
- weak reveal order -> Narrative;
- high reader effort or exposed scaffolding -> Reader Path;
- missing rhetorical function -> Module Plan;
- missing reason for a method component -> Semantic Draft;
- robotic or assembled prose -> Naturalization.

Do not solve a semantic problem with surface rewriting alone.

## Output behavior

When the user asks for finished prose, return finished prose, not the internal state, unless the state is useful or requested. When the user asks to design or inspect the writing process, expose the relevant intermediate representations.
