# Minimal example input

This synthetic example is intentionally generic.

## Research idea

A sequential decision system uses an external verification routine. Existing implementations call the verifier at a fixed frequency. We test whether a state-dependent trigger can reduce unnecessary calls while preserving task success.

## Method

A lightweight trigger predicts whether verification is needed from the current trajectory state. The decision system itself is unchanged.

## Evidence

- Fixed-frequency verification is the baseline.
- The adaptive trigger uses fewer verifier calls in the reported evaluation.
- Task success is comparable within the uncertainty of the reported runs.

## Limitation

The experiments are currently on one environment family, so broad claims about general agent systems are unsupported.
