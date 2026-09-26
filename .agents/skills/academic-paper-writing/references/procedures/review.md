# Procedure: Global review

Goal: locate the earliest layer responsible for a defect while evaluating scientific integrity, literature grounding, reader effort, and discourse quality.

## Pass 0 — source coverage and technical completeness

Before reviewing prose, verify:

- all method-defining research sources were inspected;
- interface / action-space documents were not omitted;
- loss / optimization specifications were inspected;
- environment and training-protocol notes that affect method semantics were inspected;
- Technical State contains the operational meaning of every central variable, interface, transition, mask, and protocol exception used in the paper.

Flag:

- equations whose variables have no operational definition;
- tool / Harness names without state and USE/NO semantics;
- special tokens or structured actions used without representation rules;
- a generic protocol description that silently erases a real exception;
- branch or sampling rules that conflate where decisions exist with where extra samples are collected.

If this pass fails, stop surface review and repair Research Source Coverage or Technical State.

## Pass 1 — factual integrity

Check every concrete technical and empirical statement against the Research State.

Flag:

- invented results;
- altered numbers;
- unsupported dataset or baseline properties;
- fabricated citations or literature consensus.

## Pass 2 — literature and novelty integrity

Check every literature-dependent statement against the Literature Map or verified source.

Flag:

- "prior work" claims with no source;
- novelty stated from search absence alone;
- a prior technique relabeled as our novelty;
- a difference from closest work that is not concretely evidenced;
- a baseline, metric, or protocol justified by convention when no such precedent was verified;
- scientific support inferred from a paper used only as a discourse reference.

If this pass fails, repair the Literature Map, Claim–Literature Matrix, or claim scope before rewriting prose.

## Pass 3 — framing and claim calibration

Check whether:

- the research setting and structural problem remain defensible after literature challenge;
- a mismatch has been manufactured only for narrative convenience;
- each sentence preserves the claim type and scope;
- broader implications remain broader implications;
- correlations are not rewritten as mechanisms;
- results on one setting are not generalized without support.

## Pass 4 — Paper Core consistency

Check the abstract, introduction, method, experiments, and conclusion against the same Paper Core.

Ask:

- Are they describing the same problem and key distinction?
- Does the method solve the problem the introduction actually motivates?
- Do the experiments test the thesis rather than a nearby easier claim?
- Does the conclusion stay within the evidence-supported scope?
- Is the stated contribution consistent with the verified novelty boundary?

If a section requires a different core story to make sense, repair the Paper Core, framing, or section plan.

## Pass 5 — experimental obligations

For every central claim, check whether the available or planned experiments discharge the corresponding obligations.

Flag:

- headline benchmark gains with no direct metric for the claimed mechanism;
- extra compute, samples, or tool calls that could explain the result;
- missing controls for a plausible alternative explanation;
- a claimed component with no ablation or matched comparison;
- a claim whose falsifying outcome was never defined;
- a selected baseline that does not actually represent the competing explanation it is supposed to test.

## Pass 6 — Section Contract and prerequisite integrity

For each section:

- all `must_establish` items are covered;
- all downstream-used definitions are covered or legitimately inherited;
- dependency edges do not point to missing prerequisites;
- appendix moves do not contain the only definition of a central technical object;
- section compression has not removed interface, action, state-transition, or mask semantics required to interpret the method.

If a technically necessary definition is missing, repair Technical State, Section Contract, Module Plan, or Semantic Draft before rewriting prose.

## Pass 7 — convention integrity

Check the active Convention Profile.

Flag:

- a soft academic tendency represented as a hard rule;
- a venue rule inferred only from accepted-paper frequency;
- a formula exposition that hides the baseline object or exact update when the paper's method depends on them;
- a method-specific metric first appearing in a result table;
- critical evidence moved to appendix only to mimic a reference paper;
- a representation choice that conflicts with both the scientific role and the convention prior without justification;
- contribution-count or section-count rules imposed mechanically.

If this pass fails, repair Convention Mining or Architecture. Do not rewrite the science to satisfy convention.

## Pass 8 — section calibration

For each substantial section, check:

- information required now is not deferred;
- later-section detail is not introduced prematurely;
- one primary representation carries each important concept;
- prose/table/figure/equation responsibilities are not mechanically duplicated;
- visual obligations exist only where they reduce reader effort or expose structure;
- section density and reveal order remain plausible relative to several nearby real papers.

Flag:

- an Introduction that explains the full training schedule;
- a Method that defines the same Harness semantics in prose, table, and figure;
- an Experiments section where decisive and diagnostic results receive equal visual weight;
- a figure that adds no information beyond adjacent prose.

If this pass fails, repair Section Calibration or Representation Allocation before sentence-level rewriting.

## Pass 9 — reader effort

For each paragraph, ask:

1. What new thing must the reader understand here?
2. Does it require a concept that has not been explained?
3. Could several abstract sentences be replaced by one concrete example or causal statement?
4. Is the paragraph exposing the author's internal framing process instead of the scientific problem?
5. Is the main point delayed unnecessarily?
6. Does the paragraph introduce too many new abstractions at once?
7. Can a sentence be deleted without losing the argument?

