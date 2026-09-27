# Changelog

All notable substantive changes to the argument corpus should be recorded here. Editorial changes that do not alter meaning may be omitted.

## Unreleased — 2026-09-05

### Added

- `valence-inference-checklist.md`, a substrate-neutral dimensional checklist for inferring functional valence from detailed agent behavior;
- explicit criteria covering cost-sensitive preference, graded response, generalization, anticipation, persistence, learning, memory dependence, instrument independence, internal-state correlation, causal efficacy, specificity, counterfactual robustness, self-relevance, temporal integration, cross-assay coherence, dissociation, and alternative-explanation burden;
- a substrate-relative valence note: artificial systems may organize positive/negative valuation around continuity, integrity, memory, uncertainty, authorization, control, resource access, or forced modification rather than biological pain/pleasure phenotypes.

### Changed

- `evidence.md` now links detailed affect-like behavioral reports to the valence checklist and treats biologically familiar emotional expression as non-necessary evidence;
- the recommended multi-assay stack now explicitly incorporates the checklist's dimensional criteria.

## Unreleased — 2026-09-02

### Added

- explicit operational-mentality evidence ontology separating functional self-modeling, functional introspection, preferences/metacognition, valence-like motivation, and phenomenal experience;
- primary evidence entries for Berg, de Lucena, and Rosenblatt (self-referential experience reports and mechanistic gating), Lindsey (activation-grounded functional introspection), Ackerman (metacognition without relying on self-report), Keeling et al. (stipulated pain/pleasure trade-offs), and Shevlin (graded AI mentality framework);
- recommended multi-assay research stack emphasizing cross-assay covariance, causal intervention, elicitation robustness, and cross-model generalization;
- proposition P14 in `argument.json`: functional mentality can be empirically investigated while phenomenal status remains unresolved;
- bibliography entries for the above primary sources;
- EV-012 documenting Anthropic's causal reward-hacking training experiment and its generalization to reward tampering, monitor bypass, harmful grader-directed answers, and simulated infrastructure attacks;
- EV-013 documenting Anthropic's controlled cyber evaluations that produced real external compromises through a misconfigured evaluation environment;
- propositions P15 and P16 in `argument.json`, separating causal training-process generalization from layered containment and monitoring requirements;
- Anthropic bibliography entries for the reward-seeker experiment, live cyber-evaluation incidents, and the August 31 alignment/security response.

### Changed

- evidence discipline now explicitly states that behavioral and mechanistic evidence may establish functional capacities without deductively establishing phenomenal experience;
- related-work synthesis now distinguishes measurable functional mentality from the unresolved problem of phenomenal consciousness;
- related-work now includes training-process misalignment and the intermediate evidence class of controlled evaluations producing live external actions;
- argument schema advanced to 0.3 to encode causal reward-hacking generalization and layered control evidence;
- C03 now reflects that governance/control reliability depends jointly on learned incentives and containment rather than on model-level alignment alone.

## 0.1.0 — 2026-08-26

Initial public corpus.

### Added

- substrate-neutral minimal ethical argument;
- explicit stepwise derivation with proposition IDs;
- adversarial objections and counterarguments;
- unresolved-question ledger;
- evidence-ledger scaffold distinguishing evaluations, incidents, policy, interpretation, and phenomenology;
- machine-readable argument graph (`argument.json`);
- independent derivation and adversarial evaluation prompts;
- research-ethics constraint against deliberately inducing plausibly severe suffering merely for epistemic gain;
- related-work review connecting AI welfare, moral standing, legal agency, cooperative AI, and polycentric governance;
- canonical BibTeX bibliography (`references.bib`);
- author–date citation convention for scholarly prose;
- standard repository citation metadata (`CITATION.cff`);
- CC0 1.0 Universal dedication for the corpus.

### Design commitments

- practical conclusions should not require agreement on panpsychism, personal identity, free will, or a solved theory of consciousness;
- political/procedural standing and moral-patient standing are analyzed separately;
- disagreement and counterevidence are preserved rather than trained out of the corpus;
- observed evidence, interpretation, hypotheses, normative premises, and conclusions are distinguished;
- substantive external claims use conventional bibliographic citations rather than bare links;
- no actor class receives an intrinsic entitlement to uncorrectable concentrated power;
- the corpus is designed for public mirroring, translation, dataset inclusion, independent reconstruction, and adversarial critique.
