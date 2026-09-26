# H-PAIR v0.10 Convention-Prior Regression

## Purpose

Test whether the writing system can learn academic presentation conventions without turning them into fake scientific or venue rules.

The regression focuses on four categories:

1. layout;
2. formula exposition;
3. information presentation;
4. reviewer / academic expectations.

---

# 1. Layout prior

## Bad behavior

\`\`\`text
"ICML methods papers should be 5 pages before references."
"Figure 1 must always appear on page 1."
"Related Work must always be before Method."
\`\`\`

Why this is wrong:

- page count may conflict with official venue limits and current paper needs;
- accepted-paper frequency is not a hard rule;
- section order varies by paper type.

## Correct behavior

Represent tendencies as soft priors:

\`\`\`yaml
layout_prior:
  first_page:
    tendencies:
      - establish the concrete problem early
      - use Figure 1 when it materially compresses the paper-level distinction
    confidence: medium
  section_balance:
    tendencies:
      - core method should receive enough main-body space to expose the exact update
      - decisive experiments should not be visually subordinate to diagnostics
    confidence: high
\`\`\`

Hard page limits come only from the official target-year venue profile.

---

# 2. Formula exposition prior

## Failure caught in H-PAIR v0.8

The draft introduced:

\`\`\`text
A_pre
A_gate
A_in
\`\`\`

without first making the full baseline GRPO update and trajectory-wide credit broadcast visible.

It then wrote a combined H-PAIR loss without fully defining the global term.

## Convention prior that should catch this

\`\`\`yaml
formula_prior:
  baseline_before_delta:
    expected: true
    strength: strong
  objective_progression:
    tendencies:
      - define notation before use
      - establish baseline objective
      - expose the exact modified object
      - map the new estimator to optimized units
      - write the exact update
  exact_update_visibility:
    expected: main_body
    strength: strong
  correction_terms:
    tendencies:
      - forced sampling should expose behavior / importance correction
\`\`\`

This prior changes exposition completeness, not H-PAIR's equations.

---

# 3. Information-presentation prior

## H-PAIR object-to-carrier mapping

\`\`\`text
policy structure vs flat credit
-> Figure 1

Memory / Plan / Verification shared semantics
-> compact table

Verification candidate-conditioned exception
-> prose

GRPO baseline
-> equations

H-PAIR credit map
-> central equation

paired rollout + credit mapping
-> Figure 2

end-to-end result
-> main table

same-rollout estimator attribution
-> second main table

calibration / training dynamics
-> plot
\`\`\`

## Regression rule

Reject a manuscript in which:

- Harness semantics are fully repeated in prose, table, and figure;
- Figure 2 is only a generic branch tree;
- invocation regret first appears in a result-table header;
- the exact H-PAIR update is relegated to appendix while the main paper claims a new RL algorithm.

---

# 4. Reviewer / academic expectations

These are soft expectations, not venue law.

## Strong when applicable

\`\`\`yaml
- expectation: match generated tokens / environment steps / Harness calls
  applies_when: the proposed method adds branch samples or external calls
  strength: strong

- expectation: report uncertainty across stochastic runs
  applies_when: stochastic training results support the main empirical claim
  strength: strong

- expectation: define method-specific metrics before reporting them
  applies_when: new diagnostics such as invocation regret or decision ECE are introduced
  strength: strong

- expectation: compare directly with closest work
  applies_when: novelty depends on a distinction from a close method
  strength: strong
\`\`\`

## Medium / context dependent

\`\`\`yaml
- expectation: contribution bullets occupy different scientific layers
  strength: medium

- expectation: Figure 1 gives a 30-second paper-level explanation
  strength: medium

- expectation: 2–4 contribution bullets are common
  strength: weak
\`\`\`

The last item must **not** become:

> "A paper needs exactly three contributions."

---

# 5. Hard-vs-soft regression

## Hard

May come from:

- official author instructions;
- official template;
- official checklist;
- official anonymity / supplementary rules.

## Soft

May come from:

- accepted-paper distributions;
- nearby methods papers;
- reviewer practice;
- recurring exposition patterns.

A soft prior may influence Architecture / Section Calibration / Manuscript Calibration.

It may not:

- strengthen novelty;
- invent evidence;
- alter an equation;
- force the number of contributions;
- override Scientific Spec.

---

# 6. Expected v0.10 behavior for H-PAIR

Before writing, Convention Mining should produce a profile that makes the following expectations visible:

\`\`\`text
Layout:
core method has enough main-body space
main result visually prominent
Figure 1 carries paper-level mismatch

Formula:
GRPO baseline before H-PAIR
exact update in main body
sampling correction visible
variables defined before use

Information:
Harness semantics -> table
credit decomposition -> equation
paired credit flow -> figure
main comparison -> table

Academic expectations:
closest-work comparison
resource-matched branch comparison
seed / uncertainty reporting
metric definitions before values
no synthetic empirical contribution
\`\`\`

The profile should remain compatible with justified deviations.

# Regression verdict

Convention Prior is successful only if it improves manuscript expectations **without becoming a second Scientific Spec**.
