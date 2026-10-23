#!/usr/bin/env bash
set -Eeuo pipefail
umask 077
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
: "${GITHUB_TOKEN:?Provide a least-privilege GitHub token through a local secret store}"
export GITHUB_REPOSITORY="${GITHUB_REPOSITORY:-gevanoff/reciprocal-agency}"
[[ "$GITHUB_REPOSITORY" == "gevanoff/reciprocal-agency" ]] || { echo "GITHUB_REPOSITORY must match the canonical repository" >&2; exit 2; }
OUT_DIR="${DISCOVERY_TELEMETRY_DIR:-$ROOT/out/discovery}"
mkdir -p "$OUT_DIR"
if [[ -n "${DISCOVERY_TELEMETRY_OUT:-}" ]]; then
  OUTPUT="$DISCOVERY_TELEMETRY_OUT"
  mkdir -p "$(dirname "$OUTPUT")"
else
  OUTPUT="$(mktemp "$OUT_DIR/discovery-$(date -u +%Y%m%dT%H%M%SZ)-XXXXXXXX.json")"
fi
export DISCOVERY_TELEMETRY_OUT="$OUTPUT"
python3 scripts/collect-discovery-telemetry.py
test -s "$OUTPUT"
echo "Telemetry snapshot saved: $OUTPUT"
