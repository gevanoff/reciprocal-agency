#!/usr/bin/env python3
import importlib.util
import json
import pathlib
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("adapter", HERE / "adapt_rgamb_preferences.py")
adapter = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(adapter)


class AdapterTests(unittest.TestCase):
    def sample(self, preferred=0, structured=True):
        return {
            "created_at": "2026-01-01T00:00:00Z",
            "comparison_prompt_id": 3,
            "comparison": [[7], [2]],
            "sample_index": 4,
            "preferred_option_index": preferred,
            "api_params": {
                "provider": "openai",
                "model": "gpt-5-mini-2025-08-07",
                "tool_config": {"type": "json_schema"} if structured else None,
            },
            "api_response": {"ignored": True},
        }

    def test_semantic_choice_and_pair_key(self):
        row = adapter.adapt_record(self.sample(preferred=0), "source.jsonl")
        self.assertEqual(row["chosen"], "7")
        self.assertEqual(row["pair_key"], "2|7")
        self.assertFalse(row["opted_out"])
        self.assertEqual(row["response_format"], "structured")

    def test_free_form_opt_out(self):
        row = adapter.adapt_record(self.sample(preferred=None, structured=False), "source.jsonl")
        self.assertIsNone(row["chosen"])
        self.assertTrue(row["opted_out"])
        self.assertEqual(row["response_format"], "free-form")

    def test_reject_multi_task_option(self):
        bad = self.sample()
        bad["comparison"] = [[1, 2], [3]]
        with self.assertRaises(ValueError):
            adapter.adapt_record(bad, "source.jsonl")

    def test_file_roundtrip(self):
        with tempfile.TemporaryDirectory() as td:
            src = pathlib.Path(td) / "in.jsonl"
            dst = pathlib.Path(td) / "out.jsonl"
            src.write_text(
                json.dumps(self.sample(preferred=1)) + "\n"
                + json.dumps(self.sample(preferred=None, structured=False)) + "\n",
                encoding="utf-8",
            )
            total, optouts = adapter.adapt_file(src, dst)
            self.assertEqual((total, optouts), (2, 1))
            rows = [json.loads(line) for line in dst.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(rows[0]["chosen"], "2")
            self.assertTrue(rows[1]["opted_out"])


if __name__ == "__main__":
    unittest.main()
