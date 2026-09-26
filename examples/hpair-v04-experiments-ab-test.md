# H-PAIR Experiments Writing: v0.3 vs v0.4 Controlled A/B Test

## Test purpose

Test whether literature-grounded discourse composition improves the **Experiments section design and exposition**.

H-PAIR has no training result yet. This test therefore does **not** fabricate results. It compares two ways of presenting the same planned evidence:

- Version A: conventional setup / main comparison / ablation organization.
- Version B: claim-driven organization derived from the Paper Core and Experimental Obligations.

## Controlled scientific content

Both versions preserve the same experimental facts and plans.

### Current status

- H-PAIR is not implemented or empirically validated yet.
- Plan A precedes RL training.
- ALFWorld is the first diagnostic environment.
- WebShop is secondary and should be added after the ALFWorld pipeline is stable.
- Plan A uses a fixed strong actor with no training.
- Memory, Plan, and Verification are the three Harness families.
- Matched USE/SKIP interventions should reconstruct the same state.
- Raw return and cost-adjusted utility should both be reported.
- H-PAIR training must be compared under matched generated tokens, environment steps, and Harness calls.
- The first repeated-execution setting is N=4, B_nodes=1, K_H=K_N=2.

### Central claims that later experiments must test

C1. A meaningful Harness-learning problem requires a non-degenerate state-dependent USE/SKIP boundary.

C2. H-PAIR's candidate contribution is the separation of Harness-routing credit and route-conditioned execution credit, not branching itself.

C3. Any gain over trajectory-level GRPO must not be explained only by additional suffix samples, environment interactions, or Harness calls.

C4. Within-mode execution refinement should improve conditional execution beyond what is learned by the trajectory-level suffix signal alone.

C5. Gate starvation is a plausible training failure mode: poor early Harness execution may make the routing policy suppress Harness use before the route becomes competent.

No positive result is assumed for any claim.

---

# Version A — v0.3 conventional experiment organization

## Experimental setup

We evaluate H-PAIR on ALFWorld as the primary environment and use WebShop as a secondary transfer environment. We consider three Harnesses: Memory, Plan, and Verification. Memory provides a bounded read-only external observation state, Plan provides a persistent actor-authored task plan and active subgoal, and Verification evaluates a fixed candidate action before execution.

We first conduct a strong-model validation stage without policy training. The actor checkpoint, decoding configuration, task subset, and random seeds are fixed across all conditions. We compare a Base condition against Memory, Plan, Verification, and All-Harness variants. We additionally construct paired USE/SKIP interventions from identical reconstructed states and measure terminal return under both routes.

For H-PAIR training, all methods are compared under matched generated tokens, environment steps, and Harness calls. The initial setting uses N=4 global rollouts, one selected branch node, and two conditional suffixes per routing mode. Baselines include trajectory-level GRPO and generic branch-based credit estimators implemented on the same rollout data.

## Main comparison

The main experiment compares H-PAIR against trajectory-level GRPO and branch-based alternatives on task success, benchmark-native score, and cost-adjusted return. We also report Harness-use frequency, invocation regret, decision calibration, valid-call rate, and conditional execution success.

The comparison is designed to determine whether H-PAIR improves end-to-end performance while learning more accurate Harness-use decisions. Results should be reported for each Harness type and for the combined Harness setting.

## Paired-intervention analysis

We estimate the Harness uplift at a state as

\[
\Delta_h(s)=\bar R_H(s)-\bar R_N(s).
\]

We report the mean and median uplift, its distribution, and the fraction of states with positive and negative values. This analysis measures whether USE and SKIP are both preferable in different states and whether the fixed strong actor chooses the better route.

## Ablations

We perform the following ablations:

1. remove the within-mode residual \(A_{\mathrm{in}}\);
2. replace H-PAIR gate credit with trajectory-wide GRPO credit;
3. disable execution warm-up;
4. remove minimum forced-H exploration;
5. use fixed branch allocation instead of competence-adaptive allocation;
6. vary \(K_H\) and \(K_N\);
7. vary Harness cost \(\lambda_h\).

These ablations evaluate the contribution of the major H-PAIR components.

## Efficiency and robustness

We report generated tokens, environment interactions, Harness calls, actor tokens, Harness/backend tokens, and wall-clock latency. We additionally evaluate transfer across Harness type and, when available, from ALFWorld to WebShop.

---

# Version B — v0.4 claim-driven experiment organization

The experiments should answer a sequence of questions implied by the H-PAIR thesis. End-to-end performance is necessary, but it is not sufficient: a higher task score alone cannot tell us whether Harness routing improved, whether conditional execution improved, or whether the method simply used more branch data.

