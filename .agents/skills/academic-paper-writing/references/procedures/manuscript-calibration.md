# Procedure: Final manuscript calibration

Goal: compare the **complete draft and rendered PDF** against a small set of real papers from the same venue and nearby technical area, then repair only clear manuscript-level deviations.

This is an internal checkpoint inside **Present**. It does not create a sixth execution phase.

## Inputs

Use:

- complete paper draft;
- rendered PDF;
- verified Venue Profile;
- Presentation Reference;
- Convention Profile;
- Layout Contracts;
- Section Contracts;
- Paper Core;
- 3–5 real reference papers from the same venue and, when possible, the same research family.

## Reference-set roles

Keep three roles separate even when one paper participates in more than one:

\`\`\`text
Scientific reference
-> supports prior-work / novelty / baseline reasoning

Discourse reference
-> informs section-level communication patterns

Manuscript reference
-> informs whole-paper density, visual hierarchy, and section balance
\`\`\`

Do not infer official venue rules from accepted papers. Hard constraints come only from the Venue Profile and official template.

When a Convention Profile exists, treat it as the canonical summary of layout, formula-exposition, information-carrier, and reviewer-expectation priors. Use manuscript references to validate or refresh that profile rather than mining an independent second set of conventions.

## Reference selection

Prefer a small distribution rather than one imitation target.

A useful set usually contains:

- 2–3 papers close in technical area or contribution type;
- 1–2 papers from the target venue with especially clear presentation;
- recent papers when venue conventions or agent-paper layout are changing.

Avoid selecting only papers whose structure already resembles the current draft.

## 1. Narrative calibration

Compare the full manuscript on dimensions such as:

### Introduction

- time to the concrete research problem;
- amount of generic background;
- when the method is named;
- how much Method detail appears early;
- whether contributions repeat the preceding paragraphs;
- whether evidence preview is proportional to available results.

### Method

- time from section start to the core mechanism;
- number and depth of subsections;
- balance among prose, equations, figures, and tables;
- whether the main estimator / algorithm is visually and rhetorically central;
- whether implementation detail obscures conceptual structure.

### Experiments

- prominence of the decisive experiment;
- size and readability of the main result table/figure;
- ordering of main effect, mechanism evidence, ablations, and robustness;
- amount of table narration versus scientific interpretation;
- whether negative or mixed results are qualified naturally.

### Whole paper

- repeated explanations across sections;
- transitions between sections;
- conclusion scope;
- appendix boundary;
- whether the manuscript feels like one continuous argument rather than concatenated modules.

## 2. Layout-contract calibration

Before distributional manuscript comparison, run the [Rendered Layout Verifier](rendered-layout-verifier.md).

Check:

- semantic owner section;
- prerequisite-before-visual ordering;
- first textual reference;
- cross-section float drift;
- two-column reading order;
- primary-attention competition;
- heading integrity.

A manuscript cannot pass final calibration with a blocking Layout Contract violation even if its overall page density resembles nearby papers.

## 3. Presentation calibration

Compare rendered-page behavior, not only source structure.

Inspect:

### First page

- title / abstract / Introduction density;
- whether the core problem is visible quickly;
- role and size of Figure 1;
- whether first-page visuals compete with the argument.

### Method pages

- overview figure size and placement;
- equation density;
- subsection fragmentation;
- whether definitions and main mechanism are visually discoverable.

### Experiment pages

- visual prominence of the decisive result;
- table font size and column density;
- plot readability;
- whether floats appear near the argument they support;
- whether analysis figures are accidentally placed before the Experiments section.

### Whole PDF

- dense vs sparse pages;
- excessive blank space;
- float drift;
- isolated headings;
- caption length;
- appendix transitions;
- consistency of typography and numbering.

## 4. Convention-prior calibration

Check the rendered manuscript against the Convention Profile on:

- first-page density and Figure 1 role;
- section balance;
- formula progression and equation density;
- prominence of the exact method update;
- information-carrier choices;
- main-result hierarchy;
- main-body / appendix boundary;
- soft reviewer expectations such as matched compute/call budget and uncertainty reporting when applicable.

A convention mismatch is not automatically a defect. Classify it as justified, acceptable, reader-cost increasing, or uncertain.

## 5. Deviation logic

Do not optimize toward an average paper mechanically.

Classify deviations as:

- **intentional and justified** — keep;
- **paper-specific but acceptable** — keep;
- **likely reader-cost increase** — repair;
- **likely venue/presentation defect** — repair;
- **uncertain** — do not change solely for conformity.

Examples of clear repair candidates:

- Introduction explains training schedules before the core problem is established;
- Method repeats the same Harness definition in prose, table, and figure;
- three small result tables have equal visual weight although one experiment is decisive;
- a training-dynamics figure floats into the Method section;
- a main result table uses unreadably small text;
- an official venue template is not actually used.

## 6. Preview mode

Support two manuscript modes:

\`\`\`text
real
synthetic_preview
\`\`\`

For \`synthetic_preview\`:

- clearly mark the document once, preferably with a cover notice or unobtrusive watermark;
- maintain a metadata record of fabricated values;
- write the paper body as a normal manuscript;
- do not scatter repeated red markers or "synthetic" warnings through every table and paragraph.

The preview marker must prevent confusion without making manuscript-quality evaluation impossible.

For \`real\`:

- no synthetic markers;
- every result must trace to verified experiment data.

## 7. Official-template gate

Before calling a manuscript venue-compliant:

\`\`\`text
target venue + year
-> official instructions verified
-> official template/style actually used
-> rendered PDF checked
\`\`\`

If the official target-year template is unavailable or not used:

\`\`\`text
presentation_status = preview_only
\`\`\`

Do not describe a manually approximated two-column layout as venue-compliant.

## 8. Repair policy

Repair the smallest responsible layer:

- overfull Introduction -> section information resolution;
- redundant Method -> representation allocation;
- weak main-result prominence -> evidence visual hierarchy;
- unreadable table -> table design;
- physical float drift -> local typesetting;
- semantic float drift -> Layout Contract / Page Composition;
- wrong venue formatting -> official-template realization;
- whole-paper imbalance -> page allocation;
- manuscript reads like stitched modules -> section transitions / discourse composition.

After repair, re-render and re-run only the affected calibration checks.

## Exit condition

Final calibration passes when:

- no hard venue violation remains;
- technical prerequisites remain intact;
- no blocking Layout Contract violation remains;
- no section is obviously over- or under-resolved;
- decisive evidence is visually prominent;
- prose/figure/table responsibilities are non-redundant;
- the rendered PDF is within the plausible manuscript distribution of strong nearby papers without copying any one paper.
