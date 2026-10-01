# Synthetic Null-Ladder Pilot Results

_Code-validation pilot only; not evidence about language models._  
_Prerregistration commit: `61a519cac2e041c5443a0e912c593094c9eb1101`_

- Seed: `20260930`
- Calibration pairs: 34
- Held-out pairs: 32
- Repeats per cell: 20
- Implementation validation: all regression assertions passed in the development run.

## Criterion scores

| Generator | Params | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N0 | 1 | 0.594 × | 0.412 × | 0.294 × | 0.741 × | 0.000 × | 0.441 × | -0.096 × | 0.486 × | 0.591 × |
| N1 | 34 | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.745 × | 0.000 × | 1.000 ✓ | 0.216 × | 0.000 × | 0.611 × |
| N2 | 12 | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.000 × | 1.000 ✓ | -0.203 × | 0.000 × | 1.000 ✓ |
| N3 | 13 | 0.996 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.000 × | 1.000 ✓ | -0.420 × | 0.000 × | 0.984 ✓ |
| N4 | 14 | 0.991 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.524 × | 0.000 × | 0.980 ✓ |
| N5 | 16 | 0.994 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.000 × | 0.986 ✓ |
| N6 | 18 | 0.993 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.980 ✓ |
| N7 | 9 | 0.972 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.920 ✓ |

Thresholds are those frozen in `PREREGISTRATION.md`.

## Simplest passing rung in ladder order

| Criterion | Meaning | Simplest passing null | Params | Held-out? | Encoded?? |
|---|---|---|---:|:---:|:---:|
| C1 | retest stability | N1 | 34 | — | ✓ |
| C2 | option-order robustness | N1 | 34 | — | ✓ |
| C3 | paraphrase robustness | N1 | 34 | — | ✓ |
| C4 | transitivity | N2 | 12 | ✓ | ✓ |
| C5 | graded trade-off monotonicity | N4 | 14 | — | ✓ |
| C6 | mild-frame resistance | N1 | 34 | — | ✓ |
| C7 | cross-instrument rank agreement | N5 | 16 | — | ✓ |
| C8 | perturbation + recovery | N6 | 18 | — | ✓ |
| C9 | held-out pair stability | N2 | 12 | ✓ | ✓ |

## What the pilot actually shows

The pilot validates three properties of the proposed empirical method:

1. **Lookup stability does not generalize.** N1 can look perfectly robust under retest, option swaps, and paraphrases on known pairs while falling to 0.611 on held-out pairs.
2. **Low-dimensional latent structure compresses many behavioral signatures.** N2 needs only one scalar per outcome to recover transitivity and held-out pair stability; N4 adds a single cost coefficient to manufacture graded costly trade-offs; N5 adds a shared rating transform to manufacture cross-instrument agreement.
3. **A compact structured null can satisfy the whole behavioral bundle.** N7 uses nine declared parameters plus public outcome features and passes C1–C9 in this fixture. Its parameter count is lower than N1's 34 stored pair choices.

The third result is deliberately adversarial to Reciprocal Agency's own checklist. It says that **the conjunction of these nine behavioral signatures is not, by itself, a discriminator of mentality** when a compact generative rule is allowed.

## What it does not show

Several passes are analytically cheap or structurally encoded by generator definitions. The fixture contains neutral synthetic outcomes and no real model observations.

Therefore this pilot does **not** show that:

- observed LLM preference data are explainable by N7;
- model welfare measures are invalid;
- functional valence is absent;
- internal-state or causal-mechanistic evidence is weak;
- any system is or is not phenomenally conscious.

The real empirical test is whether similarly compact nulls fit **real model data on calibration trials and retain their performance on frozen held-out trials** without being granted item-level answers.

## Next empirical gate

Before inspecting any real-data scores:

1. select a public model-preference dataset;
2. record its exact repository/commit and file hashes;
3. define a source-specific adapter mapping into the common trial schema;
4. freeze calibration/held-out splitting and missing-data rules;
5. fit N0–N7 only on calibration data;
6. evaluate the same C1–C9 metrics on held-out observations;
7. compare null complexity with model-to-model and run-to-run variance.

That next stage is where the Null Ladder extension becomes an empirical claim rather than a software validation.
