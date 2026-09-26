# End-to-end workflow

The paper is constructed through four phases. Literature enters at explicit checkpoints rather than being treated as a late Related Work add-on.

## Phase I — Research understanding and scientific grounding

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

### 2. Candidate problem construction and framing

Starting from the narrow original idea, construct a candidate paper-level research problem through the smallest defensible chain:

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

### 3. Literature challenge

If external retrieval or verified literature is available, challenge the candidate framing before stabilizing it.

Use [Literature grounding](procedures/literature-grounding.md) to ask:

- has the problem already been formulated under another vocabulary?
- has the key distinction already appeared?
- does close prior work already solve the claimed mismatch?
- which part is known technique, which part is a verified difference, and which part remains uncertain?

Revise the framing to the narrowest version that survives this challenge.

Do not search only for papers that support the intended story.

### 4. Claim Graph + Claim–Literature Matrix

Transform the Research State and surviving framing into explicit claims. Every important claim receives:

- a claim type;
- evidence or support;
- scope;
- confidence;
- dependencies on earlier claims.

When literature is available, connect central claims to the closest work in a Claim–Literature Matrix. Separate:

- scientific precedent;
- overlap;
- verified difference;
- novelty candidate;
- conflicting evidence;
- unknown / incomplete search.

Absence of a found paper is not proof of novelty.

### 5. Paper Core + novelty boundary

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

Check the Paper Core against the closest work. The goal is to make the paper's boundary explicit:

```text
what is shared with prior work
vs.
what this paper changes, separates, measures, or enables
```

The abstract, introduction, method, experiments, and conclusion should express this same core at different levels of resolution rather than inventing section-local motivations.

### 6. Experimental obligations + literature grounding

For every central claim, derive the minimum evidence a skeptical reader would require before looking at what prior papers conventionally report.

Record:

- direct supporting observation;
- plausible alternative explanation;
- matched control or ablation;
- direct metric;
- strongest competing explanation;
- falsifying or weakening result.

Then use literature to refine:

- which baseline best instantiates the competing explanation;
- which metrics directly measure the claimed effect;
- benchmark precedents;
- matched-compute / matched-call controls;
- established protocol details and known failure modes.

The logical obligation comes first; literature helps operationalize it.

This branch can proceed in parallel with prose planning once the Paper Core and Claim Graph are stable.

## Phase II — Paper construction

### 7. Narrative

Choose the reveal order that makes the Paper Core persuasive and coherent. The Narrative is an author-side argumentative spine, not prose.

Examples include:

- concrete difficulty -> hidden distinction -> research problem -> method;
- existing formulation -> missing variable -> principle -> operationalization;
- observation -> inadequate explanation -> hypothesis -> method -> verification.

### 8. Reader Path

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

### 9. Section and module plan

Map the Reader Path and Narrative into paper sections, then into rhetorical modules.

A module answers a semantic function such as "expose the concrete ambiguity" or "state the method intuition". It is not a paragraph boundary.

Never assume one module equals one paragraph.

## Phase III — Writing with discourse grounding

### 10. Semantic draft

For each module, fill the required facts, claims, reasoning, and evidence.

For every nontrivial method component, establish:

```text
WHY -> WHAT -> HOW
```

Optimize for correctness, reader necessity, and completeness—not elegance.

### 11. Discourse grounding

When real relevant papers are available, use [Discourse grounding](procedures/discourse-grounding.md) to build section-specific Discourse References.

Extract abstract communication behavior from several papers:

- how the section enters the problem;
- how paragraphs create information needs;
- how distinctions are taught;
- when definitions, method names, and equations appear;
- how claims and results are qualified;
- how experiments are framed as questions.

Do not copy wording or imitate a single paper's sentence sequence.

Scientific literature evidence and discourse references remain separate state.

### 12. Reader-facing discourse composition

Combine neighboring modules into a coherent local argument using the Reader Path as the direct guide and compatible Discourse References as positive priors.

Decide:

- which semantic moves belong in the same paragraph;
- which concept should be concrete before it is named;
- what information can be compressed;
- which relation should be explicit or implicit;
- where definitions, equations, examples, and terminology become necessary;
- how one paragraph creates the need for the next.

The paper's own logic dominates. A reference pattern is used only when it fits the current scientific content.

### 13. Natural-language realization

Produce natural academic prose under the selected discourse/style/author profile.

The target is technical writing that reads as authored rather than assembled.

Naturalization may change sentence and paragraph boundaries but may not change facts, claim strength, citations, limitations, or the Paper Core.

## Phase IV — Review

### 14. Global review

Check:

- factual grounding of the research setting and structural claims;
- source support for literature statements;
- whether novelty language exceeds the verified literature boundary;
- whether the framing problem is real rather than rhetorically manufactured;
- claim-evidence alignment and scope;
- Paper Core consistency across sections;
- whether experiments discharge the central claims' obligations;
- whether selected baselines and metrics actually represent the intended competing explanations;
- reader effort and prerequisite order;
- semantic repetition;
- narrative continuity;
- terminology consistency;
- whether discourse references improved communication without causing source imitation;
- naturalness;
- limitation visibility.

Repair the earliest failing layer and rerun only downstream steps affected by that repair.

## Repair examples

```text
wrong fact
-> Research State

unsupported novelty / literature claim
-> Literature Map

inflated problem
-> Framing

sections tell different stories
-> Paper Core

claim lacks decisive experiment
-> Experimental Obligations

baseline/metric does not test the intended claim
-> Experiment Literature Grounding

argument is correct but hard to follow
-> Reader Path

method component appears unmotivated
-> Semantic Draft WHY/WHAT/HOW

paragraph flow is generic or assembled
-> Discourse Reference / Discourse Composition

sentence-level awkwardness only
-> Naturalization
```
