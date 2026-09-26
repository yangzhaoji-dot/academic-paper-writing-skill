# Procedure: Reader-facing discourse composition and naturalization

Goal: convert semantically correct modules into natural academic prose without changing the research claims or exposing internal planning scaffolds.

## Compose for the reader before polishing

Use the Reader Path, not the internal schema, as the direct guide for prose.

Before sentence-level rewriting, decide:

- what the reader needs to understand next;
- which internal concepts can be compressed into one concrete observation;
- whether one example can replace several abstract explanatory sentences;
- what should be one paragraph;
- which sentences can carry two related rhetorical functions;
- whether a relation should be explicit or implicit;
- when a technical term becomes necessary;
- how given information leads into new information.

## Scaffold-hiding rule

Do not verbalize internal labels merely because they exist.

Terms such as:

- research setting;
- structural change;
- structural mismatch;
- method role;
- broader implication;
- reader path;

are usually author-side scaffolds.

Prefer the scientific phenomenon, ambiguity, causal relation, or comparison itself.

For example, instead of:

> This creates a mismatch between policy structure and credit structure.

prefer, when accurate:

> A failed Harness-assisted trajectory does not reveal whether invoking the Harness was unnecessary or whether the agent executed the assisted route poorly.

The second sentence lets the reader infer the abstract mismatch from a concrete ambiguity.

## Naturalization operations

Allowed:

- merge short declarative sentences;
- compress several internal reasoning nodes into one reader-facing sentence;
- turn a repeated sentence into a clause or delete it;
- vary sentence openings and syntactic structure;
- replace generic transitions with semantic relations embedded in the sentence;
- use pronouns or noun phrases when references remain unambiguous;
- move a qualification closer to the claim it limits;
- split overloaded sentences;
- introduce a concrete illustrative case using only already-supported facts or a clearly hypothetical example;
- delay naming a category until the underlying phenomenon is clear;
- delete material that is true but unnecessary for the reader.

## Common artificial patterns to suppress

Do not mechanically ban words, but inspect repeated reliance on patterns such as:

- "Recent advances in ... have ..."
- "However, existing methods still face several limitations."
- "This introduces a structural mismatch between ..."
- "We study this as a ... problem."
- "To address this issue, we propose ..."
- "Moreover / Furthermore / Additionally" at the start of successive sentences;
- one sentence that verbalizes each internal module;
- contribution lists that repeat the Introduction body verbatim;
- abstract promotional adjectives unsupported by evidence;
- multiple sentences that paraphrase the same central claim.

## Reader-facing realization prompt

When the semantic draft still sounds assembled, apply this instruction:

> Rewrite the semantic draft as reader-facing academic prose. Preserve every factual and claim-level constraint, but do not preserve the structure of the internal representation. Lead with the concrete scientific issue rather than the category used to classify it. Prefer examples, causal relations, and contrasts over abstract descriptions of structure. Combine multiple internal reasoning nodes when a reader can understand them as one idea. Introduce terminology only after the underlying phenomenon is clear. Explain why a method component is needed before describing its mechanics. Delete material that is logically true but unnecessary for the reader.

The target is technical writing that feels authored rather than assembled.

## Semantic lock

Before finalizing, compare the naturalized version against the Semantic Draft, Paper Core, and Claim Graph.

Confirm that:

- no claim became stronger, broader, more causal, or more certain;
- no Paper Core element changed meaning;
- no illustrative example introduced a new empirical fact;
- no important limitation disappeared.
