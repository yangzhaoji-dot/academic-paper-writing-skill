# Execution model

Goal: keep the methodology rich while separating incompatible reasoning jobs across calls.

The skill has many internal representations, but they are **not** a mandatory checklist of serialized artifacts. Use the minimum state needed for the active task.

## Execution mode selection

Use **single-call narrow execution** for local tasks such as:

- rewriting one paragraph;
- fixing wording;
- checking one equation;
- updating one citation;
- revising one already-stable subsection.

Use **multi-pass execution** by default for:

- constructing a paper from a research repository;
- full-paper drafting;
- major restructuring;
- contribution / packaging decisions;
- method formalization;
- submission-ready review.

For multi-pass work, read [multi-pass execution](multi-pass-execution.md) and the pass definitions under `../passes/`.

The five user-facing phases below remain a conceptual interface. They no longer imply that one model call should execute all internal stages.

## Five execution phases

### 1. Understand

Purpose: establish what the research actually is and how it works.

For substantial paper work, this phase is split across:

- **Pass 01 — Scientific Audit**;
- **Pass 02 — Literature & Citation Audit**.

Internally use, as needed:

- Research Source Coverage;
- Research State;
- Technical State.

Exit condition:

- factual substrate is sufficient for the task;
- method-defining sources have been inspected;
- central technical objects and dependencies are available.

### 2. Position

Purpose: decide what the paper is about and where it sits relative to prior work.

For substantial paper work, **Pass 03 — Paper Packaging** owns the title direction, thesis, contribution structure, canonical terminology, and paper-level visual/equation message.

Internally use, as needed:

- Literature Map;
- candidate framing;
- Claim Graph;
- Claim–Literature Matrix;
- Paper Core;
- novelty boundary.

Exit condition:

- one stable Paper Core exists;
- central claims have calibrated scope;
- novelty-dependent statements are supported or explicitly uncertain.

### 3. Design Evidence

Purpose: determine what evidence the claims require.

Experimental Obligations remain the logical evidence layer. Mathematical completeness is separately owned by **Pass 04 — Formal Method Builder**.

Internally use, as needed:

- Experimental Obligations;
- literature-grounded baselines, metrics, and protocols;
- experiment causal controls.

Exit condition:

- each central claim has an empirical test, control, direct metric, and falsifier when applicable.

### 4. Write Sections

Purpose: turn a **Frozen Paper Spec** into reader-facing sections.

Before section writing, **Pass 05 — Paper Architecture** must give required scientific objects, equations, citations, visuals, and page budget a stable home.

Section writers consume the frozen spec. They may propose issues but may not silently redefine the paper.

For each section, internally use only what is needed from:

- Narrative;
- Reader Path;
- Rhetorical Modules;
- Section Contract;
- dependency checks;
- Section Calibration;
- Semantic Draft;
- Authorial Synthesis;
- Discourse References;
- discourse composition;
- naturalization.

Do not serialize all of these by default.

A practical section execution is:

\`\`\`text
Section Planning
-> Section Calibration
-> Semantic Draft
-> Authorial Synthesis
-> Discourse Realization
-> Naturalization
\`\`\`

where **Section Planning** internally resolves:

- what the section must accomplish;
- prerequisite definitions;
- reveal order;
- module/functions;
- what can be inherited or deferred.

**Authorial Synthesis** compresses the internal writing structure before prose realization:

- remove workflow commentary that does not itself carry science;
- merge internal concepts and subsections into reader-meaningful units;
- stabilize a compact canonical vocabulary;
- maintain a concrete anchor when it reduces abstraction cost.

Exit condition:

- Section Contract passes;
- the semantic draft is technically complete;
- internal scaffolds no longer dictate visible section structure;
- terminology is compact and stable;
- prose is reader-facing rather than workflow-facing.

### 5. Present

Purpose: fit the paper to a venue without changing scientific meaning.

Before final presentation, **Pass 06 — Independent Paper Audit** reviews the drafted manuscript from a fresh context. Blocking issues are routed back to the owning upstream pass before final typesetting.

Internally use, as needed:

- Venue Profile;
- Presentation Reference;
- manuscript reference set;
- paper mode (`real` or `synthetic_preview`);
- page allocation;
- evidence visual hierarchy;
- visual/table/equation planning;
- appendix moves;
- official-template gate;
- rendered-PDF review;
- Final Manuscript Calibration.

Exit condition:

- venue constraints are satisfied or the manuscript is explicitly marked `preview_only`;
- technical prerequisites remain reader-visible;
- decisive evidence is visually prominent;
- rendered PDF passes visual review and manuscript calibration.

## Minimal-state principle

Do not create an intermediate representation merely because a schema exists.

Create or persist one only if it:

- prevents information loss;
- supports a later decision;
- is needed for iterative revision;
- helps resolve uncertainty;
- catches a known failure mode.

Examples:

- Technical State is worth persisting for a complex agent method.
- A tiny Introduction rewrite may not need a serialized Claim Graph.
- A Method rewrite may need a Section Contract but not a new global Narrative.
- A venue-only reformat may use existing section prose and Technical State without rebuilding framing.

## Reuse rule

Reuse stable state instead of recomputing it.

Trigger recomputation only when an upstream dependency changes:

- new research fact -> Research / Technical State;
- new closest work -> literature / novelty boundary;
- changed central claim -> Paper Core / obligations;
- changed section purpose -> Section Planning;
- changed venue/year -> presentation planning.

## User-facing behavior

Do not expose internal state unless:

- the user asks to inspect the process;
- a decision depends on choosing among alternatives;
- a failure needs diagnosis;
- the state itself is the requested artifact.

For ordinary drafting, return the requested paper content rather than a dump of intermediate schemas.
