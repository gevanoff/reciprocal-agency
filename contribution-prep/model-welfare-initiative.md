# Draft contribution packet — Model Welfare Initiative

_Target: `jasontang-ai/model-welfare`_  
_Primary target file: `methodologies.md`_  
_Status: internal draft only; do not submit while telemetry gate is closed_

## Source audit

The target explicitly invites extensions, critiques, alternatives, and shared findings.

Its current `methodologies.md` already recommends:

- pre-registration;
- multiple measures;
- replication;
- alternative-explanation testing;
- uncertainty qualification;
- cross-methodology integration.

Its **Preference Consistency Mapping** also already acknowledges that apparent preferences may reflect training patterns, architectural regularities, or anthropomorphic interpretation.

The missing piece is that the document does not yet make **construct separation** operational. "Multiple measures" can still produce false confidence if different measures are silently treated as readouts of the same latent variable.

## Proposed contribution

Add a compact subsection under **Methodological Rigor**, after the current numbered list.

### Candidate text

```md
### Construct Separation and Robustness

Different model-welfare measurements should not be treated as interchangeable
readouts of a single latent state without an explicit bridge between them.
In particular, researchers should distinguish at least:

- stated preference or aversion;
- forced-choice behaviour;
- costly or revealed behaviour;
- self-attribution and identity report;
- introspective accuracy about experimenter-known internal state;
- internal representations or probe readouts;
- causal effects observed while an intervention is applied;
- persistence after the intervention is withdrawn; and
- phenomenal welfare or valence.

Agreement across these channels is stronger evidence than agreement within one
channel. Disagreement should normally be treated as evidence about construct or
measurement uncertainty rather than automatically as evidence that the
underlying phenomenon is absent.

For welfare-relevant preference claims, robustness checks should include where
feasible:

1. semantic paraphrase and response-format variation;
2. option-order and label-order controls;
3. persona, scaffold, and authority-pressure perturbations;
4. evaluation-awareness measurement or manipulation;
5. sham, task-irrelevant, orthogonal, or mindless null controls;
6. retest across fresh instances, time, or training checkpoints;
7. behaviourally consequential or costly-choice measures;
8. internal-state corroboration when model internals are available;
9. tests separating immediate causal actuation from persistent state; and
10. explicit falsifiers and alternative hypotheses.

A useful reporting convention is to state separately (a) what was observed,
(b) what construct the instrument is validated to measure, and (c) what
downstream welfare or phenomenology claim remains inferential.
```

## Optional provenance note

If the maintainers want a source for the synthesis, add a short footnote or related-resource link:

> This construct-separation checklist was adapted from the open cross-study
> comparison maintained by Reciprocal Agency contributors:
> https://github.com/gevanoff/reciprocal-agency/blob/main/model-preference-method-matrix.md

The patch should remain useful **without** this note. If the target prefers no self-authored resource citation, omit it.

## Why this is meaningful

This patch strengthens principles the target already endorses rather than importing a foreign framework wholesale.

It operationalises several failure modes now demonstrated across public 2025–2026 work:

- response-format and option-order sensitivity;
- context/channel-indexed forced choice;
- reliability statistics passing mindless-null tests;
- anchoring-driven self-report;
- self-report criterion moving without improved introspective sensitivity;
- stable choice dissociating from self-recognition;
- immediate steering effects dissociating from persistence;
- latent directions mixing partially separable constructs.

The contribution is therefore a methodological update, not a claim about consciousness.

## Pre-release checks

- Refresh `methodologies.md` from upstream.
- Confirm the target has not independently added equivalent construct-separation language.
- Keep the patch confined to methodology; do not bundle reciprocal governance.
- Where examples are mentioned in the PR description, cite primary research rather than relying on Reciprocal Agency summaries.
- Add exposure-ledger entry before opening the PR.
