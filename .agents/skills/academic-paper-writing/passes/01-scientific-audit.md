# Pass 01 — Scientific Audit

## Responsibility

Determine whether the research is scientifically complete enough to become a methods paper.

This pass owns the [Scientific Spec](../schemas/scientific-spec.md).

It does **not** choose polished title wording, paper prose, page layout, or citation phrasing.

## Inputs

Use:

- Research Source Coverage;
- Research State;
- Technical State;
- method / loss / interface / experiment specifications;
- known evidence and open questions.

Read method-defining sources before deciding completeness.

## Required audit

### 1. Scientific problem

Freeze:

- setting;
- concrete failure / ambiguity;
- research question;
- scope;
- non-claims.

### 2. Baseline scientific object

Identify the exact baseline that the method modifies.

For an optimization paper, record:

- baseline state/action formulation;
- baseline objective;
- baseline reward / advantage / estimator;
- where credit is assigned;
- what is broadcast, masked, grouped, or normalized.

Do not assume a well-known baseline can be omitted from the scientific specification.

### 3. Method delta

State:

\`\`\`text
baseline
-> what changes
-> what remains unchanged
\`\`\`

If the method cannot be described as a concrete delta relative to its baseline, mark the spec incomplete.

### 4. Required equations

Create a list of equations that a technically competent reader must see to understand the contribution.

Typical requirements include:

- baseline objective;
- policy ratio or likelihood term;
- baseline credit estimator;
- proposed estimator;
- token / action / segment mapping;
- exact proposed update objective;
- correction or weighting term when sampling changes.

Missing equations are blocking scientific issues, not optional presentation details.

### 5. Required definitions and metrics

Identify any quantity that will appear in Method or Experiments and requires a formal definition.

Examples:

- regret;
- calibration target;
- cost-adjusted return;
- success;
- route / action probability;
- valid-call rate.

### 6. Assumptions and protocol exceptions

Record assumptions whose violation changes the estimator or interpretation.

### 7. Evidence status

Separate:

- observed evidence;
- planned evidence;
- missing evidence.

Never turn planned evidence into a result.

## Exit criteria

Freeze the Scientific Spec only when:

- the baseline is explicit;
- the method delta is explicit;
- all core equations are known or marked as blocking;
- central metrics have definitions or blocking issues;
- scientific assumptions and non-claims are recorded.

## Issue routing

This pass owns scientific omissions.

Later passes must route back:

- missing baseline;
- undefined metric;
- missing exact update;
- contradiction between method and loss;
- missing assumption;
- unsupported scientific object.

Do not let a writer patch these issues locally.
