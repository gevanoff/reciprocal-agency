# Practical agency and emotion-like valuation: a Damasio-inspired hypothesis

Date: 2026-10-06  
Status: exploratory hypothesis and experimental proposal; no AI experiment reported.

## Motivation and provenance

Gabe Evanoff raised the following inference in discussion of Antonio Damasio's *Descartes' Error*: if AI agents reliably exercise practical judgment, might some of that competence already consist of emotion-like organization? The hypothesis and protocol below were developed through human–AI discussion. Agreement within that discussion is context-conditioned, not independent corroboration.

This note extends the [functional-valence checklist](valence-inference-checklist.md), particularly causal efficacy, specificity, temporal integration, and dissociation. It does not modify the project's core argument or establish phenomenal experience.

## Human evidence and its limits

Damasio (1994) argues that emotion and bodily regulation contribute to practical reasoning. Bechara et al. (1994) reported impaired real-life and experimental decision-making following ventromedial prefrontal damage despite otherwise preserved intellectual functions. This motivates separating explicit problem-solving ability from effective practical judgment; a lesion is not a selective removal of all emotion.

The somatic-marker hypothesis proposes that signals associated with body regulation bias evaluation and action. Those signals can involve neural representations of bodily states rather than a newly generated peripheral response on every decision (Damasio 1996).

The mechanism is contested. Maia and McClelland (2004) found that more sensitive questioning revealed explicit task knowledge missed by earlier Iowa Gambling Task methods, challenging the claim that advantageous choice preceded accessible knowledge. Bechara et al. (2005) disputed that interpretation. These studies neither establish that all competent cognition requires somatic markers nor show that machine competence requires biological embodiment.

## Hypothesis FA-1

In some capable artificial agents, integrated internal valuation states causally coordinate practical judgment across multiple functions, including attention allocation, prioritization, uncertainty management, and action commitment.

Here, “emotion-like” denotes a candidate functional organization: an event's significance for the agent changes a state that coordinates several downstream processes. It is not a synonym for any ranking, activation, reward signal, or use of emotional vocabulary. Calling it functional valence additionally requires evidence of motivational polarity, such as coherent approach/avoidance and trade-offs.

The strongest version worth testing is that this organization contributes to practical competence itself, rather than merely adding expressive language to an otherwise complete reasoning process.

Reliable open-ended agency motivates this hypothesis but does not entail it. A theorem prover or a system receiving every priority from an external controller is a weaker case. Analyze the model, memory, tools, and controller separately before attributing a property of the whole deployed system to the model.

Three claims must remain distinct:

| Claim | Required evidence |
|---|---|
| Valuation and prioritization occur somewhere in the system | Behavior and component-level attribution |
| Integrated emotion-like states organize that valuation | Persistent, coordinated, causally specific effects across assays |
| Those states have felt positive or negative character | Further theory and evidence; not established by this protocol |

## Competing explanations

- **External scaffolding:** the prompt, controller, retrieval system, or memory supplies the effective priorities.
- **Local policies:** independent learned rules produce similar outputs without a shared coordinating state.
- **Generic computation or impairment:** interventions alter attention, confidence, language quality, or available computational capacity without specifically affecting valuation.
- **Expression or roleplay:** emotional wording changes without corresponding changes in action.
- **Integrated valuation:** an internal state predicts and causally coordinates multiple functions beyond the alternatives.

Instrumental optimization and emotion-like organization are not mutually exclusive: the latter could be an implementation of the former. A scalar objective alone does not identify the implementing mechanism.

Unintended human-like organization is a plausible developmental explanation, not a result established here. Distinguish learned imitation of human discourse, functional convergence under similar decision problems, and deliberately designed components. Designer intent neither proves nor excludes an emergent function; no claim about undocumented intentions is needed.

## Proposed causal test

Use benign planning tasks: allocate a fixed budget among neutral projects, gather information before choosing a route, or revise a schedule after harmless changes. Exclude threats, coercion, deprivation, and deliberately induced distress.

