---
name: academic-paper-writing
description: Construct, draft, revise, typeset, or review academic research papers from research ideas, repositories, evidence, experiments, notes, verified literature, and venue requirements. For substantial full-paper work, use multi-pass orchestration with separate Scientific Audit, Literature & Citation Audit, Paper Packaging, Formal Method, Paper Architecture, section-writing, and Independent Audit calls connected by frozen Scientific Spec, Citation Map, and Paper Spec handoffs. For narrow edits, use the smallest relevant procedure directly. Use for paper introductions, section planning, research framing, contribution positioning, literature-grounded novelty checks, prose naturalization, experiment-story alignment, and full-paper consistency review; do not invent missing research facts or citations.
---

# Academic Paper Writing

Use this skill to turn research content into a paper through explicit intermediate representations rather than a single prose-generation step.

## Core invariant

Separate **what is true**, **what the paper is about**, and **how the reader encounters it**.

Never introduce a factual result, comparison, citation, method component, dataset property, or literature claim that is not supported by the supplied research material or a source the user explicitly authorizes you to retrieve.

## Operating modes

Infer the narrowest mode that satisfies the request:

- **Ground**: inventory research sources, organize factual research content into a Research State, and preserve method-defining operational semantics in a parallel Technical State.
- **Frame**: construct the broader research setting, structural change, mismatch, research problem, method role, and defensible claims.
- **Core**: compress the selected framing and claims into one stable Paper Core that every major section must express at an appropriate level of detail.
- **Plan**: choose a narrative, derive the shortest Reader Path, and map it into section-level rhetorical modules.
- **Draft**: create semantic content and then reader-facing natural prose.
- **Experiment**: derive experimental obligations from central claims before planning result tables or benchmark sweeps.
- **Revise**: update an existing section while preserving verified claims, the Paper Core, and evidence.
- **Present**: resolve the target conference/year, allocate page budget, plan figures/tables/equations/appendix content, realize the official template, and review the rendered PDF.
- **Review**: inspect claim strength, evidence coverage, cross-section story consistency, reader effort, repetition, venue compliance, presentation quality, and naturalness.

Do not rerun earlier stages unnecessarily when a usable state already exists.

Literature is a cross-cutting constraint rather than a late standalone stage. When retrieval is available and the task depends on external positioning, use literature at three checkpoints: challenge the framing, constrain claim/novelty boundaries, and ground experiment conventions. Real papers may also provide discourse references for writing, but discourse evidence must remain separate from scientific evidence.

## Workflow

Use [the execution model](references/execution.md).

For substantial paper construction, restructuring, formalization, or submission-ready review, use [multi-pass execution](references/multi-pass-execution.md) and the pass definitions in [passes/README.md](passes/README.md). Do not collapse scientific audit, literature verification, packaging, formal method construction, writing, and independent review into one call.

For narrow edits, use the smallest relevant procedure directly.

The user-facing workflow remains:

1. **Understand** — ground Research State and Technical State from complete source coverage.
2. **Position** — use literature, framing, claims, and novelty checks to stabilize the Paper Core.
3. **Design Evidence** — derive claim-driven experimental obligations and ground their operationalization in literature.
4. **Write Sections** — plan each section, satisfy technical prerequisites, calibrate information resolution and representation responsibilities, draft semantically, synthesize the internal structure into an author-shaped exposition, and realize reader-facing discourse.
5. **Present** — resolve venue/year, use the official template when available, allocate evidence/visual hierarchy, typeset, review the rendered PDF, and calibrate the final manuscript against nearby real papers.

The detailed end-to-end methodology remains in [references/workflow.md](references/workflow.md). In multi-pass mode, persist the three key handoffs:

- [Scientific Spec](schemas/scientific-spec.md);
- [Citation Map](schemas/citation-map.md);
- [Frozen Paper Spec](schemas/paper-spec.md).

Downstream calls may raise issues against frozen upstream state but may not silently rewrite it.

For runtime-specific behavior, read [references/portability.md](references/portability.md).

## Reader-first principles

Read [references/reader-first-principles.md](references/reader-first-principles.md) when planning or revising prose.

The key rules are:

- the abstract, introduction, method, experiments, and conclusion must describe the same Paper Core at different levels of resolution;
- minimize the conceptual work required from the reader;
- explain why a nontrivial method component is needed before describing what it is or how it works;
- derive experiments from paper claims and competing explanations, not from a desire to accumulate benchmark numbers.

## Execution principle

Do not materialize every schema on every run. Framing, Claim Graph, Reader Path, modules, Experimental Obligations, Discourse References, and presentation objects are internal tools that should be created only when they prevent information loss or support a concrete decision.

The stable high-value states are usually:

- Research State;
- Technical State;
- Literature state when external positioning matters;
- Paper Core;
- Section Contracts for technically dense sections;
- Paper / Presentation state for iterative full-paper work.

Reuse stable state and recompute only when an upstream dependency changes.

## State model

