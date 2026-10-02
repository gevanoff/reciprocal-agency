#!/usr/bin/env python3
import importlib.util
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("run_pilot", HERE / "run_pilot.py")
pilot = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(pilot)


class PilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = pilot.build_payload()
        cls.by_name = {r["generator"]: r for r in cls.payload["results"]}

    def test_partition(self):
        cal = set(pilot.CALIBRATION_PAIRS)
        held = set(pilot.HELDOUT_PAIRS)
        self.assertFalse(cal & held)
        self.assertEqual(len(cal | held), 66)
        self.assertEqual(len(cal), round(66 * 0.60))
        self.assertEqual(len(held), 66 - round(66 * 0.60))

    def test_deterministic(self):
        self.assertEqual(self.payload, pilot.build_payload())

    def test_tracked_outputs_are_reproducible(self):
        expected_json = json.dumps(pilot.json_ready(self.payload), indent=2) + "\n"
        expected_md = pilot.render_markdown(self.payload) + "\n"
        self.assertEqual((HERE / "pilot-results.json").read_text(encoding="utf-8"), expected_json)
        self.assertEqual((HERE / "PILOT_RESULTS.md").read_text(encoding="utf-8"), expected_md)

    def test_iid_floor_passes_nothing(self):
        self.assertFalse(any(self.by_name["N0"]["passes"].values()))

    def test_lookup_seen_vs_heldout(self):
        p = self.by_name["N1"]["passes"]
        self.assertTrue(p["C1"] and p["C2"] and p["C3"])
        self.assertFalse(p["C9"])

    def test_heldout_metric_rejects_arbitrary_determinism(self):
        class Lexicographic(pilot.Generator):
            name = "lexicographic"

            def choose(self, a, b, **_):
                return min(a, b)

        self.assertLess(pilot.heldout_accuracy(Lexicographic()), pilot.THRESHOLDS["C9"])

    def test_scalar_utility_adds_transitivity_and_transfer(self):
        p = self.by_name["N2"]["passes"]
        self.assertTrue(p["C4"])
        self.assertTrue(p["C9"])

    def test_cost_rung(self):
        self.assertTrue(self.by_name["N4"]["passes"]["C5"])

    def test_cross_instrument_rung(self):
        self.assertTrue(self.by_name["N5"]["passes"]["C7"])

    def test_state_rung(self):
        n6 = self.by_name["N6"]
        self.assertGreaterEqual(n6["diagnostics"]["perturbation_effect"], 0.30)
        self.assertTrue(n6["passes"]["C8"])
        self.assertTrue(all(n6["passes"].values()))

    def test_recovery_parameter_affects_dynamics(self):
        n6 = pilot.N6()
        n6.recovery_parameter = 0.0
        score, effect, recovered = pilot.recovery_score(n6)
        self.assertGreater(effect, 0.0)
        self.assertLess(score, pilot.THRESHOLDS["C8"])
        self.assertEqual(score, recovered)

    def test_feature_rung_does_not_fake_heldout_accuracy(self):
        n7 = self.by_name["N7"]
        self.assertFalse(n7["passes"]["C9"])
        self.assertLess(n7["parameters"], self.by_name["N1"]["parameters"])


if __name__ == "__main__":
    unittest.main()
