# Section Writer Call Contract

## Responsibility

Write one manuscript section from a Frozen Paper Spec without re-deciding the paper.

Section writing may be split across calls such as:

- Abstract + Introduction;
- Related Work;
- Preliminaries + Method;
- Experiments;
- Discussion + Conclusion.

Use section-specific grouping that preserves local continuity.

## Inputs

Provide only what the section needs:

- Frozen Paper Spec;
- relevant Scientific Spec fields;
- relevant Citation Map entries;
- section contract / architecture entry;
- required equations / metrics / visuals;
- section-matched Discourse References;
- finalized previous-section prose when continuity requires it.

Do not provide unnecessary upstream planning rationale.

## Writer may decide

- paragraph boundaries;
- local ordering within the section contract;
- transitions;
- examples / concrete anchors supported by research facts;
- sentence realization;
- compression of repeated information;
- subsection boundaries when allowed by Paper Architecture.

## Writer may not decide

- title / thesis;
- contribution scope;
- novelty boundary;
- baseline definition;
- required equations;
- metric definitions;
- citation metadata;
- evidence status;
- venue page limit;
- removal of main-body technical prerequisites.

## Internal writing sequence

\`\`\`text
Section Contract
-> Section Calibration
-> Semantic Draft
-> Authorial Synthesis
-> Discourse Realization
-> Naturalization
\`\`\`

## Issue behavior

If the writer encounters an upstream problem, emit an issue instead of silently patching it.

Examples:

\`\`\`yaml
- problem: GRPO update equation is required but absent from Formal Method
  owner_pass: formal_method
  severity: blocking

- problem: citation needed for benchmark protocol but not in Citation Map
  owner_pass: literature_citation_audit
  severity: major

- problem: contribution bullet conflicts with actual evidence status
  owner_pass: paper_packaging
  severity: blocking
\`\`\`

## Exit criteria

A section is writer-complete when:

- all required content from the Frozen Paper Spec is present;
- no upstream decision was silently changed;
- citations come from Citation Map;
- required equations / definitions appear;
- prose passes Authorial Synthesis;
- unresolved issues are explicitly returned.
