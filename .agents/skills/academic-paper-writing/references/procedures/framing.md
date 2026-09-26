# Procedure: Problem construction and claim framing

Goal: turn a narrow original research idea into a defensible paper-level research problem without changing its factual substrate.

The procedure has two jobs:

1. identify the broader structure that makes the idea meaningful;
2. formalize the resulting thesis as calibrated claims.

## Part I — Construct the research problem

### Step 1: Preserve the original idea

Write the original idea in the narrowest technically accurate form.

Ask:

- What was actually changed, added, compared, learned, or measured?
- Which part is implementation detail and which part changes a decision or learning problem?
- What would remain true if all paper-style language were removed?

Do not begin from the desired contribution statement.

### Step 2: Identify the broader research setting

Ask:

> What broader class of systems, learning problems, or scientific settings makes this idea non-accidental?

A useful research setting should:

- contain the original idea naturally;
- apply to more than one implementation instance when justified;
- not require unsupported claims of universality;
- be definable independently of the proposed method.

Examples of setting types include agents with optional external computation, models with persistent state, adaptive retrieval systems, multi-stage decision policies, or learning systems with human/external feedback.

The setting may already have a standard name. If introducing a new label, define it descriptively and do not imply that the area itself is novel.

### Step 3: Identify the structural change

Compare the simpler or previous structure with the structure present in the selected setting.

Look for concrete changes such as:

- an additional decision variable;
- an additional stage;
- a new routing choice;
- a conditional execution path;
- new external state;
- a new interface or action type;
- a new optimization target;
- heterogeneous token/action roles;
- a new dependency between decisions.

Represent this explicitly:

```text
old structure:
...

new structure:
...
```

### Step 4: Search for a structural mismatch

Ask whether the modeling, training, supervision, optimization, representation, or evaluation procedure still treats the system as if the old structure were sufficient.

Common patterns:

```text
policy structure != credit structure
system structure != optimization structure
decision structure != supervision structure
architecture != training objective
capability structure != interface
state structure != representation
```

A mismatch is useful only if both sides can be stated concretely.

Reject vague forms such as:

- "existing methods are limited";
- "current approaches fail to fully exploit X";
- "the problem is challenging";
- "there is a semantic gap" without specifying the two structures.

Do not force a mismatch. If no real structural mismatch exists, use another framing type.

### Step 5: Define the research problem

Convert the mismatch into a question or optimization problem.

A good research problem names:

- the object being learned or estimated;
- the distinction or dependency that matters;
- the setting in which it matters.

Prefer:

> How should credit be assigned between routing and route-conditioned execution in agents with optional external support?

over:

> How can we improve agent performance with a better branching algorithm?

The first defines the scientific problem; the second prematurely collapses the problem into one mechanism.

### Step 6: Reposition the method

Now state what role the proposed method plays relative to the research problem.

Separate:

- **method role** — what the method estimates, aligns, decomposes, controls, or enables;
- **technical mechanism** — the concrete algorithmic device used to perform that role.

Example pattern:

```text
Research problem:
separate two sources of credit

Method role:
construct distinct learning signals for them

Technical mechanism:
paired interventions + conditional samples
```

Do not let the mechanism become the paper's reason for existing unless the mechanism itself is the research object.

### Step 7: Derive the paper thesis

Compress the framing into one relation that could organize the paper.

Examples of thesis forms:

```text
new decision structure -> training signal should respect that structure
new external state -> optimization must account for state access/update decisions
new conditional route -> supervision should separate routing from execution
```

The thesis should be broader than the implementation but narrower than an unsupported universal principle.

## Part II — Build calibrated claims

Use these categories:

1. **demonstrated** — directly supported by reported experiment, theorem, measurement, or implementation fact.
2. **supported-interpretation** — an interpretation reasonably supported by the demonstrated evidence and argument.
3. **broader-implication** — a general lesson or conceptual extension suggested by the work but not directly demonstrated at full scope.
4. **speculative** — a hypothesis or future possibility. Do not present as a contribution or conclusion without explicit qualification.

Claims should cover, when supported:

- the selected research setting;
- the structural change;
- the mismatch;
- the research problem;
- the method role;
- the technical mechanism;
- empirical consequences or hypotheses;
- broader implications.

## Candidate alternatives

Generate only a small number of genuinely different framings. Useful alternatives may emphasize:

- the broader research setting;
- the structural mismatch;
- the learning/estimation problem;
- an empirical discovery;
- a general principle;
- a systems or capability contribution.

Do not generate cosmetic variants that differ only in wording.

## Selection

Prefer a framing that satisfies all four:

- it exposes the real novelty;
- the setting and structural change are factual or conservatively defined;
- the mismatch is concrete rather than rhetorical;
- it yields a coherent method and experimental story.

Reject a framing if its significance depends mainly on unsupported universality, invented consensus, or relabeling the technical mechanism as a larger field-level problem.
