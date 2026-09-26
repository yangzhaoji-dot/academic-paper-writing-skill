# End-to-end workflow

The paper is constructed through four phases. The phases separate research truth, paper-level reasoning, reader-facing explanation, and final review.

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

Do not force a mismatch framing when the work is better described as a direct empirical discovery, new capability, systems contribution, or straightforward method improvement.

### 3. Claim Graph

After selecting a framing, transform the Research State and framing into explicit claims. Every important claim receives:

- a claim type;
- evidence or support;
- scope;
- confidence;
- dependencies on earlier claims.

Distinguish direct findings from interpretations and broader implications.

### 4. Paper Core

Compress the selected framing and central claims into a stable Paper Core:

```text
concrete problem
+ key distinction
+ thesis
+ method role
+ one-line mechanism
+ evidence needed
+ non-claims
```

This is the story invariant for the paper.

The abstract, introduction, method, experiments, and conclusion should express this same core at different levels of resolution rather than inventing section-local motivations.

### 5. Experimental obligations

For every central claim, derive the minimum evidence a skeptical reader would require.

Record:

- direct supporting observation;
- plausible alternative explanation;
- matched control or ablation;
- direct metric;
- strongest competing baseline;
- falsifying or weakening result.

This branch can proceed in parallel with prose planning once the Paper Core and Claim Graph are stable.

## Phase II — Paper construction

### 6. Narrative

Choose the reveal order that makes the Paper Core persuasive and coherent. The Narrative is an author-side argumentative spine, not prose.

Examples include:

- concrete difficulty -> hidden distinction -> research problem -> method;
- existing formulation -> missing variable -> principle -> operationalization;
- observation -> inadequate explanation -> hypothesis -> method -> verification.

### 7. Reader Path

Convert the internal narrative into the shortest sequence of concepts the reader needs.

A typical Reader Path is:

```text
easy entry point
-> first new idea
-> concrete difficulty
-> key distinction
-> missing capability
-> solution requirement
-> method entry
```

Compress or omit internal framing nodes whenever the reader can infer them from a concrete example, causal statement, or comparison.

Do not expose planning labels merely because they exist internally.

### 8. Section and module plan

Map the Reader Path and Narrative into paper sections, then into rhetorical modules.

A module answers a semantic function such as "expose the concrete ambiguity" or "state the method intuition". It is not a paragraph boundary.

Never assume one module equals one paragraph.

## Phase III — Writing

### 9. Semantic draft

For each module, fill the required facts, claims, reasoning, and evidence.

For every nontrivial method component, establish:

```text
WHY -> WHAT -> HOW
```

Optimize for correctness, reader necessity, and completeness—not elegance.

### 10. Reader-facing discourse composition

Combine neighboring modules into a coherent local argument using the Reader Path as the direct guide.

Hide internal scaffolding. Compress abstract framing into concrete scientific statements when possible. Decide where examples, definitions, equations, and terminology are actually needed.

### 11. Natural-language realization

Produce natural academic prose under a style/author profile.

The target is technical writing that reads as authored rather than assembled.

Naturalization may change sentence and paragraph boundaries but may not change facts, claim strength, or the Paper Core.

## Phase IV — Review

### 12. Global review

Check:

- factual grounding of the research setting and structural claims;
- whether the framing problem is real rather than rhetorically manufactured;
- claim-evidence alignment and scope;
- Paper Core consistency across sections;
- whether experiments discharge the central claims' obligations;
- reader effort and prerequisite order;
- semantic repetition;
- narrative continuity;
- terminology consistency;
- naturalness;
- limitation visibility.

Repair the earliest failing layer and rerun only downstream steps affected by that repair.

## Repair examples

```text
wrong fact
-> Research State

inflated problem
-> Framing

sections tell different stories
-> Paper Core

claim lacks decisive experiment
-> Experimental Obligations

argument is correct but hard to follow
-> Reader Path

method component appears unmotivated
-> Semantic Draft WHY/WHAT/HOW

prose sounds assembled
-> Naturalization
```
