# Author profile template

When enough user-authored prose is available, infer stable preferences without copying distinctive wording.

```yaml
sentence_length: short | medium | long | mixed
paragraph_length: short | medium | long | mixed
technical_density: low | medium | high
claim_strength: cautious | moderate | assertive
transition_explicitness: low | medium | high
first_person_usage: low | medium | high
rhetorical_questions: rare | occasional | frequent
parenthetical_usage: low | medium | high
notation_in_prose: low | medium | high

preferences:
  - ...

avoid:
  - ...
```

Infer only recurring stylistic behavior. Do not infer scientific beliefs, personality, or demographic attributes from prose.
