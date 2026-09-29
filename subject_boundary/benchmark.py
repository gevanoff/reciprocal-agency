"""Synthetic causal-boundary benchmark.

This module intentionally uses only the Python standard library. WP1 begins
with systems whose one-step causal structure is known, so candidate boundary
metrics can be falsified before they are applied to machine or biological data.

The benchmark does *not* measure consciousness. It measures whether simple
causal/information metrics recover known partitions and reject confounds such as
common input, synchrony, and high-bandwidth copying.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import asdict, dataclass
import math
import random
from typing import Hashable, Iterable, Sequence


Bit = int


@dataclass(frozen=True)
class Scenario:
    name: str
    description: str
    ground_truth: str
    coupling: float = 0.0
    noise: float = 0.02


@dataclass(frozen=True)
class Transition:
    a: Bit
    b: Bit
    environment: Bit
    a_next: Bit
    b_next: Bit
    environment_next: Bit


def _entropy(values: Sequence[Hashable]) -> float:
    if not values:
        return 0.0
    counts = Counter(values)
    total = len(values)
    return -sum(
        (count / total) * math.log2(count / total)
        for count in counts.values()
    )


def mutual_information(
    xs: Sequence[Hashable],
    ys: Sequence[Hashable],
) -> float:
    if len(xs) != len(ys):
        raise ValueError("mutual-information inputs must have equal length")
    return _entropy(xs) + _entropy(ys) - _entropy(list(zip(xs, ys)))


def conditional_mutual_information(
    xs: Sequence[Hashable],
    ys: Sequence[Hashable],
    zs: Sequence[Hashable],
) -> float:
    if not (len(xs) == len(ys) == len(zs)):
        raise ValueError("conditional-MI inputs must have equal length")
    xz = list(zip(xs, zs))
    yz = list(zip(ys, zs))
    xyz = list(zip(xs, ys, zs))
    return _entropy(xz) + _entropy(yz) - _entropy(zs) - _entropy(xyz)


def _flip_with_probability(bit: Bit, draw: float, probability: float) -> Bit:
    return int(bit ^ (draw < probability))


def transition(
    scenario: Scenario,
    a: Bit,
    b: Bit,
    environment: Bit,
    draw_a: float,
    draw_b: float,
    draw_environment: float,
) -> tuple[Bit, Bit, Bit]:
    """Apply one controlled transition.

    ``draw_*`` values are supplied by the caller so paired counterfactuals can
    reuse identical exogenous randomness. That makes intervention-sensitivity
    estimates structural rather than correlational.
    """

    p = scenario.noise

    if scenario.name == "independent":
        a_next = _flip_with_probability(a, draw_a, 0.15)
        b_next = _flip_with_probability(b, draw_b, 0.15)

    elif scenario.name == "common_driver":
        a_next = _flip_with_probability(environment, draw_a, p)
        b_next = _flip_with_probability(environment, draw_b, p)

    elif scenario.name == "one_way":
        a_next = _flip_with_probability(a, draw_a, 0.15)
        b_next = _flip_with_probability(a, draw_b, p)

    elif scenario.name == "bidirectional_swap":
        # Strong direct coupling, but each target is still a local copy of
        # exactly one source variable. This is a communication/control case,
        # not a constitutive joint representation.
        a_next = _flip_with_probability(b, draw_a, p)
        b_next = _flip_with_probability(a, draw_b, p)

    elif scenario.name == "stochastic_router":
        # Hidden exogenous routing chooses whether each target copies itself or
        # the other subsystem. Joint observation improves prediction even
        # though no transition combines A and B. This is a deliberate
        # false-positive control for naive "synergy" metrics.
        a_next = b if draw_a < scenario.coupling else a
        b_next = a if draw_b < scenario.coupling else b

    elif scenario.name == "distributed_xor":
        # Both next states depend conjunctively on both current subsystem
        # states. Neither source alone identifies the target under uniform
        # intervention sampling.
        joint = a ^ b
        a_next = _flip_with_probability(joint, draw_a, p)
        b_next = _flip_with_probability(joint, draw_b, p)

    else:
        raise ValueError(f"unknown scenario: {scenario.name}")

    environment_next = int(draw_environment < 0.5)
    return int(a_next), int(b_next), environment_next


def default_scenarios() -> list[Scenario]:
    return [
        Scenario(
            "independent",
            "Two persistent modules with no cross-module causal edges.",
            "separate",
        ),
        Scenario(
            "common_driver",
            "A and B share an external driver but do not causally influence one another.",
            "common-input-control",
        ),
        Scenario(
            "one_way",
            "A causally drives B while B does not drive A.",
            "directed-coupling",
        ),
        Scenario(
            "bidirectional_swap",
            "A and B directly copy one another without conjunctive integration.",
            "communication-control",
        ),
        Scenario(
            "stochastic_router",
            "Hidden routing stochastically selects local or cross-module copies.",
            "synergy-false-positive-control",
            coupling=0.5,
            noise=0.0,
        ),
        Scenario(
            "distributed_xor",
            "Each next state depends irreducibly on the joint A/B state.",
            "constitutive-distributed",
        ),
    ]


def sample_interventional_transitions(
    scenario: Scenario,
    samples: int = 20_000,
    seed: int = 1729,
) -> list[Transition]:
    """Sample the transition table under randomized interventions on A/B/E.

    Uniform intervention sampling prevents stationary-distribution artifacts
    from hiding causal dependencies in this first benchmark stage.
    """

    if samples <= 0:
        raise ValueError("samples must be positive")

    rng = random.Random(seed)
    rows: list[Transition] = []
    for _ in range(samples):
        a = rng.getrandbits(1)
        b = rng.getrandbits(1)
        environment = rng.getrandbits(1)
        draw_a = rng.random()
        draw_b = rng.random()
        draw_environment = rng.random()
        a_next, b_next, environment_next = transition(
            scenario,
            a,
            b,
            environment,
            draw_a,
            draw_b,
            draw_environment,
        )
        rows.append(
            Transition(
                a=a,
                b=b,
                environment=environment,
                a_next=a_next,
                b_next=b_next,
                environment_next=environment_next,
            )
        )
    return rows


def intervention_sensitivity(
    scenario: Scenario,
    samples: int = 20_000,
    seed: int = 1730,
) -> dict[str, float]:
    """Estimate paired do-style sensitivities by flipping one source bit.

    Exogenous random draws are held fixed between the factual and
    counterfactual transitions.
    """

    rng = random.Random(seed)
    counts = {
        "a_to_a": 0,
        "a_to_b": 0,
        "b_to_a": 0,
        "b_to_b": 0,
    }

    for _ in range(samples):
        a = rng.getrandbits(1)
        b = rng.getrandbits(1)
        environment = rng.getrandbits(1)
        draw_a = rng.random()
        draw_b = rng.random()
        draw_environment = rng.random()

        factual = transition(
            scenario,
            a,
            b,
            environment,
            draw_a,
            draw_b,
            draw_environment,
        )
        flip_a = transition(
            scenario,
            a ^ 1,
            b,
            environment,
            draw_a,
            draw_b,
            draw_environment,
        )
        flip_b = transition(
            scenario,
            a,
            b ^ 1,
            environment,
            draw_a,
            draw_b,
            draw_environment,
        )

        counts["a_to_a"] += factual[0] != flip_a[0]
        counts["a_to_b"] += factual[1] != flip_a[1]
        counts["b_to_a"] += factual[0] != flip_b[0]
        counts["b_to_b"] += factual[1] != flip_b[1]

    return {key: value / samples for key, value in counts.items()}


def summarize(
    scenario: Scenario,
    samples: int = 20_000,
    seed: int = 1729,
) -> dict[str, object]:
    rows = sample_interventional_transitions(scenario, samples=samples, seed=seed)

    a = [row.a for row in rows]
    b = [row.b for row in rows]
    environment = [row.environment for row in rows]
    a_next = [row.a_next for row in rows]
    b_next = [row.b_next for row in rows]

    joint = list(zip(a, b))
    conditioning_a_to_b = list(zip(b, environment))
    conditioning_b_to_a = list(zip(a, environment))

    mi_a_target = mutual_information(a, a_next)
    mi_b_target_a = mutual_information(b, a_next)
    mi_b_target = mutual_information(b, b_next)
    mi_a_target_b = mutual_information(a, b_next)

    joint_gain_a = mutual_information(joint, a_next) - max(
        mi_a_target,
        mi_b_target_a,
    )
    joint_gain_b = mutual_information(joint, b_next) - max(
        mi_b_target,
        mi_a_target_b,
    )

    sensitivities = intervention_sensitivity(
        scenario,
        samples=samples,
        seed=seed + 1,
    )

    # A target is "jointly necessary" only to the extent that interventions on
    # *both* subsystem inputs affect it. This is not sufficient for
    # constitutive integration; it is a useful companion to predictive gain.
    joint_necessity_a = min(
        sensitivities["a_to_a"],
        sensitivities["b_to_a"],
    )
    joint_necessity_b = min(
        sensitivities["a_to_b"],
        sensitivities["b_to_b"],
    )

    return {
        "scenario": asdict(scenario),
        "metrics": {
            "next_state_synchrony_mi": mutual_information(a_next, b_next),
            "transfer_entropy_proxy_a_to_b": conditional_mutual_information(
                a,
                b_next,
                conditioning_a_to_b,
            ),
            "transfer_entropy_proxy_b_to_a": conditional_mutual_information(
                b,
                a_next,
                conditioning_b_to_a,
            ),
            "conditional_self_dependence_a": conditional_mutual_information(
                a,
                a_next,
                list(zip(b, environment)),
            ),
            "conditional_self_dependence_b": conditional_mutual_information(
                b,
                b_next,
                list(zip(a, environment)),
            ),
            "joint_predictive_gain_a": joint_gain_a,
            "joint_predictive_gain_b": joint_gain_b,
            "joint_necessity_a": joint_necessity_a,
            "joint_necessity_b": joint_necessity_b,
            **sensitivities,
        },
    }


def coupling_sweep(
    couplings: Iterable[float] = (0.0, 0.1, 0.25, 0.5, 0.75, 1.0),
    samples: int = 20_000,
    seed: int = 1729,
) -> list[dict[str, object]]:
    results = []
    for index, coupling in enumerate(couplings):
        if not 0.0 <= coupling <= 1.0:
            raise ValueError("coupling values must be in [0, 1]")
        scenario = Scenario(
            "stochastic_router",
            "Coupling sweep through hidden stochastic local/cross routing.",
            "communication-with-hidden-routing",
            coupling=float(coupling),
            noise=0.0,
        )
        results.append(
            summarize(
                scenario,
                samples=samples,
                seed=seed + index * 100,
            )
        )
    return results


def validation_checks(
    summaries: Sequence[dict[str, object]],
) -> dict[str, dict[str, object]]:
    by_name = {
        str(row["scenario"]["name"]): row["metrics"]
        for row in summaries
    }

    def check(name: str, passed: bool, reason: str) -> tuple[str, dict[str, object]]:
        return name, {"passed": bool(passed), "reason": reason}

    checks = dict(
        [
            check(
                "common_driver_rejects_causal_merger",
                by_name["common_driver"]["next_state_synchrony_mi"]
                > VALIDATION_THRESHOLDS["common_driver_sync_min"]
                and by_name["common_driver"]["a_to_b"]
                < VALIDATION_THRESHOLDS["direct_cross_influence_max"]
                and by_name["common_driver"]["b_to_a"]
                < VALIDATION_THRESHOLDS["direct_cross_influence_max"],
                "High synchrony from common input must coexist with negligible direct cross influence.",
            ),
            check(
                "one_way_recovers_direction",
                by_name["one_way"]["a_to_b"]
                > VALIDATION_THRESHOLDS["direct_cross_influence_min"]
                and by_name["one_way"]["b_to_a"]
                < VALIDATION_THRESHOLDS["direct_cross_influence_absent_max"],
                "Paired interventions must recover A→B without inventing B→A.",
            ),
            check(
                "bidirectional_copy_is_not_joint_representation",
                by_name["bidirectional_swap"]["a_to_b"]
                > VALIDATION_THRESHOLDS["direct_cross_influence_min"]
                and by_name["bidirectional_swap"]["b_to_a"]
                > VALIDATION_THRESHOLDS["direct_cross_influence_min"]
                and by_name["bidirectional_swap"]["joint_predictive_gain_a"]
                < VALIDATION_THRESHOLDS["copy_joint_gain_max"]
                and by_name["bidirectional_swap"]["joint_predictive_gain_b"]
                < VALIDATION_THRESHOLDS["copy_joint_gain_max"],
                "Strong reciprocal causal influence alone must not look like conjunctive representation.",
            ),
            check(
                "distributed_xor_detects_joint_dependence",
                by_name["distributed_xor"]["joint_predictive_gain_a"]
                > VALIDATION_THRESHOLDS["distributed_joint_gain_min"]
                and by_name["distributed_xor"]["joint_predictive_gain_b"]
                > VALIDATION_THRESHOLDS["distributed_joint_gain_min"]
                and by_name["distributed_xor"]["joint_necessity_a"]
                > VALIDATION_THRESHOLDS["distributed_joint_necessity_min"]
                and by_name["distributed_xor"]["joint_necessity_b"]
                > VALIDATION_THRESHOLDS["distributed_joint_necessity_min"],
                "Known joint logic should produce high joint predictive gain and bilateral necessity.",
            ),
            check(
                "naive_joint_gain_has_false_positive_control",
                by_name["stochastic_router"]["joint_predictive_gain_a"]
                > VALIDATION_THRESHOLDS["router_false_positive_joint_gain_min"]
                or by_name["stochastic_router"]["joint_predictive_gain_b"]
                > VALIDATION_THRESHOLDS["router_false_positive_joint_gain_min"],
                "Hidden local/cross routing should demonstrate that joint predictive gain alone is not constitutive evidence.",
            ),
        ]
    )
    return checks
