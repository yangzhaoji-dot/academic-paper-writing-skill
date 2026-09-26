# End-to-end workflow

The paper is constructed through five phases. Literature enters at explicit checkpoints rather than being treated as a late Related Work add-on.

## Phase I — Research understanding and scientific grounding

### 1. Research source coverage, Research State, and Technical State

First inventory the available research sources by role:

```text
idea / claims
method
interfaces / action space
state / transitions
training objective / loss
environment / data
experiments
implementation constraints
limitations / open questions
```

Do not assume the README or main method note is complete. If a source is likely to define a central method object and has not been inspected, mark grounding incomplete.

Then create two parallel states:

- **Research State**: what was actually proposed, implemented, observed, measured, or left unresolved;
- **Technical State**: what operational semantics must remain defined for the method to be well-formed.

Create a factual substrate from the available material. Record:

- problem and setting already explicit in the research material;
- original idea;
- method and mechanism;
- baselines and comparisons;
- experimental evidence;
- literature facts supplied or verified;
- limitations and unresolved questions.

Do not perform significance inflation here.

Use [Technical grounding](procedures/technical-grounding.md) to preserve interfaces, special-token representations, state transitions, action semantics, optimization masks, sampling semantics, and protocol exceptions. Paper Core compression must not delete these from the author-side state.

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

### 10. Section Contract, information resolution, and prerequisite graph

Before drafting a section, build a [Section Contract](procedures/section-contract.md) from:

- Paper Core;
- Claim Graph;
- Technical State;
- Experimental Obligations;
- Reader Path;
- concepts already established in previous sections.

The contract records:

- what the section must establish;
- what must be defined before use;
- what may be inherited;
- what must be explained now versus previewed or deferred;
- which representation should primarily carry each important concept;
- what may safely move later or to appendix;
- dependencies among technical objects;
- claims the section must not make.

Run [Section calibration](procedures/section-calibration.md) for substantial sections to check completeness, information resolution, representation redundancy, visual obligations, and real-paper discourse calibration.

A Method contract must explicitly cover decision/action spaces, representation, interfaces, state transitions, loss masks, sampling semantics, central variable meanings, and protocol exceptions whenever they are part of the method.

## Phase III — Writing with discourse grounding

### 11. Semantic draft

For each module, fill the required facts, claims, reasoning, and evidence.

For every nontrivial method component, establish:

```text
WHY -> WHAT -> HOW
```

Optimize for correctness, reader necessity, and completeness—not elegance.

Before discourse optimization, run the Section Contract gate. If a downstream equation, algorithm, or result depends on an undefined technical object, repair Technical State or Semantic Draft first.

### 12. Authorial synthesis

Before paragraph-level discourse composition, run [Authorial synthesis](procedures/authorial-synthesis.md).

Compress the author-side planning structure by:

- removing workflow commentary from the visible argument;
- merging internal nodes that belong to one reader-facing idea;
- choosing canonical terms and suppressing unnecessary synonyms;
- preserving a concrete anchor where it makes abstract distinctions easier to follow.

This step may simplify visible headings and terminology but may not remove Section Contract prerequisites, alter claim scope, or erase protocol exceptions.

### 13. Discourse grounding

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

### 14. Reader-facing discourse composition

Combine neighboring modules into a coherent local argument using the Reader Path as the direct guide and compatible Discourse References as positive priors.

Decide:

- which semantic moves belong in the same paragraph;
- which concept should be concrete before it is named;
- what information can be compressed;
- which relation should be explicit or implicit;
- where definitions, equations, examples, and terminology become necessary;
- how one paragraph creates the need for the next.

The paper's own logic dominates. A reference pattern is used only when it fits the current scientific content.

### 15. Natural-language realization

Produce natural academic prose under the selected discourse/style/author profile.

The target is technical writing that reads as authored rather than assembled.

Naturalization may change sentence and paragraph boundaries but may not change facts, claim strength, citations, limitations, or the Paper Core.

## Phase IV — Venue-aware presentation

### 16. Resolve target venue and year

Load a verified [Venue Profile](../schemas/venue-profile.md) using **conference + year**.

Hard requirements must come from official target-year instructions or templates. If the target year is not yet official, mark it as unverified and use the latest verified profile only for provisional planning.

### 17. Information architecture and page allocation

Use [Venue-aware presentation](procedures/venue-presentation.md) to decide:

- page budget by section;
- which concepts require figures;
- which comparisons belong in tables;
- which equations must stay in the main paper;
- whether pseudocode reduces ambiguity;
- what can move to appendix without damaging first-pass understanding.

The page limit should constrain presentation, not scientific truth. Do not weaken or inflate claims to fit the template.

Before moving content to appendix, re-run the relevant Section Contracts. Technical prerequisites default to the main paper unless they are already established elsewhere or can be compressed without breaking a dependency.

### 18. Template realization, rendered-PDF review, and manuscript calibration

Use the official target-year template whenever available.

After rendering, inspect the PDF itself for:

- first-page density;
- figure/table legibility;
- equation breaks;
- page balance;
- captions;
- section prominence;
- overfull/underfull areas;
- whether the method and main evidence are visually buried;
- mandatory venue elements.

A source-level LaTeX check is not sufficient.

If the paper is a synthetic workflow preview, mark it once at the document level rather than contaminating every table and paragraph with mock-data warnings.

After rendering, run [Final manuscript calibration](procedures/manuscript-calibration.md) against 3–5 nearby real papers. Compare whole-manuscript narrative density, visual hierarchy, float behavior, section balance, and appendix boundary.

## Phase V — Review

### 19. Global review

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
unread core technical source / incomplete operational definition
-> Research Source Coverage / Technical State

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

technical variable / interface / token / transition used before definition
-> Technical State / Section Contract

method component appears unmotivated
-> Semantic Draft WHY/WHAT/HOW

paragraph flow is generic or assembled
-> Discourse Reference / Discourse Composition

sentence-level awkwardness only
-> Naturalization

venue rule violation
-> Venue Profile / official template

main paper overcrowded
-> Content Allocation / Appendix Plan

figure or table unreadable
-> Visual / Table Design

bad rendered page break
-> Local Typesetting
```
