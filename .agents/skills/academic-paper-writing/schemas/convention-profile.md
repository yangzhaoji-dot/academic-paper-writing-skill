# Schema: Paper Convention Profile

Purpose: represent **how strong papers in the target venue / area are usually presented** without allowing presentation convention to redefine the science.

A Convention Profile contains two fundamentally different evidence classes:

1. **Hard constraints** — official venue/year rules.
2. **Soft priors** — distributional tendencies and reviewer expectations inferred from several nearby papers, checklists, and accepted-paper practice.

\`\`\`yaml
status: draft | frozen | blocked

target:
  venue:
  year:
  paper_type:
  research_area:
  nearest_subarea:

hard_rules:
  - rule:
    source:
    verified_for_target_year: true | false
    consequence_if_violated:

reference_set:
  accepted_or_relevant_papers:
    - citation_or_id:
      section_roles_used: []
  selection_rationale:
  sample_size:
  coverage_limitations: []

layout_prior:
  first_page:
    tendencies: []
    confidence: high | medium | low
    evidence_count:
  section_balance:
    tendencies: []
    confidence:
  figures:
    tendencies: []
    confidence:
  tables:
    tendencies: []
    confidence:
  appendix_boundary:
    tendencies: []
    confidence:

formula_prior:
  notation_introduction:
    tendencies: []
    strength: strong | medium | weak
  baseline_before_delta:
    expected: true | false | context_dependent
    strength:
  objective_progression:
    tendencies: []
  exact_update_visibility:
    expected: main_body | appendix_ok | context_dependent
    strength:
  variable_definition:
    tendencies: []
  equation_density:
    tendencies: []
  limiting_cases:
    tendencies: []
  correction_terms:
    tendencies: []

information_presentation_prior:
  introduction:
    expected_moves: []
    common_primary_carriers: []
    avoid_patterns: []
  related_work:
    expected_moves: []
    common_primary_carriers: []
    avoid_patterns: []
  preliminaries:
    expected_moves: []
    common_primary_carriers: []
    avoid_patterns: []
  method:
    expected_moves: []
    common_primary_carriers: []
    avoid_patterns: []
  experiments:
    expected_moves: []
    common_primary_carriers: []
    avoid_patterns: []
  discussion:
    expected_moves: []
    common_primary_carriers: []
    avoid_patterns: []

reviewer_expectations:
  - expectation:
    applies_when:
    strength: strong | medium | weak
    evidence:
    consequence_if_missing:
    hard_rule: true | false

representation_priors:
  - scientific_object_type:
    preferred_primary_carrier: prose | equation | figure | table | algorithm | plot
    alternatives: []
    rationale:
    confidence:

anti_patterns:
  - pattern:
    why_it_hurts:
    severity: major | moderate | minor
    applies_when:

uncertainties:
  - question:
    effect_on_writing:
    resolution_path:
\`\`\`

## Interpretation rules

### Hard rules

Hard rules must come from authoritative venue/year sources.

Examples:

- page limit;
- anonymity;
- required template;
- supplementary-material policy;
- mandatory checklist;
- submission-format constraints.

Never infer a hard rule from accepted-paper frequency.

### Soft priors

Soft priors describe what is **common, useful, or reviewer-friendly**, not mandatory.

Examples:

- methods papers often establish the baseline objective before the proposed update;
- a paper-level Figure 1 often communicates the central distinction rather than implementation detail;
- method-specific metrics are normally defined before their first result table;
- a controlled same-compute comparison is expected when the method changes rollout budget.

These must be stored with:

- applicability;
- strength;
- evidence;
- confidence.

### No-science-mutation invariant

Convention Profile may influence:

- information order;
- representation choice;
- section balance;
- equation exposition;
- main-body / appendix placement;
- figure / table prominence;
- reviewer-oriented completeness checks.

It may **not**:

- add a scientific claim;
- change an equation;
- invent an experiment;
- strengthen novelty;
- force three contributions;
- turn a soft convention into a hard venue rule;
- override Scientific Spec, Citation Map, or Formal Method.

## Distributional rule

Do not imitate one paper.

Prefer several papers and record the range of observed presentation choices. If nearby papers disagree, preserve the disagreement as a low-confidence or context-dependent prior rather than averaging it into a fake rule.
