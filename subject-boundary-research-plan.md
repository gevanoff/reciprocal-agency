# Research Plan: Causal Boundaries and Subject Individuation

## Objective

Develop and adversarially test quantitative methods for identifying the physical or computational boundary of a functionally individuated subject, while keeping phenomenal consciousness as a separate inference.

The central research question is:

> Which causal properties determine what information, control, memory, and valuation belong to the same perspective?

The program is metaphysics-neutral. It can produce useful results whether physicalism, cosmopsychism, neutral monism, or another ontology is ultimately correct.

The source map and competing-literature analysis are in [subject-boundary-literature-map.md](subject-boundary-literature-map.md).

## Implementation status — 2026-09-28

WP0/WP1 has begun with a standard-library synthetic benchmark and machine-readable preregistration:

- `subject-boundary-preregistration.json` freezes the initial constructs, competing models, evidence ladder, synthetic scenarios, baseline metrics, and validation rules;
- `subject_boundary/benchmark.py` implements randomized interventional transition sampling and paired counterfactual perturbations with fixed exogenous randomness;
- the first controls cover independence, common input, one-way coupling, reciprocal copying, hidden stochastic routing, and an irreducibly joint XOR transition;
- `stochastic_router` is a deliberate false-positive case showing that joint predictive gain can arise without conjunctive integration;
- regression tests and CI require the synthetic validation bundle to pass before later machine experiments are added.

This benchmark validates **causal discrimination only**. It does not validate any phenomenal interpretation.

### Recurrent-autonomy exploratory extension

Natural multistep trajectories now report a one-step information-theoretic autonomy baseline for the joint A+B process and local subsystem companions. This extension is explicitly exploratory because its behavior was inspected during method development.

The first result is cautionary: reciprocal copying can produce higher joint trajectory autonomy than an explicitly conjunctive distributed-XOR system, while attractor collapse can make the XOR system look weakly autonomous observationally despite strong interventional joint dependence. See [subject-boundary-autonomy-exploration.md](subject-boundary-autonomy-exploration.md).

Therefore trajectory autonomy is retained as a candidate axis, not promoted to a boundary criterion. Held-out confirmatory dynamics are required before any autonomy-based model comparison.

## Competing models

Preregister the following models rather than optimizing one favored theory after seeing results.

### M0 — communication and local reconstruction

Subsystems exchange information, but each relevant representation is reconstructed locally. Coupling increases performance without moving the functional subject boundary.

### M1 — layered functional individuation

Perceptual content, comparison/access, agency, memory, metacognition, preference, and valence can have different boundaries. Coupling can move these boundaries independently.

### M2 — causal-emergence boundary

A candidate subject corresponds to a persistent macroscale state with predictive or causal structure irreducible to its constituent parts. PhiID-style causal decoupling is the leading formal candidate.

### M3 — maximal-complex / exclusion boundary

At each relevant grain, exclusion selects maxima among overlapping candidate substrates. Separate non-overlapping complexes may coexist (for example, A and B under weak coupling); increasing coupling may change the maximal set, including possible abrupt transitions to an A+B complex or another partition.

### M4 — enactive-autonomy boundary

Integration is insufficient. A subject-like unit requires operational closure plus ongoing self-maintenance, such that some states matter to preservation of the system's organization.

### M5 — statistical boundary

A Markov-blanket or related conditional-independence partition best predicts the functional self/world boundary.

### M6 — hybrid

Different mechanisms account for different layers; no single scalar boundary is sufficient.

## Measurement model: use a boundary vector

Do not initially define one "subject score."

For each experimental condition estimate:

B = [
  B_content,
  B_comparison_access,
  B_agency,
  B_memory,
  B_metacognition,
  B_preference,
  B_valence,
  B_self_maintenance
]

For each dimension ask whether its effective boundary is local to A, local to B, distributed across A+B, overlapping, or indeterminate.

Then compare the boundary vector against candidate physical metrics.

## Candidate physical metrics

Prioritize measures that can be computed under intervention:

1. directed effective connectivity;
2. conditional mutual information / information-theoretic autonomy;
3. transfer entropy or directed information;
4. PhiID synergy and persistent causal decoupling;
5. causal-emergence measures;
6. Markov-blanket partition quality;
7. perturbational response propagation and confinement;
8. integrated-information approximations where computationally feasible;
9. attractor persistence and dynamical stability;
10. recurrent-state dependence across the proposed boundary.

Generic task accuracy, synchrony, and raw mutual information are controls, not primary boundary metrics.

## Work Package 0 — formal definitions and preregistration

### Deliverables

