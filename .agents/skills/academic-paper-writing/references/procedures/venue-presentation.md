# Procedure: Venue-aware paper presentation and typesetting

Goal: map a scientifically stable paper into a venue-compliant, reader-efficient page layout without changing the Paper Core or claim scope.

This layer runs after the paper's scientific and discourse structure is sufficiently stable. It controls **where information appears on the page**, not what the paper claims.

## Three inputs

Use three distinct inputs:

1. **Venue Profile** — verified hard constraints from the target conference and year.
2. **Presentation Reference** — soft layout patterns abstracted from several recent papers in the same venue or closely related venues.
3. **Paper State** — section importance, Reader Path, equations, figures, tables, experiments, appendix candidates, and page budget.

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

## Stage 1 — Content allocation

Allocate the page budget from scientific importance, not equal section sizes.

For each main-paper element, classify it as:

- **core** — required to understand or evaluate the central claim;
- **supporting** — useful but compressible;
- **appendix candidate** — needed for reproducibility, derivation, extended evidence, or reviewer inspection but not for first-pass understanding;
- **removable** — conventional or repetitive material with no unique role.

Do not solve page overflow by shrinking fonts, violating the template, or indiscriminately compressing figures.

Prefer this repair order:

\`\`\`text
remove repetition
-> move non-core detail to appendix
-> redesign table / figure
-> merge compatible exposition
-> compress wording
-> only then revisit section allocation
\`\`\`

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

Repair the earliest responsible layer:

- too much material -> content allocation;
- unreadable figure -> figure design;
- overwide table -> information/table design;
- equation overflow -> mathematical exposition / equation layout;
- bad page break -> local typesetting;
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

## Output

Maintain:

- a verified [Venue Profile](../../schemas/venue-profile.md);
- optional [Presentation Reference](../../schemas/presentation-reference.md);
- a paper-specific page / figure / table / appendix plan;
- a rendered-PDF review record.

This layer must never strengthen scientific claims merely to fit page constraints.
