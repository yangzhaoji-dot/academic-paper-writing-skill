# H-PAIR v0.3 vs v0.4 Controlled A/B Test

## Test purpose

Test whether literature-grounded discourse composition improves the H-PAIR Introduction beyond rule-only naturalization.

## Controlled variables

Both versions use the same factual substrate and the same conservative Paper Core:

- H-PAIR is a research specification; no implementation or empirical result is claimed.
- Optional Harness use creates a routing choice plus route-conditioned execution.
- The candidate methodological contribution is not branching, snapshot/restore, or selective tool use by itself.
- The candidate contribution is the explicit credit decomposition between Harness invocation and execution conditional on the selected route.
- Plan A must first establish that the Harness produces a non-degenerate USE/SKIP boundary.

No empirical gains are invented.

## Scientific literature challenge applied before both drafts

The v0.4 literature pass narrows the novelty boundary:

- selective external assistance / tool invocation is already a studied decision problem;
- branch-based RL already uses shared intermediate states and alternative continuations for finer-grained credit;
- context-management RL already studies specialized external-state actions with branch-based or fine-grained credit;
- multi-harness RL already shows that the grouping boundary itself can carry harness-specific information.

Therefore the test does **not** frame H-PAIR as novel merely because it learns when to use a Harness or because it branches from intermediate states.

## Version A — v0.3 rules-only naturalization

Language agents are increasingly augmented with external Harnesses that provide persistent memory, planning state, or verification during interaction. Unlike ordinary environment actions, these mechanisms are optional: at each decision point, the agent may either invoke external support or proceed directly. This introduces an additional learning problem beyond selecting the next task action.

Standard trajectory-level reinforcement learning objectives provide a single outcome signal to all generated decisions. In a Harness-augmented trajectory, however, an unsuccessful outcome can arise for at least two different reasons. The agent may have made a poor routing decision by invoking the Harness when it was unnecessary, or it may have selected an appropriate route but executed the Harness-conditioned continuation poorly. Treating these cases identically entangles Harness routing with conditional execution and makes it difficult for the training signal to indicate which part of the policy should change.

We introduce H-PAIR, a paired interventional credit-assignment framework designed to separate these two learning signals. At selected Harness decision states, H-PAIR restores the same interaction prefix and forces both Harness and direct-execution routes. It then samples repeated continuations within each mode. The difference between mode-level returns provides credit for the Harness invocation decision, while return variation among continuations under the same mode provides additional credit for route-conditioned execution. The shared prefix is trained using the expected continuation value across the two routes. In this way, H-PAIR preserves the task-level objective while assigning different return components to policy decisions that play different roles.

This decomposition also reveals a training-dynamics problem. Early in training, the Harness route may obtain low returns because the agent has not yet learned how to use it effectively. If these returns immediately supervise the invocation decision, the policy may learn to avoid the Harness before Harness-conditioned execution becomes competent. H-PAIR therefore uses an execution warm-up stage in which route-conditioned behavior remains trainable while decision-token task gradients are restricted, followed by a gradual transition toward routing supervision and a minimum amount of forced Harness exploration.

The resulting method is intended to test whether explicitly separating Harness routing from route-conditioned execution yields more informative credit than trajectory-wide or generic branch-based alternatives. Before full H-PAIR training, a strong-model validation stage will measure whether Memory, Plan, and Verification Harnesses provide positive utility in some states but not others, establishing whether a meaningful USE/SKIP boundary exists. Subsequent experiments will compare credit-assignment rules under matched rollout, environment-step, and Harness-call budgets and will separately measure task success, invocation quality, and conditional execution.

## Version B — v0.4 literature-grounded discourse composition

Consider an agent that can either act directly or ask an external verifier to check a candidate action. If the assisted trajectory later fails, the terminal reward leaves an ambiguity: the verification call may have been unnecessary, or the call may have been appropriate while the agent acted poorly after receiving the feedback. The same ambiguity appears with optional memory reads and plan updates. These cases end in the same outcome, but they imply different policy updates.

