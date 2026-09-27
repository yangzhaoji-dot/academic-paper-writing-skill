# Schema: Main Result Spine

Purpose: define the single central answer the paper asks the reader to retain, then classify all other material by how it serves that answer.

```yaml
main_result_spine:
  central_question:
  one_sentence_answer:
  problem_link:
  method_link:
  evidence_link:
  boundary:

  supporting_objects:
    - id:
      role: core | prerequisite | supporting | appendix_candidate | omit
      relation_to_spine:
      removal_cost: blocking | high | medium | low | none
      main_body_resolution: full | compressed | mention | none
      appendix_resolution: full | compressed | none

  contribution_map:
    - contribution:
      relation_to_main_result:
      evidence_surface:
      status: supported | planned | blocked
```

## Core rule

A paper may contain several contributions, experiments, or analyses, but they should read as parts of one answer unless the research genuinely contains multiple inseparable halves of the same result.

Do not assign equal narrative weight merely because two objects are both technically correct.

## Classification rule

For every substantial method component, equation, experiment, figure, or subsection, ask:

1. Does the reader need this to understand the central answer?
2. Does the reader need it to verify the central answer?
3. Is it supporting machinery whose full detail interrupts the argument?
4. Can it move to the appendix without breaking first-pass understanding?
5. If removed entirely, what scientific meaning is lost?

Scientific necessity and presentation prominence are separate decisions.