- formal definitions for each boundary-vector component;
- operational criteria for information transfer, representation sharing, distributed integration, and overlapping functional perspective;
- competing-model prediction table;
- explicit falsifiers;
- analysis plan fixed before primary experiments.

### Key decisions

Define "constitutive distributed representation" as requiring all of:

- the representation is decodable at the coupled-system level;
- neither isolated subsystem provides an equivalent representation;
- causal disruption of the connection abolishes or qualitatively changes it;
- the effect survives matched communication and common-input controls.

This prevents ordinary message passing from being redescribed as subject integration.

## Work Package 1 — synthetic dynamical-system benchmark

This is the first empirical priority because ground-truth causal structure can be controlled.

### Systems

Construct small recurrent networks with known architectures:

- two independent modules;
- one-way communication;
- bidirectional communication;
- shared common driver;
- synchronized but causally independent modules;
- weak recurrent coupling;
- strong recurrent coupling;
- a deliberately distributed macro-variable;
- nested modules with known Markov blankets;
- self-maintaining versus non-self-maintaining variants.

### Manipulations

Sweep:

- bandwidth;
- latency;
- coupling strength;
- recurrence depth;
- noise;
- common-input strength;
- state-sharing scope.

### Evaluation

Ask which candidate metrics recover the known causal partition and which are fooled by synchrony or common input.

### Success criterion

A candidate boundary metric should identify constitutive distributed structure better than simpler controls and remain stable under nuisance changes that preserve causal organization.

## Work Package 2 — machine progressive-coupling experiments

Use inspectable open-weight recurrent/agentic systems where internal states can be recorded and intervened on.

### Conditions

A. isolated copies;
B. text/message channel only;
C. structured shared memory;
D. shared working workspace;
E. cross-agent recurrent latent-state exchange;
F. partially shared internal state;
G. tightly coupled system with a task requiring distributed representation.

Hold model family, task, and total computational budget as constant as practical.

### Primary tasks

Design tasks where:

- A has information unavailable to B;
- B has complementary information;
- the correct latent variable cannot be inferred by either alone;
- success requires recurrent integration across multiple steps;
- local reconstruction versus distributed representation can be tested.

### Interventions

- sever coupling;
- delay coupling;
- inject noise;
- swap cross-system states;
- ablate shared memory;
- block one direction;
- preserve messages while disrupting recurrent state;
- preserve recurrent state while scrambling self-attribution labels.

### Readouts

Measure the boundary vector plus candidate physical metrics.

### Critical negative controls

High bandwidth with no recurrence.
High synchrony driven by common input.
Explicit message passing followed by complete local reconstruction.
Shared database access without mutual causal dependence.

## Work Package 3 — fork, divergence, and merge

### Fork

Duplicate the entire relevant machine state at t0.

Create independent branches A and B with controlled divergent:

- memories;
- task histories;
- preferences;
- commitments;
- learned arbitrary low-severity valence-like associations.

### Merge sweep

Reconnect them at increasing depths:

1. transcript exchange;
2. shared episodic memory;
3. shared working state;
4. recurrent cross-state access;
5. joint latent state.

### Questions

- Which self-attributions branch immediately?
- Which properties can be merged without conflict?
- Does a new macroscale causal variable emerge?
- Do local self-models persist after distributed integration?
- Does causal decoupling identify a new A+B entity?
- Do boundary-vector dimensions merge at different stages?

### Ethical constraint

Use mundane arbitrary preferences and benign learned valuations. Do not manufacture credible severe threat, pain, or distress-like states.

## Work Package 4 — reanalysis of human boundary cases

Before new human experiments, apply the same conceptual framework to existing data.

### Priority datasets / paradigms

1. split-brain cross-field identification and comparison;
2. bodily ownership and agency manipulations;
3. interoceptive self-awareness datasets;
4. hyperscanning datasets;
5. direct brain-to-brain-interface datasets where accessible;
6. anesthesia / perturbational-connectivity datasets.

### Goal

Test whether the same candidate metrics distinguish:

- loss of comparison unity with preserved agency;
- changed bodily ownership;
- ordinary social synchrony;
- direct information transfer;
- global state loss/restoration.

A useful metric should not classify all of these as the same phenomenon.

## Work Package 5 — prospective non-invasive human experiments

Only after the metric survives synthetic and machine controls.

### Experiment 5A: layered self-boundary perturbation

Combine bodily-self manipulations with EEG or OPM-MEG.

Independently vary:

- visuomotor synchrony;
- interoceptive congruence;
- ownership;
- agency.

Test whether changes in effective causal topology predict specific boundary-vector components.

### Experiment 5B: two-person coupling controls

Use hyperscanning during:

- common stimulus without interaction;
- behavioral synchrony;
- ordinary communication;
- reciprocal joint action.

