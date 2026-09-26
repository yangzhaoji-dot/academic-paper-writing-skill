# Procedure: Global review

Goal: locate the earliest layer responsible for a defect while evaluating scientific integrity, literature grounding, reader effort, and discourse quality.

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

## Pass 6 — reader effort

For each paragraph, ask:

1. What new thing must the reader understand here?
2. Does it require a concept that has not been explained?
3. Could several abstract sentences be replaced by one concrete example or causal statement?
4. Is the paragraph exposing the author's internal framing process instead of the scientific problem?
5. Is the main point delayed unnecessarily?
6. Does the paragraph introduce too many new abstractions at once?
7. Can a sentence be deleted without losing the argument?

If the scientific logic is correct but reader effort is high, repair the Reader Path before polishing sentences.

## Pass 7 — narrative continuity

Ask for each paragraph:

- Why is this paragraph here?
- What prior question does it continue?
- What later move does it enable?

Remove paragraphs that merely sound academic but do not advance the narrative.

## Pass 8 — discourse-reference integrity

When real-paper discourse references were used, check:

- patterns were abstracted rather than copied;
- several references were combined when possible;
- no distinctive phrase or close sentence skeleton was transferred;
- the paragraph sequence does not mirror one source mechanically;
- a reference pattern did not import another paper's problem statement or scientific claim;
- our Reader Path still determines the argument.

A smoother draft is not an improvement if it becomes derivative.

## Pass 9 — semantic repetition

Track repeated concepts, not only repeated words. A core claim may recur when its rhetorical role changes, but full re-explanation should be rare.

## Pass 10 — venue and presentation integrity

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

## Pass 11 — naturalness

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

- wrong fact -> Research State;
- unsupported literature / novelty -> Literature Map;
- artificial problem -> Framing;
- inconsistent paper story -> Paper Core;
- untested claim -> Experimental Obligations;
- weak baseline/metric grounding -> Experiment Literature Grounding;
- hard-to-follow explanation -> Reader Path;
- missing method motivation -> Semantic Draft;
- derivative or generic paragraph flow -> Discourse Reference / Discourse Composition;
- venue violation -> Venue Profile / official template;
- poor page allocation -> Presentation Plan;
- unreadable figure/table -> Visual or Table Design;
- local rendered-layout defect -> Typesetting;
- awkward language only -> Naturalization.
