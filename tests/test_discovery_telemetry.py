from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "collect-discovery-telemetry.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("collect_discovery_telemetry", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DiscoveryTelemetryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.telemetry = _load_module()

    def test_only_registered_blind_audit_issue_is_selected(self) -> None:
        self.assertTrue(
            self.telemetry.is_registered_discovery_issue(
                {"number": 13, "title": "renamed submission issue", "body": ""}
            )
        )
        self.assertFalse(
            self.telemetry.is_registered_discovery_issue(
                {"number": 99, "title": "[Blind audit] unrelated", "body": ""}
            )
        )

    def test_freeze_marker_is_required_for_blind_submission(self) -> None:
        marker = "This report was completed before inspecting files outside `blind-audit/`."
        self.assertTrue(self.telemetry.is_frozen_blind_audit_submission(marker))
        self.assertTrue(
            self.telemetry.is_frozen_blind_audit_submission(
                "Results follow.\nTHIS REPORT WAS COMPLETED BEFORE INSPECTING FILES OUTSIDE `BLIND-AUDIT/`.\nsource:web"
            )
        )
        self.assertFalse(
            self.telemetry.is_frozen_blind_audit_submission(
                "Question about the audit procedure; no report is frozen yet."
            )
        )

    def test_existing_registered_challenge_surfaces_still_match(self) -> None:
        self.assertTrue(
            self.telemetry.is_registered_discovery_issue(
                {"number": 7, "title": "[Challenge] falsify this", "body": ""}
            )
        )
        self.assertTrue(
            self.telemetry.is_registered_discovery_issue(
                {
                    "number": 8,
                    "title": "ordinary title",
                    "body": "discovery-surface: agent-finding",
                }
            )
        )


if __name__ == "__main__":
    unittest.main()