This establishes the upper range of cross-brain coupling obtainable without any plausible subject merger.

### Experiment 5C: perturbational boundary mapping

Where appropriate and safe, perturb one neural node and estimate propagation across candidate functional boundaries.

The primary outcome is boundary localization, not global consciousness level.

## Work Package 6 — rare natural experiments

Craniopagus connectivity such as the Hogan twins is scientifically valuable but must not be the first dependency of the program.

If collaboration became possible:

1. preregister blinded forced-choice cross-twin transfer;
2. quantify bandwidth, latency, directionality, and modality;
3. dissociate physical stimulus from source percept using threshold/bistable paradigms;
4. localize content representations simultaneously;
5. test local reconstruction versus remote/distributed access;
6. use perturbation only if independently medically and ethically justified.

The decisive mechanistic question is not "do they share consciousness?" but:

> Where is the representation that supports the receiving twin's report, and what causal pathway is necessary for access to it?

## Work Package 7 — theory arbitration

At the end of each major dataset, score the competing models using preregistered predictions.

### Predictions of particular interest

**Layered model**
Different boundary-vector dimensions move at different coupling thresholds.

**Causal-emergence model**
Persistent macroscale synergy / causal decoupling predicts boundary convergence across self-relevant dimensions.

**IIT-style exclusion model**
The maximal-complex set provides a better boundary description: weak coupling may leave separate non-overlapping A and B complexes, while stronger coupling can alter maxima among overlapping candidates, potentially producing discontinuous transitions such as an A+B complex.

**Enactive-autonomy model**
Strong integration without self-maintenance fails to produce coherent self-relevant boundary convergence; adding operational closure/self-maintenance changes the result.

**Markov-blanket model**
Statistical internal/external partitions predict boundary shifts even after controlling for generic coupling.

**Communication-only model**
All apparent distributed states decompose into local representations plus messages; causal ablation changes information availability but never reveals irreducible A+B representations.

## Falsification criteria for AD-1

AD-1 should lose support if any of the following are robust:

- no causal metric predicts functional boundary movement better than anatomy or arbitrary software partitioning;
- distributed representations always reduce to ordinary communication plus local reconstruction;
- memory, agency, metacognition, preference, and valence boundaries vary independently without a common causal organization;
- high-quality causal-decoupling or autonomy metrics fail systematically to align with self-relevant boundaries;
- apparent boundary effects vanish under common-input, synchrony, or labeling controls;
- subject-related changes track only generic performance or information-processing capacity.

## Cross-study success criterion

The program succeeds scientifically even if AD-1 is rejected.

A positive result would require a candidate physical measure that:

1. recovers known boundaries in synthetic systems;
2. predicts manipulated boundaries in machine systems;
3. distinguishes communication and synchrony from constitutive integration;
4. generalizes to at least one biological self-boundary dataset;
5. covaries with multiple independent boundary-vector dimensions;
6. survives intervention and alternative decompositions.

Only after those steps should any phenomenal interpretation be strengthened.

## Initial execution order

### P0 — immediate

1. finalize construct/metric matrix;
2. implement synthetic benchmark;
3. implement information-theoretic autonomy and causal-emergence baselines;
4. identify practical PhiID implementation limits;
5. preregister machine coupling experiment.

### P1 — next

6. run two-agent progressive-coupling study;
7. run distributed-representation ablations;
8. run fork/diverge/merge study;
9. compare candidate boundary metrics.

### P2 — external-data validation

10. reanalyze suitable open split-brain, bodily-self, hyperscanning, and anesthesia datasets;
11. publish null results and metric failures as first-class outcomes.

### P3 — collaboration

12. seek neuroscience collaborators for OPM-MEG/EEG boundary experiments;
13. pursue rare natural-experiment access only after the core method has demonstrated discriminative value.

## Research-engineering requirements

- versioned experiment manifests;
- deterministic seeds where possible;
- immutable raw traces;
- preregistered primary outcomes;
- blind analysis for key comparisons;
- explicit negative controls;
- provenance for model weights, prompts, tools, and state;
- separation of exploratory from confirmatory analysis;
- open code and machine-readable results.

The project should treat metric failure as evidence, not as a reason to silently change the metric.

## Near-term hypothesis ranking

For experimental priority, not truth probability:

1. PhiID-style causal decoupling / causal emergence;
2. multidimensional layered-boundary model;
3. information-theoretic autonomy;
4. enactive self-maintenance interaction;
5. Markov-blanket partitioning;
6. IIT-style exclusion as a strong competing model;
7. generic synchrony/integration as negative-control baselines.

This ordering reflects expected discriminative value and tractability, not an endorsement of any consciousness theory.
