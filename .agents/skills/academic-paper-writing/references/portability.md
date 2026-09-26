# Portability across runtimes

The skill is intentionally instruction-first. Scripts are optional accelerators.

## ChatGPT

Treat Research State, Claim Graph, Narrative, and Module Plan as logical state carried by the conversation unless the environment offers persistent files and persistence is useful.

A packaged skill may be uploaded where the ChatGPT product/workspace exposes Skill installation. Product availability and installation behavior can vary.

## Codex

When the skill is stored under `.agents/skills/academic-paper-writing/`, use it as a repository-local workflow.

For long iterative projects, Codex may persist working state under `.paper-writing/`, for example:

```text
.paper-writing/
  research-state.md
  claims.md
  narrative.md
  section-plan.md
```

This persistence is optional. Do not create or rewrite these files unless doing so benefits the active repository workflow.

## API / agent sandbox

The same logical state may be represented as JSON, Markdown, database records, or application state. The skill must not depend on one serialization.

The API implementation may call stages separately, but stage separation must not create duplicated prompt logic. The canonical methodology remains in this skill directory.

## Portability rule

Any critical instruction required to obtain a correct paper must be executable by a model that can only read text files. A script may automate checking or packaging, but the writing methodology must remain usable without executing code.
