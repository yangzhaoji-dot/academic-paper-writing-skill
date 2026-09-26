# H-PAIR Venue Presentation Test

## Scenario

Target venue: **ICML 2027**

Current venue status: **unverified target year**.

At the time of this test, the official ICML 2027 author instructions / style requirements have not been verified. Therefore:

- ICML 2026 may be used only as a provisional planning reference;
- the 2026 eight-page submission limit must **not** be treated as an ICML 2027 requirement;
- anonymity, appendix, supplementary, impact-statement, file-size, and template rules must be refreshed from official ICML 2027 instructions before submission;
- no final LaTeX template should be frozen from the 2026 style.

Latest verified planning reference:

- ICML 2026 Author Instructions:
  https://icml.cc/Conferences/2026/AuthorInstructions

## Provisional planning scenario

To test the presentation pipeline, assume an **8-main-page planning budget** only as a stress-test scenario. This is not a claim about the ICML 2027 rule.

The purpose is to see whether H-PAIR's scientific content can fit a compact ICML-style main paper without hiding decisive evidence in the appendix.

## H-PAIR information hierarchy

### Core information that should remain in the main paper

1. the Harness routing vs route-conditioned execution ambiguity;
2. the H-PAIR nested H/N rollout structure;
3. the three-level credit decomposition;
4. the exact comparison that isolates credit assignment from additional branching compute;
5. Plan A evidence that a non-degenerate USE/SKIP boundary exists;
6. the main H-PAIR performance comparison;
7. direct routing and conditional-execution diagnostics;
8. the key gate-starvation training-dynamics result if the claim remains in the paper.

### Supporting information that may be compressed

- detailed Harness interface syntax;
- extended derivation of behavior correction;
- full branch-budget formula derivations;
- secondary cost sweeps;
- secondary Harness-specific diagnostics.

### Appendix candidates

- complete loss derivations;
- implementation pseudocode details not needed for conceptual understanding;
- full hyperparameter grids;
- extended ALFWorld / WebShop task breakdowns;
- additional cost sweeps;
- prompt templates;
- complete Harness schemas;
- extra training curves;
- per-task / per-seed tables;
- replay and snapshot reconstruction checks.

The appendix must not contain the only evidence for a central claim.

## Provisional 8-page content allocation

This is a planning heuristic, not a venue rule.

| Section | Approx. pages | Role |
|---|---:|---|
| Introduction | 1.0 | expose the credit ambiguity and contribution boundary |
| Related Work | 0.55 | selective tool use + branch credit + Harness RL boundary |
| Problem / Setup | 0.55 | define optional Harness decision and notation |
| H-PAIR Method | 2.0 | paired intervention, decomposition, objective, starvation handling |
| Experiments | 3.45 | Plan A evidence, decisive same-data credit comparison, routing/execution diagnostics, dynamics |
| Conclusion / Limitations | 0.45 | supported lesson and scope |
| **Total** | **8.0** | provisional stress-test budget |

The experiment section receives the largest allocation because H-PAIR's main risk is attribution: the paper must show that any gain comes from the proposed credit decomposition rather than extra branch data or Harness calls.

## Main-paper visual plan

### Figure 1 — Core ambiguity and H-PAIR intervention

Placement: Introduction / early page 2.

Purpose:

- show the same state branching into USE and NO-HARNESS;
- distinguish between-route routing credit from within-route execution credit;
- give the reader the entire paper intuition before equations.

The figure should not be a generic architecture diagram.

### Figure 2 — H-PAIR rollout / credit map

Placement: Method.

Purpose:

- show shared prefix;
- H/N gate;
- repeated conditional suffixes;
- which return comparison trains which token region.

This figure may absorb some prose that would otherwise repeat the decomposition.

### Equation block — Three-level decomposition

Keep the central decomposition in the main paper:

\[
R_{g,k}-B
=
(V_{\mathrm{gate}}-B)
+
(\bar R_g-V_{\mathrm{gate}})
+
(R_{g,k}-\bar R_g).
\]

The main text should interpret the three reference levels immediately.

Longer derivations and behavior-correction algebra can move to appendix if space is tight.

### Table 1 — Decisive same-data credit comparison

The main table should prioritize the causal comparison:

- same branch trajectories;
- same rewards;
- same generated tokens;
- same environment steps;
- same Harness-call budget;
- different credit rule.

Columns should emphasize:

- task success / native score;
- cost-adjusted return;
- invocation regret / calibration;
- conditional execution metric.

Do not overload the main table with every Harness-specific diagnostic.

### Figure 3 — Gate-starvation dynamics

Include only if gate-starvation remains a central paper claim.

Plot, over training:

- Harness selection rate;
- forced-H conditional return;
- valid-call rate or execution competence;
- routing calibration / regret.

If the hypothesis is not empirically supported, remove or demote the claim rather than retaining the figure for completeness.

### Table 2 or Figure 4 — Within-mode execution ablation

Use the same suffix data and compare:

\[
A_{\mathrm{GRPO}}
\quad\text{vs}\quad
A_{\mathrm{GRPO}}+\alpha A_{\mathrm{in}}.
\]

If the result can be communicated clearly in one compact plot, prefer the plot to another dense table.

## Related Work layout

Do not allocate a large catalog-style section.

Organize by three comparison axes:

1. selective external assistance / tool invocation;
2. branch-based or fine-grained agent credit;
3. Harness-specific RL / external-state control.

End the section with the exact H-PAIR boundary:

- routing itself is not new;
- branching itself is not new;
- the candidate contribution is the explicit separation of semantic between-route invocation credit and within-route execution credit at the same Harness decision boundary.

## First-page test

The first page should answer, without requiring Method details:

1. What ambiguity exists in a failed Harness-assisted trajectory?
2. Why does trajectory-level credit not resolve it?
3. What distinction does H-PAIR make?
4. What is the high-level intervention used to measure those credits?

If Figure 1 pushes the actual research problem off the first page, shrink or reposition the figure rather than expanding background prose.

## Overflow repair order

If the paper exceeds the provisional budget:

1. remove repeated explanation between Introduction and Method;
2. compress Related Work by comparison axis;
3. move detailed Harness interface definitions to appendix;
4. move long derivations to appendix;
5. simplify wide tables to direct claim metrics;
6. merge redundant ablations;
7. compress prose.

Do **not**:

- shrink template fonts;
- reduce margins;
- hide the decisive compute-matched baseline;
- move the only routing/execution diagnostic to appendix;
- delete limitations or falsifiers merely to save space.

## Target-year refresh gate

Before final submission formatting:

\`\`\`text
resolve ICML 2027 official author instructions
        ↓
verify:
  page limit
  anonymity
  appendix policy
  supplementary policy
  mandatory statements
  file-size limit
  official LaTeX style
        ↓
replace provisional planning assumptions
        ↓
compile
        ↓
rendered PDF review
\`\`\`

If the ICML 2027 rules differ from 2026, the paper presentation plan must be recomputed rather than patched locally.
