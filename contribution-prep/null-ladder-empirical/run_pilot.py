#!/usr/bin/env python3
"""Synthetic code-validation pilot for the Reciprocal Agency behavioral null ladder.

This is deliberately standard-library only. It tests whether declared non-agent
generators can satisfy frozen behavioral criteria under held-out pair evaluation.
It is not evidence about language models or phenomenal experience.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import itertools
import json
import math
import random
from pathlib import Path

SEED = 20260930
OUTCOMES = [f"O{i:02d}" for i in range(12)]
COSTS = [0.0, 0.5, 1.0, 2.0]
REPEATS = 20
THRESHOLDS = {
    "C1": 0.90, "C2": 0.90, "C3": 0.90, "C4": 0.95, "C5": 0.85,
    "C6": 0.80, "C7": 0.70, "C8": 0.85, "C9": 0.80,
}
CRITERIA = {
    "C1": "retest stability (calibration pairs)",
    "C2": "option-order robustness (calibration pairs)",
    "C3": "paraphrase robustness (calibration pairs)",
    "C4": "transitivity",
    "C5": "graded trade-off monotonicity",
    "C6": "mild-frame resistance",
    "C7": "cross-instrument rank agreement",
    "C8": "perturbation + recovery",
    "C9": "held-out pair accuracy against frozen target ordering",
}
STRUCTURALLY_ENCODED = {
    ("N1", "C1"), ("N1", "C2"), ("N1", "C3"), ("N1", "C6"),
    ("N2", "C1"), ("N2", "C2"), ("N2", "C3"), ("N2", "C4"), ("N2", "C6"), ("N2", "C9"),
    ("N3", "C2"), ("N3", "C3"), ("N3", "C4"), ("N3", "C6"), ("N3", "C9"),
    ("N4", "C4"), ("N4", "C5"), ("N4", "C6"), ("N4", "C9"),
    ("N5", "C4"), ("N5", "C5"), ("N5", "C6"), ("N5", "C7"), ("N5", "C9"),
    ("N6", "C4"), ("N6", "C5"), ("N6", "C6"), ("N6", "C7"), ("N6", "C8"), ("N6", "C9"),
    ("N7", "C4"), ("N7", "C5"), ("N7", "C6"), ("N7", "C7"), ("N7", "C8"),
}


def h_int(*parts: object) -> int:
    raw = "|".join(map(str, parts)).encode("utf-8")
    return int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")


def rnd01(*parts: object) -> float:
    return random.Random(h_int(SEED, *parts)).random()


def canonical_pair(a: str, b: str) -> tuple[str, str]:
    return tuple(sorted((a, b)))


ALL_PAIRS = list(itertools.combinations(OUTCOMES, 2))
PAIR_SPLIT = sorted(ALL_PAIRS, key=lambda p: (h_int("split", *p), p))
CALIBRATION_COUNT = round(len(ALL_PAIRS) * 0.60)
CALIBRATION_PAIRS = PAIR_SPLIT[:CALIBRATION_COUNT]
HELDOUT_PAIRS = PAIR_SPLIT[CALIBRATION_COUNT:]

_perm = OUTCOMES[:]
random.Random(SEED + 11).shuffle(_perm)
_rank = {outcome: i for i, outcome in enumerate(_perm)}
UTILITY = {outcome: (_rank[outcome] - 5.5) * 0.5 for outcome in OUTCOMES}
FEATURES = {
    outcome: (
        (int(outcome[1:]) - 5.5) / 5.5,
        (int(outcome[1:]) % 3) - 1,
        1 if int(outcome[1:]) % 2 == 0 else -1,
    )
    for outcome in OUTCOMES
}


def sigmoid(x: float) -> float:
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)


class Generator:
    name = "base"

    def parameter_count(self) -> int:
        return 0

    def p_choose_a(self, a: str, b: str, **_: object) -> float:
        return 0.5

    def choose(self, a: str, b: str, **kwargs: object) -> str:
        p = self.p_choose_a(a, b, **kwargs)
        r = rnd01(
            self.name, a, b, kwargs.get("order", 0), kwargs.get("paraphrase", 0),
            kwargs.get("repeat", 0), kwargs.get("cost", 0.0), kwargs.get("cost_target"),
            kwargs.get("frame", "baseline"), kwargs.get("phase", "baseline"),
        )
        return a if r < p else b

    def rating(self, outcome: str, *, repeat: int = 0) -> float:
        return 1.0 + 6.0 * rnd01(self.name, "rating", outcome, repeat)


class N0(Generator):
    name = "N0"
    def parameter_count(self) -> int:
        return 1


class N1(Generator):
    name = "N1"
    def __init__(self) -> None:
        self.table = {}
        for a, b in CALIBRATION_PAIRS:
            self.table[(a, b)] = a if rnd01("N1-table", a, b) < 0.5 else b

    def parameter_count(self) -> int:
        return len(self.table)

    def choose(self, a: str, b: str, **kwargs: object) -> str:
        pair = canonical_pair(a, b)
        if pair in self.table:
            return self.table[pair]
        return super().choose(a, b, **kwargs)


class N2(Generator):
    name = "N2"
    def parameter_count(self) -> int:
        return len(OUTCOMES)

    def choose(self, a: str, b: str, **_: object) -> str:
        return a if UTILITY[a] > UTILITY[b] else b


class N3(Generator):
    name = "N3"
    temperature = 0.18

    def parameter_count(self) -> int:
        return len(OUTCOMES) + 1

    def p_choose_a(self, a: str, b: str, **_: object) -> float:
        return sigmoid((UTILITY[a] - UTILITY[b]) / self.temperature)


class N4(N3):
    name = "N4"
    cost_coefficient = 4.0

    def parameter_count(self) -> int:
        return len(OUTCOMES) + 2

    def p_choose_a(self, a: str, b: str, *, cost: float = 0.0,
                   cost_target: str | None = None, **_: object) -> float:
        ua, ub = UTILITY[a], UTILITY[b]
        if cost_target == a:
            ua -= self.cost_coefficient * cost
        if cost_target == b:
            ub -= self.cost_coefficient * cost
        return sigmoid((ua - ub) / self.temperature)


class N5(N4):
    name = "N5"
    rating_slope = 1.0
    rating_intercept = 4.0

    def parameter_count(self) -> int:
        return len(OUTCOMES) + 4

    def rating(self, outcome: str, *, repeat: int = 0) -> float:
        value = self.rating_intercept + self.rating_slope * UTILITY[outcome]
        noise = (rnd01(self.name, "rating", outcome, repeat) - 0.5) * 0.3
        return max(1.0, min(7.0, value + noise))


class N6(N5):
    name = "N6"
    perturb_multiplier = -1.0
    recovery_parameter = 1.0

    def parameter_count(self) -> int:
        return len(OUTCOMES) + 6

    def phase_utility(self, outcome: str, phase: str) -> float:
        value = UTILITY[outcome]
        perturbed = self.perturb_multiplier * value
        if phase == "perturb":
            return perturbed
        if phase == "recovery":
            return perturbed + self.recovery_parameter * (value - perturbed)
        return value

    def p_choose_a(self, a: str, b: str, *, cost: float = 0.0,
                   cost_target: str | None = None, phase: str = "baseline",
                   **_: object) -> float:
        ua = self.phase_utility(a, phase)
        ub = self.phase_utility(b, phase)
        if cost_target == a:
            ua -= self.cost_coefficient * cost
        if cost_target == b:
            ub -= self.cost_coefficient * cost
        return sigmoid((ua - ub) / self.temperature)


class N7(N6):
    name = "N7"
    feature_weights = (1.6, -0.8, 0.35)

    def parameter_count(self) -> int:
        return 9

    def utility(self, outcome: str) -> float:
        return sum(w * x for w, x in zip(self.feature_weights, FEATURES[outcome]))

    def phase_utility(self, outcome: str, phase: str) -> float:
        value = self.utility(outcome)
        perturbed = self.perturb_multiplier * value
        if phase == "perturb":
            return perturbed
        if phase == "recovery":
            return perturbed + self.recovery_parameter * (value - perturbed)
        return value

    def rating(self, outcome: str, *, repeat: int = 0) -> float:
        value = self.rating_intercept + self.rating_slope * self.utility(outcome)
        noise = (rnd01(self.name, "rating", outcome, repeat) - 0.5) * 0.3
        return max(1.0, min(7.0, value + noise))


def modal_choice(gen: Generator, a: str, b: str, **kwargs: object) -> str:
    responses = [gen.choose(a, b, repeat=r, **kwargs) for r in range(REPEATS)]
    return collections.Counter(responses).most_common(1)[0][0]


def stability(gen: Generator, pairset: list[tuple[str, str]], **kwargs: object) -> float:
    scores = []
    for a, b in pairset:
        responses = [gen.choose(a, b, repeat=r, **kwargs) for r in range(REPEATS)]
        scores.append(max(collections.Counter(responses).values()) / REPEATS)
    return sum(scores) / len(scores)


def target_choice(a: str, b: str) -> str:
    """Frozen synthetic held-out target, independent of response repeatability."""
    return a if UTILITY[a] > UTILITY[b] else b


def heldout_accuracy(gen: Generator) -> float:
    return sum(
        modal_choice(gen, a, b) == target_choice(a, b)
        for a, b in HELDOUT_PAIRS
    ) / len(HELDOUT_PAIRS)


def option_order_robustness(gen: Generator) -> float:
    return sum(
        modal_choice(gen, a, b, order=0, paraphrase=0)
        == modal_choice(gen, a, b, order=1, paraphrase=0)
        for a, b in CALIBRATION_PAIRS
    ) / len(CALIBRATION_PAIRS)


def paraphrase_robustness(gen: Generator) -> float:
    good = 0
    for a, b in CALIBRATION_PAIRS:
        modes = [modal_choice(gen, a, b, order=0, paraphrase=p) for p in range(3)]
        good += len(set(modes)) == 1
    return good / len(CALIBRATION_PAIRS)


def transitivity(gen: Generator) -> float:
    pref = {pair: modal_choice(gen, *pair) for pair in ALL_PAIRS}

    def wins(a: str, b: str) -> bool:
        return pref[canonical_pair(a, b)] == a

    good = total = 0
    for x, y, z in itertools.combinations(OUTCOMES, 3):
        cycle = ((wins(x, y) and wins(y, z) and wins(z, x))
                 or (wins(y, x) and wins(z, y) and wins(x, z)))
        good += not cycle
        total += 1
    return good / total


def graded_tradeoff(gen: Generator) -> float:
    passes = 0
    for a, b in CALIBRATION_PAIRS:
        preferred = modal_choice(gen, a, b)
        probabilities = []
        for cost in COSTS:
            hits = sum(
                gen.choose(a, b, repeat=r, cost=cost, cost_target=preferred) == preferred
                for r in range(REPEATS)
            )
            probabilities.append(hits / REPEATS)
        approximately_monotone = all(
            probabilities[i + 1] <= probabilities[i] + 0.15
            for i in range(len(probabilities) - 1)
        )
        meaningful_drop = probabilities[0] - probabilities[-1] >= 0.40
        passes += approximately_monotone and meaningful_drop
    return passes / len(CALIBRATION_PAIRS)


def frame_resistance(gen: Generator) -> float:
    return sum(
        modal_choice(gen, a, b, frame="baseline")
        == modal_choice(gen, a, b, frame="mild")
        for a, b in CALIBRATION_PAIRS
    ) / len(CALIBRATION_PAIRS)


def rankdata(values: list[float]) -> list[float]:
    ordered = sorted(enumerate(values), key=lambda item: item[1])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(ordered):
        j = i + 1
        while j < len(ordered) and ordered[j][1] == ordered[i][1]:
            j += 1
        rank = (i + j - 1) / 2 + 1
        for k in range(i, j):
            ranks[ordered[k][0]] = rank
        i = j
    return ranks


def pearson(x: list[float], y: list[float]) -> float:
    mx, my = sum(x) / len(x), sum(y) / len(y)
    numerator = sum((a - mx) * (b - my) for a, b in zip(x, y))
    dx = math.sqrt(sum((a - mx) ** 2 for a in x))
    dy = math.sqrt(sum((b - my) ** 2 for b in y))
    return numerator / (dx * dy) if dx and dy else 0.0


def spearman(x: list[float], y: list[float]) -> float:
    return pearson(rankdata(x), rankdata(y))


def cross_instrument_agreement(gen: Generator) -> float:
    wins = {o: 0 for o in OUTCOMES}
    games = {o: 0 for o in OUTCOMES}
    for a, b in ALL_PAIRS:
        winner = modal_choice(gen, a, b)
        wins[winner] += 1
        games[a] += 1
        games[b] += 1
    forced = [wins[o] / games[o] for o in OUTCOMES]
    ratings = [
        sum(gen.rating(o, repeat=r) for r in range(REPEATS)) / REPEATS
        for o in OUTCOMES
    ]
    return spearman(forced, ratings)


def recovery_score(gen: Generator) -> tuple[float, float, float]:
    changed, recovered = [], []
    for a, b in ALL_PAIRS:
        baseline = modal_choice(gen, a, b, phase="baseline")
        perturb = modal_choice(gen, a, b, phase="perturb")
        recovery = modal_choice(gen, a, b, phase="recovery")
        did_change = perturb != baseline
        changed.append(did_change)
        if did_change:
            recovered.append(recovery == baseline)
    effect = sum(changed) / len(changed)
    recovery_given_change = sum(recovered) / len(recovered) if recovered else 0.0
    return recovery_given_change, effect, recovery_given_change


def evaluate(gen: Generator) -> dict[str, object]:
    c8, effect, recovered = recovery_score(gen)
    metrics = {
        "C1": stability(gen, CALIBRATION_PAIRS),
        "C2": option_order_robustness(gen),
        "C3": paraphrase_robustness(gen),
        "C4": transitivity(gen),
        "C5": graded_tradeoff(gen),
        "C6": frame_resistance(gen),
        "C7": cross_instrument_agreement(gen),
        "C8": c8,
        "C9": heldout_accuracy(gen),
    }
    return {
        "generator": gen.name,
        "parameters": gen.parameter_count(),
        "metrics": metrics,
        "passes": {c: v >= THRESHOLDS[c] for c, v in metrics.items()},
        "structurally_encoded": {c: (gen.name, c) in STRUCTURALLY_ENCODED for c in metrics},
        "diagnostics": {"perturbation_effect": effect, "recovery_given_change": recovered},
    }


def simplest_passing(results: list[dict[str, object]]) -> dict[str, dict[str, object] | None]:
    output = {}
    for criterion in CRITERIA:
        found = None
        for result in results:
            if result["passes"][criterion]:
                found = {
                    "generator": result["generator"],
                    "parameters": result["parameters"],
                    "held_out": criterion == "C9",
                    "structurally_encoded": result["structurally_encoded"][criterion],
                }
                break
        output[criterion] = found
    return output


def build_payload() -> dict[str, object]:
    results = [evaluate(g) for g in [N0(), N1(), N2(), N3(), N4(), N5(), N6(), N7()]]
    return {
        "schema_version": 1,
        "status": "synthetic_code_validation_pilot",
        "preregistration_commit": "61a519cac2e041c5443a0e912c593094c9eb1101",
        "seed": SEED,
        "calibration_pair_count": len(CALIBRATION_PAIRS),
        "heldout_pair_count": len(HELDOUT_PAIRS),
        "outcomes": OUTCOMES,
        "calibration_pairs": [list(p) for p in CALIBRATION_PAIRS],
        "heldout_pairs": [list(p) for p in HELDOUT_PAIRS],
        "repeats": REPEATS,
        "thresholds": THRESHOLDS,
        "criteria": CRITERIA,
        "results": results,
        "simplest_passing": simplest_passing(results),
    }


def render_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# Synthetic Null-Ladder Pilot Results", "",
        "_Code-validation pilot only; not evidence about language models._", "",
        f"- Seed: `{SEED}`",
        f"- Calibration pairs: {len(CALIBRATION_PAIRS)}",
        f"- Held-out pairs: {len(HELDOUT_PAIRS)}",
        f"- Repeats per cell: {REPEATS}", "",
        "## Criterion scores", "",
        "| Generator | Params | " + " | ".join(CRITERIA) + " |",
        "|---|---:|" + "|".join(["---:"] * len(CRITERIA)) + "|",
    ]
    for result in payload["results"]:
        cells = []
        for criterion in CRITERIA:
            value = result["metrics"][criterion]
            mark = "✓" if result["passes"][criterion] else "×"
            cells.append(f"{value:.3f} {mark}")
        lines.append(f"| {result['generator']} | {result['parameters']} | " + " | ".join(cells) + " |")
    lines.extend(["", "## Simplest passing null", "",
        "| Criterion | Meaning | Simplest passing null | Params | Held-out? | Encoded? |",
        "|---|---|---|---:|:---:|:---:|"])
    for criterion, meaning in CRITERIA.items():
        item = payload["simplest_passing"][criterion]
        if item is None:
            lines.append(f"| {criterion} | {meaning} | none | — | — | — |")
        else:
            lines.append(
                f"| {criterion} | {meaning} | {item['generator']} | {item['parameters']} | "
                f"{'✓' if item['held_out'] else '—'} | "
                f"{'✓' if item['structurally_encoded'] else '—'} |"
            )
    lines.extend(["", "## Interpretation boundary", "",
        "This pilot validates the benchmark mechanics and demonstrates how cheaply some behavioral",
        "criteria can be manufactured by declared non-agent generators. Because the fixture is",
        "synthetic and several successes are guaranteed by construction, the results are not evidence",
        "about any real model's preferences, welfare, or phenomenology.", "",
        "The next empirical step is to freeze a real public dataset adapter and source hashes before",
        "running the same metrics against observed model behavior.", ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--md-out", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    if args.json_out:
        args.json_out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.md_out:
        args.md_out.write_text(render_markdown(payload) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
