# Blind Audit Packet

This directory supports an independence-controlled reconstruction exercise.

Start with:

1. [`prompt.md`](prompt.md)
2. [`sources.json`](sources.json)
3. [`report-template.md`](report-template.md)

The intended sequence is:

```text
external sources -> frozen independent report -> only then comparison with the parent corpus
```

Do not use the parent repository's conclusions as input if the result is intended to count as a blind reconstruction.

This is an **L2-style** design: the source bundle is selected in advance for relevance, so source selection itself is not independent. It is cleaner than repository-conditioned critique, but weaker than an audit in which the reasoner independently chooses both evidence and framing.

Null results and disagreement are valid outcomes.
