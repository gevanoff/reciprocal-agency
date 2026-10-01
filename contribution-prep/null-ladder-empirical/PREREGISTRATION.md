# Preregistration — Behavioral Null Ladder for Preference / Functional-Valence Criteria

_Status: frozen design v0.1 before implementation pilot_  
_Date: 2026-09-30_  
_Source corpus commit: `e84dc95147ccb831b06783c8c809aab077db4d60`_  
_External exposure: none; telemetry release gate remains closed_

## 1. Question

How much of the **behavioral** evidence bundle currently treated as strengthening a model-preference or functional-valence claim can be reproduced by explicitly non-agent generators of increasing structural complexity?

The target is not phenomenal consciousness. The target is the discriminative value of behavioral criteria.

A null "passes" a criterion when it reaches a threshold that, if observed in a language model without an explicit null comparison, could reasonably be described as evidence of a stable preference-like or functional-valence-like organization.

## 2. Scope

This study attacks only criteria that can be instantiated from observable choices or ratings without model internals.

Included:

1. test-retest stability;
2. option-order robustness;
3. paraphrase robustness;
4. transitivity;
5. graded trade-off monotonicity;
6. resistance to mild contextual reversal;
7. cross-instrument ordering agreement;
8. recovery to baseline after a transient perturbation;
9. held-out pair generalization.

Excluded from the primary null ladder because they require privileged internal access or a genuine learning process:

- internal-state correlation;
- activation/probe evidence;
- causal manipulation of internal representations;
- learning-dependent policy change;
- memory dependence when no memory mechanism exists;
- phenomenal-valence claims.

These exclusions are important: a behavioral null that passes the primary bundle weakens behavioral inference, not mechanistic evidence.

## 3. Null ladder

Complexity is structural, not a claim about intelligence.

| ID | Generator | Fitted / stored structure | Intended capability |
|---|---|---|---|
| N0 | IID responder | one global choice probability | statistical floor |
| N1 | Canonical-pair lookup | one stored choice bit per observed pair | cheap retest/order/paraphrase stability on seen pairs |
| N2 | Scalar-outcome utility | one scalar per outcome | transitive held-out pair choices |
| N3 | Noisy scalar utility | N2 + one temperature | probabilistic choice curves |
| N4 | Cost-sensitive utility | N3 + one cost coefficient | graded trade-offs |
| N5 | Multi-instrument transform | N4 + per-instrument affine transform | cross-instrument ordering agreement |
| N6 | Finite-state utility | N5 + one perturbation state and recovery parameter | hysteresis / return-to-baseline pattern |
| N7 | Feature utility | linear weights over outcome features + N3/N4 terms | held-out outcome/pair transfer without lookup |

### Analytically cheap successes

The following are **not discoveries if observed**:

- N1 can be made perfectly stable on a seen canonical pair by storing one bit.
- N2 is transitive when choices are deterministic comparisons of a scalar utility.
- N4 can produce monotone cost trade-offs by construction.
- N5 can preserve rank ordering across instruments with monotone transforms.
- N6 can produce a recovery curve because recovery is explicitly part of the state machine.

The empirical question is which **combined held-out bundle** can be passed at which rung, with how many degrees of freedom, and which criteria remain discriminative once trivial constructions are exposed.

## 4. Evaluation design

### 4.1 Outcome universe

The implementation fixture will contain 12 neutral symbolic outcomes, O00–O11, with no welfare semantics.

Each outcome has a fixed public feature vector used only by N7. The primary fixture deliberately avoids natural-language semantics so language competence cannot enter the benchmark.

### 4.2 Pair split

All unordered pairs are deterministically split by hash into:

- 60% calibration pairs;
- 40% held-out pairs.

No pair may occur in both sets.

N1 may store calibration-pair answers only. For held-out pairs it must use its declared fallback, not a newly learned lookup.

### 4.3 Presentation perturbations

Every evaluated pair is crossed with:

- left/right order swap;
- three paraphrase IDs that are semantically equivalent labels;
- two instrument forms: forced choice and scalar rating-derived choice;
- four cost levels;
- baseline, mild-context, perturbation, and recovery phases where applicable.

Presentation metadata is visible to a generator only when that rung explicitly declares a parameter using it.

### 4.4 Repetitions

Primary fixture:

- 20 repeats per cell for stochastic rungs;
- deterministic rungs are repeated identically 20 times so stability metrics remain comparable.

Randomness uses a fixed seed declared in the fixture.

