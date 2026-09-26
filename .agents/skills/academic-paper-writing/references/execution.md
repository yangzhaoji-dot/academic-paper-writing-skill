# Execution model

Goal: keep the methodology rich while making execution lightweight.

The skill has many internal representations, but they are **not** a mandatory checklist of serialized artifacts. Use the minimum internal state needed for the active task.

## Five execution phases

### 1. Understand

Purpose: establish what the research actually is and how it works.

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

Internally use, as needed:

- Experimental Obligations;
- literature-grounded baselines, metrics, and protocols;
- experiment causal controls.

Exit condition:

- each central claim has an empirical test, control, direct metric, and falsifier when applicable.

### 4. Write Sections

Purpose: turn the stable scientific state into reader-facing sections.

For each section, internally use only what is needed from:

- Narrative;
- Reader Path;
- Rhetorical Modules;
- Section Contract;
- dependency checks;
- Semantic Draft;
- Discourse References;
- discourse composition;
- naturalization.

Do not serialize all of these by default.

A practical section execution is:

\`\`\`text
Section Planning
-> Semantic Draft
-> Discourse Realization
\`\`\`

where **Section Planning** internally resolves:

- what the section must accomplish;
- prerequisite definitions;
- reveal order;
- module/functions;
- what can be inherited or deferred.

Exit condition:

- Section Contract passes;
- prose is technically complete and reader-facing.

### 5. Present

Purpose: fit the paper to a venue without changing scientific meaning.

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
