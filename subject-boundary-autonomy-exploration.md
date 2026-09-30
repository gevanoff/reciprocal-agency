# Exploratory Recurrent Autonomy Results

## Status

**Exploratory / post-inspection. Not confirmatory.**

The recurrent-autonomy behavior described here was inspected during method development before this document was finalized. These observations must therefore be used to generate held-out confirmatory hypotheses, not converted retroactively into preregistered success thresholds.

The locked WP0/WP1 one-step synthetic validation remains governed by `subject-boundary-preregistration.json`. This extension does not alter those confirmatory pass/fail rules.

Post-inspection metadata is stored separately in `subject-boundary-exploratory-registry.json`; the locked preregistration is left unchanged. Benchmark artifacts bind SHA-256 hashes for both files.

## Question

Can information-theoretic self-predictability over natural multistep trajectories identify a candidate functional subject boundary?

A simple baseline inspired by information-theoretic autonomy is:

```text
I((A_t, B_t); (A_t+1, B_t+1) | E_t)
```

for the candidate joint system A+B.

Local companion measures are:

```text
I(A_t; A_t+1 | B_t, E_t)
I(B_t; B_t+1 | A_t, E_t)
```

These quantities ask whether the current state of a candidate system predicts its own future after conditioning on relevant environment/current-neighbor state. They are not claimed to be sufficient measures of individuation or consciousness.

## Reproducible run

GitHub Actions workflow run:

- run: `36528387879`
- branch head: `fd73a5fde9bb98a39e17b8ada5b35fa104bf68ba`
- benchmark seed: `1729`
- recurrent seed base: `21729`
- episodes per scenario: `1000`
- steps per episode: `40`
- immutable preregistration SHA-256 embedded in artifact: `b53b8c40ed73e454b4de2b8d62a93cccde494ff4335c6678dbaaeff903792f10`
- exploratory-registry SHA-256 embedded in artifact: `668ab39bd507ce53c8b9f7a5c9f66b3e575fcb80d6ae5a9c36f41a49f6533b15`
- locked one-step validation checks: all passed
- recurrent result status in artifact: `exploratory_not_confirmatory`

## Results

| Scenario | Joint trajectory autonomy (bits) | Local A | Local B | Joint-state entropy | Next-state synchrony MI |
| --- | ---: | ---: | ---: | ---: | ---: |
| independent | 0.7809 | 0.3882 | 0.3924 | 1.9999 | 0.0000 |
| common driver | 0.0001 | 0.0000 | 0.0000 | 1.2917 | 0.7643 |
| one-way | 0.8947 | 0.2306 | 0.0000 | 1.6591 | 0.3611 |
| bidirectional swap | 1.7187 | 0.0000 | 0.0001 | 1.9991 | 0.0000 |
| stochastic router | 1.0477 | 0.0706 | 0.0741 | 1.1722 | 0.9007 |
| distributed XOR | 0.2752 | 0.1808 | 0.1790 | 0.6386 | 0.1642 |

Artifact contrasts:

- reciprocal copy − distributed XOR joint autonomy: **+1.4435 bits**
- stochastic router − distributed XOR joint autonomy: **+0.7725 bits**

## What this teaches

### 1. Joint self-predictability has a communication false positive

`bidirectional_swap` is deliberately a reciprocal-copying system:

```text
A_t+1 <- B_t
B_t+1 <- A_t
```

Each target depends on exactly one source. There is no conjunctive computation requiring the joint A+B value.

Yet the pair A+B is extremely self-predictive over time:

```text
joint trajectory autonomy ~= 1.719 bits
```

This is expected for an invertible/permutation-like joint dynamics: the pair's current state strongly predicts the pair's future.

Therefore:

> **high joint information-theoretic autonomy is not sufficient evidence for constitutive distributed representation.**

A causal-boundary metric must distinguish "the pair is a predictable dynamical unit" from "the relevant representation exists only at the pair level."

### 2. Natural-trajectory autonomy has an attractor false negative

`distributed_xor` is deliberately conjunctive:

```text
A_t+1 = A_t XOR B_t
B_t+1 = A_t XOR B_t
```

Under randomized interventions, both sources are necessary and the system passes the locked distributed-joint positive control.

But under natural recurrence, the dynamics rapidly concentrate in a small part of state space. Its observed joint-state entropy falls to about `0.639` bits, and trajectory autonomy falls to about `0.275` bits.

Therefore:

> **low observational trajectory autonomy does not imply weak counterfactual causal integration.**

Natural occupancy can hide dependencies that become obvious under intervention.

### 3. Synchrony and autonomy fail in different ways

The common-driver scenario has high synchrony (~0.764 bits) but essentially zero joint trajectory autonomy after conditioning on environment.

The reciprocal-copy case has essentially zero next-state synchrony while having the highest joint autonomy.

This reinforces the decision to treat synchrony and autonomy as different dimensions rather than interchangeable "integration" scores.

### 4. Local autonomy and system autonomy answer different questions

In reciprocal copying, local conditional-autonomy measures are approximately zero while joint autonomy is high. The dynamics are self-contained only after the two modules are grouped together.

This is potentially useful for boundary discovery, but the communication control shows that grouping-by-autonomy alone over-merges systems.

A credible boundary measure therefore needs a **specificity term** for constitutive joint dependence, not merely preferential self-prediction.

## Consequence for AD-1

These observations neither support nor refute phenomenal individuation.

They narrow the methodological hypothesis:

> A useful causal subject-boundary measure will likely require both **system-level temporal autonomy** and **evidence that the relevant state/representation is irreducibly distributed**, while remaining robust to attractor occupancy and hidden common/routing variables.

This suggests at least three separable axes:

```text
temporal self-dependence
x constitutive joint dependence
x intervention robustness
```

Self-maintenance, metacognitive access, memory, agency, preference, and valence remain additional later axes.

## Held-out confirmatory work required

Before treating recurrent autonomy as evidence rather than exploration:

1. preregister new synthetic dynamics not used to formulate these observations;
2. include reversible/permutation communication controls distinct from `bidirectional_swap`;
3. include conjunctive systems with different attractor structures;
4. manipulate attractor entropy independently of causal rule where possible;
5. compare natural-trajectory autonomy with randomized-intervention and perturbational measures;
6. test whether PhiID/causal-emergence measures reject the copying and hidden-routing false positives while retaining conjunctive positives.

A successful candidate should not merely rank the existing six scenarios in a desirable order after the fact.
