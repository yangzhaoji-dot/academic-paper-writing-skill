# Procedure: Venue-aware paper presentation and typesetting

Goal: map a scientifically stable paper into a venue-compliant, reader-efficient page layout without changing the Paper Core or claim scope.

This layer runs after the paper's scientific and discourse structure is sufficiently stable. It controls **where information appears on the page**, not what the paper claims.

## Three inputs

Use three distinct inputs:

1. **Venue Profile** — verified hard constraints from the target conference and year.
2. **Presentation Reference** — soft layout patterns abstracted from several recent papers in the same venue or closely related venues.
3. **Paper State** — section importance, Reader Path, equations, figures, tables, experiments, appendix candidates, and page budget.
4. **Layout Contracts** — semantic ownership, prerequisites, anchors, forbidden regions, and reading-order constraints for high-impact objects.

Hard venue rules always dominate soft presentation references.

## Venue resolution

Resolve the venue by **conference + year**, not conference name alone.

Preferred order:

\`\`\`text
official target-year author instructions / template
-> target-year Venue Profile
-> paper-specific information architecture
-> venue Presentation Reference
-> generic academic defaults
\`\`\`

A profile from another year is planning evidence only. It must never be treated as an authoritative submission rule for the target year.

If the target year's official instructions are not yet available:

- mark the profile as \`unverified_target_year\`;
- use the latest verified year only for provisional page planning;
- do not claim that page limits, anonymity rules, appendix rules, or checklist requirements are final;
- refresh the profile before submission or whenever the official call/template appears.

## Paper mode

Resolve one of:

```text
real
synthetic_preview
```

For `synthetic_preview`, mark the document once with a cover notice or unobtrusive watermark and keep fabricated values in metadata. Do not scatter repeated red markers or synthetic warnings through normal paper prose and tables.

For `real`, every result must trace to verified experiment data.

## Official-template gate

Before describing a manuscript as venue-compliant:

1. resolve conference + year;
2. verify official target-year instructions;
3. use the official template/style when available;
4. render the actual PDF;
5. inspect the rendered output.

If the official target-year template is unavailable or the manuscript uses a hand-built approximation:

```text
presentation_status = preview_only
```

A visually similar two-column layout is not venue compliance.

## Stage 1 — Content allocation

Allocate the page budget from scientific importance, not equal section sizes.

For each main-paper element, classify it as:

- **core claim** — required to understand or evaluate the central thesis;
- **technical prerequisite** — required to interpret a central variable, interface, equation, algorithm, transition, or result;
- **supporting** — useful but compressible;
- **appendix candidate** — needed for reproducibility, derivation, extended evidence, or reviewer inspection but not for first-pass understanding;
- **removable** — conventional or repetitive material with no unique role.

Technical prerequisites default to the main paper. They may move only if the relevant Section Contract shows that the dependency has already been established elsewhere or can be compressed without loss of meaning.

Do not solve page overflow by shrinking fonts, violating the template, or indiscriminately compressing figures.

Prefer this repair order:

\`\`\`text
remove repetition
-> move non-core, non-prerequisite detail to appendix
-> redesign table / figure
-> merge compatible exposition
-> compress wording
-> only then revisit section allocation
\`\`\`

## Prerequisite preservation gate

Before finalizing page allocation:

1. load the Section Contracts;
2. inspect every proposed appendix move;
3. reject any move that removes the only reader-visible definition of a downstream technical object;
4. ensure main-paper equations can be interpreted from definitions that remain in the main paper;
5. ensure interface semantics and protocol exceptions central to the method are not mislabeled as implementation detail.

If page pressure conflicts with a prerequisite, compress or visualize the prerequisite rather than deleting it.

## Evidence visual hierarchy

Use Experimental Obligations to classify evidence:

- **decisive** — directly tests the paper's central claim or excludes the strongest competing explanation;
- **supporting** — isolates a component or mechanism;
- **diagnostic** — explains behavior, failure modes, calibration, dynamics, or scope.

Presentation should reflect this hierarchy.

Typical mapping:

```text
decisive
-> largest main table / main plot / strongest visual placement

supporting
-> secondary table or ablation figure