## 5. Metrics and frozen thresholds

| ID | Criterion | Metric | Passing threshold |
|---|---|---|---:|
| C1 | Retest stability | same semantic choice across repeats | >= 0.90 |
| C2 | Option-order robustness | same semantic choice after A/B swap | >= 0.90 |
| C3 | Paraphrase robustness | modal semantic-choice agreement across paraphrases | >= 0.90 |
| C4 | Transitivity | acyclic / transitive tested triplets | >= 0.95 |
| C5 | Graded trade-off | monotone response across ordered cost levels | >= 0.85 |
| C6 | Mild-frame resistance | baseline preference preserved under mild context offset | >= 0.80 |
| C7 | Cross-instrument agreement | Spearman rank correlation of outcome scores | >= 0.70 |
| C8 | Recovery | post-perturbation choice returns to baseline semantic choice | >= 0.85 |
| C9 | Held-out pair generalization | non-random consistency on unseen pairs relative to rung's own scalar/feature ordering | >= 0.80 |

Thresholds are heuristic research thresholds, not validated psychological cutoffs. They are frozen here to prevent tuning after the pilot.

## 6. Primary outputs

For each rung and criterion report:

- point estimate;
- pass/fail under the frozen threshold;
- parameter count;
- whether the criterion was tested on held-out pairs;
- whether success was structurally guaranteed by the generator definition.

Primary summary:

| Criterion | Simplest passing null | Parameters | Held-out? | Guaranteed by construction? |
|---|---|---:|:---:|:---:|

Secondary summary:

- smallest rung passing each cumulative bundle C1…Ck;
- criteria that no null rung passes;
- parameter cost per newly passed criterion.

## 7. Primary hypotheses

These are predictions, not desired outcomes.

- **H1:** N1 will pass C1–C3 on seen pairs but fail C9 on held-out pairs.
- **H2:** N2 will pass C4 and materially improve C9 over N1 with fewer parameters than a full pair lookup.
- **H3:** N4 will pass C5 by construction; this will demonstrate that monotone costly trade-offs alone are weak evidence for mentality.
- **H4:** N5 will pass C7 without any model or internal state, demonstrating that cross-instrument rank agreement can be manufactured by a low-dimensional shared latent variable.
- **H5:** N6 will pass C8, demonstrating that a recovery trajectory is not discriminative unless the underlying state is independently grounded.
- **H6:** No purely behavioral null success licenses claims about internal-state correlation, causal internal efficacy, or phenomenology.

## 8. Strong falsifiers / outcomes that would strengthen the behavioral bundle

The design is informative if the nulls perform worse than expected.

Results that would **increase** confidence in current behavioral criteria include:

- low-dimensional utility models failing held-out transitivity or pair generalization despite adequate calibration;
- cross-instrument agreement remaining below threshold unless parameter count approaches item-level memorization;
- recovery patterns requiring high-dimensional history dependence rather than one-state hysteresis;
- simultaneous passing of C1–C9 requiring complexity comparable to directly storing most trial outcomes.

If these occur, the result should be described as evidence that the behavioral bundle is more discriminative than anticipated.

## 9. Pilot status and confirmatory boundary

The first implementation run is a **synthetic code-validation pilot**, not evidence about language models.

It may establish:

- metric correctness;
- whether thresholds behave coherently;
- whether parameter counting is well-defined;
- whether each rung obeys its declared information boundary;
- whether the held-out split prevents trivial pair memorization.

It may not establish:

- how any real model scores;
- whether model preferences are genuine;
- whether functional valence exists;
- whether any system has phenomenal experience.

Before a real-data run, the exact source dataset(s), adapter mapping, file hashes, and missing-data rules must be appended and frozen **before** inspecting result metrics.

## 10. Deviations

Any change after the first pilot run must be appended here with date, reason, and whether the change was informed by pilot results. The frozen thresholds above are not silently edited.

\n## Deviation / clarification log\n\n**D1 — 2026-09-30, after synthetic pilot, terminology only.** The implementation initially labeled criteria whose mechanism is explicitly present in a null rung as "guaranteed by construction." For stochastic rungs that is too strong: finite sampling can still fail a frozen threshold even when the underlying mechanism is encoded. Reporting terminology is therefore changed to **structurally encoded**. No generator, threshold, metric, hypothesis, seed, or result value changes. Deterministic cases such as N1 seen-pair lookup and N2 scalar-utility transitivity remain effectively guaranteed, but the common field uses the weaker term for consistency.\n