# H-PAIR v0.11 Layout-Contract Regression

## Failure being tested

Rendered first page:

~~~text
Abstract
↓
Figure 1
↓
Introduction heading
~~~

with Figure 1 semantically owned by the Introduction and its explanatory prose appearing later in the right column.

LaTeX may consider this placement legal.

The writing system must not.

## Why it fails

The visual creates several reader-path defects:

1. Figure 1 appears visually attached to the Abstract.
2. The Introduction heading no longer cleanly starts the section.
3. The figure appears before its conceptual prerequisites.
4. The first textual interpretation appears later.
5. The left-column figure competes with the right-column thesis / method paragraph.
6. Two-column geometry creates an ambiguous reading order.

## Expected Figure 1 Layout Contract

~~~yaml
id: fig1
object_type: figure
owner_section: Introduction
semantic_role: summarize policy-structure / flat-credit mismatch

prerequisites:
  must_be_established_before:
    - concrete Harness ambiguity
    - optional Harness changes policy structure
    - trajectory-level GRPO keeps credit flat

textual_reference:
  first_reference_required: true
  preferred_anchor: intro_p2_credit_mismatch
  must_not_precede_first_reference: true

semantic_placement:
  preferred_after: intro_p2_credit_mismatch
  preferred_before: intro_method_overview
  forbidden_regions:
    - Abstract
    - before Introduction heading
    - Related Work
  cross_section_boundary_allowed: false

physical_placement:
  preferred_width: single_column
  preferred_position: top
  fallback_positions:
    - inline_single_column
    - double_column_top
  max_page_distance_from_anchor: 1
  caption_budget: short
  page_prominence: primary

reading_order:
  required_before:
    - intro_p1_concrete_ambiguity
    - intro_p2_credit_mismatch
  required_after:
    - intro_heading
  avoid_side_by_side_with:
    - intro_core_method_paragraph
  heading_integrity_required: true
~~~

## Expected rendered-layout violation

~~~yaml
violation:
  type: semantic_float_drift
  object_id: fig1
  expected:
    owner_section: Introduction
    after: intro_p2_credit_mismatch
  actual:
    position: immediately after Abstract
    before: Introduction heading
  impact:
    - figure appears owned by Abstract
    - Introduction opening loses heading integrity
    - visual precedes prerequisites
    - two-column reading order becomes ambiguous
  repair_owner: typesetting
  severity: blocking
~~~

## Correct repair

If the contract is valid, do **not** rewrite the Introduction.

Repair only Page Composition / Typesetting:

~~~text
move figure declaration after anchor paragraph
-> constrain float within Introduction
-> rerender
-> verify reading order
~~~

If single-column placement still creates attention competition, use the declared fallback:

~~~text
double-column top after the semantic anchor
~~~

provided it does not cross a forbidden section boundary.

## Generalized regression cases

The verifier should also reject:

### Method figure before Method

~~~text
Related Work prose
Figure 2
Method heading
~~~

when Figure 2 is Method-owned.

### Main result before metric definition

~~~text
Main Table
Experiments setup
metric definition
~~~

when the result table requires the metric.

### Prior-section float occluding next heading

~~~text
Method closing paragraph
large Method table
Experiments heading squeezed beside/under float
~~~

### Reading-order inversion

Left column:

~~~text
main conceptual figure
~~~

Right column at same vertical band:

~~~text
paragraph that readers must understand before the figure
~~~

## Regression verdict

A layout system passes only if it distinguishes:

~~~text
physical legality
!=
semantic reading-order correctness
~~~

and routes the first H-PAIR screenshot failure to Layout Contract / Page Composition rather than prose rewriting.
