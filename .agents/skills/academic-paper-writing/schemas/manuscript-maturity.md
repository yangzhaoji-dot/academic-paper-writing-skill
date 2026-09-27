# Schema: Manuscript Maturity

Purpose: prevent a manuscript from presenting unfinished research state as if it were submission-ready evidence.

```yaml
manuscript_maturity:
  stage: research_spec | pre_results | evidence_ready | submission
  evidence_state:
    real_results_available: true | false
    central_metrics_frozen: true | false
    evaluation_protocol_frozen: true | false
  allowed_surfaces: []
  forbidden_surfaces: []
  transition_requirements: []
```

## Stages

### research_spec

Use while the method, claims, or experimental design are still materially changing.

Allowed:
- unresolved design alternatives;
- explicit research questions;
- experiment obligations;
- provisional equations or interfaces marked as such.

Do not package this state as a polished final manuscript.

### pre_results

Use when the scientific method and paper story are stable enough to draft, but real central results are not yet available.

Allowed:
- Abstract problem / method statements;
- Introduction;
- Related Work;
- Preliminaries / Method;
- Experimental protocol, metrics, baselines, and planned comparisons;
- limitations implied by the method definition.

Forbidden:
- synthetic or placeholder result claims;
- full result tables whose body is only pending/TBD;
- empirical contribution bullets;
- abstract/conclusion sentences that imply observed improvement;
- prose that describes planned evidence as if it were a finding.

Prefer a compact protocol section or explicit result slot over a fake final results surface.

### evidence_ready

Use when central result artifacts are available and traceable.

Allowed:
- result tables and plots;
- result-first experiment prose;
- empirical contribution statements;
- abstract/conclusion result claims bounded by verified evidence.

### submission

Use when evidence and scientific claims are largely frozen.

Default intervention becomes conservative:
- preserve claim scope;
- prioritize editorial distillation, consistency, venue compliance, exact-candidate verification, and rendered presentation;
- reopen science only for a genuine blocker.

## Invariants

Maturity controls presentation permission, not scientific truth.

A later-looking manuscript surface must never be used to conceal an earlier research state.

### Invisible-maturity invariant

Manuscript Maturity is compiler state. Its labels must not appear in reader-facing prose merely because the compiler uses them.

Do not render internal lifecycle language such as:

- pre-results;
- evidence-ready;
- current manuscript stage;
- empirical claims withheld;
- pending because experiments have not run.

Instead, let maturity control what surfaces exist:

~~~text
pre_results
-> protocol may exist
-> unobserved result tables do not exist
-> empirical claims do not exist
~~~

If the reader must understand an actual scientific limitation caused by unavailable evidence, state the limitation directly without naming the internal maturity state.
