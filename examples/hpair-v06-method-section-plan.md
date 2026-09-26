# H-PAIR v0.6 Method Section Planning Regression

## Test target

Input only the stable paper-level state:

- H-PAIR Paper Core;
- H-PAIR Technical State;
- current novelty boundary;
- Method section role.

Do **not** expose Narrative, Reader Path, module list, dependency graph, and Section Contract as separate runtime artifacts unless needed for diagnosis.

The output should be one usable Method section plan whose ordering already satisfies those internal constraints.

---

# Stable Paper Core

H-PAIR studies a specific ambiguity in Harness-augmented agent RL: a low-return assisted trajectory does not reveal whether the agent should have avoided the Harness or whether the Harness route was appropriate but poorly executed.

The method uses paired interventions from the same decision state and repeated continuations within each semantic route to construct separate learning signals for:

1. shared task reasoning;
2. Harness invocation;
3. execution conditional on the chosen route.

Snapshot/restore, branching, selective Harness use, and generic segmented credit are treated as prior techniques rather than the paper's novelty.

---

# Method Section Plan

## 3. H-PAIR

### 3.1 Harness-Augmented Decision Process

**Reader question:** What exactly is the policy deciding before any branching or credit assignment is introduced?

Introduce a policy-controlled action boundary. At every such boundary the actor emits exactly one atomic routing token:

\[
g_t\in\{H,N\},
\]

represented by single tokenizer IDs

