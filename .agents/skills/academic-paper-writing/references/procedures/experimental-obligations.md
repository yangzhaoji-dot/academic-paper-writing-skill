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
