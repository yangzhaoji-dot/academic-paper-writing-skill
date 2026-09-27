# Schema: Layout Contract

Purpose: encode **when and where a visual object may appear in the reader's path**, not only what scientific role it serves.

A Layout Contract is created during Paper Architecture / representation allocation and checked again after typesetting.

It is not a scientific object and may not change the paper's claims, equations, or evidence.

~~~yaml
layout_contract:
  id:
  object_type: figure | table | algorithm | equation_block | callout
  object_ref:
  owner_section:
  semantic_role:

  prerequisites:
    must_be_established_before: []
    may_be_previewed_before: []

  textual_reference:
    first_reference_required: true | false
    preferred_anchor:
    acceptable_anchor_range:
    must_not_precede_first_reference: true | false

  semantic_placement:
    preferred_after:
    preferred_before:
    forbidden_regions: []
    cross_section_boundary_allowed: true | false

  physical_placement:
    preferred_width: single_column | double_column | flexible
    preferred_position: top | bottom | inline | flexible
    fallback_positions: []
    max_page_distance_from_anchor:
    caption_budget: short | medium | long
    page_prominence: primary | secondary | tertiary

  reading_order:
    required_before: []
    required_after: []
    avoid_side_by_side_with: []
    heading_integrity_required: true | false

  failure_policy:
    on_semantic_drift:
      repair_owner: typesetting | architecture
    on_overflow:
      repair_owner: visual_design | typesetting
    on_attention_competition:
      repair_owner: page_composition | architecture

  status: draft | frozen | violated | satisfied
~~~

## Core invariants

### 1. Float ownership

A figure/table should not appear before the section that semantically owns it unless its contract explicitly allows teaser placement.

### 2. Prerequisite before visual

If a visual depends on a concept, that concept should normally be established before the visual appears.

A visual may introduce a concept only when the contract explicitly assigns it that introductory role.

### 3. First-reference ordering

By default, a float should not appear materially earlier than the prose that introduces it.

Exceptions such as first-page teaser figures must be explicit.

### 4. Section-boundary integrity

High-risk boundaries include:

- Abstract -> Introduction;
- Related Work -> Method;
- Method -> Experiments;
- main paper -> appendix.

A float must not make one section appear visually owned by another.

### 5. Reading-order dependency

In a two-column paper, geometric proximity is not sufficient.

Represent required reader order explicitly:

~~~text
paragraph P
-> Figure 1
-> paragraph Q
~~~

A rendered layout that visually encourages Q before Figure 1 may violate the contract even if LaTeX placement is legal.

### 6. Attention competition

Avoid placing two primary-attention objects side-by-side when both demand first reading.

Examples:

- a large conceptual figure in the left column next to the thesis paragraph in the right column;
- two unrelated full-height tables at the same vertical band;
- a section heading visually trapped beside a float owned by the previous section.

### 7. Heading integrity

A new section heading should visibly begin its section.

Do not let a float from the previous section dominate the region around the heading unless the contract explicitly permits it.

## Repair ownership

Distinguish two failure classes.

### Architecture failure

The contract itself requests a bad placement.

Repair:

~~~text
Paper Architecture
-> Layout Contract
-> downstream invalidation
~~~

### Typesetting / page-composition failure

The contract is correct but LaTeX floats drift.

Repair:

~~~text
Page Composition / Typesetting
-> re-render
~~~

Do not change scientific content to repair a float-placement problem.