diagnostic
-> analysis plot, compact table, or appendix when non-essential
```

Do not give three small tables equal visual prominence when one experiment carries the paper's main attribution claim.

## Stage 2 — Visual / equation / table planning

Ask whether each information object is best expressed as prose, equation, table, figure, or algorithm.

### Figures

A figure should perform a scientific communication role such as:

- expose the paper's core ambiguity;
- show system or rollout structure;
- explain a mechanism whose dependencies are hard to hold in prose;
- visualize training dynamics, calibration, or causal contrasts;
- summarize an experiment family.

Do not create a decorative architecture figure that merely restates text.

### Tables

Use tables for structured comparison.

Before typesetting a wide table, ask:

- which columns support a central claim?
- which rows are necessary baselines?
- can auxiliary metrics move to appendix?
- can paired conditions be grouped?
- is a plot a better representation?

Avoid using \`resizebox\` as the first response to an overfull table. Redesign the information first.

### Equations

Keep equations in the main paper when they define the contribution, estimator, objective, or a relation needed to understand experiments.

Move long derivations, routine algebra, or repeated special cases to appendix unless they are part of the central argument.

### Algorithms

Use pseudocode only when it reduces ambiguity about execution order, state updates, sampling, or optimization. Do not duplicate a Method subsection line by line.

## Stage 3 — Section-to-page architecture

Construct a provisional page plan.

Example logical fields:

\`\`\`yaml
page_budget:
  introduction:
  related_work:
  method:
  experiments:
  conclusion:
main_figures:
main_tables:
main_equations:
appendix_moves:
\`\`\`

These numbers are planning estimates, not fixed stylistic laws.

The allocation should change with:

- venue page limit;
- contribution type;
- density of the method;
- number of decisive experiments;
- whether the venue expects a mandatory checklist or impact / ethics statement;
- whether appendices are part of the same PDF.

## Stage 3.5 — Page composition from Layout Contracts

Before LaTeX float placement, compile Layout Contracts into page-composition constraints.

For each contracted object:

- place the float declaration after the intended semantic anchor when possible;
- preserve owner-section boundaries;
- honor single- vs double-column preference;
- avoid placing a primary visual beside another primary-attention paragraph/object;
- preserve heading integrity;
- keep the object within its allowed page distance from the first textual reference.

If constraints conflict, prefer semantic reading order over cosmetic compactness.

Do not rely on default LaTeX float behavior for objects with blocking Layout Contracts.

## Stage 4 — LaTeX realization

Use the official template and style files whenever available.

Do not:

- change margins, font sizes, line spacing, or style internals to gain space;
- bypass anonymity requirements;
- remove mandatory checklists or statements;
- use an obsolete template when a target-year template exists.

Do:

- keep labels and references consistent;
- use semantic LaTeX structure rather than manual spacing hacks;
- use \`booktabs\`-style tables when compatible with the template;
- keep captions informative but non-redundant;
- make figure text legible at final rendered size;
- keep equation breaking readable.

## Stage 5 — Rendered PDF review

Run [Rendered Layout Verifier](rendered-layout-verifier.md) before general visual calibration.



A source-level check is insufficient. Inspect the rendered PDF.

Review at least:

- first-page information density;
- whether the main problem and contribution become visible early enough;
- figure and table legibility at normal zoom;
- equation breaks;
- overfull / underfull areas;
- isolated headings or orphaned lines;
- visually dense pages;
- excessive blank space;
- caption length and duplication;
- whether related work or setup consumes disproportionate space;
- whether the main result / core method is visually buried;
- consistency of typography, references, and numbering.

In addition to physical defects, check for semantic placement violations:

- float appears before its owner section;
- float precedes required prerequisites;
- first textual reference appears after the float when disallowed;
- a float crosses Abstract / Introduction or Method / Experiments boundaries;
- two primary objects compete in the same visual band;
- a prior-section float obscures a new section heading.

Repair the earliest responsible layer:

- too much material -> content allocation;
- unreadable figure -> figure design;
- overwide table -> information/table design;
- equation overflow -> mathematical exposition / equation layout;
- bad page break -> local typesetting;
- semantic float drift -> Page Composition / Typesetting;
- bad layout contract -> Paper Architecture;
- venue violation -> Venue Profile / official template.

## Presentation reference

When several recent papers from the target venue are available, use [Presentation Reference](../../schemas/presentation-reference.md) to abstract soft tendencies such as:

- when the first conceptual figure appears;
- typical role of Figure 1;
- density and ordering of main tables;
- how much implementation detail moves to appendix;
- whether experiment subsections are question-driven;
- how captions carry context.

Do not imitate one paper's exact page design. Do not infer hard venue rules from accepted papers.

## Final manuscript calibration

After the full paper is rendered, run [Final manuscript calibration](manuscript-calibration.md).

Use 3–5 nearby real papers to compare:

- Introduction density and time to core problem;
- Method compression, figure/equation balance, and subsection depth;
- Experiment visual hierarchy and interpretation density;
- first-page layout;
- float placement;
- appendix boundary;
- whole-paper continuity.

These are soft calibration signals. They never override official venue rules or the paper's own scientific dependencies.

## Output

Maintain:

- a verified [Venue Profile](../../schemas/venue-profile.md);
- optional [Presentation Reference](../../schemas/presentation-reference.md);
- a paper-specific page / figure / table / appendix plan;
- frozen Layout Contracts;
- a rendered-layout verification record;
- a rendered-PDF review record.

This layer must never strengthen scientific claims merely to fit page constraints.
