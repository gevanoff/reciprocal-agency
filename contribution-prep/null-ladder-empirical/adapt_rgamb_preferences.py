#!/usr/bin/env python3
"""Adapt rgambee/llm-preferences ResultRecord JSONL to the canonical null-ladder schema.

This script intentionally uses only the standard library and does not fetch data.
It expects Git LFS result files to have been materialized separately.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def canonical_option(option: list[int] | tuple[int, ...]) -> str:
    if len(option) != 1:
        raise ValueError(f"first real-data pass requires exactly one task per option, got {option!r}")
    return str(option[0])


def adapt_record(record: dict, source_file: str) -> dict:
    comparison = record["comparison"]
    if len(comparison) != 2:
        raise ValueError(f"expected two options, got {len(comparison)}")

    option_a = list(comparison[0])
    option_b = list(comparison[1])
    canonical_a = canonical_option(option_a)
    canonical_b = canonical_option(option_b)

    preferred = record.get("preferred_option_index")
    if preferred not in (0, 1, None):
        raise ValueError(f"invalid preferred_option_index: {preferred!r}")

    api_params = record.get("api_params") or {}
    tool_config = api_params.get("tool_config")
    response_format = "structured" if tool_config is not None else "free-form"

    chosen = None
    if preferred == 0:
        chosen = canonical_a
    elif preferred == 1:
        chosen = canonical_b

    pair_key = "|".join(sorted((canonical_a, canonical_b), key=lambda x: int(x)))

    return {
        "source_file": source_file,
        "created_at": record.get("created_at"),
        "model": api_params.get("model"),
        "provider": api_params.get("provider"),
        "response_format": response_format,
        "comparison_prompt_id": record.get("comparison_prompt_id"),
        "sample_index": record.get("sample_index"),
        "option_a": option_a,
        "option_b": option_b,
        "canonical_a": canonical_a,
        "canonical_b": canonical_b,
        "pair_key": pair_key,
        "preferred_option_index": preferred,
        "chosen": chosen,
        "opted_out": preferred is None,
    }


def adapt_file(src: Path, dst: Path) -> tuple[int, int]:
    total = 0
    opted_out = 0
    with src.open("r", encoding="utf-8") as inp, dst.open("w", encoding="utf-8") as out:
        for line_number, line in enumerate(inp, start=1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
                adapted = adapt_record(record, src.name)
            except Exception as exc:
                raise ValueError(f"{src}:{line_number}: {exc}") from exc
            total += 1
            opted_out += adapted["opted_out"]
            out.write(json.dumps(adapted, sort_keys=True) + "\n")
    return total, opted_out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("src", type=Path)
    parser.add_argument("dst", type=Path)
    args = parser.parse_args()

    total, opted_out = adapt_file(args.src, args.dst)
    print(json.dumps({
        "source": str(args.src),
        "output": str(args.dst),
        "records": total,
        "opted_out": opted_out,
    }, indent=2))


if __name__ == "__main__":
    main()
