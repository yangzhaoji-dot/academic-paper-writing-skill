# Procedure: Narrative planning

Goal: turn the Paper Core, selected framing, and claims into a global argumentative spine.

Narrative planning does not rediscover the research problem. It decides which part of the Paper Core the reader sees first and how the argument unfolds.

## Inputs

Use:

- Research State;
- selected Framing;
- Claim Graph;
- Paper Core;
- available evidence and limitations.

The selected Framing may contain:

```text
Original Idea
-> Research Setting
-> Structural Change
-> Structural Mismatch
-> Research Problem
-> Method Role
-> Technical Mechanism
```

Not every node must appear explicitly in the paper.

## Steps

1. Identify the Paper Core's primary problem and thesis.
2. Decide the reader's entry point: concrete situation, observation, limitation, structural change, ambiguity, or principle.
3. Order the remaining moves by dependency.
4. Ensure the method appears as a response to a previously visible need.
5. Ensure the technical mechanism appears as an implementation of the method role rather than the paper's reason for existing.
6. Attach each major empirical result or planned obligation to a claim it answers.
7. Remove framing nodes that are useful internally but unnecessary for the reader.
8. Preserve the same Paper Core across the whole paper even when local emphasis changes.

## Structural-mismatch narrative

When the selected framing is based on a real mismatch, an internal spine may be:

```text
Research setting
-> Structural change
-> Existing training/modeling structure
-> Mismatch
-> Consequence
-> Research problem
-> Method role
-> Technical mechanism
-> Evidence
```

Do not assume the final prose should verbalize this sequence. The Reader Path procedure will compress it into reader-facing logic.

## Alternative narrative emphasis

The same Paper Core can support different reveal orders:

- **setting-driven**: situation -> new decision/difficulty -> problem -> method;
- **problem-driven**: concrete failure/ambiguity -> underlying cause -> method;
- **principle-driven**: new structure -> principle -> operational method;
- **discovery-driven**: observation -> explanation -> hypothesis -> method -> verification.

The narrative layer changes reveal order and emphasis, not the factual substrate.

## Output

Represent the narrative as a sequence of argumentative moves, not polished paragraphs.

Then run the [Reader Path procedure](reader-path.md) before mapping the narrative to modules.
