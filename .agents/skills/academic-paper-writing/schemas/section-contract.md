# Schema: Section Contract

\`\`\`yaml
section:
role:
must_establish: []
must_define_before_use: []
must_not_claim: []
may_reference_as_established: []
information_resolution:
  must_explain_now: []
  preview_only: []
  defer_to_later_section: []
  defer_to_appendix: []
  omit_from_main_paper: []
representation_allocation:
  - item:
    primary_carrier: prose | figure | table | equation | algorithm
    secondary_mentions: []
visual_obligations:
  - concept:
    role:
    required_information: []
    best_form: figure | table | plot | equation | algorithm
may_defer: []
dependencies:
  - prerequisite:
    dependent:
    satisfied_by:
coverage:
  - item:
    status: covered | inherited | missing | deferred
    location:
contract_status: ready | blocked
blocking_reasons: []
\`\`\`

## Rules

- \`must_establish\` is semantic, not paragraph structure.
- A downstream technical object cannot be marked covered if its prerequisite is missing.
- \`may_defer\` must not contain the only definition needed to interpret a central equation, algorithm, or result.
- Presentation compression must preserve all non-inherited technical prerequisites.