This distinction is easy to lose in trajectory-level RL. A single return is typically broadcast across the decisions that produced the trajectory, even when those decisions play different roles. Selective tool-use methods already study whether external assistance is worth invoking, and branch-based agent RL already compares alternative continuations from shared intermediate states. The unresolved issue in our setting is what those comparisons should supervise when the branch itself has semantic meaning: one contrast concerns the choice of route, while another concerns the quality of execution after that route has been chosen.

H-PAIR makes this split explicit in the rollout structure. At a selected decision state, it restores the same prefix and evaluates both Harness and direct routes. Repeated continuations under each route form two nested groups. Their mean-return difference estimates whether the Harness should be used at that state; variation among continuations inside one group compares executions conditioned on the same routing choice. The shared prefix is trained from the expected value of the available routes. Branching is therefore used as a measurement device for two distinct credits, rather than treated as the contribution by itself.

Separating the credits also changes how early training should be handled. A weak Harness route can look like a bad routing choice simply because the policy has not yet learned to execute that route. Training the gate on those early returns can remove the very data needed to improve Harness-conditioned behavior. H-PAIR therefore lets execution acquire competence before the invocation decision receives the full task gradient, while retaining forced Harness exploration after the transition. Whether this staging is necessary is an empirical question rather than an assumption of the paper.

Before testing the full learning rule, we first need to establish that there is a routing problem to learn at all. Plan A uses matched interventions from identical ALFWorld states to measure the return difference between USE and SKIP for Memory, Plan, and Verification. If one route dominates almost everywhere, a learned gate is unnecessary. If both signs occur and a strong fixed actor still chooses imperfectly, the setting provides the non-degenerate decision boundary that H-PAIR is designed to optimize. Full training can then compare H-PAIR with trajectory-wide and generic branch-based credit under matched generation and Harness budgets, while measuring routing quality and conditional execution separately.

## Discourse references used for Version B

The prose was not paraphrased from any source. The following abstract patterns were extracted and combined:

- **BPO**: identify a property of the agent environment that makes an inherited RL structure inappropriate; then introduce the algorithmic change.
- **BranPO**: expose a concrete credit ambiguity, explain why the existing supervision unit is insufficient, and move from state evaluation to continuation comparison.
- **ContextPilot**: connect heterogeneous external actions to heterogeneous downstream impact, then motivate credit assignment tailored to those actions.

## Evaluation rubric

| Criterion | Version A | Version B | Observation |
|---|---:|---:|---|
| Time to concrete research ambiguity | 3/5 | 5/5 | B opens directly with the failed-assisted-trajectory ambiguity. |
| Internal scaffold leakage | 3/5 | 5/5 | A visibly follows context -> problem -> method -> dynamics -> experiments. B hides that pipeline better. |
| Method necessity before mechanics | 4/5 | 5/5 | Both work; B makes the two required contrasts explicit immediately before H-PAIR. |
| Novelty calibration | 4/5 | 5/5 | B explicitly positions selective invocation and generic branching as prior territory. |
| Paragraph continuity | 3/5 | 5/5 | A paragraphs correspond closely to semantic modules; B paragraphs create the next information need. |
| Claim safety before experiments | 5/5 | 5/5 | Neither version invents results; B explicitly marks staging as an empirical question. |
| Technical precision | 5/5 | 5/5 | Both preserve the same H-PAIR mechanism. |
| Overall reader-facing naturalness | 3/5 | 5/5 | B reads less like a transformed schema and more like a paper argument. |

The scores are a qualitative author-side diagnostic, not an external human evaluation.

## Main finding

The v0.4 layer changes more than word choice. Its largest benefit is **paragraph-level information order**:

```text
concrete ambiguity
-> distinguish two causes
-> locate what prior families already solve
-> identify the remaining supervision question
-> introduce H-PAIR as the required measurement structure
```

The v0.3 version is technically sound but still exposes the construction pipeline. The v0.4 version better preserves the same semantics while hiding the internal scaffold.

## Remaining weakness

Version B is still produced from a small reference set and has not been evaluated by blinded human readers. The next useful test is section transfer:

1. Method explanation: rules-only WHY/WHAT/HOW vs discourse-grounded method exposition.
2. Experiment writing: table-first description vs claim/question-driven experiment exposition.
3. Repeat the Introduction test with 5–8 papers from the final H-PAIR related-work set and compare whether the discourse profile remains stable.
