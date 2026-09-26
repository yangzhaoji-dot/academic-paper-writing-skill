# Schema: Scientific Spec

Purpose: freeze the scientific object before packaging or prose writing.

\`\`\`yaml
status: draft | frozen | blocked

problem:
  setting:
  concrete_failure_or_ambiguity:
  research_question:
  scope:
  non_claims: []

baseline:
  name:
  formulation:
  state_and_action_space:
  objective:
  credit_assignment:
  required_equations: []
  source_dependencies: []

method_delta:
  what_changes: []
  what_stays_fixed: []
  new_objects: []
  operational_semantics: []

required_definitions:
  - name:
    definition:
    needed_for:

required_equations:
  - id:
    role:
    variables: []
    prerequisite_definitions: []
    status: complete | missing | uncertain

assumptions:
  - assumption:
    consequence:
    verification_status:

metrics:
  - name:
    definition_required: true
    scientific_role:
    formula_or_protocol:
    status: complete | missing | uncertain

evidence:
  available: []
  planned: []
  missing: []

technical_risks: []
open_scientific_questions: []

issues:
  - severity: blocking | major | minor
    owner_pass:
    description:
    required_action:
\`\`\`

## Invariant

A Scientific Spec is **not** a paper outline.

It answers:

- what scientific object is being studied;
- what baseline mathematical object the method modifies;
- what exact change the proposed method makes;
- which equations and metric definitions are required for the paper to be technically complete;
- what remains unknown.

After \`status: frozen\`, downstream passes may consume this state but may not silently rewrite it. New scientific gaps must be returned as issues to the Scientific Audit pass.
