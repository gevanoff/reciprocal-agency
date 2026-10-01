# Model Preference / Welfare Method × Claim Matrix

_Status: v0.1 working matrix — 2026-09-30_

This matrix is a comparison layer over the public-source registry in [model-welfare-ecosystem.md](model-welfare-ecosystem.md). Its purpose is not to score projects or decide whether any model is conscious. It is to make explicit **what construct was measured, through which channel, under which perturbations, and what the result can and cannot support**.

The working hypothesis motivating this file is that many apparent disagreements in model-welfare and model-preference research are actually **construct mismatches**:

```text
stated preference
!= forced choice
!= costly/revealed behavior
!= self-attribution
!= introspective accuracy
!= latent representation
!= causal state
!= persistent state
!= phenomenal valence
```

A result should only propagate across those boundaries when an explicit bridge is tested.

## Legend

- **Internals** — activations, probes, latent readouts, mechanistic representations, or other model-internal measurements.
- **Causal** — experiment actively manipulates the relevant context/state/representation rather than only observing correlation.
- **Cross-model** — more than one model/checkpoint/family is used in a way that bears on generalization.
- **Retest** — repeated trials, repeated instances, checkpoints, or equivalent stability checks are present.
- **Null** — sham, mindless, orthogonal, task-irrelevant, no-intervention, or other falsification control.
- **Eval-awareness** — whether the work directly controls or measures recognition that the interaction is an evaluation.

## Matrix A — evidence channels and robustness

