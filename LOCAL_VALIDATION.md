# Local validation and telemetry

`bash scripts/check-local.sh`: repository unittest regression suite, null-ladder tests and reproducibility, and subject-boundary benchmark (20,000 samples, seed 1729). `--quick` explicitly skips the large benchmark.

`GITHUB_TOKEN=... bash scripts/run-discovery-telemetry-local.sh`: collects repository aggregates on a trusted host. The wrapper sets and validates `GITHUB_REPOSITORY=gevanoff/reciprocal-agency` and writes unique timestamped output files in `out/discovery/` by default (`DISCOVERY_TELEMETRY_DIR` overrides location). If `DISCOVERY_TELEMETRY_OUT` is explicitly supplied, **the caller is responsible for making it unique**. GitHub tokens must be stored and provided via local secret management.

**No scheduler is installed by these changes.** To replace the retired Actions schedule, configure an independently managed systemd timer or other host scheduler at 08:17 UTC daily with persistent output, backups and an explicit retention policy. The GitHub Traffic API has a rolling observation window, so missing runs lose historical evidence. There is no longer a 90-day GitHub artifact retention guarantee.

Three hosted workflows are removed. Local execution has not been verified; capture exact SHA, interpreter and output during independent review.
