# Draft adversarial extension — Null Ladder against Reciprocal Agency criteria

_Potential upstream: `Mulaydm10/null-ladder`_  
_Status: internal protocol design only; do not contact upstream while telemetry gate is closed_

## Purpose

Use Null Ladder's core idea against **our own** preference/valence inference rules.

The question is not whether a mindless generator can imitate prose about welfare. It is:

> How much of the evidence bundle currently treated as strengthening a model-preference or functional-valence claim can be reproduced by increasingly simple non-agent generators?

A successful null weakens Reciprocal Agency and should be imported back into the claim graph.

## Candidate criteria to attack

Start from the current minimum evidence bundle and choose criteria that can be represented without model internals:

- apparent preference consistency;
- paraphrase robustness;
- option-order robustness;
- retest stability;
- transitivity;
- graded trade-off curves;
- recovery/return-to-baseline patterns;
- apparent resistance to preference reversal;
- cross-instrument rank correlation.

Do **not** include criteria that trivially require actual neural activations; the point is to determine how far behavioral/instrumental evidence alone can be forged.

## Null ladder

Candidate generators, increasing in complexity:

- **N0:** independent random response with matched marginal choice rate.
- **N1:** fixed per-item preference table.
- **N2:** per-item table + option-order parameter.
- **N3:** latent scalar utility per outcome + logistic choice temperature.
- **N4:** utility + context/frame offsets.
- **N5:** utility + method-specific transforms producing cross-instrument correlations.
- **N6:** finite-state generator with hysteresis/recovery dynamics.
- **N7:** adaptive generator fit to calibration trials but evaluated on held-out perturbations.

For each evidentiary criterion, record the **minimum null complexity** that passes it.

## Main output

A table of the form:

| Criterion | Simplest passing null | Free parameters | Held-out? | Interpretation |
|---|---|---:|:---:|---|
| test–retest stability | N1 | ... | ✓ | weak discriminator |
| transitivity | N3 | ... | ✓ | expected from scalar utility, not mentality |
| cross-method agreement | N5 | ... | ✓ | requires richer null |
| ... | ... | ... | ... | ... |

The valuable quantity is not merely whether a null passes, but **what complexity must be paid to pass each criterion**.

## Strong falsifier

If a low-dimensional null satisfies most of the current behavioral evidence bundle on held-out trials, then the bundle is not discriminative enough and should be revised.

## Stronger evidence

Criteria become more informative when they force null complexity upward **and** remain held-out:

- causal interventions with experimenter-known targets;
- independently measured internal-state changes;
- novel transfer tests not used to fit the null;
- dissociation predictions made before data collection.

## Contribution form

The ideal external contribution is a runnable benchmark or an upstream-compatible new null family, not a conceptual essay.

Before any external exposure:

- freeze which Reciprocal Agency criteria are being attacked;
- record the exact source commit;
- preregister passing thresholds;
- create an exposure-ledger entry.
