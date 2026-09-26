# Schema: Frozen Paper Spec

Purpose: provide one frozen interface that section writers can consume without re-deciding the paper.

\`\`\`yaml
status: draft | frozen | blocked

scientific_spec_ref:
citation_map_ref:

packaging:
  title:
  short_title:
  one_sentence_thesis:
  research_problem:
  key_insight:
  contribution_structure:
    - layer: problem | method | evidence | other
      statement:
      support_status:
  novelty_boundary:
  non_claims: []
  canonical_terms: []
  figure_1_message:
  core_equation_message:
  empirical_story:

formal_method:
  baseline_objective:
  baseline_credit_rule:
  method_factorization:
  method_delta:
  required_equations: []
  exact_update_equation:
  metric_definitions: []
  assumptions: []

architecture:
  sections:
    - name:
      scientific_role:
      must_include: []
      may_defer: []
      citations_required: []
      equation_ids: []
      visual_ids: []
      page_target:
  main_figures: []
  main_tables: []
  appendix_boundary: []
  venue:
    conference:
    year:
    status: verified | provisional

writer_contract:
  immutable_fields:
    - packaging
    - formal_method
    - architecture
  writers_may:
    - choose paragraph boundaries
    - choose local transitions
    - compress within section contracts
    - propose issues
  writers_may_not:
    - invent citations
    - remove required equations
    - change contribution scope
    - redefine baseline
    - change title/thesis silently
    - alter evidence status

open_issues: []
\`\`\`

## Freeze rule

Once \`status: frozen\`, section writers consume this spec.

If a writer discovers a contradiction, missing equation, unsupported claim, or missing citation, the writer emits an issue routed to the owning upstream pass. The writer does not patch the upstream state locally.
