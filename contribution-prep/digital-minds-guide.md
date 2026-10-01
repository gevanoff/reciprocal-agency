# Draft contribution packet — Digital Minds Guide

_Target: `Mitchel-Alexander/getting-started-digital-minds-next`_  
_Target file: `src/data/research-areas.ts`_  
_Status: internal draft only; do not submit while telemetry gate is closed_

## Source audit

The guide explicitly welcomes contributions and currently treats **Welfare Capacity and Assessment** as a distinct research area. Its existing `goDeeper` list contains:

- limitations of model self-report;
- Anthropic's system-card welfare work;
- a broad survey of AI-welfare questions.

What is not currently represented in that local section is a **cross-study methodological map separating distinct evidence channels and robustness failures**.

That is a real gap rather than a generic request to list Reciprocal Agency.

## Proposed smallest useful contribution

Add **one** `goDeeper` reading/resource entry under `Welfare Capacity and Assessment`.

### Candidate TypeScript object

```ts
{
  author: "Reciprocal Agency contributors",
  title: "Model Preference / Welfare Method × Claim Matrix",
  year: 2026,
  url: "https://github.com/gevanoff/reciprocal-agency/blob/main/model-preference-method-matrix.md",
  description:
    "A cross-study methodology map separating stated preference, behavioural choice, self-attribution, introspective accuracy, internal representations, causal intervention, persistence, and phenomenal claims, with explicit robustness controls and claim boundaries.",
},
```

This uses British English (`behavioural`) to match the target's style.

## Why this is useful to the target

The guide's current framing already warns that plausible self-reports may reflect training data rather than internal state. The matrix adds a practical next layer:

- what other channels exist;
- which studies combine them;
- which robustness dimensions have actually been tested;
- which apparent contradictions are channel/construct mismatches;
- which conclusions remain downstream of the available evidence.

It would therefore function as **navigation across the literature**, consistent with the guide's purpose.

## Why not propose more

Do **not** initially add Reciprocal Agency to:

- Governance Under Uncertainty;
- Safety-Welfare Coordination;
- Rights and Legal Frameworks;
- Identity and Individuation.

There are genuine overlaps, but adding multiple self-authored entries at once would create avoidable promotional appearance and make acceptance harder to interpret.

If the matrix entry is accepted on its merits, later governance/individuation contributions should still require independent justification.

## Pre-release checks

- Refresh `src/data/research-areas.ts` from upstream.
- Confirm no new cross-study methodology resource has already filled the gap.
- Run the target's normal build/typecheck on an actual fork before submission.
- Prefer a one-entry PR with a concise description of the gap.
- Record the exact matrix commit SHA in the exposure ledger before opening the PR.
