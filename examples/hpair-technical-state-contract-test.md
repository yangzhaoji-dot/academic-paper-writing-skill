# H-PAIR Technical-State / Section-Contract Regression Test

## Purpose

This regression test reproduces the failure exposed by the first ICML mock paper:

- the paper story and credit-decomposition equations were present;
- the policy-token protocol was underexplained;
- the Harness suite was named but not operationally defined;
- presentation planning incorrectly treated some prerequisite definitions as appendix-level implementation detail.

The v0.6 technical-completeness layer should block that draft before discourse composition or typesetting.

---

# 1. Research Source Coverage

| Role | H-PAIR source | Coverage |
|---|---|---|
| idea / claims | \`README.md\`, \`docs/method.md\` | complete |
| method | \`docs/method.md\` | complete |
| interfaces / action space | \`docs/harness_design.md\`, \`docs/method.md\` | complete |
| state / transitions | \`docs/harness_design.md\` | complete |
| training objective / loss | \`docs/loss.md\`, \`docs/method.md\` | complete |
| environment / experiment protocol | \`docs/plan_a_harness_validation.md\` | complete for current Plan A |
| prior-work boundary | \`docs/related_work.md\` | complete for current repository state |
| implementation constraints | \`docs/method.md\`, \`docs/harness_design.md\` | complete |
| limitations / open questions | \`README.md\`, \`docs/harness_design.md\`, \`docs/decisions.md\` | partial until every open decision is frozen |

### Regression condition

A grounding pass that reads \`method.md\`, \`loss.md\`, and \`plan_a_harness_validation.md\` but skips \`harness_design.md\` must be marked **incomplete**, because the skipped file defines:

- the three Harness states and APIs;
- the exact USE / NO-HARNESS transition semantics;
- the candidate-conditioned Verification exception;
- information-boundary constraints;
- which external outputs are observations rather than policy actions.

The previous ICML mock would therefore have been blocked at grounding.

---

# 2. H-PAIR Technical State

## 2.1 Decision space

\`\`\`yaml
decision:
  variable: g
  choices:
    H: USE_HARNESS
    N: NO_HARNESS
  representation:
    H: "<|USE_HARNESS|>"
    N: "<|NO_HARNESS|>"
  tokenizer_constraint:
    atomic_single_token: true
  decision_constraints:
    exhaustive: true
    mutually_exclusive: true
  occurs_at:
    generic_protocol: every policy-controlled action boundary
\`\`\`

The existence of the H/N gate is not the same as branch selection.

\`\`\`yaml
gate:
  exists_at: every policy-controlled action boundary

paired_branch:
  applied_at: budgeted subset of existing gate positions
  initial_selector: smallest H/N old-policy log-probability margin
\`\`\`

This distinction is a main-paper technical prerequisite because the loss and rollout procedure depend on it.

## 2.2 Generic token / action protocol

### Harness route

\`\`\`text
<think>task reasoning</think>
<|USE_HARNESS|>
<harness_think>which Harness operation and why</harness_think>
<action>Harness operation</action>
[Harness observation enters context]
[actor continues]
\`\`\`

### Direct route

\`\`\`text
<think>task reasoning</think>
<|NO_HARNESS|>
<action>environment action</action>
[environment feedback enters context]
[actor continues]
\`\`\`

### Optimization semantics

\`\`\`yaml
generated_policy_tokens:
  optimized: true

gate_token:
  optimized: true
  special_credit: A_gate at selected paired branch

harness_observation:
  optimized: false
  role: context

environment_feedback:
  optimized: false
  role: context

shared_generated_prefix:
  selected_branch_credit: A_pre

generated_suffix:
  selected_branch_credit: A_GRPO + alpha * A_in
\`\`\`

---

# 3. Harness Suite

The three Harnesses are not interchangeable tool names. They instantiate different external-state/computation semantics.

## 3.1 Memory — selective external-state access

\`\`\`yaml
state:
  kind: auto-updated read-only observation memory
  writer: deterministic environment adapter
  content: observed facts only

api:
  READ_MEMORY()

USE:
  read current external-memory snapshot
  -> return bounded memory observation
  -> actor continues

NO_HARNESS:
  no memory access
  -> actor continues directly

gate_question:
  Is external memory access worth its cost at this state?
\`\`\`

Important boundary:

- actor does not write Memory in V0;
- hidden simulator state and inferred next actions are forbidden;
- the returned memory snapshot is context, not a policy token.

## 3.2 Plan — selective persistent-state mutation

\`\`\`yaml
persistent_state:
  GLOBAL_PLAN:
  ACTIVE_SUBGOAL:

api:
  PLAN_UPDATE(
    global_plan = optional,
    active_subgoal = optional
  )

USE:
  actor emits PLAN_UPDATE(...)
  -> Harness mutates persistent plan state
  -> actor continues using updated plan

NO_HARNESS:
  keep plan unchanged
  -> actor executes directly

gate_question:
  Is revising the external plan worth its cost now?
\`\`\`

Current V0 assumes an initial high-level plan exists before gated RL. Therefore the first experiment studies **when to revise / maintain a plan**, not the more general question of whether to instantiate planning at all.

## 3.3 Verification — candidate-conditioned external checking

Verification is a real protocol exception.

\`\`\`text
state s_t
    ↓
actor proposes candidate action a_tilde
    ↓
H/N gate conditioned on the same candidate
    ├── H:
    │    VERIFY(a_tilde)
    │    -> feedback
    │    -> actor may keep or revise action
    │
    └── N:
         execute the same a_tilde directly
\`\`\`

\`\`\`yaml
api:
  VERIFY(candidate)

returns:
  STATUS:
  EVIDENCE:
  ISSUE:

USE:
  check the fixed candidate before commitment

NO_HARNESS:
  commit the same candidate directly

gate_question:
  Is checking this candidate worth its cost?
\`\`\`

The verifier must not output the next environment action or use hidden benchmark truth.

This exception must remain in the main Method if Verification is part of the reported experiment suite. Treating Verification as an ordinary pre-action H/N gate changes the intervention being estimated.

---

# 4. Sampling / Branching State

At a selected gate:

\`\`\`yaml
restore:
  - generated token prefix
  - environment state
  - Harness state
  - tool / Harness budget metadata
  - controllable exogenous randomness where applicable

force:
  - H route
  - N route

sample:
  H: K_H conditional suffixes
  N: K_N conditional suffixes
\`\`\`

The initial repeated-execution setting is:

\[
N=4,\qquad B_{\mathrm{nodes}}=1,\qquad K_H=K_N=2.
\]

For Verification, restoration additionally preserves the same candidate action before the H/N intervention.

---

# 5. Dependency Graph

The core Method dependencies are:

\`\`\`text
policy-controlled action boundary
    ↓
atomic H/N gate-token semantics
    ↓
meaning of g ∈ {H,N}
    ↓
Harness-specific USE / NO transition
    ↓
restored paired H/N intervention
    ↓
mode-specific return groups G_H(s), G_N(s)
    ↓
mode means Rbar_H, Rbar_N
    ↓
V_gate
    ↓
A_gate
\`\`\`

and:

\`\`\`text
Harness-specific route semantics
    ↓
repeated suffixes under same route
    ↓
within-mode comparison
    ↓
A_in
    ↓
A_suffix = A_GRPO + alpha A_in
\`\`\`

Optimization dependency:

\`\`\`text
token / observation grammar
    ↓
policy-token vs context-token mask
    ↓
segment-specific advantage assignment
    ↓
segmented GRPO objective
\`\`\`

The old mock paper violated the first graph by introducing the credit estimator before adequately establishing the gate token and Harness semantics.

---

# 6. Method Section Contract

\`\`\`yaml
section: Method
contract_status: ready_after_coverage

must_establish:
  - every policy-controlled action boundary contains exactly one atomic H/N gate token
  - gate existence is distinct from branch-point selection
  - generic H-route and N-route action grammar
  - Harness observations and environment feedback are context and masked from policy-gradient loss
  - Memory state, READ_MEMORY API, and USE/SKIP semantics
  - Plan state, PLAN_UPDATE API, and USE/SKIP semantics
  - Verification candidate-conditioned protocol and USE/SKIP semantics
  - state restored by a paired intervention
  - meanings of K_H and K_N
  - mode means Rbar_g
  - V_gate
  - A_pre, A_gate, A_in
  - suffix retains trajectory-level GRPO
  - behavior correction / route weighting
  - gate-starvation warm-up if it remains part of the method claim

must_define_before_use:
  - g before pi(g | s)
  - H/N gate tokens before gate loss
  - each Harness before a Harness-specific branch is discussed
  - Rbar_g before V_gate
  - V_gate before A_gate
  - within-mode group before A_in
  - policy/context masks before segmented loss

must_not_claim:
  - empirical superiority before actual training
  - novelty for snapshot/restore
  - novelty for generic branching
  - novelty for selective Harness/tool use by itself

may_reference_as_established:
  - high-level routing-vs-execution ambiguity from Introduction

may_defer:
  - full Memory field schema
  - full PLAN_UPDATE serialization details
  - verifier prompt
  - tokenizer implementation details beyond atomic-token requirement
  - long behavior-correction derivation
  - environment-adapter implementation
\`\`\`

---

# 7. Presentation Classification

For the main paper:

## Core claims

- routing credit and route-conditioned execution credit are distinct;
- paired semantic routes expose these contrasts.

## Technical prerequisites — keep reader-visible

- atomic H/N gate-token representation;
- every-step gate vs selected branch-point distinction;
- route grammar at conceptual resolution;
- Memory / Plan / Verification operational semantics;
- Verification candidate-conditioned exception;
- policy-token vs context-token mask;
- variables required to interpret the central decomposition.

## Supporting / compressible

- full Harness output schemas;
- detailed cost coefficients;
- exact memory-rendering budget;
- parser implementation.

## Appendix candidates

- full environment-adapter fields;
- complete verifier prompt;
- long algebraic derivations;
- complete tokenization and parser tests;
- extended implementation pseudocode.

A page-budget optimizer is not allowed to move the only definition of any technical prerequisite above into the appendix.

---

# 8. Regression verdict

The previous ICML mock would fail v0.6 at three gates:

1. **Source Coverage** — \`harness_design.md\` was not fully incorporated.
2. **Method Section Contract** — gate-token representation and Harness operational semantics were missing.
3. **Presentation Prerequisite Gate** — Harness interfaces were incorrectly classified as appendix-level detail.

Therefore the correct repair is upstream state reconstruction, not local prose expansion.
