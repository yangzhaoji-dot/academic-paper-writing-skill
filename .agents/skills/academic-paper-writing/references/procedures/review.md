# Procedure: Global review

Goal: locate the earliest layer responsible for a defect while evaluating both scientific integrity and reader effort.

## Pass 1 — factual integrity

Check every concrete technical and empirical statement against the Research State.

Flag:

- invented results;
- altered numbers;
- unsupported dataset or baseline properties;
- fabricated citations or literature consensus.

## Pass 2 — framing and claim calibration

Check whether:

- the research setting and structural problem are defensible;
- a mismatch has been manufactured only for narrative convenience;
- each sentence preserves the claim type and scope;
- broader implications remain broader implications;
- correlations are not rewritten as mechanisms;
- results on one setting are not generalized without support.

## Pass 3 — Paper Core consistency

Check the abstract, introduction, method, experiments, and conclusion against the same Paper Core.

Ask:

- Are they describing the same problem and key distinction?
- Does the method solve the problem the introduction actually motivates?
- Do the experiments test the thesis rather than a nearby easier claim?
- Does the conclusion stay within the evidence-supported scope?

If a section requires a different core story to make sense, repair the Paper Core, framing, or section plan.

## Pass 4 — experimental obligations

For every central claim, check whether the available or planned experiments discharge the corresponding obligations.

Flag:

- headline benchmark gains with no direct metric for the claimed mechanism;
- extra compute, samples, or tool calls that could explain the result;
- missing controls for a plausible alternative explanation;
- a claimed component with no ablation or matched comparison;
- a claim whose falsifying outcome was never defined.

## Pass 5 — reader effort

For each paragraph, ask:

1. What new thing must the reader understand here?
2. Does it require a concept that has not been explained?
3. Could several abstract sentences be replaced by one concrete example or causal statement?
4. Is the paragraph exposing the author's internal framing process instead of the scientific problem?
5. Is the main point delayed unnecessarily?
6. Does the paragraph introduce too many new abstractions at once?
7. Can a sentence be deleted without losing the argument?

If the scientific logic is correct but reader effort is high, repair the Reader Path before polishing sentences.

## Pass 6 — narrative continuity

Ask for each paragraph:

- Why is this paragraph here?
- What prior question does it continue?
- What later move does it enable?

Remove paragraphs that merely sound academic but do not advance the narrative.

## Pass 7 — semantic repetition

Track repeated concepts, not only repeated words. A core claim may recur when its rhetorical role changes, but full re-explanation should be rare.

## Pass 8 — naturalness

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
- artificial problem -> Framing;
- inconsistent paper story -> Paper Core;
- untested claim -> Experimental Obligations;
- hard-to-follow explanation -> Reader Path;
- missing method motivation -> Semantic Draft;
- awkward language only -> Naturalization.
