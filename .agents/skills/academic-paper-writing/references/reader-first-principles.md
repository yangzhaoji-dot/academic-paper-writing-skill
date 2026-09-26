# Reader-first writing principles

This skill uses four reader-first principles when converting research structure into paper structure.

## 1. One paper, one core story

The abstract, introduction, main technical sections, experiments, and conclusion should describe the same research object at different levels of resolution.

- **Abstract**: the compressed problem, method, and evidence.
- **Introduction**: why the problem exists, what distinction matters, and why the method is a reasonable response.
- **Method**: the detailed mechanism that realizes the paper's core idea.
- **Experiments**: evidence for the claims made by the same core story.
- **Conclusion**: the supported lesson, not a new framing.

Do not invent a new motivation for each section.

## 2. Minimize reader effort

The paper should not expose the author's internal planning process unless it helps the reader.

Prefer the shortest sequence of concepts that makes the next idea necessary.

Useful questions:

- What can the reader already understand?
- What is the first genuinely new idea?
- Can an abstract distinction be exposed by one concrete example?
- Is a definition needed now, or only later?
- Is the main point delayed behind background the reader does not need?
- Can a sentence be deleted without weakening the argument?

## 3. Explain why before what or how

A technical component is easier to understand when the reader first knows what unresolved need it addresses.

For nontrivial components, establish the semantic sequence:

```text
WHY
-> WHAT
-> HOW
```

Do not mechanically render these as headings.

## 4. Claims determine experiments

Experiments should support paper claims and eliminate plausible alternative explanations.

Do not plan experiments only by listing datasets, baselines, and ablations. First identify what a skeptical reader would need to observe for each central claim to become credible.

## Source note

These principles adapt high-level ideas from the public repository [wmd3i/Some-tips-for-writing-an-AI-ML-paper](https://github.com/wmd3i/Some-tips-for-writing-an-AI-ML-paper), especially its emphasis on a consistent story across sections, reducing reader/reviewer effort, explaining method motivation before mechanics, and aligning experiments with claims. The procedures in this skill are original operationalizations of those ideas rather than copied prose.
