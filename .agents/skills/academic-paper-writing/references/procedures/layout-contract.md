# Procedure: Layout Contract Construction

Goal: turn representation responsibilities into explicit reader-order and float-placement constraints before typesetting.

This is **not a new user-facing pass**. It is a compiler step inside Paper Architecture and Present.

## Inputs

Use:

- Paper Architecture;
- Section Contracts;
- Convention Profile;
- representation allocation;
- visual / table / algorithm responsibilities;
- section dependency graph;
- target venue column/page format.

## When to create a contract

Create a Layout Contract for any object whose placement can materially change interpretation or reading flow:

- Figure 1 / conceptual overview;
- method overview figure;
- main result table;
- same-rollout / causal comparison table;
- large ablation table;
- algorithm;
- wide equation block;
- callout / theorem box when page placement matters.

Tiny local equations and incidental figures do not need separate contracts unless they have known placement risk.

## Construction sequence

### 1. Assign semantic owner

Ask:

> Which section owns the scientific meaning of this object?

Do not infer ownership from where LaTeX happens to place the float.

### 2. Record prerequisites

Ask:

> What must the reader already understand to read this object correctly?

Examples:

- Figure 1 may require the Harness ambiguity and flat-credit mismatch;
- a method overview may require the USE/SKIP decision definition;
- a main result table may require metric definitions;
- a calibration plot may require the calibration target and protocol.

### 3. Set first-reference relation

Record:

- first prose sentence expected to introduce the object;
- whether the object may precede that sentence;
- acceptable distance from the reference.

Default:

~~~text
prose introduces object
-> object appears nearby
-> prose interprets object
~~~

### 4. Set forbidden regions

Typical forbidden regions:

- before owner-section heading;
- inside Abstract region;
- before metric definition;
- before Method when the object is Method-owned;
- after the next major section when local interpretation would be lost.

### 5. Define physical preferences

Use venue format and Convention Profile:

- single-column vs double-column;
- top / bottom / inline;
- maximum acceptable page distance;
- caption length;
- primary / secondary / tertiary prominence.

These are preferences unless required by meaning.

### 6. Define reading-order dependencies

Represent relationships explicitly.

Example:

~~~yaml
required_before:
  - intro_p2_credit_mismatch
required_after:
  - abstract_end
  - intro_heading
avoid_side_by_side_with:
  - intro_p3_core_thesis
~~~

### 7. Freeze with Architecture

Layout Contracts are frozen with the Paper Spec.

Writers may write the textual anchors, but may not silently relocate the semantic owner.

## H-PAIR Figure 1 example

~~~yaml
id: fig1
object_type: figure
owner_section: Introduction
semantic_role: compress policy-structure / flat-credit mismatch

prerequisites:
  must_be_established_before:
    - concrete Harness invocation ambiguity
    - optional Harness changes policy structure
    - trajectory-level credit remains flat

textual_reference:
  first_reference_required: true
  preferred_anchor: after Introduction paragraph 2
  must_not_precede_first_reference: true

semantic_placement:
  preferred_after: intro_p2_credit_mismatch
  preferred_before: intro_method_overview
  forbidden_regions:
    - Abstract
    - before Introduction heading
    - Related Work

physical_placement:
  preferred_width: single_column
  preferred_position: top
  fallback_positions:
    - double_column_top
    - inline_single_column
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

This contract would reject a rendered layout in which Figure 1 appears directly after the Abstract and before the Introduction heading.

## Exit condition

A layout contract is ready when:

- owner section is explicit;
- prerequisites are explicit;
- first-reference relation is explicit;
- forbidden regions are explicit;
- physical preferences are defined;
- reading-order dependencies are defined where necessary;
- repair ownership is known.
