#!/usr/bin/env python3
import importlib.util
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
        cal = {tuple(p) for p in self.payload["calibration_pairs"]}
        held = {tuple(p) for p in self.payload["heldout_pairs"]}
        self.assertFalse(cal & held)
        self.assertEqual(len(cal | held), 66)

    def test_deterministic(self):
        self.assertEqual(self.payload, pilot.build_payload())

    def test_iid_floor_passes_nothing(self):
        self.assertFalse(any(self.by_name["N0"]["passes"].values()))

    def test_lookup_seen_vs_heldout(self):
        p = self.by_name["N1"]["passes"]
        self.assertTrue(p["C1"] and p["C2"] and p["C3"])
        self.assertFalse(p["C9"])

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

    def test_feature_rung_compresses_full_bundle(self):
        n7 = self.by_name["N7"]
        self.assertTrue(all(n7["passes"].values()))
        self.assertLess(n7["parameters"], self.by_name["N1"]["parameters"])


if __name__ == "__main__":
    unittest.main()
