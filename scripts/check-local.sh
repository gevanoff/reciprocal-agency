#!/usr/bin/env bash
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
PYTHON="${PYTHON:-python3}"
"$PYTHON" -m unittest discover -s tests -p 'test_*.py' -v
(cd contribution-prep/null-ladder-empirical &&
  "$PYTHON" test_pilot.py &&
  "$PYTHON" test_adapter.py &&
  "$PYTHON" run_pilot.py --json-out pilot-results.json --md-out PILOT_RESULTS.md >/dev/null &&
  git diff --exit-code -- pilot-results.json PILOT_RESULTS.md)
if [[ "${1:-}" != "--quick" ]]; then
  temp="$(mktemp -d)"
  trap 'rm -rf -- "$temp"' EXIT
  "$PYTHON" scripts/run-subject-boundary-benchmark.py --samples 20000 --seed 1729 --out "$temp/subject-boundary-benchmark.json"
  test -s "$temp/subject-boundary-benchmark.json"
else
  echo "Quick mode selected: large synthetic benchmark NOT run"
fi
echo "Reciprocal Agency local validation passed"
