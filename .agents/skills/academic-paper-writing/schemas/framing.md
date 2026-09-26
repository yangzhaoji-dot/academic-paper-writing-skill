# Schema: Framing

Use this logical schema to represent problem construction.

```yaml
original_idea:
  statement:

research_setting:
  name:
  definition:
  support:
  why_this_work_belongs_here:

structural_change:
  old_structure:
  new_structure:
  changed_variables_or_dependencies: []

structural_mismatch:
  system_side:
  training_modeling_or_evaluation_side:
  mismatch:
  support:
  confidence: high | medium | low

research_problem:
  statement:
  object:
  distinction_or_dependency:
  scope:

method_role:
  statement:
  relation_to_problem:

technical_mechanism:
  statement:
  components: []

paper_thesis:
  statement:
  support_level: demonstrated | supported-interpretation | broader-implication | speculative

candidate_alternatives: []
rejected_framings: []
```

## Rules

- `research_setting` must be definable without the proposed method.
- `structural_change` should compare concrete structures, not adjectives.
- `structural_mismatch` is optional. Leave it empty when no defensible mismatch exists.
- `research_problem` should not be a disguised description of the technical mechanism.
- `method_role` explains what the method does conceptually.
- `technical_mechanism` records how it is implemented.
- `paper_thesis` must not be broader than its support level permits.
