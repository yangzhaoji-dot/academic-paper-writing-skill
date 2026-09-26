# Procedure: Experimental obligations

Goal: derive the minimum experimental evidence required by the paper's central claims before designing benchmark sweeps, tables, or figures.

## Inputs

Use:

- Paper Core;
- Claim Graph;
- proposed mechanism;
- known baselines and competing explanations;
- available or planned experimental setting.

## For each central claim

Ask:

1. **Direct support** — what observation would directly support this claim?
2. **Alternative explanation** — what other mechanism could produce the same headline result?
3. **Control or ablation** — what comparison would separate the claim from that alternative?
4. **Direct metric** — what metric measures the claimed effect rather than only end-to-end performance?
5. **Strongest baseline** — what method or estimator embodies the strongest competing explanation?
6. **Falsifier** — what result would materially weaken or reject the claim?
7. **Status** — is the required evidence available, planned, or currently missing?

## Obligation types

Common obligations include:

- **effect obligation**: show the claimed effect exists;
- **mechanism obligation**: show the proposed mechanism, not an incidental change, explains the effect;
- **compute/control obligation**: match additional samples, calls, parameters, or compute;
- **scope obligation**: test whether the claim survives outside the narrow construction used to motivate it;
- **calibration obligation**: measure the specific decision quality the paper claims to improve;
- **ablation obligation**: remove or replace a component whose necessity is claimed.

## Experimental planning rule

Do not add an experiment only because it is conventional.

Every major experiment should answer a research question, support a central claim, eliminate a plausible alternative explanation, or delimit the scope of the conclusion.

Several claims may share one experiment, and one claim may require several obligations.

## From obligation to empirical question

Before drafting the Experiments section, convert each major obligation into a compact author-side experiment specification:

```text
claim being tested
-> empirical question
-> competing explanation
-> controlled variable(s)
-> independent variable
-> direct metric
-> secondary metric(s)
-> result pattern that supports the claim
-> result pattern that weakens or falsifies it
```

Not every field must appear explicitly in prose. The purpose is to make the experiment a causal test of a claim rather than a conventional benchmark row.

Prefer a **single-factor intervention** when possible: change the mechanism whose effect is being tested while holding rollout data, compute, model, prompts, environment interactions, or other relevant factors fixed.

For methods that alter rollout topology, branching, tool calls, retrieval calls, or external computation, matching those resources is part of the scientific control. Do not relegate this only to an efficiency appendix.

A headline task score is insufficient evidence for a mechanism claim when a more direct metric exists.

## Output

Use the [Experimental Obligation schema](../../schemas/experimental-obligation.md).

These obligations are constraints on later experiment design, not predictions of positive results.

## Literature grounding after obligation derivation

After deriving the obligations from the claims themselves, use [Literature grounding](literature-grounding.md) to identify concrete baselines, metrics, benchmark precedents, compute/call matching rules, and evaluation protocols.

Keep the order:

```text
claim
-> logical obligation
-> literature-supported operationalization
```

Do not reverse it by copying a prior paper's experiment table and treating those experiments as sufficient for our claims.
