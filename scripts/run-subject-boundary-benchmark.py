#!/usr/bin/env python3
"""Run the WP1 synthetic subject-boundary benchmark."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from subject_boundary.benchmark import (
    coupling_sweep,
    default_scenarios,
    summarize,
    validation_checks,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=1729)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("subject-boundary-benchmark.json"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    summaries = [
        summarize(
            scenario,
            samples=args.samples,
            seed=args.seed + index * 100,
        )
        for index, scenario in enumerate(default_scenarios())
    ]
    checks = validation_checks(summaries)
    output = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "samples_per_scenario": args.samples,
        "seed": args.seed,
        "epistemic_scope": (
            "Synthetic causal-boundary validation only; not a consciousness "
            "or phenomenal-subject assay."
        ),
        "scenario_results": summaries,
        "coupling_sweep": coupling_sweep(
            samples=args.samples,
            seed=args.seed + 10_000,
        ),
        "validation_checks": checks,
        "all_validation_checks_passed": all(
            row["passed"] for row in checks.values()
        ),
    }
    args.out.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["all_validation_checks_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
