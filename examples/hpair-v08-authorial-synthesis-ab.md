# H-PAIR v0.8 Authorial-Synthesis A/B Regression

## Purpose

Test whether the writing pipeline can preserve the full H-PAIR science while removing the visible traces of the internal workflow.

The regression targets four failure modes:

1. scaffold / workflow commentary;
2. one-visible-section-per-internal-concept structure;
3. terminology proliferation;
4. abstraction without a concrete object for the reader to follow.

---

# 1. Introduction A/B

## A — semantically correct but scaffold-visible

> Harness-augmented agents introduce a mismatch between policy structure and trajectory-level credit. Our question is narrower than generic tool-use learning: a failed Harness-assisted trajectory may result from either an incorrect routing decision or poor execution after selecting the Harness route. This distinction motivates our central claim that invocation and route-conditioned execution require separate credit signals. We therefore propose H-PAIR, which uses matched H/N branches and repeated within-mode continuations. Our evaluation is organized around two questions: whether a non-trivial use/skip boundary exists, and whether the proposed credit decomposition improves routing and execution under matched compute. The decisive experiment keeps branch data fixed and changes only the credit rule.

Why it feels wrong:

- "our question is narrower" is positioning commentary;
- "motivates our central claim" exposes Claim Graph logic;
- "our evaluation is organized around" exposes Experimental Obligations;
- "the decisive experiment" tells the reader how to rank evidence instead of letting the evidence establish its role;
- abstract nouns arrive before a concrete Harness decision is visible.

## B — authorially synthesized

> Consider an agent that has already proposed an action and can either verify it before acting or execute it immediately. If the resulting trajectory fails, the final reward alone does not say which choice was wrong. Verification may have been unnecessary, or it may have been the right choice followed by a poor continuation. The same ambiguity appears whenever an agent can selectively read external memory or revise an external plan.
>
> H-PAIR separates these two sources of error at the point where the Harness decision is made. From the same restored state, it compares using the Harness with skipping it to estimate **invocation credit**. It then compares multiple continuations after the same choice to refine **execution credit**. The resulting signals train the Harness decision separately from the continuation while preserving ordinary task-level learning.

What changed:

- one concrete Verification decision anchors the abstraction;
- "routing / route-conditioned execution / semantic route / gate" collapse to "Harness decision", "use / skip", "invocation credit", and "execution credit";
- the experiment plan disappears from the Introduction;
- H-PAIR grows from the ambiguity rather than from internal framing labels.

---

# 2. Method Surface Compression

## A — internal structure exposed as visible paper structure

