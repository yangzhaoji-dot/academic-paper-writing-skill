# Procedure: Rendered Layout Verifier

Goal: inspect the **rendered PDF** against frozen Layout Contracts.

Source-code validity is not sufficient.

## Inputs

Use:

- rendered PDF;
- Layout Contracts;
- Paper Architecture;
- Section Contracts;
- Convention Profile;
- page / float map when available.

## Verification order

### 1. Semantic ownership

For every contracted object:

- identify the page / column where it appears;
- identify the surrounding section heading;
- confirm the object visually belongs to its owner section.

Flag semantic_float_drift when LaTeX placement makes a float appear owned by another section.

### 2. Prerequisite ordering

Check whether every prerequisite in must_be_established_before is encountered before the visual in the likely reader order.

Flag prerequisite_after_visual when the figure/table requires a concept that appears only later.

### 3. First-reference ordering

Check:

- first textual reference;
- float position;
- page distance;
- whether the float appears substantially earlier than its introduction.

Flag float_precedes_anchor unless explicitly allowed.

### 4. Section-boundary integrity

Inspect high-risk boundaries:

- Abstract -> Introduction;
- Related Work -> Method;
- Method -> Experiments;
- main paper -> appendix.

Flag when:

- a prior-section float dominates the next heading;
- a next-section float appears above the prior section's closing prose;
- a conceptual figure appears visually attached to Abstract although owned by Introduction.

### 5. Two-column reading order

Estimate likely reading sequence:

~~~text
left column top -> left column bottom -> right column top -> right column bottom
~~~

while accounting for double-column floats.

Check explicit required_before / required_after dependencies.

Flag reading_order_inversion when geometry encourages an interpretation order that violates dependencies.

### 6. Attention competition

Inspect each vertical page band.

Flag primary_attention_competition when two primary objects compete, e.g.:

- left-column Figure 1 vs right-column thesis paragraph;
- two unrelated main tables;
- a large caption vs a section-opening paragraph.

### 7. Heading integrity

Check that each major heading visibly starts its section.

Flag heading_occluded_by_float when a float from another section visually consumes the opening.

### 8. Page-composition quality

Semantic placement can be correct while the page is still poorly composed.

Inspect every rendered page for:

- **composition underfill** — a large avoidable blank region caused by an over-constrained float or forced column break;
- **heading burst** — too many section/subsection transitions in a small page region, making the page read like an outline rather than a continuous argument;
- **hierarchy-transition density** — repeated major hierarchy changes on one page (e.g. Experiments -> Discussion -> Conclusion -> Appendix);
- **full-width-block page-break cost** — a figure/table satisfies its semantic contract but forces premature column termination or severe whitespace;
- **column imbalance** — one column terminates substantially earlier without semantic reason;
- **visual rhythm** — consecutive pages alternate between extreme density and sparse unused space because of compositor decisions.

Flag these separately from semantic float errors:

~~~text
composition_underfill
heading_burst
hierarchy_transition_overload
full_width_block_break_cost
column_imbalance
~~~

Do not optimize page fill by weakening scientific hierarchy. First reconsider float width, placement mode, local section boundary, or whether the object truly needs full-width treatment.

### 9. Physical integrity

Also check:

- overfull / clipped content;
- unreadable figure labels;
- table font size;
- caption density;
- excessive blank space;
- float drift;
- isolated heading;
- bad column balance.

## Violation format

~~~yaml
violation:
  type:
  object_id:
  expected:
  actual:
  impact:
    - ...
  repair_owner:
  severity: blocking | major | minor
~~~

## Repair routing

### Typesetting repair

Use when:

- Layout Contract is correct;
- rendered location violates it.

Examples:

- use stricter float placement;
- move float declaration after anchor paragraph;
- switch single-column to double-column top;
- use barrier / page-composition controls;
- shorten caption;
- redesign float size.

### Architecture repair

Use when:

- the requested placement itself creates a bad reader path;
- prerequisite relationships were wrong;
- primary prominence was misassigned.

Do not rewrite scientific claims to solve layout defects.

## Exit condition

Rendered layout passes when:

- all blocking Layout Contracts are satisfied;
- no semantic float drift remains;
- section boundaries are visually coherent;
- reading-order dependencies are respected;
- no major attention competition remains;
- no major page-composition defect remains;
- physical overflow / readability defects are repaired.
