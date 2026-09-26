# Portability across runtimes

The skill is intentionally instruction-first. Scripts and retrieval tools are optional accelerators.

## Retrieval abstraction

The methodology must not depend on one search provider.

Conceptually, literature-dependent stages require an operation such as:

```text
retrieve_literature(query, constraints)
-> verified source material
```

Different runtimes may implement this with web search, scholarly APIs, repository/browser tools, a local paper corpus, or user-supplied papers.

If retrieval is unavailable, continue with supplied material and mark literature-dependent conclusions as unresolved. Never simulate a search by inventing citations or consensus.

## ChatGPT

For substantial paper work, treat multi-pass outputs as explicit handoff state:

- Scientific Spec;
- Citation Map;
- Frozen Paper Spec;
- cross-pass issues.

Separate calls should reuse these frozen outputs rather than reconstructing them from prose history.

For narrow tasks, Research State, Technical State, Section Contracts, Literature Map, Claim Graph, Paper Core, Reader Path, Discourse References, and Module Plan may remain logical conversation state unless persistence is useful.

When web or document retrieval is available, use it at the literature checkpoints. Keep source identity attached to extracted scientific facts. For discourse grounding, abstract section-level and rhetorical patterns rather than storing long source passages.

A packaged skill may be uploaded where the ChatGPT product/workspace exposes Skill installation. Product availability and installation behavior can vary.

## Codex

When the skill is stored under `.agents/skills/academic-paper-writing/`, use it as a repository-local workflow.

For long iterative projects, Codex may persist working state under `.paper-writing/`, for example:

```text
.paper-writing/
  scientific-spec.md
  citation-map.md
  frozen-paper-spec.md
  cross-pass-issues.md
  research-state.md
  technical-state.md
  section-contracts.md
  literature-map.md
  claims.md
  paper-core.md
  discourse-references.md
  narrative.md
  section-plan.md
```

This persistence is optional. Do not create or rewrite these files unless doing so benefits the active repository workflow.

Codex may use browser/search tools, local PDFs, bibliography files, or repository notes as retrieval backends. The core skill must not assume any one of them exists.

## API / agent sandbox

The same logical state may be represented as JSON, Markdown, database records, or application state. The skill must not depend on one serialization.

An API implementation may provide separate retrieval services for:

- scientific literature evidence;
- full-text / section text used for discourse abstraction.

Keep these roles distinct even if the same paper is returned by both services.

For substantial paper construction, API implementations should normally run the pass sequence as separate calls with serialized handoffs. A pass should receive only the frozen upstream state it needs plus source material relevant to its responsibility.

Stage separation must not duplicate prompt logic. The canonical methodology and ownership rules remain in this skill directory.

## Venue/template portability

Venue presentation also uses an abstract resolver:

```text
resolve_venue(conference, year)
-> verified Venue Profile + official template reference
```

A runtime may retrieve official instructions through web access, a local cached profile, or user-supplied venue files. The target year must be explicit.

If the target-year profile is unavailable, the runtime may use the latest verified profile only for provisional planning and must mark the result as unverified. It must not silently substitute an older template for final submission.

Rendered-PDF review may be performed by any runtime capable of compiling or viewing the document. If rendering is unavailable, report that the visual review remains pending rather than treating source validation as equivalent.

## Portability rule

Any critical instruction required to obtain a correct paper must be executable by a model that can only read text files. A script or external search service may automate checking, retrieval, or packaging, but the writing methodology must remain usable without executing code.
