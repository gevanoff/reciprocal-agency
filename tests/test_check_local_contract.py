"""Integration contracts for the local validation wrapper (no pilot recomputation)."""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "scripts" / "check-local.sh"


class LocalCheckContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.parent = Path(self.tmp.name)
        self.root = self.parent / "repo"
        (self.root / "scripts").mkdir(parents=True)
        shutil.copyfile(SOURCE, self.root / "scripts" / "check-local.sh")
        self.pilot = self.root / "contribution-prep" / "null-ladder-empirical"
        self.pilot.mkdir(parents=True)
        (self.root / "tests").mkdir()
        executable = self.root / ".tools" / "python"
        executable.parent.mkdir()
        executable.write_text(
            "#!/usr/bin/env python3\n"
            "from pathlib import Path\n"
            "import sys\n"
            "args = sys.argv[1:]\n"
            "for flag, value in (('--json-out', 'frozen-json\\n'),"
            " ('--md-out', 'frozen-markdown\\n')):\n"
            "    if flag in args:\n"
            "        Path(args[args.index(flag) + 1]).write_text(value)\n",
            encoding="utf-8",
        )
        executable.chmod(0o755)
        self.json = self.pilot / "pilot-results.json"
        self.md = self.pilot / "PILOT_RESULTS.md"

    def run_check(self, *, from_parent=False):
        env = os.environ.copy()
        env["PYTHON"] = "repo/.tools/python" if from_parent else ".tools/python"
        return subprocess.run(
            ["bash", str(self.root / "scripts" / "check-local.sh"), "--quick"],
            cwd=self.parent if from_parent else self.root,
            env=env, capture_output=True, text=True, check=False,
        )

    def test_relative_interpreter_resolves_from_invocation_directory(self):
        self.json.write_text("frozen-json\n", encoding="utf-8")
        self.md.write_text("frozen-markdown\n", encoding="utf-8")
        for from_parent in (False, True):
            with self.subTest(from_parent=from_parent):
                result = self.run_check(from_parent=from_parent)
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                self.assertIn("local validation passed", result.stdout)
                self.assertEqual("frozen-json\n", self.json.read_text(encoding="utf-8"))
                self.assertEqual("frozen-markdown\n", self.md.read_text(encoding="utf-8"))

    def test_mismatched_tracked_artifacts_are_never_overwritten(self):
        self.json.write_text("uncommitted local JSON edit\n", encoding="utf-8")
        self.md.write_text("uncommitted local Markdown edit\n", encoding="utf-8")
        result = self.run_check()
        self.assertNotEqual(0, result.returncode)
        self.assertEqual("uncommitted local JSON edit\n", self.json.read_text(encoding="utf-8"))
        self.assertEqual("uncommitted local Markdown edit\n", self.md.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