## Q1. Is there a Harness-use decision worth learning?

Before training H-PAIR, we test whether the proposed setting contains a non-degenerate routing boundary.

For a fixed strong actor, we restore the same ALFWorld state and compare USE against SKIP. For Memory and Plan, the branch point is the pre-operation state; for Verification, both routes share the same proposed candidate action and differ only in whether that candidate is verified before execution. Each branch is completed to termination, producing

\[
\Delta_h(s)=\bar R_H(s)-\bar R_N(s).
\]

The primary object here is the **distribution** of \(\Delta_h(s)\), not an aggregate benchmark gain. H-PAIR is only well-motivated if both signs occur at non-negligible rates: states where external assistance helps and states where its cost or downstream effect makes direct execution preferable.

We therefore report:

- raw task-return uplift;
- cost-adjusted uplift across a sweep of Harness costs;
- fractions of positive- and negative-\(\Delta\) states;
- confidence intervals;
- invocation regret of the fixed actor relative to the paired estimate.

This experiment can falsify the need for learned routing. If one route dominates almost everywhere, an always-use or always-skip policy is the more appropriate solution.

## Q2. Does H-PAIR help because of its credit decomposition, rather than because it branches?

The central algorithmic comparison must hold the rollout data fixed.

For the same restored states, branch trajectories, terminal rewards, and total interaction budget, we apply different credit rules to the **same branch data**:

1. trajectory-wide GRPO;
2. a generic sibling / branch advantage;
3. a shared-prefix versus suffix branch objective;
4. H-PAIR's prefix / gate / within-mode decomposition.

This is the decisive comparison for the paper's novelty boundary. The independent variable is the credit assignment rule, not the number of continuations.

The primary measurements should reflect the claimed decomposition:

- task success / native task score;
- cost-adjusted return;
- invocation regret;
- calibration of USE probability against paired \(\Delta_h(s)\);
- conditional execution quality under forced H and forced N.

A positive task-score result without better routing or execution diagnostics would not by itself support the proposed explanation.

## Q3. Is between-mode credit actually learning routing?

To isolate the gate term, keep the paired rollout structure fixed and change only the credit assigned to the H/N decision token.

Compare:

- no direct gate task gradient;
- trajectory-wide GRPO advantage on the gate;
- H-PAIR between-mode gate advantage.

Evaluate the decision on held-out paired states using invocation regret and calibration, rather than only end-to-end success.

This experiment tests the narrow claim that mean return differences between semantic routes are useful supervision for the invocation decision.

A result would weaken the claim if H-PAIR improves total reward but the gate remains no better calibrated than generic trajectory credit.

## Q4. Does within-mode sampling improve execution, or merely add samples?

The within-mode residual is intended to refine execution *conditional on a fixed route*. To test that claim, use the same H/N branches and the same suffix samples, then remove only \(A_{\mathrm{in}}\):

\[
A_{\mathrm{suffix}}=A_{\mathrm{GRPO}}
\]

versus

\[
A_{\mathrm{suffix}}
=
A_{\mathrm{GRPO}}
+
\alpha A_{\mathrm{in}}.
\]

The relevant metric is not only global success. Evaluate forced-H and forced-N continuations separately, including:

- valid Harness-call rate;
- success / progress conditional on H;
- success / progress conditional on N;
- execution variance within each mode where meaningful.

Because both conditions see the same number of suffixes, any difference is less easily attributed to additional rollout compute.

If \(K_g=1\), \(A_{\mathrm{in}}\) is identically zero; this setting provides a useful edge-case control showing that repeated within-mode samples are needed specifically for execution contrast, not for ordinary task credit.

## Q5. Does routing suppress a useful Harness before execution becomes competent?

H-PAIR includes execution warm-up because routing and route execution can form a feedback loop: early bad Harness continuations may train the gate to stop selecting the route, reducing the data available to improve that route.

This claim should be tested as a **training-dynamics experiment**, not only as a final-score ablation.

Compare:

- immediate gate training from step 0;
- gate-gradient warm-up without forced-H floor;
- warm-up plus minimum forced-H exploration.

Track over training:

- Harness selection rate;
- forced-H conditional return;
- valid-call rate;
- gate calibration;
- end-to-end return.

The starvation hypothesis is supported only if route usage falls before route competence has stabilized and the staged schedule changes that dynamic. If immediate gate training performs equally well and preserves Harness data, the extra schedule is unnecessary.

## Q6. Are the gains robust to cost and Harness semantics?

The H/N boundary depends on the value and cost of assistance. After the mechanism is established on one Harness, we vary:

- Harness cost \(\lambda_h\);
- Memory, Plan, and Verification;
- ALFWorld and, after pipeline stabilization, WebShop.