\`\`\`text
3.1 Harness-Augmented Decision Process
3.2 Harness Suite and Route Semantics
3.3 Paired Interventions at Existing Gates
3.4 Three Reference Levels for Credit
3.5 Segment-Specific Policy Optimization
3.6 Forced Sampling and Route-Probability Correction
3.7 Preventing Gate Starvation
3.8 Training Objective and Algorithm Summary
\`\`\`

This organization is logically correct, but each internal mechanism receives its own visible identity.

## B — synthesized visible structure

\`\`\`text
3 H-PAIR

3.1 Harness Decisions and Paired Rollouts
    - atomic use / skip decision
    - Memory / Plan / Verification semantics
    - candidate-conditioned Verification exception
    - restored-state paired sampling

3.2 Paired Credit Assignment
    - route means
    - unresolved-gate value
    - invocation credit
    - within-choice execution residual
    - mapping to prefix / decision / suffix tokens

3.3 Optimization and Training
    - trajectory credit retained on suffixes
    - route-probability correction
    - total objective
    - execution warm-up / gate-starvation prevention
\`\`\`

No scientific object is removed.

The compression changes only the manuscript surface:

- decision protocol + Harness semantics + branching become one continuous operational story;
- all credit quantities live under one estimator subsection;
- optimization corrections and training schedule live together.

---

# 3. Canonical Terminology

## Before

The draft alternates among:

\`\`\`text
gate
routing decision
Harness decision
mode
route
semantic route
decision boundary
H-route / N-route
conditional execution
\`\`\`

## After

Preferred active vocabulary:

\`\`\`yaml
Harness decision:
  preferred: Harness decision
  notation: g in {H, N}
  literal realization: USE_HARNESS / NO_HARNESS
  avoid_as_primary:
    - gate
    - routing decision
    - decision boundary

use / skip:
  preferred: use / skip
  notation: H / N
  avoid_as_primary:
    - mode
    - semantic route

paired rollout:
  preferred: paired rollout
  meaning: same restored state, forced use and skip continuations

invocation credit:
  preferred: invocation credit
  mathematical_object: A_gate

execution credit:
  preferred: execution credit
  mathematical_object: A_in refinement on suffix learning
\`\`\`

Exceptions:

- "gate" may remain in equations such as \(V_{\mathrm{gate}}\) because it is already fixed notation;
- "route" may be used locally when distinguishing the two conditional continuation distributions, but it should not become a second name for the Harness decision throughout the paper.

The purpose is semantic stability, not vocabulary uniformity for its own sake.

---

# 4. Concrete-Anchor Continuity

## Introduction anchor

\`\`\`text
candidate action
-> verify or skip
-> continuation
-> terminal outcome
\`\`\`

This exposes the ambiguity directly.

## Early Method anchor

Use the same restored state:

\`\`\`text
same state + same candidate
        |
      use / skip
      /       \
 verified     direct
 continuation continuation
\`\`\`

The mathematical quantities then arise from this object:

\`\`\`text
difference between use and skip means
-> invocation credit

difference among continuations after the same choice
-> execution credit
\`\`\`

Once the estimator is understood, the paper can generalize from Verification to Memory and Plan without carrying the example mechanically through every subsection.

---

# 5. Experiments A/B

## A — Experimental Obligation translated into prose

> The decisive experiment is designed to isolate the contribution of H-PAIR's credit rule from the additional exploration introduced by branching. We therefore hold branch states, suffixes, rewards, generated tokens, environment steps, and Harness calls fixed, and change only the credit estimator. This comparison directly tests the paper's central claim. Table 2 is therefore the primary result. Invocation regret and calibration error are important because they directly measure whether the gate learns the intended use/skip boundary.

Why it feels wrong:

- "decisive", "central claim", and "primary result" are workflow labels;
- the paragraph explains the evidence hierarchy instead of presenting the scientific control;
- the metric rationale is written like a checklist.

## B — authorially synthesized

> All credit estimators are trained on the same restored states, sampled suffixes, and terminal rewards; generated tokens, environment steps, and Harness calls are also matched. Under this controlled comparison, H-PAIR improves task success over the strongest branch-credit baseline while reducing both invocation regret and calibration error. The joint improvement is important: a higher task score alone could come from better continuation learning, whereas lower regret indicates that the model is also choosing the Harness more appropriately.
>
> Removing invocation credit largely erases the regret improvement, while removing the within-choice residual primarily hurts conditional execution. These ablations match the roles assigned to the two signals by the estimator.

What changed:

- causal control is stated directly;
- observation precedes interpretation;
- the paper never calls its own table "decisive";
- the reason for the regret metric is expressed through an alternative explanation rather than through workflow language;
- ablations are interpreted as behavior, not as an obligation checklist.

---

# 6. Contribution-Bullet Regression

## Reject

\`\`\`text
- a claim-driven evaluation protocol that matches compute and isolates competing explanations
\`\`\`

Reason:

This describes how the paper validates itself, not what H-PAIR contributes scientifically.

## Prefer

Until real results exist, keep contributions focused on the method:

\`\`\`text
- a paired use/skip intervention that exposes Harness invocation credit at a restored decision state;
- a nested credit decomposition that separates invocation from execution while retaining trajectory-level task learning.
\`\`\`

A third empirical contribution should be added only after real experiments establish a stable finding.

---

# 7. v0.8 Regression Verdict

The visible manuscript should no longer be a one-to-one rendering of:

\`\`\`text
Framing
-> Claim Graph
-> Experimental Obligations
-> Section Contract
-> Modules
\`\`\`

Those structures remain useful internally.

The reader-facing transformation is:

\`\`\`text
complete semantic state
-> calibrated information
-> authorial synthesis
-> natural scientific argument
\`\`\`

For H-PAIR, the target surface is:

\`\`\`text
one concrete ambiguity
-> one compact distinction
-> paired comparison
-> invocation vs execution credit
-> controlled empirical evidence
\`\`\`

The scientific content remains unchanged; only the visible granularity, vocabulary, and narrative stance change.
