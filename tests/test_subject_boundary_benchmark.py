from __future__ import annotations

import json
from pathlib import Path
import unittest

from subject_boundary.benchmark import (
    Scenario,
    VALIDATION_THRESHOLDS,
    coupling_sweep,
    default_scenarios,
    summarize,
    validation_checks,
)


class SubjectBoundaryBenchmarkTests(unittest.TestCase):
    SAMPLES = 6_000
    SEED = 1729

    def _summary(self, name: str):
        scenario = next(row for row in default_scenarios() if row.name == name)
        return summarize(scenario, samples=self.SAMPLES, seed=self.SEED)

    def test_independent_control_remains_separate(self) -> None:
        metrics = self._summary("independent")["metrics"]
        self.assertLess(metrics["next_state_synchrony_mi"], 0.05)
        self.assertLess(metrics["a_to_b"], 0.05)
        self.assertLess(metrics["b_to_a"], 0.05)

    def test_common_driver_is_synchronous_without_cross_causation(self) -> None:
        metrics = self._summary("common_driver")["metrics"]
        self.assertGreater(metrics["next_state_synchrony_mi"], 0.5)
        self.assertLess(metrics["a_to_b"], 0.05)
        self.assertLess(metrics["b_to_a"], 0.05)

    def test_one_way_coupling_recovers_direction(self) -> None:
        metrics = self._summary("one_way")["metrics"]
        self.assertGreater(metrics["a_to_b"], 0.8)
        self.assertLess(metrics["b_to_a"], 0.1)
        self.assertGreater(metrics["transfer_entropy_proxy_a_to_b"], 0.5)
        self.assertLess(metrics["transfer_entropy_proxy_b_to_a"], 0.05)

    def test_bidirectional_copy_is_not_joint_representation(self) -> None:
        metrics = self._summary("bidirectional_swap")["metrics"]
        self.assertGreater(metrics["a_to_b"], 0.8)
        self.assertGreater(metrics["b_to_a"], 0.8)
        self.assertLess(metrics["joint_predictive_gain_a"], 0.1)
        self.assertLess(metrics["joint_predictive_gain_b"], 0.1)

    def test_distributed_xor_has_joint_predictive_and_causal_dependence(self) -> None:
        metrics = self._summary("distributed_xor")["metrics"]
        self.assertGreater(metrics["joint_predictive_gain_a"], 0.6)
        self.assertGreater(metrics["joint_predictive_gain_b"], 0.6)
        self.assertGreater(metrics["joint_necessity_a"], 0.8)
        self.assertGreater(metrics["joint_necessity_b"], 0.8)

    def test_hidden_routing_is_false_positive_for_naive_joint_gain(self) -> None:
        scenario = Scenario(
            "stochastic_router",
            "test",
            "synergy-false-positive-control",
            coupling=0.5,
            noise=0.0,
        )
        metrics = summarize(
            scenario,
            samples=self.SAMPLES,
            seed=self.SEED,
        )["metrics"]
        self.assertGreater(
            max(
                metrics["joint_predictive_gain_a"],
                metrics["joint_predictive_gain_b"],
            ),
            0.15,
        )
        self.assertLess(metrics["joint_necessity_a"], 0.7)
        self.assertLess(metrics["joint_necessity_b"], 0.7)

    def test_default_validation_bundle_passes(self) -> None:
        summaries = [
            summarize(
                scenario,
                samples=self.SAMPLES,
                seed=self.SEED + index * 100,
            )
            for index, scenario in enumerate(default_scenarios())
        ]
        checks = validation_checks(summaries)
        self.assertTrue(all(row["passed"] for row in checks.values()), checks)

    def test_preregistration_thresholds_match_code(self) -> None:
        repo_root = Path(__file__).resolve().parents[1]
        prereg = json.loads(
            (repo_root / "subject-boundary-preregistration.json").read_text()
        )
        self.assertEqual(
            prereg["synthetic_validation_thresholds"],
            VALIDATION_THRESHOLDS,
        )

    def test_coupling_sweep_contains_endpoints(self) -> None:
        rows = coupling_sweep(
            couplings=(0.0, 0.5, 1.0),
            samples=2_000,
            seed=self.SEED,
        )
        self.assertEqual(
            [row["scenario"]["coupling"] for row in rows],
            [0.0, 0.5, 1.0],
        )


if __name__ == "__main__":
    unittest.main()