If the scientific logic is correct but reader effort is high, repair the Reader Path before polishing sentences.

## Pass 10 — authorial synthesis

Check whether the manuscript surface is still mirroring internal planning structure.

Flag:

- workflow commentary such as "the decisive experiment", "the primary result", "to test our claim", or "we separate the evaluation into" when the science can state the setup or observation directly;
- one subsection per internal mechanism or schema node;
- repeated near-synonyms for one concept (`gate`, `routing decision`, `mode`, `semantic route`) without a real technical distinction;
- contribution bullets that describe evaluation design rather than research contribution;
- experiment prose that announces claim/evidence structure instead of moving from comparison to observation to interpretation;
- long abstract passages with no concrete state, trajectory, example, mathematical object, or comparison for the reader to follow.

If the science is complete but the paper reads like an explanation of its own construction process, repair [Authorial synthesis](authorial-synthesis.md) before discourse or sentence-level rewriting.

## Pass 11 — narrative continuity

Ask for each paragraph:

- Why is this paragraph here?
- What prior question does it continue?
- What later move does it enable?

Remove paragraphs that merely sound academic but do not advance the narrative.

## Pass 12 — discourse-reference integrity

When real-paper discourse references were used, check:

- patterns were abstracted rather than copied;
- several references were combined when possible;
- no distinctive phrase or close sentence skeleton was transferred;
- the paragraph sequence does not mirror one source mechanically;
- a reference pattern did not import another paper's problem statement or scientific claim;
- our Reader Path still determines the argument.

A smoother draft is not an improvement if it becomes derivative.

## Pass 13 — semantic repetition

Track repeated concepts, not only repeated words. A core claim may recur when its rhetorical role changes, but full re-explanation should be rare.

## Pass 14 — venue and presentation integrity

Check:

- target conference and year were resolved explicitly;
- hard formatting rules come from official target-year sources;
- an older Venue Profile is not being treated as current;
- main-page allocation reflects scientific importance;
- core figures, tables, and equations remain legible;
- appendix moves do not hide information required to understand or evaluate the central claim;
- mandatory checklist / statements / anonymity rules are satisfied;
- the rendered PDF, not only the source, has been inspected.

Flag:

- font or margin hacks used to gain space;
- wide tables shrunk until unreadable rather than redesigned;
- figures whose labels cannot be read at final size;
- main claims pushed into appendix solely to fit a conventional section;
- page overflow repaired by deleting limitations or controls;
- stale conference rules.

## Pass 15 — final manuscript calibration

After rendering the complete paper, compare it with 3–5 nearby real papers using [Final manuscript calibration](manuscript-calibration.md).

Check:

- first-page density and Figure 1 role;
- Introduction time to the concrete problem;
- Method overview-figure / equation / prose balance;
- experiment visual hierarchy;
- float placement;
- table readability;
- subsection fragmentation;
- appendix boundary;
- whole-paper continuity.

Repair only deviations that plausibly increase reader cost or weaken presentation. Do not force conformity to one reference paper.

If the official target-year template is not actually used, the manuscript remains `preview_only`.

## Pass 16 — naturalness

Inspect:

- transition overuse;
- repetitive sentence shapes;
- generic filler;
- paragraph boundaries that mirror module boundaries too mechanically;
- one-sentence-per-internal-node realization;
- abrupt topic shifts;
- excessive noun stacking or vague abstraction.

## Repair policy

Repair the earliest failing representation, then regenerate only downstream content affected by the change.

Typical routing:

- unread method-defining source -> Research Source Coverage;
- missing operational definition / interface / token / transition -> Technical State;
- missing section prerequisite -> Section Contract / Module Plan;
- wrong fact -> Research State;
- unsupported literature / novelty -> Literature Map;
- artificial problem -> Framing;
- inconsistent paper story -> Paper Core;
- untested claim -> Experimental Obligations;
- weak baseline/metric grounding -> Experiment Literature Grounding;
- hard-to-follow explanation -> Reader Path;
- overfull / prematurely detailed section -> Section Calibration;
- redundant prose/table/figure explanation -> Representation Allocation;
- workflow/scaffold leakage -> Authorial Synthesis;
- over-fragmented subsection structure -> Authorial Synthesis;
- terminology drift / synonym overload -> Authorial Synthesis;
- missing concrete anchor in abstraction-heavy exposition -> Authorial Synthesis;
- missing method motivation -> Semantic Draft;
- derivative or generic paragraph flow -> Discourse Reference / Discourse Composition;
- venue violation -> Venue Profile / official template;
- poor page allocation -> Presentation Plan;
- unreadable figure/table -> Visual or Table Design;
- local rendered-layout defect -> Typesetting;
- convention profile missing / stale / over-hardcoded -> Convention Mining;
- whole-paper density / visual hierarchy mismatch -> Final Manuscript Calibration;
- awkward language only -> Naturalization.
