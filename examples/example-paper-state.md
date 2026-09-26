# Example partial Paper State

## Research State

- **Problem:** fixed-frequency external verification may spend calls when verification is unnecessary.
- **Original idea:** make verification triggering state-dependent.
- **Method:** add a lightweight trigger; keep the underlying decision policy unchanged.
- **Evidence:** fewer verification calls on the evaluated environment family; task success remains comparable within reported uncertainty.
- **Limitation:** one environment family.

## Claims

- **C1 — demonstrated:** the adaptive trigger reduces verifier calls in the reported evaluation.
- **C2 — demonstrated:** reported success remains comparable within the observed uncertainty.
- **C3 — supported interpretation:** verification need is sufficiently state-dependent in this setting to benefit from adaptive triggering.
- **C4 — broader implication:** some external execution policies may be worth treating as adaptive decisions rather than fixed schedules.

## Candidate narrative

Existing systems use fixed verification schedules -> verification utility can vary across states -> fixed scheduling may spend unnecessary calls -> learn a state-dependent trigger -> evaluate call efficiency and success -> discuss the broader implication conservatively.
