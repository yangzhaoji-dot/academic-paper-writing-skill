# End-to-end workflow

The paper is constructed through four phases.

## Phase I — Research understanding

### 1. Research State

Create a factual substrate from the available material. Record:

- problem and setting already explicit in the research material;
- original idea;
- method and mechanism;
- baselines and comparisons;
- experimental evidence;
- literature facts supplied or verified;
- limitations and unresolved questions.

Do not perform significance inflation here.

### 2. Problem construction and framing

Starting from the narrow original idea, construct a paper-level research problem through the smallest defensible chain:

```text
Original Idea
-> Research Setting
-> Structural Change
-> Structural Mismatch
-> Research Problem
-> Method Role
-> Technical Mechanism
```

The key question is not merely "why is this important?" but:

> In what broader research setting does this idea become structurally meaningful, and what changes in that setting make the old modeling, training, supervision, optimization, or evaluation structure incomplete?

Typical structural changes include:

- a new decision variable;
- a new stage in the policy or system;
- a new interface;
- a new conditional dependency;
- new external state or computation;
- a new optimization object;
- a new source of heterogeneity.

Typical mismatches include:

- policy structure vs. credit structure;
- system structure vs. optimization structure;
- decision structure vs. supervision structure;
- architecture vs. training objective;
- capability vs. interface;
- state structure vs. representation.

Do not force a mismatch framing when the work is better described as a direct empirical discovery, new capability, systems contribution, or straightforward method improvement.

The selected framing must record what is factual, what is interpretation, and what remains a broader implication.

### 3. Claim Graph

After selecting a framing, transform the Research State and framing into explicit claims. Every important claim receives:

- a claim type;
- evidence or support;
- scope;
- confidence;
- dependencies on earlier claims.

Distinguish direct findings from interpretations and broader implications.

Claims should formalize the selected problem construction rather than silently widening it.

## Phase II — Paper construction

### 4. Narrative

Choose the story logic that makes the selected framing and claims cohere. The narrative is a sequence of argumentative moves, not prose.

A structural-mismatch framing often yields:

```text
research setting
-> structural change
-> mismatch
-> consequence
-> research problem
-> method role
-> technical mechanism
-> evidence
```

Other valid examples include:

- existing paradigm -> hidden limitation -> consequence -> insight -> method -> evidence;
- existing formulation -> missing variable -> new principle -> operationalization -> evidence;
- observation -> inadequacy of current explanation -> hypothesis -> method -> verification.

### 5. Section and module plan

Map the narrative into paper sections, then into rhetorical modules. A module answers a semantic function such as "establish the existing paradigm" or "state the core insight".

Never assume one module equals one paragraph.

## Phase III — Writing

### 6. Semantic draft

For each module, fill the required facts, claims, reasoning, and evidence. Optimize for semantic correctness and completeness, not elegance.

### 7. Discourse composition

Combine neighboring modules into a coherent local argument. Resolve ordering, references, information density, and transition structure.

### 8. Natural-language realization

Produce natural academic prose under a style/author profile. Avoid formulaic LLM phrasing and excessive explicit transitions.

## Phase IV — Review

### 9. Global review

Check:

- factual grounding of the research setting and structural claims;
- whether the mismatch is real rather than rhetorically manufactured;
- claim-evidence alignment;
- claim strength;
- semantic repetition;
- narrative continuity;
- terminology consistency;
- section purpose;
- naturalness;
- limitation visibility.

Repair the earliest failing layer and rerun only downstream steps affected by that repair.
