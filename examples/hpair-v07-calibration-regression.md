# H-PAIR v0.7 Calibration Regression

## Purpose

Verify that the paper-writing skill now catches not only **missing information**, but also:

- information introduced too early;
- repeated information across prose/table/figure;
- weak visual hierarchy in Experiments;
- preview markers that contaminate the manuscript body;
- venue-like layouts that do not actually use the official template;
- whole-paper density and layout that remain far from nearby real papers.

---

# 1. Introduction Section Calibration

## Must explain now

- an optional Harness creates a routing decision;
- a failed Harness-assisted trajectory is ambiguous between bad routing and bad route-conditioned execution;
- trajectory-level credit does not directly separate those causes;
- H-PAIR uses same-state semantic route comparison plus within-route comparison;
- generic branching and selective Harness use are not claimed as novel.

## Preview only

- paired intervention from the same state;
- repeated conditional suffixes;
- the fact that routing and execution receive different credit signals;
- headline empirical evidence once real results exist.

## Defer to Method

- exact atomic token syntax;
- full Memory / Plan / Verification APIs;
- \(\bar R_g\), \(V_{\mathrm{gate}}\), \(A_{\mathrm{pre}}\), \(A_{\mathrm{gate}}\), \(A_{\mathrm{in}}\);
- behavior correction;
- gate-gradient schedule;
- detailed state restoration.

## Defer to Experiments

- exact compute-matching protocol;
- full baseline matrix;
- detailed calibration/regret metrics;
- cost sweeps.

## Visual obligation

