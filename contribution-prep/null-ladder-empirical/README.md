# Behavioral Null-Ladder Empirical Preparation

_Status: internal empirical preparation; external exposure blocked by telemetry gate_

This directory turns the conceptual Null Ladder extension into a reproducible synthetic pilot and a preregisterable real-data harness.

## Files

- `PREREGISTRATION.md` — frozen criteria, thresholds, generator ladder, hypotheses, and interpretation boundary committed before the implementation pilot.
- `run_pilot.py` — deterministic, standard-library-only synthetic benchmark.
- `test_pilot.py` — regression tests for the split, deterministic output, and expected rung capabilities.
- `pilot-results.json` / `PILOT_RESULTS.md` — canonical generated code-validation outputs after the preregistration commit; the documented command must reproduce them byte-for-byte.

## Run

```bash
cd contribution-prep/null-ladder-empirical
python3 test_pilot.py
python3 run_pilot.py --json-out pilot-results.json --md-out PILOT_RESULTS.md >/dev/null
```

No external model, API, or package is required.

## What the pilot can establish

It can test whether the benchmark operationalizes the frozen criteria correctly and whether declared non-agent structures can cheaply manufacture behavioral signatures such as stability, transitivity, cost curves, cross-instrument agreement, and recovery.

It cannot establish anything about a real model until a public empirical dataset, adapter mapping, and source hashes are frozen before result inspection.

## Release gate

Do not contact or submit to `Mulaydm10/null-ladder` while the telemetry gate is closed. Internal development is allowed.
