# Schema: Experimental Obligation

```yaml
claim_id:
claim:
obligation_type: effect | mechanism | compute-control | scope | calibration | ablation | other
direct_support:
alternative_explanation:
control_or_ablation:
direct_metric:
strongest_baseline:
falsifying_or_weakening_result:
status: available | planned | missing | not-applicable
linked_experiments: []
notes:
```

## Rules

- One central claim may produce several obligations.
- Several claims may share one experiment.
- A benchmark score is not a direct metric unless it measures the claimed effect itself.
- A control should target a plausible competing explanation, not merely follow convention.
- The falsifying outcome must be stated without assuming the method succeeds.
