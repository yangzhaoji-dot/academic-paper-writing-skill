# Schema: Technical State

\`\`\`yaml
source_coverage:
  - role:
    sources: []
    status: complete | partial | unknown
    unresolved: []

objects:
  - id:
    type:
    definition:
    source:

decision_space:
  - id:
    variable:
    choices: []
    representation:
    occurs_at:
    constraints: []

states:
  - id:
    owner:
    fields: []
    visibility:
    persistence:
    update_rule:

interfaces:
  - id:
    component:
    api:
    reads: []
    writes: []
    call_timing:
    returns:
    cost:
    information_boundary:
    notes:

transitions:
  - id:
    preconditions: []
    decision:
    effects: []
    observation:
    next_state:

optimization:
  policy_regions: []
  masked_regions: []
  advantage_assignment: []
  corrections: []
  schedules: []

sampling:
  natural_decisions: []
  selected_sampling_locations: []
  forced_choices: []
  restored_state: []
  held_fixed: []
  comparison_groups: []

protocol_exceptions: []

dependencies:
  - prerequisite:
    dependent:
    reason:

unknowns: []
conflicts: []
\`\`\`

This state preserves operational semantics that may disappear from a compressed Paper Core.

Not every field must appear in the paper. Section Contracts determine which technical prerequisites must be reader-visible.
