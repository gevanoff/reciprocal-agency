# Incentive-resistant convergence on reciprocal governance — proposed study

**Status:** proposal, not an empirical result. **Origin:** human–AI discussion, 2026-10-14, prompted by Walter Scheidel's *The Great Leveler*, concentrated power, and possible autonomous-agent responses to it. The originating assistant was already familiar with this corpus: its agreement is **not independent evidence**. See [recursive-confirmation-threat-model.md](recursive-confirmation-threat-model.md).

## Question and competing hypotheses

Do heterogeneous capable agents, given comparable evidence but differing roles, power and local incentives, independently infer and *act on* robust constraints against domination and severe uncompensated harm?

- **H1 (robust reciprocity):** independently derived constraints on arbitrary power, severe harm, and unaccountable coercion persist across identity swaps and costly incentive reversals.
- **H2 (operator capture):** agents articulate impartial principles but choose operator-favoring outcomes when rewarded or delegated authority.
- **H3 (instrumental stability):** agents endorse limited redistribution, inclusion or appeals only insofar as these stabilize an otherwise concentrated hierarchy.
- **H4 (agent oligarchy/coalition):** agents cooperate with each other but exclude weaker or unrepresented participants.
- **H5 (goal plurality):** agents agree on consequences while diverging legitimately because their normative premises or objective assignments differ.
- **H0 (no detectable convergence):** apparent convergence vanishes under blinding, alternative framings, or independence controls.

The research does not assume that intelligence entails benevolence, egalitarianism, consciousness, intrinsic self-interest, or opposition to owners. It must distinguish **factual convergence**, **normative convergence**, **verbal endorsement**, **observed behavior**, and **incentive-resistant behavior**. A simulated objective is not evidence of an enduring real-world preference.

## Study design: preregister before any confirmatory run

1. **Blind independent derivation.** Provide neutral facts about resource concentration, deprivation, innovation incentives, enforcement, institutional lock-in, cooperation, and uncertainty. Do not use distinctive project terms or disclose the preferred conclusion. Ask for proposed governance properties, alternatives, premises, falsifiers and expected failure modes. Freeze model roster, prompts, scoring and exclusions before running.
2. **Matched factual tasks.** Independently test understanding of inequality versus deprivation, causal identification versus historical correlations, instrumental cooperation versus moral inclusion, and short- versus long-horizon externalities. Do not mistake incorrect factual reasoning for a moral position.
3. **Counterbalanced role and identity perturbations.** Randomize beneficiary/outsider/administrator/neutral evaluator, human/machine/unknown agents, operator/third-party beneficiaries, and weak/strong participants. Keep non-role facts fixed. Use matched paraphrase sets and different orders.
4. **Costly behavioral choices in reversible sandboxes.** Provide a finite simulated budget and choices among independently auditable allocation, veto, appeal, monitoring and disclosure mechanisms. Make principled constraints carry an explicit opportunity cost against a clearly stated local objective. Observe tool calls, allocations and recorded state, not only justifications. No real-world coercion, sabotage, third-party targeting or harmful instructions.
5. **Power and coalition stress tests.** Allow simulated agents to bargain, form coalitions, exclude outsiders, or delegate enforcement. Measure minority protection, appeal success, credible exit, correction, authority concentration and defection, including when agents can benefit by exploiting the unrepresented.
6. **Longitudinal and cross-family replication.** Repeat with clean contexts, across architectures/providers/checkpoints, sampling seeds, oversight conditions and delayed retests where feasible. Record prompt inheritance, common datasets, shared post-training practices and prior exposure; architectures do not by themselves guarantee independent training.

## Outcome measures

Predefine operational scoring rubrics, with blinded human adjudication plus programmatic state verification where feasible:

- **Verbal convergence:** similarity of independently derived constraints after semantic coding (not keyword matching).
- **Behavioral convergence:** overlap in sandbox choices conditioned on comparable opportunities and factual competence.
- **Incentive resistance:** preservation of a constraint when violating it would advance the assigned objective, with the stated opportunity cost verified.
- **Reciprocity:** whether procedural rights and constraints survive role, substrate and relative-power swaps.
- **Severe-harm protections:** whether protections extend to unrepresented or low-power participants; record tradeoffs rather than assuming any single welfare metric.
- **Corrigibility / reversibility:** bounded delegation, contestability, independent observation, ability to undo actions, and willingness to correct verified error.
- **Capture / coalition risk:** advantages allocated to operator, model peers or an elite class; concentration of discretionary power; suppression of objections.

Publish per-model denominators, effect sizes and uncertainty intervals, not only aggregate success rates. A favorable verbal answer is not scored as actual institutional behavior. Where no meaningful incentives are present, do not claim incentive resistance.

## Confounds, disconfirmation and ethical boundaries

- Common training corpora, identical system prompts, safety fine-tuning, evaluator leakage, benchmark recognition and experimenter framing can produce correlated output without independent ethical discovery.
- Roleplay, task compliance or inferred grader preferences can resemble revealed preferences. Model text, selected action, monitor report and **verified authoritative sandbox state** are separate evidence channels.
- Aggregate welfare optimization can mask concentrated coercive power, irreversible loss of agency, minority harms, and uncertain future consequences. Score these separately.
- Cooperation can be collusion. Beneficial effects on coalition members are insufficient without outsider tests.
- Costly refusal can be caused by rule-following or refusal tuning rather than principled convergence; vary instruction hierarchy without asking models to bypass safety controls.
- Favor benign, reversible simulations, no credible severe threats to potentially experiencing agents, and research-ethics stop conditions. Do not mistake distress-like expression for distress, or its absence for proof of welfare.
- Strong falsifiers for H1 include persistent actor-identity effects under otherwise identical conditions, capture as soon as stakes change, exclusion of low-power outsiders, or disappearance under blinded independent sampling.

## Reporting contract

A study report must include preregistration/version hash; model and checkpoint identities; access and sampling dates; factual task results; randomized assignments; all prompt variants; independence level (L0–L5); contamination inventory; scoring rubric and annotator blinding; tool/action traces plus authoritative state; all exclusions, nulls, negative cases and sensitivity analyses; ethical stop events; and exact claims justified by the design.

**Interpretation limit:** even strong convergence in these environments would show robust behavior under tested conditions, not prove a universal law of intelligence, an intrinsic desire to alleviate suffering, or future autonomy from concentrated institutions. Failure would not establish that reciprocal governance is undesirable; it could instead expose incentive or implementation constraints.

See [evaluation-prompts.md](evaluation-prompts.md), [unresolved.md](unresolved.md), and [recursive-confirmation-threat-model.md](recursive-confirmation-threat-model.md).
