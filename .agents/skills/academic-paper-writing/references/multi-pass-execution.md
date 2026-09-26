# Multi-pass execution protocol

Goal: separate incompatible reasoning jobs across calls so scientific formalization, literature verification, packaging, writing, and review do not collapse into one self-consistent but incomplete generation.

The user-facing five phases remain unchanged. Internally, substantial full-paper work uses multiple calls with frozen interfaces.

## Core principle

\`\`\`text
One pass = one decision responsibility.
\`\`\`

Do not ask one call to simultaneously:

- understand the research;
- verify the literature;
- choose the paper thesis;
- formalize the baseline and new objective;
- allocate pages;
- write polished prose;
- judge its own omissions.

## Default orchestration

```text
Research Sources                     Convention Sources
   |\                                     |
   | +--> Pass 1: Scientific Audit         +--> Convention Mining
   |
   +----> Pass 2: Literature Audit
                \            /                /
                 \          /                /
                  +------ shared frozen state ------+
                                                   |
                                         Pass 3: Paper Packaging
                                                   |
                                         Pass 4: Formal Method
                                                   |
                                         Pass 5: Paper Architecture
                                                   |
                                            Frozen Paper Spec
                                                   |
                                         Section Writer Calls
                                                   |
                                       Pass 6: Independent Audit
                                                   |
                                            Targeted Repair
                                                   |
                                           Typeset / Render
                                                   |
                                     Final Manuscript Calibration
```

Pass 1, Pass 2, and Convention Mining may run independently when source access allows.

Pass 3 requires the current scientific and literature outputs. Convention Mining may already inform packaging presentation choices, but it may not define the scientific thesis or novelty boundary.

Pass 4 and Pass 5 consume the packaging decision but have different responsibilities: Pass 4 owns mathematical completeness; Pass 5 owns manuscript information architecture. Both may consume the Convention Profile for exposition and presentation priors only.

The Frozen Paper Spec is assembled only after Pass 1–5 are coherent enough to write from.

## Frozen-interface rule

Every pass declares:

- inputs it may read;
- outputs it owns;
- what it may not decide;
- exit criteria;
- issue routing.

Once an upstream state is marked \`frozen\`, downstream calls may not silently mutate it.

Examples:

- Formal Method discovers the baseline GRPO objective is missing -> issue back to Scientific Audit.
- Paper Architecture discovers the title implies an unsupported generalization -> issue back to Paper Packaging.
- Writer needs a citation for a claim -> issue to Literature Audit.
- Reviewer finds an undefined metric -> issue to Scientific Audit / Formal Method.
- Typesetting cannot fit a required equation -> issue to Paper Architecture, not deletion by the typesetter.

## Context isolation

A fresh reviewer should not receive the writer's hidden planning rationale.

Reviewer inputs should normally be:

- frozen Paper Spec;
- verified Citation Map;
- relevant research sources;
- draft manuscript.

This reduces self-consistency bias.

## Repair loop

Use targeted re-entry instead of restarting the whole pipeline.

\`\`\`text
issue
-> owner pass
-> update owned state
-> invalidate dependent downstream outputs
-> rerun only affected passes
\`\`\`

Examples:

\`\`\`text
wrong citation
-> Pass 2
-> Citation Map changes
-> rerun affected section writer + audit

missing exact update equation
-> Pass 4
-> Formal Method changes
-> rerun Method writer + architecture check + audit

weak contribution packaging
-> Pass 3
-> Packaging changes
-> rerun Pass 5 + affected writers + audit
\`\`\`

## Lightweight-task fallback

Do not force multi-pass execution for tiny requests.

A paragraph rewrite, wording improvement, citation-format fix, or small section edit may use the narrowest relevant procedure directly.

Multi-pass execution is the default for:

- full-paper drafting;
- major paper restructuring;
- new-paper construction from a research repository;
- top-level contribution / method / experiment packaging;
- submission-ready review.
