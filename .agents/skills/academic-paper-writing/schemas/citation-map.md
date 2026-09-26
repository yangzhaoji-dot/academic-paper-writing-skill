# Schema: Citation Map

Purpose: separate literature verification from prose generation.

\`\`\`yaml
status: draft | frozen | blocked

references:
  - key:
    title:
    authors:
    year:
    venue:
    publication_type:
    canonical_url:
    doi:
    arxiv_id:
    bibtex:
    metadata_status: verified | partial | unresolved
    source_used_for_verification:
    notes:

claim_support:
  - claim_id:
    claim:
    citation_keys: []
    support_type: background | definition | prior_method | comparison | benchmark | metric | protocol
    support_status: verified | insufficient | unresolved

closest_work:
  - citation_key:
    shared_problem:
    shared_mechanism:
    verified_difference:
    novelty_risk:
    evidence:

baseline_identity:
  - manuscript_label:
    citation_key:
    exact_method_or_adaptation:
    naming_rule:
    status: verified | ambiguous

section_usage:
  introduction: []
  related_work: []
  preliminaries: []
  method: []
  experiments: []

uncited_literature_dependent_claims: []
metadata_conflicts: []

issues:
  - severity: blocking | major | minor
    owner_pass:
    description:
    required_action:
\`\`\`

## Invariant

Writers do not invent citations or bibliographic metadata.

A downstream writer may request an additional source, but the source must be verified here before it enters the manuscript.

When an experiment uses only an adaptation of a prior estimator rather than the published method itself, record that distinction explicitly so the manuscript does not mislabel the baseline.
