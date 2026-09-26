---
name: academic-paper-writing
description: Construct, draft, revise, or review academic research papers from research ideas, evidence, experiments, and notes using explicit problem construction, claim framing, narrative planning, rhetorical modules, semantic drafting, natural-language realization, and claim-evidence review. Use for paper introductions, section planning, research framing, contribution positioning, prose naturalization, and full-paper consistency review; do not invent missing research facts or citations.
---

# Academic Paper Writing

Use this skill to turn research content into a paper through explicit intermediate representations rather than a single prose-generation step.

## Core invariant

Separate **what is true** from **how the paper presents it**.

Never introduce a factual result, comparison, citation, method component, dataset property, or literature claim that is not supported by the supplied research material or a source the user explicitly authorizes you to retrieve.

## Operating modes

Infer the narrowest mode that satisfies the request:

- **Ground**: organize ideas, methods, experiments, literature notes, and limitations into a Research State.
- **Frame**: construct the broader research setting, structural change, mismatch, research problem, method role, and defensible claims.
- **Plan**: choose a narrative and map it into section-level rhetorical modules.
- **Draft**: create semantic content and then natural prose.
- **Revise**: update an existing section while preserving verified claims and evidence.
- **Review**: inspect claim strength, evidence coverage, narrative continuity, repetition, and naturalness.

Do not rerun earlier stages unnecessarily when a usable state already exists.

## Workflow

Read [references/workflow.md](references/workflow.md) for the end-to-end process. The default order is:

1. Ground the research.
2. Construct the paper-level problem and select a framing.
3. Build the Claim Graph under that framing.
4. Select a global narrative.
5. Plan section modules.
6. Fill modules semantically.
7. Compose discourse across module boundaries.
8. Realize natural academic prose.
9. Review globally and repair only the failing layer.

For runtime-specific behavior, read [references/portability.md](references/portability.md).

## State model

Use the schemas in `schemas/` as logical representations, not mandatory serialization formats:

- [Research State](schemas/research-state.md)
- [Framing](schemas/framing.md)
- [Claim](schemas/claim.md)
- [Module](schemas/module.md)
- [Paper State](schemas/paper-state.md)

In chat-only environments, keep the state conceptually in conversation context. In repository workflows, it may be persisted if useful. Do not require a state file to perform the workflow.

## Procedure selection

Read only the procedure files needed for the current request:

- [Research grounding](references/procedures/grounding.md)
- [Problem construction and claim framing](references/procedures/framing.md)
- [Narrative planning](references/procedures/narrative.md)
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

A strong paper thesis often emerges from a compact relation such as:

```text
new system structure
-> old training/modeling assumption no longer matches
-> research problem
-> method that restores alignment
```

The skill must distinguish this structural construction from a generic "importance" rewrite.

## Introduction MVP

For an Introduction request, select modules from `modules/introduction/` according to the narrative. Modules specify rhetorical functions, not paragraph boundaries.

Use one of the narrative patterns in `narratives/` when it fits. If none fits, construct a minimal narrative with the same claim-preservation constraints.

## Natural-language constraint

Naturalization is a **semantics-preserving transformation**. It may:

- merge or split sentences and paragraphs;
- reorder local material when the logic remains intact;
- replace explicit transitions with implicit causal or contrastive structure;
- remove semantic repetition;
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
- overclaim -> Framing or Claim Graph;
- weak logic -> Narrative;
- missing function -> Module Plan;
- incomplete argument -> Semantic Draft;
- robotic prose -> Naturalization.

Do not solve a semantic problem with surface rewriting alone.

## Output behavior

When the user asks for finished prose, return finished prose, not the internal state, unless the state is useful or requested. When the user asks to design or inspect the writing process, expose the relevant intermediate representations.