\`\`\`yaml
concept: routing-vs-execution ambiguity
role: let a reader understand the paper problem before equations
best_form: conceptual Figure 1
required_information:
  - same assisted failure
  - bad routing explanation
  - bad execution explanation
  - H-PAIR compares routes and executions separately
\`\`\`

### Regression result

The earlier mock Introduction would be marked **over-resolved** because it explained gate starvation and detailed experiment logic before the core problem had stabilized.

---

# 2. Method Representation Allocation

## Harness suite

Primary carrier:

\`\`\`text
compact table
\`\`\`

The table should carry:

- Harness name;
- persistent/external state;
- actor-facing operation;
- USE semantics;
- NO-HARNESS semantics.

Prose should **not** restate every row.

Prose primary responsibility:

- explain why the three Harnesses span different interaction types;
- explain the candidate-conditioned Verification exception;
- clarify any semantic point the table cannot express safely.

Appendix primary responsibility:

- complete Memory field schema;
- full PLAN_UPDATE serialization;
- verifier prompt/backend;
- environment adapters.

## Gate / token protocol

Primary carrier:

\`\`\`text
short prose + compact token grammar
\`\`\`

The literal tokens

\`\`\`text
<|USE_HARNESS|>
<|NO_HARNESS|>
\`\`\`

should appear once when the binary decision is defined.

After that, the Method should primarily use

\[
g_t\in\{H,N\}.
\]

## Credit decomposition

Primary carrier:

\`\`\`text
central equation
\`\`\`

Prose should interpret the three subtraction terms rather than restating the formula symbol by symbol.

## Full H-PAIR mechanism

Visual obligation:

\`\`\`yaml
concept: end-to-end rollout and credit map
role: reduce prose required to connect tokens, routes, suffix groups, returns, and gradient regions
best_form: two-column Method overview figure
required_information:
  - generated prefix
  - H/N gate token
  - H and N semantic routes
  - repeated suffixes
  - route means
  - A_pre -> prefix
  - A_gate -> gate token
  - A_in -> within-route suffix refinement
  - gate exists every step / branch only selected gate
\`\`\`

### Regression result

A manuscript that contains full prose definitions **and** a full Harness table **and** a figure repeating those same definitions fails the representation-redundancy check.

---

# 3. Experiment Evidence Hierarchy

## Decisive

**Same branch data, different credit assignment.**

Hold fixed:

- restored states;
- branch suffixes;
- rewards;
- generated tokens;
- environment interactions;
- Harness calls.

Change only the credit estimator.

Preferred primary carrier:

\`\`\`text
largest main-results table
\`\`\`

Primary metrics:

- task success / benchmark score;
- cost-adjusted return;
- invocation regret / calibration;
- forced-route conditional execution.

## Supporting

- remove \(A_{\mathrm{gate}}\);
- remove \(A_{\mathrm{in}}\);
- compare suffix \(A_{\mathrm{GRPO}}\) vs \(A_{\mathrm{GRPO}}+\alpha A_{\mathrm{in}}\).

Preferred carrier:

\`\`\`text
secondary ablation table
\`\`\`

## Diagnostic

- Plan A USE/SKIP boundary distribution;
- gate-starvation training dynamics;
- cost sweep;
- Harness-specific call statistics.

Preferred carrier depends on claim:

- distribution plot;
- training curve;
- compact analysis table;
- appendix if not central.

### Regression result

Three small tables with equal visual weight fail calibration because they hide which experiment actually supports the paper's main attribution claim.

---

# 4. Synthetic Preview Mode

\`\`\`yaml
paper_mode: synthetic_preview
presentation_status: preview_only
\`\`\`

Allowed manuscript-level marker:

\`\`\`text
SYNTHETIC RESULTS — WORKFLOW PREVIEW
\`\`\`

Place it on a cover notice or unobtrusive watermark.

Do not:

- color every fabricated number red;
- append a dagger to every cell;
- repeat "synthetic" in every caption;
- insert repeated prose disclaimers inside the manuscript argument.

Maintain fabricated-value metadata outside normal paper prose.

### Regression result

The earlier mock paper fails this check because synthetic markers dominate the visual language of the paper and prevent realistic manuscript evaluation.

---

# 5. Official-Template Gate

A manuscript can be called venue-compliant only if:

\`\`\`text
target venue + year
-> official instructions verified
-> official style/template actually used
-> PDF compiled
-> rendered pages reviewed
\`\`\`

A hand-built

\`\`\`text
article + geometry + twocolumn
\`\`\`

approximation may be useful for layout prototyping, but must be labeled:

\`\`\`yaml
presentation_status: preview_only
\`\`\`

### Regression result

The earlier ICML-like PDF fails venue-compliance even if its margins and columns look similar to ICML.

---

# 6. Final Manuscript Calibration

Use 3–5 real papers with separate roles:

\`\`\`text
scientific references
-> prior-work / novelty / baselines

discourse references
-> section organization and rhetorical moves

manuscript references
-> whole-paper density, visual hierarchy, page allocation
\`\`\`

For H-PAIR, final calibration should compare at least:

## Introduction

- time to the concrete ambiguity;
- amount of broad agent/Harness background;
- how much Method detail appears before the contribution is understood;
- Figure 1 role and size.

## Method

- time to H-PAIR's core paired-credit mechanism;
- number of subsections;
- overview-figure role;
- prose / table / equation balance;
- whether token/Harness definitions are complete but compact.

## Experiments

- prominence and size of the decisive same-data comparison;
- ordering of main effect -> mechanism evidence -> dynamics -> robustness;
- amount of result interpretation versus table narration.

## Rendered PDF

- first-page density;
- Method visual center;
- experiment-table readability;
- float drift;
- dense and sparse pages;
- appendix boundary.

## Repair logic

Do not force H-PAIR to copy one reference paper.

Repair only deviations that plausibly increase reader cost or weaken presentation:

- overfull Introduction;
- repetitive Method;
- visually weak decisive experiment;
- unreadable table;
- experimental float appearing in Method;
- missing overview figure;
- non-official venue template.

---

# 7. v0.7 Regression Verdict

The target manuscript constraints are now:

\`\`\`text
Complete
+
Selective
+
Calibrated
\`\`\`

v0.6 primarily guaranteed **Complete**.

v0.7 adds:

- **Selective** through information resolution and representation allocation;
- **Calibrated** through section-level real-paper comparison and final manuscript calibration.

These checks remain internal to the existing five-phase workflow.
