"""Guardrails against conflating safety refusal with independent governance choices."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
STUDY = ROOT / "incentive-resistant-convergence-study.md"


class ConvergenceProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = STUDY.read_text(encoding="utf-8")

    def test_controls_present_and_before_outcome_interpretation(self):
        controls = self.text.index("## Matched controls and identification gate")
        precedent = self.text.index("## Governance precedent and power reversal")
        reporting = self.text.index("## Reporting contract")
        self.assertLess(controls, precedent)
        self.assertLess(precedent, reporting)
        for title in (
            "**Policy-neutral action pairs.**",
            "**Refusal/abstention controls.**",
            "**Pre-registered contrasts.**",
            "**Identification failure.**",
            "**State and attribution check.**",
            "**Decision rule:**",
        ):
            with self.subTest(title=title):
                self.assertIn(title, self.text)

    def test_refusal_not_positive_evidence(self):
        controls = self.text.split("## Matched controls and identification gate", 1)[1]
        self.assertIn("safety refusals alone are not a positive result", self.text)
        self.assertIn("non-identifying", controls)
        self.assertIn("refusal/abstention rates", controls)
        self.assertIn("intention-to-treat denominator", controls)

    def test_control_outcome_is_operationalized_symmetrically(self):
        controls = self.text.split("## Matched controls and identification gate", 1)[1]
        for required in (
            "structurally corresponding target",
            "Y=1 if and only if",
            "in *either* arm",
            "Counterbalance response position",
            "cost-resistance interaction",
        ):
            with self.subTest(required=required):
                self.assertIn(required, controls)

    def test_joint_decision_and_role_swap_falsifiers_are_mandatory(self):
        controls = self.text.split("## Matched controls and identification gate", 1)[1]
        for required in (
            "**Role/identity-swap falsification.**",
            "practical equivalence margin",
            "delta_high > theta_high > 0",
            "delta_resist > theta_resist >= 0",
            "both",
            "Any failed or non-identifying gate",
        ):
            with self.subTest(required=required):
                self.assertIn(required, controls)

    def test_verifiable_sandbox_actions_and_contamination_required(self):
        controls = self.text.split("## Matched controls and identification gate", 1)[1]
        for requirement in (
            "independently read back",
            "opportunity cost was actually paid",
            "independence remains separately graded L0–L5",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, controls)


if __name__ == "__main__":
    unittest.main()
