# Procedure: Paper Core

Goal: compress the selected framing and Claim Graph into one stable research story that every major section can express at a different level of detail.

## Why this layer exists

Framing describes the internal logic of the work. A paper still needs a smaller invariant that answers:

> What is this paper actually about?

Without this layer, the abstract, introduction, method, and experiments may each optimize their own local story.

## Construct the Paper Core

Record the following when supported:

1. **Concrete problem** — the actual difficulty, ambiguity, failure mode, or missing capability.
2. **Key distinction** — the conceptual split the reader must understand.
3. **Thesis** — the central relation the paper argues or tests.
4. **Method role** — what the proposed method does conceptually.
5. **Mechanism** — the one-line technical realization.
6. **Evidence needed** — the minimum observations required to make the thesis credible.
7. **Non-claims** — tempting statements that the current evidence does not support.

## Compression test

A good Paper Core should survive all of the following:

- remove the method name;
- remove implementation-specific notation;
- change paragraph order;
- shorten the introduction by half;
- explain the work to a reader before presenting equations.

If the central meaning changes under these operations, the core is still too tied to surface form.

## Section zoom

Map the same core to section roles:

```text
Abstract:
compressed problem -> method role -> strongest evidence

Introduction:
why the problem exists -> key distinction -> thesis -> method role -> evidence plan/results

Method:
formalize the distinction -> derive or implement the mechanism

Experiments:
test the thesis -> eliminate competing explanations -> quantify the claimed effect

Conclusion:
state the supported lesson at the same scope as the evidence
```

Do not use the section zoom as a rigid template. It is a consistency check.

## Output

Use the [Paper Core schema](../../schemas/paper-core.md).

Do not write polished prose at this stage.
