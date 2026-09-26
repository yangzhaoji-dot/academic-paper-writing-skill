# Schema: Paper Core

```yaml
paper_core:
  concrete_problem:
  key_distinction:
  thesis:
    statement:
    support_level: demonstrated | supported-interpretation | broader-implication | speculative
  method_role:
  technical_mechanism:
  evidence_needed: []
  non_claims: []
  section_zoom:
    abstract:
    introduction:
    method:
    experiments:
    conclusion:
```

## Rules

- The Paper Core should remain stable across sections.
- `concrete_problem` should be understandable without method-specific jargon when possible.
- `key_distinction` identifies the conceptual split the reader must not conflate.
- `thesis` is the central relation argued or tested by the work.
- `method_role` is conceptual; `technical_mechanism` is implementation-level.
- `evidence_needed` constrains experiments but does not predict positive results.
- `non_claims` records tempting overstatements that later writers and reviewers should reject.
