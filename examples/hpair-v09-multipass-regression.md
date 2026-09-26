# H-PAIR v0.9 Multi-Pass Regression Audit

## Purpose

Use the known failures from the v0.6–v0.8 mock papers to test whether the new call-level ownership model catches them at the correct stage.

## Failure 1 — Harness interface omitted

Observed failure: Method discussed credit decomposition before fully defining H/N token semantics and Memory / Plan / Verification behavior.

Correct owner: **Pass 01 — Scientific Audit**.

Why: this is a missing scientific / technical object, not a prose problem.

Expected blocking issue:

\`\`\`yaml
owner_pass: scientific_audit
severity: blocking
problem: method-dependent interface semantics are incomplete
invalidates:
  - formal_method
  - paper_architecture
  - method_writer
\`\`\`

## Failure 2 — Citation metadata is wrong / stale

Correct owner: **Pass 02 — Literature & Citation Audit**.

Expected behavior:

- verify title/authors/year/venue/identifier;
- produce BibTeX;
- distinguish full published method from an estimator adaptation;
- writers consume citation keys only.

The writer must not repair metadata from memory.

## Failure 3 — Contributions are weak / same-level

Correct owner: **Pass 03 — Paper Packaging**.

Expected packaging check:

\`\`\`text
Problem / formulation
+
Method / estimator
+
Evidence / empirical finding (when supported)
\`\`\`

The pass does not force exactly three bullets, but it rejects several bullets that all describe one implementation layer when the paper has a broader problem-level contribution.

## Failure 4 — Standard GRPO update is absent

Observed failure:

- H-PAIR introduced A_pre, A_gate, and A_in;
- the paper never established the complete baseline GRPO clipped update;
- the exact mapping from the new advantage tensor back into the policy update was not central.

Correct ownership:

\`\`\`text
Pass 01 — Scientific Audit
-> marks baseline objective / exact update as required equations

Pass 04 — Formal Method Builder
-> constructs baseline objective
-> exposes baseline credit broadcast
-> defines H-PAIR token/segment advantage
-> writes exact H-PAIR update
\`\`\`

Blocking rule: a new advantage estimator without the actual policy-update equation cannot pass Formal Method.

## Failure 5 — No Preliminaries / Problem Formulation

Correct owner: **Pass 05 — Paper Architecture**.

Inputs:

- Scientific Spec says baseline formulation is required;
- Formal Method contains baseline equations.

Expected outcome: a Preliminaries / Problem Formulation section, or an equivalently clear section location.

Architecture may choose another surface structure, but it cannot leave required baseline objects homeless.

## Failure 6 — Paper compressed to 5 pages too early

Correct owner: **Pass 05 — Paper Architecture**.

Expected rule:

\`\`\`text
place required scientific content first
-> then assign page budget
\`\`\`

The paper must not optimize toward an arbitrary short preview.

## Failure 7 — Core packaging is not visible

Correct owner: **Pass 03 — Paper Packaging**.

Expected frozen bundle:

\`\`\`text
Title direction
One-sentence thesis
Contribution layers
Figure-1 message
Core-equation message
Empirical story
Canonical terminology
\`\`\`

All section writers consume this same bundle.

## Failure 8 — Writer exposes workflow language

Correct owner:

\`\`\`text
Section Writer
-> Authorial Synthesis
\`\`\`

This is not a packaging change unless the underlying thesis is wrong.

## Failure 9 — Writer discovers a missing citation

Correct behavior:

\`\`\`text
Writer
-> issue
-> Pass 02
-> Citation Map update
-> invalidate affected section
-> rerun affected writer
\`\`\`

Incorrect behavior: Writer invents or guesses the citation.

## Failure 10 — Method table floats before Method

Correct owner:

\`\`\`text
Pass 06 — Independent Audit
then Presentation / Typesetting repair
\`\`\`

This is not a reason to rewrite the science.

# Expected H-PAIR Pass 1–5 outputs

Before any new full-paper prose is written, the Frozen Paper Spec should already contain at least:

\`\`\`text
Title direction
One-sentence thesis
Contribution structure

Harness-augmented policy formulation

Standard GRPO objective
trajectory-level advantage broadcast
H-PAIR method delta
A_pre / A_gate / A_in
token/segment advantage assignment
exact H-PAIR clipped update
sampling correction

Invocation regret definition
calibration definition / protocol
cost-adjusted return definition

Verified Citation Map + references.bib

Figure 1 message
Method figure message

Section architecture
main experiment hierarchy
page budget
appendix boundary
\`\`\`

If one of these is absent, the paper should remain blocked before section writing.

# Regression verdict

The new architecture treats the repeated v0.6–v0.8 failures as ownership failures rather than reasons to add more prose rules.

\`\`\`text
missing science -> Scientific Audit / Formal Method
bad citation -> Literature Audit
weak packaging -> Packaging
homeless content / bad page budget -> Architecture
workflow prose -> Writer / Authorial Synthesis
missed defect -> Independent Audit
\`\`\`

This is the intended behavior of v0.9 multi-pass execution.
