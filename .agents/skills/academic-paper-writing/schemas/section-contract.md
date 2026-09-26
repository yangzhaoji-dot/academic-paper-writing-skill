# Schema: Section Contract

\`\`\`yaml
section:
role:
must_establish: []
must_define_before_use: []
must_not_claim: []
may_reference_as_established: []
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
