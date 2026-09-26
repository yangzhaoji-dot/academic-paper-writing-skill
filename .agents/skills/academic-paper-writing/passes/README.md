# Multi-pass paper construction

These pass files define call-level responsibilities for substantial paper work.

They are **not** separate user-facing skills. The parent \`academic-paper-writing\` skill orchestrates them.

Default sequence:

\`\`\`text
01 Scientific Audit
02 Literature & Citation Audit
Convention Mining (parallel)
03 Paper Packaging
04 Formal Method
05 Paper Architecture
-> Frozen Paper Spec
-> Section Writer calls using section-writer.md
06 Independent Audit
-> targeted repair
-> Present / Render / Final Manuscript Calibration
\`\`\`

Pass 01, Pass 02, and Convention Mining may run independently. Convention Mining owns presentation conventions only and may not redefine scientific content.

A pass owns its output state. Downstream passes may raise issues but may not silently rewrite frozen upstream decisions.

Use [multi-pass execution](../references/multi-pass-execution.md) for orchestration rules.
