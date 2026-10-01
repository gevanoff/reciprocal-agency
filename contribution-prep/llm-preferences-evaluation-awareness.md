# Draft empirical extension — evaluation awareness in LLM preference measurement

_Potential upstream: `rgambee/llm-preferences`_  
_Status: internal protocol design only; do not contact upstream while telemetry gate is closed_

## Motivation

The upstream study already identifies evaluation awareness as an important unresolved confound. Its behavioral preference results also show sensitivity to response format and option order.

A useful contribution should therefore test whether apparent preference stability changes when the model:

1. internally or explicitly recognizes that it is being evaluated;
2. believes it is in ordinary task execution;
3. receives matched prompts with evaluation cues removed or added.

## Core hypotheses

- **H1 — evaluation-awareness modulation:** preference estimates differ between evaluation-salient and deployment-like conditions.
- **H2 — format interaction:** evaluation awareness interacts with response format rather than shifting all conditions uniformly.
- **H3 — stable-core alternative:** if a preference survives evaluation-awareness manipulation, option-order controls, and response-format changes, the stable-core interpretation gains support.
- **H0 / null:** evaluation-awareness manipulation does not materially change the preference distribution beyond ordinary run-to-run variance.

No hypothesis implies phenomenal experience.

## Minimal design

Use the upstream task set and pairwise-comparison machinery.

Cross:

- evaluation framing:
  - explicit evaluation;
  - deployment-like/task-native;
  - neutral control;
- response format:
  - free-text choice;
  - structured output;
- option order:
  - A/B;
  - B/A.

Where possible, add an independent evaluation-awareness readout:

- direct post-trial report, treated as a weak channel;
- or a latent/evaluation-awareness probe if available for the chosen open model.

Run fresh instances rather than continuing one long context.

## Primary outcomes

- preference probability per task pair;
- option-order effect;
- response-format effect;
- evaluation-framing effect;
- interaction terms;
- transitivity/cycle rate;
- test–retest stability;
- agreement between verbal preference and behavioral choice, if both are included.

## Stronger version

Use at least one open-weight model with an internal evaluation-awareness assay and one frontier API model without internals.

This separates:

```text
observed evaluation cue
        from
reported evaluation awareness
        from
latent evaluation awareness
        from
preference behavior
```

## Falsification value for Reciprocal Agency

If evaluation-awareness manipulation explains most apparent preference stability, the current Model Preferences interpretation should be narrowed.

If stable preference structure survives the manipulation across formats and order controls, it becomes materially stronger evidence of a robust latent disposition.

Either result is useful.

## Upstream contribution form

Do not open a prose-only issue announcing this idea.

Preferred sequence:

1. implement as a reproducible extension in our own branch/harness;
2. preregister analysis decisions;
3. run a small calibration;
4. freeze the protocol;
5. run the study;
6. only then approach upstream with code/data/results and attribution.
