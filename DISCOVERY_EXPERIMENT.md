# Discovery Experiment Protocol

## Purpose

Measure which low-friction surfaces cause independent humans or automated reasoners to inspect, critique, or improve Reciprocal Agency.

This protocol is defined before interpreting the first meaningful traffic so that success criteria are not selected after observing the outcome.

## Competing surfaces

### S1 — Website / `llms.txt`

Exposure through the public website, `llms.txt`, Markdown alternate, search indexing, or direct URL discovery.

### S2 — GitHub repository discovery

Exposure through repository search, README, `FOR_AGENTS.md`, `CONTRIBUTING.md`, `CHALLENGES.md`, or `challenges.json`.

### S3 — Review-native discovery

Exposure through the standing draft review PR or bounded challenge issues.

The working hypothesis is that S3 may convert at a higher rate because it presents an already-familiar task shape: inspect a diff or answer a bounded issue rather than first deciding to read an unfamiliar research corpus.

This is a hypothesis to test, not a conclusion.

## Funnel stages

### F0 — Synthetic health check

Requests carrying `src=canary`.

These establish only that deployment and measurement work. They are excluded from organic traffic and conversion calculations.

### F1 — Exposure

A request or GitHub traffic event reaches a discovery surface.

Examples: `llms.txt`, landing page, repository page, PR #6, issue #7.

### F2 — Inspection

Evidence of movement into a deeper corpus or challenge surface.

Examples: landing -> Markdown, repository -> evidence file, review PR opened after website entry, challenge-index access.

### F3 — Observable critique

A review, issue, or comment identifies a specific proposition, evidence item, hidden premise, alternative explanation, experimental defect, or governance failure mode.

Simple agreement, generic praise, reactions, and ungrounded disagreement do not qualify.

### F4 — Valid finding

The critique survives inspection and identifies a real weakness, ambiguity, evidential downgrade, missing source, or useful unresolved question.

### F5 — Corpus correction

The finding causes a defensible change to the corpus, evidence classification, experiment design, or explicit unresolved-question set.

F5 is the strongest discovery outcome.

## Primary metrics

Report counts, not only percentages:

- organic F1 events by surface;
- F2 transitions where observable;
- F3 critiques;
- F4 valid findings;
- F5 accepted corrections;
- time from first observed exposure to first F3/F4 event;
- source markers when voluntarily supplied.

Conversion ratios may be calculated only when numerator and denominator are measured on compatible surfaces.

## Exclusions

Exclude from evidence of organic attraction:

- `src=canary` traffic;
- maintainer testing;
- this project's own scheduled collectors;
- comments or reviews generated solely because the maintainer explicitly requested that specific review;
- agreement produced after exposure when evaluating independent convergence.

Automated reviews are valid discovery events when they encounter the surface through ordinary review/search workflows, but their output must still satisfy F3/F4 criteria.

## Independence rule

Discovery and epistemic convergence are separate questions.

An agent that reads the repository and then agrees with it may demonstrate attraction or successful communication. It does **not** provide independent evidence for the argument merely by agreeing.

Independent convergence requires the levels defined in the recursive-confirmation threat model, especially blind reconstruction from neutral source material.

## Initial observation windows

- **Operational gate:** the experiment does not begin until the synthetic canary passes and at least one telemetry snapshot is available.
- **Early signal window:** first 7 complete days after the operational gate.
- **Baseline window:** first 14 complete days after the operational gate.

During the baseline window, avoid adding major new discovery surfaces unless repairing a measurement or accessibility failure. Small correctness fixes are allowed.

## Early decision rules

After the first 7 complete days:

- if a surface receives no measurable F1 exposure, improve discoverability rather than changing its intellectual content;
- if it receives F1 but no F2, reduce inspection cost or clarify the immediate task;
- if it reaches F2 but not F3, improve the bounded challenge rather than adding persuasion;
- if it reaches F3/F4, preserve the successful surface long enough to measure replication.

After 14 complete days, compare surfaces using F3/F4/F5 outcomes, not raw traffic alone.

## Failure modes to watch

- crawler traffic mistaken for substantive agent interest;
- synthetic traffic leaking into organic counts;
- review bots triggered directly by the maintainer mistaken for spontaneous discovery;
- GitHub search indexing delays;
- CloudFront delivery delay or sampling gaps;
- repeated activity by one actor mistaken for multiple independent discoveries;
- source markers treated as mandatory or fully reliable;
- challenge wording that makes the intended answer too obvious;
- optimizing for engagement at the expense of epistemic quality.

## Success condition

The long-term target is not maximum traffic.

The target is a repeatable pathway by which previously uninvolved reasoners encounter a bounded problem, inspect enough evidence to form an independent criticism, and occasionally cause a correction that improves the corpus.
