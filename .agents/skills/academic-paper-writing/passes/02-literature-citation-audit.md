# Pass 02 — Literature & Citation Audit

## Responsibility

Build a verified literature substrate and bibliographic record before prose writing.

This pass owns the [Citation Map](../schemas/citation-map.md).

It does **not** choose the final paper story or write Related Work prose.

## Inputs

Use:

- Research State;
- Scientific Spec when available;
- existing literature notes;
- external literature retrieval when authorized / available.

For time-sensitive or niche literature, verify current metadata from reliable sources.

## Required audit

### 1. Metadata verification

For every manuscript reference, verify when possible:

- canonical title;
- authors;
- year;
- formal venue if published;
- DOI / arXiv identifier;
- current canonical URL;
- BibTeX entry.

Prefer formal publication metadata over stale arXiv-only metadata when appropriate.

### 2. Claim-to-source map

Every literature-dependent claim should map to one or more verified references.

Examples:

- definition / formulation claims;
- "prior work branches at..." claims;
- benchmark or metric conventions;
- closest-work mechanism;
- attribution of an algorithm.

### 3. Closest-work boundary

For each close paper, record:

- shared problem;
- shared mechanism;
- verified difference;
- novelty risk.

Do not infer novelty from search absence.

### 4. Baseline identity audit

Distinguish:

\`\`\`text
published method
vs.
our adaptation of one component / estimator
\`\`\`

If an experiment changes only a credit rule inspired by BranPO/BPO/etc., do not label the row as the full published method unless it truly is.

### 5. Section citation coverage

Plan likely citation use for:

- Introduction;
- Related Work;
- Preliminaries;
- Method;
- Experiments.

## Output

Produce:

- frozen Citation Map;
- verified \`references.bib\` content when a paper artifact is being built;
- unresolved citation issues.

## Exit criteria

Freeze only when:

- core prior-work metadata is verified;
- closest-work boundaries are concrete;
- literature-dependent claims have source coverage;
- baseline labels are not misleading;
- unresolved claims are explicitly marked.

## Issue routing

Writers may request more sources, but may not invent references or metadata.

New literature claims return here for verification.
