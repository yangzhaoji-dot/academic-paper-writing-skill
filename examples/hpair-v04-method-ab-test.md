# H-PAIR Method Writing: v0.3 vs v0.4 Controlled A/B Test

## Test purpose

Test whether literature-grounded discourse composition improves **Method exposition**, not just Introduction prose.

The controlled target is H-PAIR's paired rollout and three-part advantage decomposition.

## Controlled technical content

Both versions must preserve exactly the following method facts.

1. At a selected Harness gate, H-PAIR restores the same state and forces both modes:
   \`g in {H, N}\`.
2. Each mode has repeated conditional suffix samples \`R_{g,k}\`.
3. The mode mean is
   \`\`\`
   Rbar_g = (1 / K_g) sum_k R_{g,k}.
   \`\`\`
4. The old-policy expected gate value is
   \`\`\`
   V_gate = p_H^old Rbar_H + p_N^old Rbar_N.
   \`\`\`
5. Relative to a prompt-group baseline \`B\` and common scale \`sigma_G\`, the return decomposes as
   \`\`\`
   (R_{g,k} - B) / sigma_G
   =
   (V_gate - B) / sigma_G
   +
   (Rbar_g - V_gate) / sigma_G
   +
   (R_{g,k} - Rbar_g) / sigma_G.
   \`\`\`
6. The three terms correspond to:
   - shared-prefix credit;
   - Harness routing credit;
   - within-mode execution refinement.
7. The actual suffix advantage retains trajectory-level GRPO:
   \`\`\`
   A_suffix^{g,k} = A_GRPO^{g,k} + alpha A_in^{g,k}.
   \`\`\`
8. If \`K_g = 1\`, then \`A_in = 0\`; ordinary task-learning signal remains through \`A_GRPO\`.
9. No critic is introduced.
10. No empirical effectiveness claim may be made because H-PAIR has not been trained yet.

The A/B test changes only discourse organization.

---

## Version A — v0.3 rule-driven Method exposition

### Paired rollout

For a selected Harness decision state, H-PAIR restores the same interaction prefix and samples both routing modes. Let \(g\in\{H,N\}\) denote Harness and direct execution, respectively. Under each mode, H-PAIR samples \(K_g\) conditional suffixes with terminal returns \(R_{g,k}\).

For each mode, we first compute the conditional mean return

\[
\bar R_g=\frac{1}{K_g}\sum_{k=1}^{K_g}R_{g,k}.
\]

Using the old-policy routing probabilities, we define the expected return at the gate as

\[
V_{\mathrm{gate}}
=
p_H^{\mathrm{old}}\bar R_H
+
p_N^{\mathrm{old}}\bar R_N.
\]

### Three-part advantage decomposition

H-PAIR separates the trajectory return into three components. Let \(B\) denote the prompt-group baseline and \(\sigma_G\) the common group scale. For a suffix \(k\) under mode \(g\),

\[
\frac{R_{g,k}-B}{\sigma_G}
=
\underbrace{\frac{V_{\mathrm{gate}}-B}{\sigma_G}}_{A_{\mathrm{pre}}}
+
\underbrace{\frac{\bar R_g-V_{\mathrm{gate}}}{\sigma_G}}_{A_{\mathrm{gate}}^g}
+
\underbrace{\frac{R_{g,k}-\bar R_g}{\sigma_G}}_{A_{\mathrm{in}}^{g,k}}.
\]

The first term is the shared-prefix advantage. It measures whether the state reached by the common prefix has higher expected continuation value than the prompt-level baseline.

The second term is the decision-token advantage. It measures whether selecting the Harness or direct route is better than the old-policy mixture at the same state. This term is assigned to the corresponding Harness decision token.

The third term is the within-mode execution advantage. It compares one continuation against other continuations sampled under the same routing decision, thereby refining credit among different executions of the selected route.

### Suffix learning

H-PAIR does not replace trajectory-level task credit with the within-mode residual. Instead, suffix tokens retain the ordinary GRPO advantage and receive the within-mode term as an additional refinement:

\[
A_{\mathrm{suffix}}^{g,k}
=
A_{\mathrm{GRPO}}^{g,k}
+
\alpha A_{\mathrm{in}}^{g,k},
\]

where

\[
A_{\mathrm{GRPO}}^{g,k}
=
\frac{R_{g,k}-B}{\sigma_G}.
\]

This preserves the terminal task-success signal while adding conditional execution contrast. When a mode has only one sampled suffix, \(K_g=1\), its within-mode residual is zero, so suffix learning reduces to ordinary trajectory-level GRPO.

---

## Version B — v0.4 literature-grounded Method exposition

A paired branch from one Harness gate produces two kinds of variation that should not be collapsed into the same comparison. Returns can change because the policy takes a different route—Harness or direct execution—or because two continuations of the *same* route are executed differently. H-PAIR keeps these sources of variation separate while using the same terminal return.

Suppose a selected gate is restored and evaluated under \(g\in\{H,N\}\). We sample \(K_g\) continuations for each mode and denote their returns by \(R_{g,k}\). The first quantity we need is therefore not an advantage, but the expected outcome of each route:

\[
\bar R_g=\frac{1}{K_g}\sum_{k=1}^{K_g}R_{g,k}.
\]

These two means isolate the routing comparison from incidental variation among suffix samples. Under the old policy, the value of reaching the gate before committing to either route is their probability-weighted mixture,

\[
V_{\mathrm{gate}}
=
p_H^{\mathrm{old}}\bar R_H
+
p_N^{\mathrm{old}}\bar R_N.
\]

This gives three natural reference levels for any sampled return \(R_{g,k}\): the prompt group, the unresolved gate, and the selected route. Using the same group baseline \(B\) and scale \(\sigma_G\) at all three levels, its normalized return can be written exactly as

\[
\frac{R_{g,k}-B}{\sigma_G}
=
\frac{V_{\mathrm{gate}}-B}{\sigma_G}
+
\frac{\bar R_g-V_{\mathrm{gate}}}{\sigma_G}
+
\frac{R_{g,k}-\bar R_g}{\sigma_G}.
\]

Each difference answers a different credit question. The first asks whether the shared prefix reached a gate whose available continuations are promising relative to the prompt group. The second holds the state fixed and compares the chosen route with the old-policy mixture, so it provides the signal used for the Harness decision token. The last holds both the state and route fixed; it only distinguishes better and worse ways of executing that route.

The final term is intentionally a refinement rather than the sole suffix objective. A route can have no useful within-mode contrast—for example when only one continuation is sampled—while the resulting trajectory can still succeed or fail at the task. We therefore retain the ordinary trajectory-level GRPO advantage on suffix tokens and add the within-route residual,

\[
A_{\mathrm{suffix}}^{g,k}
=
A_{\mathrm{GRPO}}^{g,k}
+
\alpha A_{\mathrm{in}}^{g,k},
\qquad
A_{\mathrm{GRPO}}^{g,k}
=
\frac{R_{g,k}-B}{\sigma_G}.
\]

Because \(A_{\mathrm{in}}^{g,k}=R_{g,k}-\bar R_g\) up to the common normalization, it averages to zero within a mode and vanishes when \(K_g=1\). Thus repeated suffix sampling adds conditional execution contrast without removing the task-level signal already carried by GRPO. The decomposition requires no learned critic; all three references are computed from sampled returns.

---

## Discourse references used for Version B

No source wording is reused. The following Method-level patterns were abstracted and combined.

### BPO

BPO first defines the state/return objects needed for its estimator, then states the local sibling comparison, and only afterward explains propagation and the policy objective. It also motivates design choices immediately next to the corresponding mechanism—for example, explaining why entropy is used as the branch criterion immediately after defining that criterion.

Transferable pattern:

\`\`\`text
define the comparison set
-> define the local estimator
-> state what statistical quantity it represents
-> show how it enters optimization
-> explain design choice locally
\`\`\`

### BranPO

BranPO first explains why an intermediate state is not by itself a sufficient credit unit. It then changes the supervision target from "how good is this state?" to "which continuation should be taken from this state?" before introducing branch construction and the formal advantage equations.

Transferable pattern:

\`\`\`text
identify ambiguity in the old supervision unit
-> state the new comparison unit
-> construct samples that instantiate that comparison
-> formalize the estimator
-> interpret different gradient regions
\`\`\`

### ContextPilot

ContextPilot introduces the quantities used to select important context-management actions before defining the combined sensitivity score. For credit assignment, it first states the problem with copying terminal reward to every snapshot, then defines snapshot value from descendant returns, then defines the normalized advantage and policy update.

Transferable pattern:

\`\`\`text
state what must be measured
-> define primitive quantities
-> combine them only after their role is clear
-> connect the resulting statistic to the optimization target
\`\`\`

---

## Evaluation

| Criterion | Version A | Version B | Observation |
|---|---:|---:|---|
| Purpose visible before equations | 4/5 | 5/5 | B states the two sources of return variation before any notation. |
| Equation motivation | 3/5 | 5/5 | A defines quantities sequentially; B explains why each reference level is required. |
| Local WHY–WHAT–HOW integration | 3/5 | 5/5 | A exposes separate semantic blocks; B places motivation next to each mechanism. |
| Reader memory load | 3/5 | 4/5 | B gives the reader one organizing idea: three reference levels / three questions. |
| Interpretation of decomposition | 4/5 | 5/5 | B derives the interpretation from the subtraction structure rather than naming components afterward. |
| Connection to suffix objective | 4/5 | 5/5 | B motivates retaining GRPO through the \(K_g=1\) edge case before presenting the final objective. |
| Technical fidelity | 5/5 | 5/5 | Same estimator and optimization facts are preserved. |
| Scaffold leakage | 3/5 | 5/5 | A visibly follows paired rollout -> decomposition -> suffix learning modules. |
| Natural Method prose | 3/5 | 5/5 | B reads as an argument around an estimator rather than documentation of components. |

These are author-side diagnostic scores, not blinded human evaluation.

## Main finding

The Method test supports the same conclusion as the Introduction test, but for a different reason.

For Introduction, discourse grounding mainly improved **reveal order**.

For Method, its main benefit is **equation motivation**:

\`\`\`text
scientific/optimization question
-> quantity needed to answer it
-> definition
-> equation
-> interpretation
-> next unresolved question
\`\`\`

This is materially different from merely enforcing \`WHY -> WHAT -> HOW\` on every component. The latter is useful as a semantic completeness check, but if exposed directly it produces a repetitive component-by-component cadence.

## Skill implication

Keep \`WHY -> WHAT -> HOW\` as an internal invariant, but do not use it as the default visible Method organization.

For Method discourse composition, prefer:

1. identify the unresolved estimation/optimization question;
2. introduce the minimum mathematical object needed next;
3. define it;
4. interpret the equation immediately;
5. let that interpretation create the need for the next object.

In other words, equations should participate in the argument rather than appear after a prose description of a component.

## Remaining test

The next high-value test is **Experiments**. The key question is whether discourse grounding can turn a conventional table-first experiment section into a claim-driven sequence:

\`\`\`text
paper claim
-> empirical question
-> comparison that isolates it
-> metric
-> result
-> interpretation / falsifier
\`\`\`

without making the section verbose or repetitive.