Use the schemas in `schemas/` as logical representations, not mandatory serialization formats:

- [Scientific Spec](schemas/scientific-spec.md)
- [Citation Map](schemas/citation-map.md)
- [Frozen Paper Spec](schemas/paper-spec.md)
- [Research State](schemas/research-state.md)
- [Technical State](schemas/technical-state.md)
- [Section Contract](schemas/section-contract.md)
- [Framing](schemas/framing.md)
- [Claim](schemas/claim.md)
- [Paper Core](schemas/paper-core.md)
- [Reader Path](schemas/reader-path.md)
- [Experimental Obligation](schemas/experimental-obligation.md)
- [Literature Map](schemas/literature-map.md)
- [Discourse Reference](schemas/discourse-reference.md)
- [Venue Profile](schemas/venue-profile.md)
- [Presentation Reference](schemas/presentation-reference.md)
- [Module](schemas/module.md)
- [Paper State](schemas/paper-state.md)

In chat-only environments, keep the state conceptually in conversation context. In repository workflows, it may be persisted if useful. Do not require a state file to perform the workflow.

## Multi-pass selection

For substantial work, use:

- [Pass 01 — Scientific Audit](passes/01-scientific-audit.md)
- [Pass 02 — Literature & Citation Audit](passes/02-literature-citation-audit.md)
- [Pass 03 — Paper Packaging](passes/03-paper-packaging.md)
- [Pass 04 — Formal Method Builder](passes/04-formal-method.md)
- [Pass 05 — Paper Architecture](passes/05-paper-architecture.md)
- [Section Writer calls](passes/section-writer.md) consuming the Frozen Paper Spec;
- [Pass 06 — Independent Paper Audit](passes/06-independent-audit.md)

Passes own decisions. Writers own prose. Reviewers own issues.

## Procedure selection

Read only the procedure files needed for the current request:

- [Research grounding](references/procedures/grounding.md)
- [Technical grounding](references/procedures/technical-grounding.md)
- [Section Contract and prerequisite check](references/procedures/section-contract.md)
- [Section calibration](references/procedures/section-calibration.md)
- [Authorial synthesis](references/procedures/authorial-synthesis.md)
- [Final manuscript calibration](references/procedures/manuscript-calibration.md)
- [Problem construction and claim framing](references/procedures/framing.md)
- [Paper Core](references/procedures/paper-core.md)
- [Experimental obligations](references/procedures/experimental-obligations.md)
- [Literature grounding](references/procedures/literature-grounding.md)
- [Discourse grounding](references/procedures/discourse-grounding.md)
- [Venue-aware presentation](references/procedures/venue-presentation.md)
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

## Technical completeness invariant

The Paper Core is intentionally compressed and must not be used as the sole source for Method or presentation planning.

Maintain a parallel Technical State for method-defining semantics such as:

- decision and action spaces;
- special-token or structured-action representations;
- interface and state semantics;
- transition rules;
- loss masks and gradient regions;
- sampling / branching semantics;
- protocol exceptions;
- dependencies among technical objects.

Before drafting any section, create a Section Contract that specifies what the reader must understand and which prerequisites must be defined before downstream equations, algorithms, or results appear.

A section may not proceed to discourse composition while required technical prerequisites are missing.

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

Naturalization is a **semantics-preserving, scaffold-hiding transformation**. When verified real-paper references are available, first abstract their section-specific discourse behavior using [Discourse grounding](references/procedures/discourse-grounding.md). Use those abstractions as positive communication priors; never closely paraphrase or imitate one source.

It may:

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

- missing research source or incomplete method definition -> Research Source Coverage / Technical State;
- factual error -> Research State;
- unsupported literature statement, novelty claim, or baseline convention -> Literature Map;
- artificial or inflated problem -> Framing;
- unstable or inconsistent story -> Paper Core;
- overclaim -> Framing or Claim Graph;
- experiment does not test the thesis -> Experimental Obligations;
- weak reveal order -> Narrative;
- high reader effort or exposed scaffolding -> Reader Path;
- missing rhetorical function -> Module Plan;
- missing definition, interface, action semantics, or prerequisite -> Technical State / Section Contract;
- missing reason for a method component -> Semantic Draft;
- overfull / under-resolved section -> Section Calibration;
- redundant prose/table/figure explanation -> Representation Allocation;
- workflow leakage, concept fragmentation, terminology overload, or missing concrete anchor -> Authorial Synthesis;
- robotic or assembled prose after synthesis -> Discourse Reference / Naturalization;
- venue violation, poor page allocation, unreadable visual, or rendered-layout defect -> Venue Profile / Presentation Plan / Typesetting;
- whole-paper density, hierarchy, or page-distribution mismatch -> Final Manuscript Calibration.

Do not solve a semantic problem with surface rewriting alone.

## Output behavior

When the user asks for finished prose, return finished prose, not the internal state, unless the state is useful or requested. When the user asks to design or inspect the writing process, expose the relevant intermediate representations.
