#!/usr/bin/env bash
set -Eeuo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
: "${GITHUB_TOKEN:?Provide a limited-scope GitHub token locally, not in a repo}"
OUTPUT="${DISCOVERY_TELEMETRY_OUT:-$ROOT/out/discovery-telemetry.json}"
mkdir -p "$(dirname "$OUTPUT")"
export DISCOVERY_TELEMETRY_OUT="$OUTPUT"
python3 scripts/collect-discovery-telemetry.py
test -s "$OUTPUT"
echo "Telemetry saved: $OUTPUT"
