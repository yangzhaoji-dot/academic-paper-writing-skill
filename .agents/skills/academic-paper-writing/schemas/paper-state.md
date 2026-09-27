# Schema: Paper State

```yaml
execution_mode: narrow_single_call | multi_pass

passes:
  scientific_audit:
    status: not_started | draft | frozen | blocked
  literature_citation_audit:
    status: not_started | draft | frozen | blocked
  convention_mining:
    status: not_started | draft | frozen | blocked
  paper_packaging:
    status: not_started | draft | frozen | blocked
  formal_method:
    status: not_started | draft | frozen | blocked
  paper_architecture:
    status: not_started | draft | frozen | blocked
  independent_audit:
    status: not_started | running | passed | blocked

scientific_spec: {}
citation_map: {}
convention_profile: {}
layout_contracts: []
frozen_paper_spec: {}

research_state: {}
technical_state: {}
source_coverage: []
literature:
  map: {}
  claim_literature_matrix: []
framing:
  original_idea:
  research_setting:
  structural_change:
  structural_mismatch:
  research_problem:
  method_role:
  technical_mechanism:
  paper_thesis:
claims: []
paper_core:
  concrete_problem:
  key_distinction:
  thesis:
  method_role:
  technical_mechanism:
  evidence_needed: []
  non_claims: []
experimental_obligations: []
experiment_literature_grounding: []
selected_framing:
narrative:
reader_path:
section_contracts:
  introduction: {}
  method: {}
  experiments: {}
  related_work: {}
  conclusion: {}
discourse_references:
  introduction: []
  method: []
  experiments: []
  related_work: []
venue:
  profile: {}
  presentation_reference: {}
paper_mode: real | synthetic_preview
presentation_status: venue_compliant | preview_only | unresolved
manuscript_reference_set: []
presentation:
  page_budget: {}
  main_figures: []
  main_tables: []
  main_equations: []
  algorithms: []
  appendix_moves: []
  evidence_visual_hierarchy: {}
  rendered_pdf_review: {}
  rendered_layout_verification: {}
  manuscript_calibration: {}
sections:
  introduction:
    modules: []
    semantic_draft:
    authorial_synthesis:
      surface_outline: []
      canonical_terms: []
      concrete_anchor:
      merge_decisions: []
      scaffold_to_remove: []
    discourse_plan:
    prose:
cross_pass_issues:
  - severity:
    owner_pass:
    description:
    required_action:
    invalidates: []

review:
  source_coverage:
  technical_completeness:
  prerequisite_integrity:
  factual_integrity:
  literature_integrity:
  framing_validity:
  paper_core_consistency:
  claim_calibration:
  experimental_coverage:
  reader_effort:
  information_resolution:
  representation_redundancy:
  authorial_synthesis:
  terminology_consistency:
  scaffold_leakage:
  discourse_reference_integrity:
  narrative_continuity:
  repetition:
  venue_compliance:
  presentation_quality:
  convention_alignment:
  layout_contract_integrity:
  naturalness:
```

This is a logical model. Chat, Codex, and API implementations may serialize it differently.

Scientific literature state and discourse-reference state are intentionally separate. A source may participate in both, but the evidence roles must not be conflated.
