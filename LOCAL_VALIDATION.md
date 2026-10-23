# Local validation and telemetry

`bash scripts/check-local.sh`: repository unittest regression suite, null-ladder tests and reproducibility, and subject-boundary benchmark (20,000 samples, seed 1729). `--quick` explicitly skips the large benchmark. Requires a Python environment with repository dependencies.

`GITHUB_TOKEN=... bash scripts/run-discovery-telemetry-local.sh`: replaces the collection job with an explicit local invocation. Set `DISCOVERY_TELEMETRY_OUT` for durable output storage (default `out/discovery-telemetry.json`). Never commit the GitHub token. Use a least-privilege token provisioned through a local secret store.

**Scheduling is deliberately not installed by these changes.** To restore the previous daily collection, install a systemd timer or host scheduler on a trusted Nexus machine at 08:17 UTC daily, with the required token and persistent output location. Until then no fresh automatic telemetry arrives. The benchmark JSON now lands in a temporary directory by default; save an artifact explicitly if needed.

All three GitHub Actions workflows are removed. Local execution remains unverified. Record exact SHA, versions and output when reviewing.