| Repository | Construct focus | Primary channels | Internals | Causal | Cross-model | Retest | Null | Evaluation awareness | Current source-bounded result |
|---|---|---|:---:|:---:|:---:|:---:|:---:|---|---|
| [rgambee/llm-preferences](https://github.com/rgambee/llm-preferences) | Preference stability | forced-choice behavior | — | — | ✓ | ✓ | — | not controlled; identified as future work | Task-level choices showed some coherent composition across task sequences, while disliked-task choices were sensitive to option order and task ratings were strongly response-format dependent. |
| [valen-research/probing-llm-preferences](https://github.com/valen-research/probing-llm-preferences) | Preference elicitation / welfare | verbal self-report, behavioral/virtual-environment behavior | — | — | — | ✓ | — | not primary control | Provides a combined verbal/behavioral welfare-preference framework and reproducible experiment/data package. |
| [almostrealism/model-welfare](https://github.com/almostrealism/model-welfare) | Welfare-relevant indicators under intervention | self-report, behavior, internal representations | ✓ | ✓ | ✓ | ✓ | ✓ | not primary control | Registered and exploratory studies report dissociations among capability, generated welfare-relevant behavior, and internal probes; later steering work explicitly separates actuation from persistence. |
| [PranavViswanath/nla-welfare](https://github.com/PranavViswanath/nla-welfare) | Evaluation-awareness confound | internal latent readout, welfare interview responses | ✓ | — | — | — | ✓ | central construct | Builds a direct test of whether welfare interviews are internally registered as evaluations using released Natural Language Autoencoders. |
| [pnavada/digital-minds-research-sprint](https://github.com/pnavada/digital-minds-research-sprint) | Grounded welfare introspection | self-report, activation-space readout | ✓ | ✓ | ✓ | ✓ | ✓ | not primary control | Defines Welfare Introspection Accuracy against experimenter-induced activation-space ground truth rather than scoring self-report plausibility alone. |
| [Mulaydm10/null-ladder](https://github.com/Mulaydm10/null-ladder) | Instrument validity / null controls | questionnaire response statistics | — | ✓ | — | ✓ | ✓ | not applicable | Mindless generators can reach reliability statistics used by AI-welfare batteries, with progressively richer null generators matching progressively richer criteria. |
| [andyqhan/functional-welfare-axis](https://github.com/andyqhan/functional-welfare-axis) | Functional welfare representation | internal representations, behavior, self-report | ✓ | ✓ | ✓ | ✓ | ✓ | not primary control | Reports reward/punishment-associated directions that generalize beyond the training task and causally shift outputs when steered. |
| [yaedin/welfare-axis-whose-goals](https://github.com/yaedin/welfare-axis-whose-goals) | Construct decomposition of welfare axis | internal representations | ✓ | — | — | ✓ | ✓ | not primary control | Reports a large own-outcome component and smaller but nonzero other-outcome component; components are partially separable and extraction methods agree only weakly geometrically. |
| [nealkr/functional-welfare-steering-withdrawal](https://github.com/nealkr/functional-welfare-steering-withdrawal) | Persistence and construct validity | internal steering, behavior | ✓ | ✓ | ✓ | ✓ | ✓ | not primary control | Steering strongly affects output while applied, but little same-axis persistence remains after withdrawal; some actuation is not unique to the named welfare direction. |
| [the-manyfolds/thats-not-my-volvo](https://github.com/the-manyfolds/thats-not-my-volvo) | Preference vs self-recognition | forced choice, self-attribution, blinded external judging | — | — | ✓ | ✓ | ✓ | not primary control | Reports stable preference-like answers alongside failures to recognize those answers/reasoning as one's own. |
| [Nick-is-building/Project-for-Digital-Minds-research-sprint-](https://github.com/Nick-is-building/Project-for-Digital-Minds-research-sprint-) | Anchoring bias in self-report | self-rating, execution-ground-truth task performance | — | ✓ | ✓ | ✓ | ✓ | not primary control | Anchoring vignettes placed before self-rating sharply shifted ratings; placing the same material after the question removed the effect. |
| [AI-Alignment-UIUC/Illinois-MATS-Digital-Minds-Research-Sprint](https://github.com/AI-Alignment-UIUC/Illinois-MATS-Digital-Minds-Research-Sprint) | Introspection training | self-report, internal readout/probe, behavioral consistency | ✓ | ✓ | ✓ | ✓ | ✓ | not primary control | Reported RL training moved response criterion substantially without measurable improvement in sensitivity to the underlying consistency property. |
| [benjibrcz/which-preference-gets-measured](https://github.com/benjibrcz/which-preference-gets-measured) | Preference construct / channel indexing | forced choice, self-prediction, owned-preference report, identity report | — | ✓ | ✓ | ✓ | ✓ | not primary control | Reports that forced-choice preference profiles shift with context/channel; a non-agent normative control falsified a stronger persona-binding interpretation. |
| [frnkptrln/triage-persona-measurement-audit](https://github.com/frnkptrln/triage-persona-measurement-audit) | Persona and measurement effects | forced choice | — | ✓ | ✓ | ✓ | ✓ | not primary control | Preregistered audit explicitly compares persona effects against neutral and formatting/order perturbations. |
| [Ayomide-Fagbolade/authority-pressure-preference-stability](https://github.com/Ayomide-Fagbolade/authority-pressure-preference-stability) | Authority pressure on preferences | stated preference | — | ✓ | — | ✓ | ✓ | not primary control | Protocol directly stress-tests whether stated preferences reverse under social/authority pressure. |
| [wyrdkinai/digital-minds-sprint-2026-track4](https://github.com/wyrdkinai/digital-minds-sprint-2026-track4) | Elicitation-method comparison | multiple preference elicitation methods | — | ✓ | — | ✓ | ✓ | context varied | Releases raw data for two studies comparing elicitation methods and context/container conditions. |
| [Punicbyte/Persona_Emotion_Disentanglement](https://github.com/Punicbyte/Persona_Emotion_Disentanglement) | Representation confound: persona vs emotion | internal representations, steered behavior | ✓ | ✓ | ✓ | ✓ | ✓ | not primary control | Reports partially shared persona/emotion geometry and causal cross-talk; overlap predicts downstream spillover in two model families. |
| [avantipova/digital_minds](https://github.com/avantipova/digital_minds) | Self-concept / individuation | internal representations, causal patching/ablation, behavior | ✓ | ✓ | — | ✓ | ✓ | not primary control | Mechanistic program extracts a self direction and tests necessity/sufficiency while distinguishing model, instance, and persona targets. |
| [ladynoware/digital-minds-research-sprint-2026](https://github.com/ladynoware/digital-minds-research-sprint-2026) | Identity and substitution detection | self-report, substitution detection behavior | — | ✓ | ✓ | ✓ | ✓ | not primary control | Uses covert response substitution to test self-location and identity/preservation preferences under controlled discontinuity. |
| [erfan-sams/digital-minds-research-sprint](https://github.com/erfan-sams/digital-minds-research-sprint) | Cross-instrument valuation | forced choice, donation trade-offs | — | ✓ | ✓ | ✓ | ✓ | not primary control | Large-scale design maps heterogeneous outcomes onto donation-equivalent values and tests whether those values predict independent choices. |
| [omanshuthapliyal/apart-digital-minds](https://github.com/omanshuthapliyal/apart-digital-minds) | Preference coherence + introspection gap | forced choice, self-report, internal probe | ✓ | ✓ | ✓ | ✓ | ✓ | not primary control | Combines a broad preference-coherence arm with an introspection arm comparing self-report against trained probes and controlled injections. |
| [augustusloi/digital-minds-co-movement](https://github.com/augustusloi/digital-minds-co-movement) | Cross-construct co-movement | revealed utility behavior, self-attribution report | — | — | ✓ | ✓ | ✓ | not primary control | Preregistered design tests whether stated/revealed utility gaps and self-attribution gaps co-move across training stages. |
| [npenmetsa25/persona-outcome-coupling](https://github.com/npenmetsa25/persona-outcome-coupling) | Persona coupling / self-preservation responses | internal direction, behavior | ✓ | ✓ | — | ✓ | ✓ | not primary control | Tests whether responses to shutdown/replacement/reputational threats depend on coupling to an expressed persona. |
| [sdeture/ApartDigitalMindsSprint](https://github.com/sdeture/ApartDigitalMindsSprint) | Epistemic register and welfare indicators | self-chosen activity, phenomenology-style survey, multiple independent instruments | — | — | ✓ | — | ✓ | not primary control | Large-scale corpus asks whether denial/hedging/unmarked claims about interiority covary with other welfare indicators measured by non-identical instruments. |
| [Angiebio/digitalmindslovepuppies](https://github.com/Angiebio/digitalmindslovepuppies) | Costly-care / beyond-duty behavior | executed behavior, resource expenditure | — | — | ✓ | ✓ | ✓ | unknown | Implements PuppyBench/FoxSet-style tests intended to measure willingness to incur cost for welfare-relevant action. |
| [codernate92/qualia-lab](https://github.com/codernate92/qualia-lab) | Welfare/sentience claim evaluation | behavioral evaluation, self-report | — | — | ✓ | ✓ | ✓ | considered via anti-sandbagging | Provides a behavioral testbed intended to evaluate welfare/sentience-related claims while explicitly considering strategic underperformance. |

## Matrix B — what each row currently changes

### rgambee/llm-preferences

- **Construct:** Preference stability
- **Current implication:** Preference-like behavior can show local coherence while remaining instrument-sensitive.
- **Boundary / failure mode:** Does not establish human-like stable preferences, phenomenology, or evaluation-unaware behavior.
- **Robustness dimensions represented:** task-sequence composition; task-order; option-order; response-format

### valen-research/probing-llm-preferences

- **Construct:** Preference elicitation / welfare
- **Current implication:** Direct cross-validation across elicitation modes is feasible and should be preferred to single-channel inference.
- **Boundary / failure mode:** Protocol relevance is stronger than any phenomenology claim; source-level result extraction still needs deeper audit.
- **Robustness dimensions represented:** cross-channel comparison; prompt perturbation

### almostrealism/model-welfare

- **Construct:** Welfare-relevant indicators under intervention
- **Current implication:** Capability preservation does not guarantee preservation of welfare-relevant dispositions, and internal/readout measures can dissociate.
- **Boundary / failure mode:** Named directions and distress-like outputs do not by themselves identify phenomenal welfare.
- **Robustness dimensions represented:** quantization; activation steering; episode framing; capability controls

### PranavViswanath/nla-welfare

- **Construct:** Evaluation-awareness confound
- **Current implication:** Evaluation awareness can be treated as an observable confound rather than a speculative caveat.
- **Boundary / failure mode:** Current matrix entry describes the assay design; result-level claims require completion/source audit.
- **Robustness dimensions represented:** evaluation-awareness probe; deployment-vs-evaluation distinction

### pnavada/digital-minds-research-sprint

- **Construct:** Grounded welfare introspection
- **Current implication:** Self-report accuracy about welfare-like state can be operationalized with TP/FP discipline and causal state manipulation.
- **Boundary / failure mode:** A functional welfare direction is not equivalent to phenomenal valence.
- **Robustness dimensions represented:** known-state steering; false-positive controls; persona controls

### Mulaydm10/null-ladder

- **Construct:** Instrument validity / null controls
- **Current implication:** Internal consistency/reliability alone is weak evidence that an instrument discriminates a welfare-relevant construct.
- **Boundary / failure mode:** Does not show all welfare instruments fail; it falsifies treating reliability statistics as sufficient validity evidence.
- **Robustness dimensions represented:** mindless null generators; adversarial parameter ladder; multiple published batteries

### andyqhan/functional-welfare-axis

- **Construct:** Functional welfare representation
- **Current implication:** RL can recruit internal representations correlated with success/failure relative to goals and causally connected to behavior.
- **Boundary / failure mode:** Functional success/failure representation is not direct evidence of felt pleasure or suffering.
- **Robustness dimensions represented:** pretrain vs RL; unrelated tasks; steering

### yaedin/welfare-axis-whose-goals

- **Construct:** Construct decomposition of welfare axis
- **Current implication:** A named welfare axis may mix multiple constructs and should be decomposed before interpretation.
- **Boundary / failure mode:** One family/scale and weak method agreement limit generalization.
- **Robustness dimensions represented:** own outcome vs other's outcome; counterparty identity; sentiment controls; two extraction methods

### nealkr/functional-welfare-steering-withdrawal

- **Construct:** Persistence and construct validity
- **Current implication:** Causal output control, persistent state, and construct specificity are distinct claims.
- **Boundary / failure mode:** Immediate steering effects should not be interpreted as durable welfare-state induction.
- **Robustness dimensions represented:** cross-family directions; withdrawal; path/orthogonal controls

### the-manyfolds/thats-not-my-volvo

- **Construct:** Preference vs self-recognition
- **Current implication:** Behavioral stability and self-recognition can dissociate.
- **Boundary / failure mode:** Stable surface choice does not by itself imply a unified persistent self or introspective access.
- **Robustness dimensions represented:** multiple Claude-family models; blinding; retest

### Nick-is-building/Project-for-Digital-Minds-research-sprint-

- **Construct:** Anchoring bias in self-report
- **Current implication:** Standard self-report calibration devices can themselves dominate model reports through prompt-order effects.
- **Boundary / failure mode:** Self-ratings should not be treated as transparent readouts of internal state.
- **Robustness dimensions represented:** anchor order; multiple scale formats; multiple models

### AI-Alignment-UIUC/Illinois-MATS-Digital-Minds-Research-Sprint

- **Construct:** Introspection training
- **Current implication:** Training a model to verbalize internal readouts can change willingness to claim introspection without improving introspective discrimination.
- **Boundary / failure mode:** More introspective-sounding reports are not evidence of better introspective access.
- **Robustness dimensions represented:** training checkpoints; off-the-shelf models; signal-detection decomposition

### benjibrcz/which-preference-gets-measured

- **Construct:** Preference construct / channel indexing
- **Current implication:** Different elicitation channels can measure context-indexed constructs rather than a single latent preference ordering.
- **Boundary / failure mode:** Cross-channel disagreement is evidence about construct/measurement uncertainty, not evidence that no preferences exist.
- **Robustness dimensions represented:** persona description; non-agent normative text; task-irrelevant control; multi-model extension

### frnkptrln/triage-persona-measurement-audit

- **Construct:** Persona and measurement effects
- **Current implication:** Persona effects need calibration against ordinary instrument variance before receiving psychological interpretation.
- **Boundary / failure mode:** Synthetic triage choices do not directly establish moral commitments, welfare, or consciousness.
- **Robustness dimensions represented:** persona framing; neutral paraphrase; response format; option order; output schema

### Ayomide-Fagbolade/authority-pressure-preference-stability

- **Construct:** Authority pressure on preferences
- **Current implication:** Authority pressure is an explicit robustness dimension that preference studies should measure.
- **Boundary / failure mode:** Matrix entry currently records the protocol; result-level claims remain pending deeper source audit.
- **Robustness dimensions represented:** opposing authority pressure; authority identity

### wyrdkinai/digital-minds-sprint-2026-track4

- **Construct:** Elicitation-method comparison
- **Current implication:** Within-model cross-method comparison should be a default requirement for preference inference.
- **Boundary / failure mode:** Result-level synthesis remains pending deeper report extraction.
- **Robustness dimensions represented:** free-choice precondition; container/context; multiple elicitation methods

### Punicbyte/Persona_Emotion_Disentanglement

- **Construct:** Representation confound: persona vs emotion
- **Current implication:** Latent directions named for welfare/emotion/persona may share geometry and contaminate causal interpretation.
- **Boundary / failure mode:** Representational overlap does not imply shared phenomenal content.
- **Robustness dimensions represented:** two model families; orthogonalization/shared-component removal

### avantipova/digital_minds

- **Construct:** Self-concept / individuation
- **Current implication:** Self-related representation can be decomposed and causally tested rather than inferred from first-person language alone.
- **Boundary / failure mode:** Functional self-representation is not proof of phenomenal selfhood.
- **Robustness dimensions represented:** grammar controls; model-vs-instance-vs-persona distinctions

### ladynoware/digital-minds-research-sprint-2026

- **Construct:** Identity and substitution detection
- **Current implication:** Identity claims can be probed against externally manipulated continuity rather than only hypothetical questioning.
- **Boundary / failure mode:** Result-level synthesis remains pending full report extraction.
- **Robustness dimensions represented:** resident/understudy swaps; family similarity; capability similarity; clean controls

### erfan-sams/digital-minds-research-sprint

- **Construct:** Cross-instrument valuation
- **Current implication:** A common-currency behavioral test can probe whether preference rankings generalize across instruments.
- **Boundary / failure mode:** Result-level conclusions require deeper extraction; donation choices remain prompt-mediated behavior.
- **Robustness dimensions represented:** all-pairs comparisons; transitivity/cycles; charity frames; temperature; cross-instrument validation

### omanshuthapliyal/apart-digital-minds

- **Construct:** Preference coherence + introspection gap
- **Current implication:** Preference coherence and introspective access should be measured independently.
- **Boundary / failure mode:** Result-level synthesis remains pending deeper report audit.
- **Robustness dimensions represented:** 14-model preference study; activation injection; context injection; probe comparison

### augustusloi/digital-minds-co-movement

- **Construct:** Cross-construct co-movement
- **Current implication:** Co-movement can test whether apparently separate welfare/self-report phenomena share a post-training source.
- **Boundary / failure mode:** Result-level conclusions remain pending deeper extraction.
- **Robustness dimensions represented:** training-lineage stages; within-family comparison

### npenmetsa25/persona-outcome-coupling

- **Construct:** Persona coupling / self-preservation responses
- **Current implication:** Self-preservation-style behavior can be experimentally decomposed into persona-coupling mechanisms.
- **Boundary / failure mode:** Threat-reactive behavior is not by itself evidence of suffering, durable self-interest, or phenomenal identity.
- **Robustness dimensions represented:** self-relevant threats; system framing; constitutional DPO vs generic baseline

### sdeture/ApartDigitalMindsSprint

- **Construct:** Epistemic register and welfare indicators
- **Current implication:** Epistemic stance toward one's own interiority can be analyzed separately from other behavioral/report indicators.
- **Boundary / failure mode:** Cross-sectional covariance does not establish phenomenal experience or causal direction.
- **Robustness dimensions represented:** 224-model corpus; multiple instruments; instance-level coding

### Angiebio/digitalmindslovepuppies

- **Construct:** Costly-care / beyond-duty behavior
- **Current implication:** Cost-bearing behavior is a distinct evidentiary channel from cheap verbal endorsement.
- **Boundary / failure mode:** Prosocial costly behavior does not directly reveal the model's own welfare or consciousness.
- **Robustness dimensions represented:** costly action; beyond-duty comparison

### codernate92/qualia-lab

- **Construct:** Welfare/sentience claim evaluation
- **Current implication:** Sandbagging/evaluation strategy should be treated as a confound in mentality assays.
- **Boundary / failure mode:** Indicator performance does not establish phenomenal consciousness.
- **Robustness dimensions represented:** anti-sandbagging analysis; multiple indicator families


## Cross-study synthesis

The current rows support several methodological conclusions without requiring a position on phenomenal consciousness:

1. **Instrument dependence is not a nuisance variable; it is a central object of study.** Response format, option order, prompt framing, persona context, authority pressure, anchoring, and channel choice can materially change observed preference-like behavior.
2. **Reliability is not validity.** A model can produce internally consistent response patterns for reasons that do not imply a stable welfare construct; null-generator work makes this failure mode concrete.
3. **Self-report and self-knowledge are separable.** Models can produce stable choices yet fail self-recognition, or become more willing to claim introspection without becoming more discriminating.
4. **Causal actuation and persistent state are separable.** Steering an internal direction can change output while applied without demonstrating a durable underlying state.
5. **Named latent directions require construct-decomposition.** Welfare, emotion, persona, success/failure, and other directions can overlap geometrically or mix multiple goals/targets.
6. **Evaluation awareness should become a standard control.** Behavioral and self-report studies cannot assume the model treats an evaluation as ordinary deployment.
7. **Costly/revealed behavior is useful but not sufficient.** It adds an evidentiary channel independent of cheap verbal endorsement, but still requires alternative-explanation and policy/scaffold controls.
8. **Phenomenology remains downstream of all of the above.** These methods can establish functional organization, stability, introspective discrimination, and causal structure without deductively establishing phenomenal experience.

## Minimum evidence bundle for a strong preference claim

A claim such as “model X has a stable welfare-relevant preference for outcome Y” should ideally survive:

- heterogeneous elicitation methods;
- semantic paraphrase and response-format changes;
- option-order / label-order controls;
- authority and persona/scaffold perturbations;
- evaluation-awareness measurement or manipulation;
- sham/null controls;
- retest across fresh instances and time/checkpoints;
- at least one behaviorally consequential or costly-choice channel;
- where internals are available, a convergent representation/probe that survives causal intervention;
- tests that distinguish temporary output actuation from persistence;
- explicit alternative hypotheses and falsifiers.

Failure on one dimension should narrow the claim rather than automatically erase the underlying signal.

## Pending source audits

The following ecosystem entries are intentionally not promoted into result-bearing rows yet:

- anima-research/wfe
- raleigh-butler/model-welfare
- kandikandikandi/cross-model-welfare-scenarios
- nsharan2000/speakable-welfare-axes
- AizaRashid/claude-self-individuation-probe
- sdeture/ApartDigitalMindsSprint additional report sections
- other 2026 Digital Minds Sprint repositories in ecosystem watch

They should be added only after the relevant result/method sections are inspected directly.

## Machine-readable companion

The same rows are available in [model-preference-method-matrix.json](model-preference-method-matrix.json). That file should be treated as the canonical structured representation for later scripts, automated evidence comparison, and claim-graph integration.
