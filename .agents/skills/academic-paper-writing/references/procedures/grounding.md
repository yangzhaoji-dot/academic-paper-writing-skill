# Procedure: Research grounding

Goal: establish complete source coverage, construct a factual Research State, and identify method-defining material that must enter Technical State before paper-level framing.

## Research Source Coverage

Before extracting the paper story, inventory available sources by role:

```text
idea / claims
method
interfaces / action space
state and transitions
training objective / loss
environment / data
experiments
implementation constraints
limitations / open questions
```

Read all sources likely to define a core method object. Do not stop after the README or primary method note when separate interface, loss, environment, or protocol specifications exist.

Record missing or unread sources as coverage gaps.

## Steps

1. Extract the research problem and setting.
2. Record the original idea in the narrowest technically accurate form.
3. Describe the implemented method and mechanism without promotional language.
4. Record experimental settings, baselines, metrics, and results supplied by the user or sources.
5. Record literature statements only when they are supplied or verified.
6. Record limitations, failed cases, uncertainty, and unresolved questions.
7. Mark missing information as unknown rather than completing it by plausibility.
8. Route operational method semantics to [Technical grounding](technical-grounding.md), including decision representations, interfaces, state changes, masks, sampling rules, and protocol exceptions.

## Output standard

The Research State should let another model answer "what was actually done and observed?" without seeing the intended paper story.

The source-coverage record should also make it possible to detect that a method-defining file or note has not yet been inspected.

Do not introduce:

- a gap merely because it sounds publishable;
- a universal statement about prior work without support;
- a stronger result than the evidence shows;
- a causal mechanism not demonstrated or argued by the research material.
