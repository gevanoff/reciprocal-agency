#!/usr/bin/env bash
set -Eeuo pipefail
CALLER_DIR="$(pwd -P)"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
PYTHON="${PYTHON:-python3}"
# Honor interpreter paths relative to the invoking directory, not the
# benchmark subshell's working directory.
if [[ "$PYTHON" == */* && "$PYTHON" != /* ]]; then
  PYTHON="$CALLER_DIR/$PYTHON"
fi
cd "$ROOT"
temp="$(mktemp -d)"
trap 'rm -rf -- "$temp"' EXIT

"$PYTHON" -m unittest discover -s tests -p 'test_*.py' -v
(cd contribution-prep/null-ladder-empirical &&
  "$PYTHON" test_pilot.py &&
  "$PYTHON" test_adapter.py &&
  "$PYTHON" run_pilot.py --json-out "$temp/pilot-results.json" --md-out "$temp/PILOT_RESULTS.md" >/dev/null)
# Never overwrite an operator's tracked or uncommitted experiment output.
diff -u contribution-prep/null-ladder-empirical/pilot-results.json "$temp/pilot-results.json"
diff -u contribution-prep/null-ladder-empirical/PILOT_RESULTS.md "$temp/PILOT_RESULTS.md"

if [[ "${1:-}" != "--quick" ]]; then
  "$PYTHON" scripts/run-subject-boundary-benchmark.py --samples 20000 --seed 1729 --out "$temp/subject-boundary-benchmark.json"
  test -s "$temp/subject-boundary-benchmark.json"
else
  echo "Quick mode selected: large synthetic benchmark NOT run"
fi
echo "Reciprocal Agency local validation passed"
