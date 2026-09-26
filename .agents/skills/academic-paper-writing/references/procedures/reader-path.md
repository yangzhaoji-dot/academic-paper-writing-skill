# Procedure: Reader Path

Goal: convert the internal Framing and Narrative into the shortest reader-facing conceptual path that makes the method understandable and necessary.

## Input

Use:

- Paper Core;
- selected Narrative;
- Claim Graph;
- the reader knowledge reasonably assumed for the target venue;
- available examples from the Research State.

## Core rule

Do not translate the internal schema into sentences one node at a time.

Internal labels such as:

- research setting;
- structural change;
- structural mismatch;
- method role;
- broader implication;

are planning scaffolds. They should appear in prose only when they are themselves useful scientific terms.

## Build the path

Identify:

1. **Entry point** — what can the reader understand immediately with minimal setup?
2. **First new idea** — what is the first concept the paper actually needs to teach?
3. **Concrete difficulty** — what goes wrong, becomes ambiguous, or cannot be inferred?
4. **Illustrative case** — is there one concrete example that exposes the difficulty without adding unsupported facts?
5. **Key distinction** — what two cases, variables, causes, or decisions must the reader stop conflating?
6. **Missing capability** — what can the current training/model/evaluation signal not tell apart or optimize directly?
7. **Solution requirement** — what must any adequate solution be able to do?
8. **Method entry** — introduce the proposed method only after the solution requirement is visible.

## Compression rules

- Merge multiple framing nodes when one concrete observation conveys them.
- Prefer a causal relation over meta-language about "structure" when both are equivalent.
- Introduce terminology after the underlying phenomenon is clear unless the term is needed to state the phenomenon.
- Avoid requiring the reader to hold more than one new abstraction at a time.
- Remove a step if the reader can infer it safely.
- Do not delay the central difficulty behind broad historical background.

## Reader-path prompt

Use this mental prompt when needed:

> What is the shortest sequence of ideas that lets a skeptical reader understand why this method is needed, without exposing the author's internal planning scaffolds?

## Output

Use the [Reader Path schema](../../schemas/reader-path.md).

The Reader Path is not prose and is not required to preserve the names or boundaries of framing nodes.
