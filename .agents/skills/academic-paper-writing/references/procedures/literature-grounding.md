# Procedure: Literature grounding

Goal: use external literature as evidence that constrains the paper's framing, claims, novelty boundary, and experiment design.

Literature is not a late Related Work decoration. It is an external constraint on author-side reasoning.

## Two uses of literature

Keep these roles separate:

1. **Scientific grounding** — what prior work studies, demonstrates, assumes, compares, or leaves unresolved.
2. **Discourse grounding** — how strong papers communicate scientific ideas. Use the separate [Discourse grounding procedure](discourse-grounding.md).

A paper used as a writing reference does not automatically support a scientific claim, and a scientifically relevant paper does not need to be used as a prose model.

## Literature state

For each paper that materially affects the paper construction, record only verified information:

```text
paper identity
problem / setting
core mechanism
demonstrated evidence
assumptions / scope
relation to our work
citation evidence
```

Useful relation types include:

- same problem;
- adjacent problem;
- competing solution;
- reused mechanism;
- empirical or theoretical precedent;
- conflicting evidence;
- evaluation precedent.

Do not reduce the literature state to paper summaries. Organize it around the decisions the current paper must make.

## Checkpoint A — Framing challenge

Run after a candidate framing exists and before treating that framing as stable.

1. Decompose the candidate framing into searchable concepts:
   - research setting;
   - structural change or key distinction;
   - claimed mismatch;
   - research problem;
   - proposed method role.
2. Search neighboring terminology, not only the paper's preferred vocabulary.
3. Identify work that could invalidate, weaken, rename, or absorb the proposed framing.
4. Ask:
   - Has this problem already been formulated?
   - Has the key distinction already been made under another name?
   - Is the claimed mismatch already handled by an existing objective or architecture?
   - Is the method role genuinely different from a known solution?
5. Revise the framing to the narrowest version that survives the challenge.

The goal is not to find papers that agree with the framing. The goal is to test whether the framing remains defensible after exposure to the closest prior work.

## Checkpoint B — Claim and novelty boundary

Run on the Claim Graph and Paper Core.

For each central claim, record a literature relation:

```text
supported precedent
known overlap
contrast / difference
conflicting evidence
not established by literature
search incomplete
```

Construct a Claim–Literature Matrix with at least:

- claim;
- closest relevant work;
- shared content;
- different content;
- evidence for the difference;
- novelty status;
- citation needed;
- confidence.

Do not state that a component is novel merely because the current search did not find it. Distinguish:

- **verified difference**: a concrete difference from identified closest work;
- **novelty candidate**: appears different under the current search but is not exhaustively established;
- **not novel / prior technique**: already present in prior work;
- **unknown**: insufficient evidence.

When novelty is uncertain, narrow the claim or preserve the uncertainty.

## Checkpoint C — Experiment grounding

Run after logical Experimental Obligations have been derived from the paper's own claims.

Literature should refine, not replace, those obligations.

For each obligation, search for:

- strongest competing baselines;
- accepted direct metrics;
- benchmark precedents;
- matched-compute / matched-call controls;
- standard ablations;
- known failure modes;
- evaluation protocols that make the comparison interpretable.

Use this distinction:

```text
claim
-> logical evidence requirement
-> literature-supported evaluation convention
-> final experiment design
```

Do not add an experiment merely because prior papers report it.

## Retrieval discipline

When retrieval is available:

- prefer original papers and official proceedings/arXiv pages over secondary summaries;
- use recent work when the research area is moving quickly;
- search by concepts and synonyms, not only exact method names;
- follow citations backward for foundational mechanisms and forward for close successors when useful;
- keep source identity attached to every extracted literature fact.

When retrieval is unavailable:

- use only literature supplied by the user or already present in the research material;
- mark unresolved literature questions explicitly;
- do not invent citations, consensus, baselines, or novelty claims.

## Output

Maintain a compact [Literature Map](../../schemas/literature-map.md) and update the Claim Graph / Paper Core / Experimental Obligations only when the retrieved evidence justifies a change.

The Literature Map is an author-side representation. Do not dump it mechanically into Related Work or Introduction prose.
