# Procedure: Main Result Spine

Goal: compress the stable scientific/formal state into one central paper answer before Paper Architecture assigns space.

This is an internal compiler step between Formal Method and Paper Architecture, not a new user-facing pass.

## Inputs

Use:

- Scientific Spec;
- Paper Core / Packaging;
- Formal Method;
- Experimental Obligations;
- Citation Map;
- current Manuscript Maturity.

## Construction

### 1. State the central question

Use the narrowest question that the method and planned/verified evidence can actually answer.

### 2. State the one-sentence answer

The answer should identify:

- the key distinction or changed structure;
- what the method does about it;
- the level of evidence currently available.

Do not include secondary heuristics or implementation details.

### 3. Build the spine

Map:

```text
problem
-> central distinction
-> method operation
-> decisive evidence
-> bounded conclusion
```

### 4. Classify scientific objects

For each substantial object from Formal Method / Experiments, assign:

```text
core
prerequisite
supporting
appendix_candidate
omit
```

Then assign main-body resolution.

A technically required object can still be an appendix candidate if a compressed main-body definition preserves reader understanding and the appendix provides full verification detail.

### 5. Check contribution centrality

Every contribution must either:

- instantiate the main result;
- establish the method needed for it;
- provide decisive evidence for it; or
- delimit its scope.

If a contribution cannot be connected to the spine, reframe, merge, demote, or remove it.

## Exit criteria

The spine is ready when:

- one sentence captures the paper's central answer;
- every major section has a relation to that answer;
- supporting machinery no longer competes visually/rhetorically with the core;
- evidence wording respects Manuscript Maturity.