\`\`\`text
<|USE_HARNESS|>
<|NO_HARNESS|>
\`\`\`

The two tokens are mutually exclusive and exhaustive.

Then show the two generic routes at conceptual resolution:

\`\`\`text
Harness route:
reasoning
-> <|USE_HARNESS|>
-> Harness operation
-> Harness observation
-> actor continuation

Direct route:
reasoning
-> <|NO_HARNESS|>
-> environment action
-> environment feedback
-> actor continuation
\`\`\`

Clarify optimization semantics here, before any loss equations:

- model-generated policy tokens participate in policy optimization;
- Harness observations and environment feedback are context only and are masked from policy-gradient loss.

Make the first essential distinction:

> **The gate exists at every policy-controlled action boundary; counterfactual branching is performed only at a budgeted subset of those already-existing gates.**

This prevents readers from interpreting branch selection as the mechanism that creates the Harness decision.

---

### 3.2 Harness Interfaces

**Reader question:** What does choosing \(H\) actually mean?

Define the three Harnesses before using \(g=H\) as a common mathematical route.

A compact main-paper table can carry the shared structure:

| Harness | External state / computation | Actor API | USE | NO-HARNESS |
|---|---|---|---|---|
| Memory | auto-updated observed-state memory | \`READ_MEMORY()\` | read bounded external memory, then continue | continue without memory access |
| Plan | persistent \`GLOBAL_PLAN\` + \`ACTIVE_SUBGOAL\` | \`PLAN_UPDATE(...)\` | mutate external plan state, then continue | preserve current plan and act directly |
| Verification | candidate-conditioned checking | \`VERIFY(candidate)\` | check fixed candidate, observe feedback, then keep/revise | commit the same candidate directly |

#### Memory

Only the semantics needed for the estimator remain in the main paper:

- memory contains previously observed facts;
- it is updated deterministically by the environment adapter;
- the actor selectively reads but does not write it in V0;
- hidden simulator state, next-action recommendations, and benchmark labels are excluded.

The routing question is:

> Is reading external memory worth its cost at this state?

Full memory field schemas move to appendix.

#### Plan

Define the persistent fields:

\`\`\`text
GLOBAL_PLAN
ACTIVE_SUBGOAL
\`\`\`

The actor authors the content; the Harness stores it.

The current V0 begins gated RL with an initial high-level plan already present. Therefore H-PAIR initially learns **when to revise the plan**, not whether planning should exist at all.

The routing question is:

> Is revising the external plan worth its cost now?

Full serialization details move to appendix.

#### Verification

Treat this as an explicit protocol exception instead of forcing it into the generic pre-action gate.

The actor first proposes a fixed candidate \(\tilde a_t\):

\[
s_t\rightarrow \tilde a_t \rightarrow
\begin{cases}
H:\operatorname{VERIFY}(\tilde a_t)\rightarrow \text{feedback}\rightarrow a_t,\\
N:a_t=\tilde a_t.
\end{cases}
\]

Both branches share the same state and the same candidate action.

The routing question is:

> Is checking this candidate worth its cost before commitment?

This exception must remain reader-visible because it changes the counterfactual intervention being estimated.

---

### 3.3 Paired Interventions at Existing Gates

**Reader question:** Once the Harness decision is defined, how do we obtain a routing comparison?

Generate \(N\) ordinary global trajectories. Record the old-policy H/N probabilities at every gate:

\[
p_{t,H}^{\mathrm{old}},\qquad p_{t,N}^{\mathrm{old}}.
\]

Under the initial branch budget, select one low-margin gate

\[
t^\star=\arg\min_t
\left|
\log p_{t,H}^{\mathrm{old}}
-
\log p_{t,N}^{\mathrm{old}}
\right|.
\]

Restore the exact pre-decision state, including:

- generated prefix;
- environment state;
- Harness state;
- remaining Harness / tool budget;
- controllable exogenous randomness where required.

Then force both semantic routes:

\[
g\in\{H,N\},
\]

and sample \(K_H\) and \(K_N\) conditional continuations.

For Verification, the restored object additionally includes the fixed candidate action.

Explain the initial budget only after the sampling structure is clear:

\[
N=4,\qquad B_{\mathrm{nodes}}=1,\qquad K_H=K_N=2.
\]

A figure should visualize:

\`\`\`text
shared prefix
      |
      gate
     /    \
    H      N
   / \    / \
 H1  H2  N1  N2
\`\`\`

with token regions annotated for later credit assignment.

---

### 3.4 From Paired Returns to Three Reference Levels

**Reader question:** What information do these nested samples give that one trajectory return does not?

For each route, define its sampled mean:

\[
\bar R_g
=
\frac{1}{K_g}
\sum_{k=1}^{K_g}
R_{g,k}.
\]

Interpret it immediately:

- \(\bar R_H-\bar R_N\) compares semantic routes at the same state;
- \(R_{g,k}-\bar R_g\) compares executions after holding the route fixed.

Before introducing advantages, define the old-policy value of reaching the unresolved gate:

\[
V_{\mathrm{gate}}
=
p_H^{\mathrm{old}}\bar R_H
+
p_N^{\mathrm{old}}\bar R_N.
\]

Now the reader has three nested reference levels:

\`\`\`text
prompt group
-> unresolved gate
-> selected route
-> sampled execution
\`\`\`

Only here introduce the exact decomposition:

\[
\frac{R_{g,k}-B_x}{\sigma_x+\epsilon}
=
\underbrace{\frac{V_{\mathrm{gate}}-B_x}{\sigma_x+\epsilon}}_{A_{\mathrm{pre}}}
+
\underbrace{\frac{\bar R_g-V_{\mathrm{gate}}}{\sigma_x+\epsilon}}_{A_{\mathrm{gate}}^g}
+
\underbrace{\frac{R_{g,k}-\bar R_g}{\sigma_x+\epsilon}}_{A_{\mathrm{in}}^{g,k}}.
\]

Interpret the three terms directly after the equation:

- \(A_{\mathrm{pre}}\): quality of the shared reasoning that reached the gate;
- \(A_{\mathrm{gate}}^g\): relative value of choosing Harness vs direct execution at that same state;
- \(A_{\mathrm{in}}^{g,k}\): execution quality relative to other continuations of the same route.

This is the conceptual center of the Method.

---

### 3.5 Segment-Specific Policy Optimization

**Reader question:** Which tokens are actually trained by each signal?

Map the three semantic comparisons back to token regions.

#### Shared prefix

Generated tokens before the selected gate receive \(A_{\mathrm{pre}}\).

The replicated prefix must contribute only one branch-node's optimization mass rather than being multiplied by the number of descendants.

#### Gate token

The atomic H/N token receives \(A_{\mathrm{gate}}^g\).

The two forced decisions are aggregated under the old routing distribution:

\[
\mathcal L_{\mathrm{gate}}
=
-
\sum_{g\in\{H,N\}}
p_g^{\mathrm{old}}
\phi(\rho_g,A_{\mathrm{gate}}^g).
\]

This equation is now interpretable because \(g\), the gate token, Harness semantics, and the paired return groups were all established earlier.

#### Conditional suffix

Do not use \(A_{\mathrm{in}}\) as the only suffix signal.

Retain trajectory-level task credit:

\[
A_{\mathrm{suffix}}^{g,k}
=
A_{\mathrm{global}}^{g,k}
+
\alpha A_{\mathrm{in}}^{g,k}.
\]

Use the edge case to motivate the design:

\[
K_g=1
\Longrightarrow
A_{\mathrm{in}}^{g,1}=0.
\]

Even then, a trajectory may still succeed or fail, so ordinary task credit must remain.

Harness observations and environment feedback stay masked throughout.

---

### 3.6 Forced Sampling and Route-Probability Correction

**Reader question:** Does forcing equal H/N samples change the policy objective?

Explain that balanced branching samples from a behavior distribution

\[
\mu(g)=\frac{K_g}{K_H+K_N},
\]

rather than directly from \(\pi_{\mathrm{old}}(g\mid s)\).

Give one implementation form:

\[
c_g=\frac{p_g^{\mathrm{old}}}{\mu(g)}.
\]

Then state the equivalent mode-first implementation:

- average samples within each route;
- weight the route loss by \(p_g^{\mathrm{old}}\).

Explicitly warn that the two corrections are equivalent representations and must not both be applied.

The full derivation can move to appendix; the main paper must retain enough information to explain why forced counterfactual coverage does not imply uniform route weighting in the objective.

---

### 3.7 Preventing Gate Starvation

**Reader question:** What happens if the Harness route is initially bad only because the agent has not learned to execute it yet?

Introduce the failure mode only after routing and execution credit are separately defined.

Early low Harness returns can produce a feedback loop:

\`\`\`text
weak Harness execution
-> low H return
-> gate avoids H
-> fewer H continuations
-> execution remains weak
\`\`\`

H-PAIR therefore separates early execution acquisition from full routing optimization:

- during warm-up, direct task gradients on gate tokens are masked or downweighted;
- Harness-conditioned suffix learning remains active;
- gate weight increases with an observable execution-competence statistic;
- a minimum forced-H exploration floor remains after the transition.

Give the schedule at compact resolution:

\[
\lambda_g(u)
=
\operatorname{clip}
\left(
\frac{C_{\mathrm{exec}}(u)-\tau_0}
{\tau_1-\tau_0},
0,1
\right).
\]

Long implementation details and threshold definitions may move to appendix.

---

### 3.8 Training Objective and Algorithm Summary

**Reader question:** How do the pieces fit into one update?

Only now present the compact total objective:

\[
\mathcal L_{\mathrm{HPAIR}}
=
\mathcal L_{\mathrm{global}}
+
\lambda_b
\left(
\lambda_p\mathcal L_{\mathrm{pre}}
+
\lambda_g(u)\mathcal L_{\mathrm{gate}}
+
\lambda_s\mathcal L_{\mathrm{suffix}}
\right)
+
\beta\mathcal L_{\mathrm{KL}}.
\]

Follow with a short algorithm box summarizing:

1. global rollout generation;
2. gate-probability logging;
3. branch-state selection;
4. exact state restoration;
5. forced H/N conditional sampling;
6. return scoring;
7. prefix/gate/suffix advantage construction;
8. behavior-corrected segmented GRPO update.

Do not repeat every equation in pseudocode.

---

# Main-Paper / Appendix Boundary

## Must remain in the main Method

- atomic H/N gate-token representation;
- gate-every-step vs branch-selected-subset distinction;
- generic route grammar;
- Memory / Plan / Verification semantics;
- candidate-conditioned Verification exception;
- policy-token vs observation-token mask;
- restoration semantics;
- \(K_H,K_N\);
- \(\bar R_g\);
- \(V_{\mathrm{gate}}\);
- three-part decomposition;
- suffix retention of trajectory GRPO;
- behavior-correction principle;
- gate-starvation mechanism if it remains a claimed component.

## May move to appendix

- full ALFWorld/WebShop Memory field schemas;
- full PLAN_UPDATE serialization;
- verifier prompt and backend implementation;
- parser/tokenizer tests beyond atomic-token requirement;
- long weighted-baseline / variance derivations;
- complete behavior-correction proof;
- snapshot engineering details;
- full hyperparameters.

---

# Regression Result

This section plan passes the v0.6 technical-completeness gate.

It fixes the first mock paper's failure without turning the Method into a schema dump:

\`\`\`text
decision semantics
-> Harness semantics
-> paired intervention
-> return groups
-> credit decomposition
-> token-region optimization
-> sampling correction
-> training dynamics
-> compact total objective
\`\`\`

The important change is that token and Harness definitions are not added as isolated documentation. They become prerequisites that make the later equations meaningful.
