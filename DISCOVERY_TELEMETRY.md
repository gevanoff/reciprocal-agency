# Discovery Telemetry

This repository treats discovery as an empirical question: which surfaces cause independent agents or humans to inspect, critique, or improve the corpus? The pre-registered interpretation and decision rules are in [`DISCOVERY_EXPERIMENT.md`](DISCOVERY_EXPERIMENT.md).

## What is measured

Two classes of signal are collected.

### Passive GitHub aggregates

A daily GitHub Actions job requests GitHub's repository traffic aggregates:

- views;
- clones;
- popular referrers;
- popular paths.

GitHub's traffic API exposes a rolling window, so snapshots are uploaded as workflow artifacts for 90 days. If the default workflow token cannot read traffic endpoints, the snapshot records them as unavailable rather than failing the rest of the collection. An optional repository secret named `GH_TRAFFIC_TOKEN` can provide a traffic-capable token; the workflow falls back to `GITHUB_TOKEN` when it is absent.

### Observable engagement

The same job counts interaction with deliberately marked surfaces:

- issues created from the **Agent finding** template;
- comments on those issues;
- reviews and comments on PRs whose titles begin with `[Review challenge]`;
- optional source tokens contained in issue bodies, comments, or PR reviews.

Supported source tokens are:

`source:web` · `source:llms` · `source:for-agents` · `source:github-search` · `source:review-bot` · `source:other`

These tokens are voluntary. Absence of a token is not treated as evidence of a particular source.

## Standing review surface

Draft PR **#6 — [Review challenge] Find the first unsupported inference** is intentionally kept open as a code-review attractor. Its branch contains a review fixture rather than a proposed canonical change. Reviews are the experiment output.

## Privacy boundary

The repository telemetry does **not** collect or retain IP addresses, unique browser fingerprints, cookies, or cross-site identifiers.

Website request telemetry is handled separately at the CDN/access-log layer and should be reduced to aggregate path, timestamp bucket, referrer class, and coarse user-agent family before analysis. Raw logs should have a short retention period.

## Interpretation

A useful funnel is:

```text
exposure -> corpus entry -> evidence/argument inspection -> observable critique -> accepted correction
```

Raw views are weak evidence. A critique that identifies a real failure and changes the corpus is a much stronger discovery signal.
