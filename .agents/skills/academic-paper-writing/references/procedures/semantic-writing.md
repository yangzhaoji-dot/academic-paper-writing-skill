# Procedure: Semantic writing

Goal: fill each rhetorical module with correct semantic content before optimizing prose.

## For each module

1. Read the module's purpose and required inputs.
2. Select the smallest set of claims and facts needed to perform that function.
3. Identify which Reader Path step the module helps the reader cross.
4. Make the reasoning relation explicit in the semantic draft: contrast, cause, limitation, consequence, mechanism, evidence, or qualification.
5. Avoid restating a claim that has already been fully explained unless the new section gives it a different function.
6. Preserve uncertainty and limitations.

## Method components: WHY -> WHAT -> HOW

For every nontrivial method component, establish three semantic roles before writing polished prose:

```text
WHY:
What unresolved need from the preceding argument requires this component?

WHAT:
What conceptual operation does this component perform?

HOW:
What algorithm, equation, interface, or implementation realizes it?
```

The WHY must be meaningful independently of the component name.

Bad:

```text
WHY:
We need the branch module because H-PAIR contains a branch module.
```

Better:

```text
WHY:
One use/skip comparison estimates route preference but cannot distinguish better and worse executions within the selected route.

WHAT:
Obtain an execution contrast conditional on the same route.

HOW:
Sample repeated suffixes within each route and center their returns by the route mean.
```

Do not force WHY/WHAT/HOW into explicit headings or a visible component-by-component cadence in final prose. They are semantic completeness checks.

For mathematical Method sections, also record the **estimation or optimization question** that each equation answers. The preferred author-side chain is:

```text
unresolved question
-> quantity needed to answer it
-> definition / equation
-> interpretation
-> next unresolved question
```

An equation should not appear merely because the component has reached its HOW step. It should enter when the reader already understands why that mathematical object is needed.

## Semantic draft format

A semantic draft may be terse and structured:

```text
Reader need:
- ...

Facts:
- ...

Claim:
- ...

Reasoning:
- ...

WHY / WHAT / HOW (if a method component is introduced):
- ...

Transition target:
- ...
```

Polished language is not required here. Correctness and reader necessity are more important than fluency.

## Experiment subsections

For a major experiment subsection, do not semantically draft from a table outward. Start from the linked Experimental Obligation.

Record:

```text
Claim:
Empirical question:
Competing explanation:
Comparison / control:
Direct metric:
Planned or observed result:
Interpretation boundary:
Falsifier / weakening result:
```

When results do not yet exist, keep "Planned or observed result" explicitly unresolved. Do not write placeholder success claims.

In the finished section, these fields may compress into a few sentences. The internal representation exists to ensure that the experiment answers a paper question and that the interpretation does not exceed what the comparison isolates.
