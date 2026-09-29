# Synthetic Subject-Boundary Benchmark

This package implements the first executable slice of the subject-individuation
research program described in `subject-boundary-research-plan.md`.

## Scope

The benchmark has known **causal** ground truth. It does not have phenomenal
ground truth and must not be interpreted as a consciousness test.

Its purpose is to reject candidate metrics that cannot distinguish:

- common input from direct coupling;
- one-way from reciprocal causation;
- reciprocal copying from conjunctive distributed computation;
- genuine joint dependence from statistical false positives.

## Key false-positive control

`stochastic_router` randomly chooses whether each target copies its local or
remote source. Because the routing variable is hidden, observing `(A, B)`
jointly improves prediction of the target even though the transition never
computes a function requiring both values.

This makes `joint_predictive_gain` positive without constitutive distributed
representation. Any later metric that equates "synergy-like predictability"
with a subject boundary should fail this control.

## Current scenarios

- `independent`
- `common_driver`
- `one_way`
- `bidirectional_swap`
- `stochastic_router`
- `distributed_xor`

The benchmark also sweeps stochastic-routing coupling from 0 to 1.

## Metrics

The current standard-library baseline reports:

- paired intervention sensitivities with fixed exogenous randomness;
- conditional mutual-information transfer-entropy proxies;
- conditional self-dependence;
- next-state synchrony mutual information;
- joint predictive gain;
- joint causal necessity.

These are deliberately simple baselines. PhiID, causal-emergence, Markov-
blanket, integrated-information, and more sophisticated autonomy measures are
future candidate implementations and should be compared against these controls.

The runner also emits an **exploratory** recurrent-autonomy section based on natural multistep trajectories. It is intentionally excluded from the locked validation gate because its behavior was inspected during development. The interpretation and held-out confirmation requirements are documented in `subject-boundary-autonomy-exploration.md`.

The confirmatory preregistration is immutable. Post-inspection metadata lives in `subject-boundary-exploratory-registry.json`, and runner artifacts include hashes for both provenance files.

## Run

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
python3 scripts/run-subject-boundary-benchmark.py \
  --samples 20000 \
  --seed 1729 \
  --out subject-boundary-benchmark.json
```

The runner exits non-zero if a locked synthetic validation check fails.

## Preregistration

`subject-boundary-preregistration.json` freezes the initial constructs,
competing-model labels, metrics, synthetic scenarios, and validation rules before
the primary machine-coupling experiments.

Thresholds in that file apply only to synthetic benchmark validation. They are
not thresholds for consciousness, phenomenal unity, or machine moral status.
