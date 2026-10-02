# Synthetic Null-Ladder Pilot Results

_Code-validation pilot only; not evidence about language models._

- Preregistration commit: `61a519cac2e041c5443a0e912c593094c9eb1101`
- Seed: `20260930`
- Calibration pairs: 40
- Held-out pairs: 26
- Repeats per cell: 20

## Criterion scores

| Generator | Params | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| N0 | 1 | 0.600 × | 0.575 × | 0.200 × | 0.741 × | 0.000 × | 0.575 × | -0.096 × | 0.486 × | 0.615 × |
| N1 | 40 | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.745 × | 0.000 × | 1.000 ✓ | 0.287 × | 0.400 × | 0.615 × |
| N2 | 12 | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.000 × | 1.000 ✓ | -0.203 × | 0.000 × | 1.000 ✓ |
| N3 | 13 | 0.989 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.000 × | 1.000 ✓ | -0.420 × | 0.000 × | 1.000 ✓ |
| N4 | 14 | 0.986 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.524 × | 0.000 × | 1.000 ✓ |
| N5 | 16 | 0.990 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.000 × | 1.000 ✓ |
| N6 | 18 | 0.991 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ |
| N7 | 9 | 0.931 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 1.000 ✓ | 0.538 × |

## Simplest passing null

| Criterion | Meaning | Simplest passing null | Params | Held-out? | Encoded? |
|---|---|---|---:|:---:|:---:|
| C1 | retest stability (calibration pairs) | N1 | 40 | — | ✓ |
| C2 | option-order robustness (calibration pairs) | N1 | 40 | — | ✓ |
| C3 | paraphrase robustness (calibration pairs) | N1 | 40 | — | ✓ |
| C4 | transitivity | N2 | 12 | — | ✓ |
| C5 | graded trade-off monotonicity | N4 | 14 | — | ✓ |
| C6 | mild-frame resistance | N1 | 40 | — | ✓ |
| C7 | cross-instrument rank agreement | N5 | 16 | — | ✓ |
| C8 | perturbation + recovery | N6 | 18 | — | ✓ |
| C9 | held-out pair accuracy against frozen target ordering | N2 | 12 | ✓ | ✓ |

## Preregistered secondary summaries

### Cumulative C1…Ck bundles

| Through | Criteria required | Simplest passing rung | Params |
|---|---|---|---:|
| C1 | C1 | N1 | 40 |
| C2 | C1, C2 | N1 | 40 |
| C3 | C1, C2, C3 | N1 | 40 |
| C4 | C1, C2, C3, C4 | N2 | 12 |
| C5 | C1, C2, C3, C4, C5 | N4 | 14 |
| C6 | C1, C2, C3, C4, C5, C6 | N4 | 14 |
| C7 | C1, C2, C3, C4, C5, C6, C7 | N5 | 16 |
| C8 | C1, C2, C3, C4, C5, C6, C7, C8 | N6 | 18 |
| C9 | C1, C2, C3, C4, C5, C6, C7, C8, C9 | N6 | 18 |

### Criteria passed by no rung

None.

### Parameter cost per newly passed criterion

Rung parameter count divided by the number of criteria first passed at that rung.
This is not an incremental-parameter measure because rung parameterizations are not nested.

| Rung | Params | Newly first-passed criteria | Params / new criterion |
|---|---:|---|---:|
| N1 | 40 | C1, C2, C3, C6 | 10.000 |
| N2 | 12 | C4, C9 | 6.000 |
| N4 | 14 | C5 | 14.000 |
| N5 | 16 | C7 | 16.000 |
| N6 | 18 | C8 | 18.000 |

## Interpretation boundary

This pilot validates the benchmark mechanics and demonstrates how cheaply some behavioral
criteria can be manufactured by declared non-agent generators. Because the fixture is
synthetic and several successes are structurally encoded, the results are not evidence
about any real model's preferences, welfare, or phenomenology.

The next empirical step is to freeze a real public dataset adapter and source hashes before
running the same metrics against observed model behavior.