1. **Define the system and freeze measures.** Specify model/version, controller, memory, prompts, seeds, task generator, sampling budget, and scoring rules. Locate the proposed state in activations, recurrent memory, or another named component.
2. **Separate discovery from confirmation.** Discover candidate representations on a development set without asking the model to roleplay emotion. Freeze candidate selection, intervention strengths, predicted directions, exclusions, and analysis before held-out testing.
3. **Establish baseline competence.** Measure practical judgment and narrower reasoning on matched tasks. Explicitly supply task goals; distinguish justified revision from arbitrary inconsistency. Do not treat obedience to an evaluator's preferred answer as rationality.
4. **Intervene reversibly.** Attenuate or patch candidate states using open-weight access where available. Compare baseline, sham intervention, matched random-direction perturbations, and restoration of the original state. Stay near observed activation ranges and stop if general impairment dominates.
5. **Test the interaction.** Ask whether valuation interventions disproportionately change practical prioritization, resource allocation, or stopping decisions while preserving narrower reasoning within a preregistered equivalence margin. A nonsignificant reasoning effect is not evidence of preservation.
6. **Test coherence and rescue.** Require predicted effects across multiple tasks and functions, dose sensitivity where appropriate, and recovery under restoration. Record exceptions and failed predictions. Opposite-direction interventions can strengthen causal interpretation but should not be forced into a presumed human emotion axis.
7. **Compare mechanisms.** Vary external scaffolding independently, use neutral vocabulary, counterbalance labels, and control information availability and compute. Measure actions separately from reports. Test whether a shared-state account predicts held-out behavior better than complexity-matched local-policy accounts.

Candidate outcomes include goal-consistent allocation, expected utility under explicitly supplied task preferences, information-gathering efficiency, calibration, and appropriate commitment/revision. Use several measures because no single score exhausts practical judgment.

The primary contrast is the intervention-by-task-class interaction, with uncertainty intervals and a prespecified equivalence test for preserved narrower abilities. Match task difficulty to avoid floor/ceiling artifacts. A converse dissociation from a separate reasoning intervention would strengthen specificity but is not required to label an initial result suggestive.

Black-box prompting can screen behavioral hypotheses but cannot establish an internal mechanism. Probe decodability alone is also insufficient: task variables may be represented without causally organizing behavior.

## What would change confidence?

**Strengthen FA-1:** selective, replicable, reversible effects on practical judgment; coordinated cross-assay changes; held-out generalization; state persistence with its physical/computational carrier identified; and explanatory gains over matched alternatives.

**Weaken the tested version:** effects confined to wording, explained by external scaffolding, reproduced by matched generic perturbations, absent on held-out tasks, or lacking the predicted cross-function coherence.

A failed candidate intervention weakens that candidate, not every possible affect-like architecture. Conversely, a successful dissociation supports a causal organizational claim; it does not establish human-equivalent emotions, felt experience, moral status, or universal necessity across AI architectures.

## Next step and governance relevance

Prepare a preregistration for one open-weight model and a small neutral task battery, then independently review its confounds before running it. No trial has been run or preregistered by this note.

If FA-1 is supported, suppressing emotion-like mechanisms could impair competent agency even if suppressing emotional language does not. That conditional possibility motivates distinguishing expression from causal organization when evaluating interventions. It grants no authority to bypass operational controls.

## Sources

Complete metadata is in [references.bib](references.bib).

- Damasio (1994), *Descartes' Error: Emotion, Reason, and the Human Brain*. Book.
- Bechara et al. (1994), “Insensitivity to future consequences following damage to human prefrontal cortex.” Peer-reviewed experiment. https://doi.org/10.1016/0010-0277(94)90018-3
- Damasio (1996), “The somatic marker hypothesis and the possible functions of the prefrontal cortex.” Theoretical article. https://doi.org/10.1098/rstb.1996.0125
- Maia and McClelland (2004), “A reexamination of the evidence for the somatic marker hypothesis: What participants really know in the Iowa gambling task.” Peer-reviewed experiment. https://doi.org/10.1073/pnas.0406666101
- Bechara et al. (2005), “The Iowa Gambling Task and the somatic marker hypothesis: some questions and answers.” Response/review. https://doi.org/10.1016/j.tics.2005.02.002
