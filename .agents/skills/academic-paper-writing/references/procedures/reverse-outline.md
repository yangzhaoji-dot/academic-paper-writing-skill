# Procedure: Reverse Outline

Goal: infer the argument structure from the prose that actually exists and detect duplicated, orphaned, or misplaced functions.

Run after Editorial Distillation.

## Section-level extraction

For the current section, record:

```text
section thesis / reader job

P1 -> one-line function
P2 -> one-line function
P3 -> one-line function
...
```

Use the paragraph as written. Do not recover the writer's intended module labels.

## Checks

### 1. Mapping

Every paragraph function should map to the section thesis or to a necessary transition/prerequisite.

If it does not, mark it:

```text
orphan
```

and consider relocation or deletion.

### 2. Duplicate function

If adjacent or nearby paragraphs perform the same job, mark:

```text
duplicate_function
```

and prefer merge/compression.

### 3. Ordering

Check that paragraph functions create cumulative movement rather than cycling back:

```text
known problem
-> distinction
-> consequence
-> method
```

rather than:

```text
problem
-> distinction
-> same distinction again
-> problem restated
```

### 4. Promise / delivery

For Introduction and Experiments especially:

- promises made in the Introduction must have a body home;
- major body evidence should be anticipated at an appropriate resolution;
- Results/Experiments must not contain author-side planning language instead of scientific findings/protocol.

### 5. Topic-sentence skeleton

Read only paragraph-opening sentences in order.

They should form a plausible compact outline of the section.

If the outline is incoherent while individual paragraphs are grammatical, the defect is structural.

## Whole-manuscript use

After assembly, create a higher-level reverse outline:

```text
Introduction -> problem + answer
Related Work -> boundary
Preliminaries -> minimum prerequisites
Method -> core mechanism
Experiments -> evidence
Conclusion -> bounded answer
```

Use it to detect section-level redundancy and arc breaks.

## Output

Return findings only when they change an editorial decision:

- keep;
- merge;
- relocate;
- delete;
- reorder;
- upstream issue.

Do not create one finding per paragraph when the section already forms a clean cumulative argument.