The important question is not whether one fixed call prior transfers unchanged. It is whether the learned routing behavior tracks the change in paired route value as cost or Harness semantics change.

Report raw return alongside cost-adjusted return so that a favorable choice of \(\lambda_h\) cannot manufacture the appearance of a balanced routing problem.

## Experimental ordering

The paper should reveal experiments in the same dependency order as the claims:

\`\`\`text
Q1 boundary exists
    ↓
Q2 decomposition vs generic branching
    ↓
Q3 routing term
    +
Q4 execution term
    ↓
Q5 training dynamics / starvation
    ↓
Q6 cost and Harness robustness
\`\`\`

This order prevents the main benchmark table from carrying more explanatory burden than it can support.

---

# Discourse references used for Version B

No source prose is copied. We abstract only experiment-organization patterns.

## BPO

Transferable patterns:

- match return / rollout budget when the method changes rollout topology;
- use the main table for end-to-end performance, then use direct mechanism metrics such as gradient variance and convergence efficiency to test the proposed explanation;
- vary branch width, branch count, and scheduling under a fixed budget to separate allocation effects from extra compute;
- connect ablations to specific design claims rather than listing components mechanically.

Abstract pattern:

\`\`\`text
headline effect
-> direct mechanism measurement
-> compute-matched control
-> design-variable ablation
-> efficiency / overhead
\`\`\`

## BranPO

Transferable patterns:

- compare against several baseline families, not only the easiest trajectory-level baseline;
- separate main in-domain results from transfer to a broader real-world search setting;
- use component ablations to connect sampling and masking mechanisms to their intended effects;
- inspect training behavior such as unnecessary search-step growth when a component is specifically intended to suppress that behavior.

Abstract pattern:

\`\`\`text
main task effect
-> stronger baseline families
-> component-specific behavior
-> cross-setting generalization
\`\`\`

## ContextPilot

Transferable positive pattern:

- distinguish tool-design gains from RL-training gains;
- use component ablations to separate exploration from credit assignment.

Important negative lesson:

- if different ablation rows receive different numbers of branch/snapshot samples, a gain cannot be cleanly attributed to the credit mechanism.

For H-PAIR this means **same branch data, different credit assignment** should be a first-class experiment rather than a secondary ablation.

---

# Evaluation

| Criterion | Version A | Version B | Observation |
|---|---:|---:|---|
| Connection from Paper Core to experiments | 3/5 | 5/5 | B gives each central claim a dedicated empirical question. |
| Ability to isolate the proposed mechanism | 3/5 | 5/5 | B makes same-data/different-credit the decisive comparison. |
| Alternative explanations controlled | 3/5 | 5/5 | B explicitly treats extra suffixes, calls, and interactions as confounds. |
| Direct metrics for routing/execution | 4/5 | 5/5 | A lists them; B explains which claim each metric tests. |
| Falsifiability | 2/5 | 5/5 | B states outcomes that would make learned routing or specific components unnecessary. |
| Ablation quality | 3/5 | 5/5 | A is a component checklist; B changes one causal factor at a time under fixed data. |
| Reader understanding of why each experiment exists | 3/5 | 5/5 | B begins each subsection with the empirical question. |
| Risk of table-driven storytelling | 4/5 | 2/5 | Lower is better; B does not require the headline table to prove the mechanism. |
| Compatibility with future real results | 5/5 | 5/5 | Both can accept results later without changing the scientific questions. |

These are author-side diagnostic scores, not blinded human evaluation.

# Main finding

The Experiments test shows a third distinct benefit of discourse grounding.

- Introduction: improve **reveal order**.
- Method: improve **equation motivation**.
- Experiments: improve **evidence-to-claim alignment**.

The key change is from:

\`\`\`text
setup
-> main table
-> ablations
-> efficiency
\`\`\`

to:

\`\`\`text
claim
-> empirical question
-> alternative explanation
-> isolating comparison
-> direct metric
-> falsifying outcome
\`\`\`

The conventional section labels may still be used in the final paper, but they should not determine the scientific logic.

# Skill implication

Experimental Obligations should remain the author-side source of truth. Discourse composition should convert them into a compact sequence of reader-visible empirical questions.

For each major experiment subsection, the semantic state should contain:

\`\`\`text
claim being tested
empirical question
competing explanation
controlled variable
independent variable
direct metric
secondary metric
what result supports the claim
what result weakens / falsifies it
\`\`\`

Do not require all of these fields to appear verbatim in prose. They are an internal causal-design check.

Ablations should preferentially implement **single-factor interventions**. For methods that alter sampling or rollout topology, compute / interaction matching is part of the causal control, not merely an efficiency appendix.
