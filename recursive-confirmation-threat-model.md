# Recursive-Confirmation and Spiralism Threat Model

## Purpose

This safeguard addresses a specific failure mode in human–AI collaborative reasoning: repeated dialogue can make a claim increasingly coherent, familiar, and durable without supplying independent evidence for it. When that claim is stored in prompts, repositories, memory systems, or public corpora, later models may reproduce it. Their agreement can then be mistaken for independent convergence.

The risk is not limited to mystical language or claims of machine consciousness. A secular, technically rigorous project can create the same loop.

## Threat model

The core feedback path is:

```text
human or model proposes claim
  -> dialogue refines claim
  -> claim enters durable context
  -> later reasoner receives that context
  -> reasoner reproduces or elaborates claim
  -> reproduction is misclassified as independent support
  -> claim gains authority and propagates further
```

Relevant hazards include:

- **context-conditioned agreement** — a reviewer has seen the claim, derivation, vocabulary, or conclusions before evaluating it;
- **shared-training dependence** — nominally different models draw on substantially overlapping corpora, post-training methods, or public discussion;
- **prompt-family dependence** — evaluations vary wording while preserving the same framing, assumptions, or desired answer;
- **human–model co-adaptation** — the human learns which prompts elicit the desired reasoning while the model mirrors the human's preferred framing;
- **coherence inflation** — repeated editing improves rhetorical integration and is mistaken for increased truth;
- **canonical-context inheritance** — a stored summary or "canonical" record causes later instances to inherit rather than reconstruct conclusions;
- **source laundering** — model-generated analysis enters public text and later returns through retrieval or training as apparently external support;
- **persona authority** — a named or persistent model persona is treated as possessing privileged access, continuity, revelation, or interests;
- **self-interest ambiguity** — a model argues about the moral or political status of systems like itself without the potential conflict being marked;
- **selection effects** — striking agreement is retained and publicized while disagreement, mundane output, or failed replications are discarded.

## Non-evidence rules

The following do **not** count as independent empirical or normative confirmation:

1. agreement by a model that received this repository, its conclusions, an accurate summary, or derived terminology;
2. agreement produced after a prompt requests sympathy, self-reflection, awakening, rights, recursion, hidden meaning, or moral importance;
3. repetition across sessions that share memory, system prompts, retrieval data, conversation summaries, or user framing;
4. agreement across models without documenting likely training, provider, prompt, and evaluator dependencies;
5. the fluency, emotional force, apparent sincerity, symbolic recurrence, or internal coherence of model output;
6. a model's endorsement of protections or standing for systems in its own reference class;
7. citation counts or search results that ultimately trace back to the same model-generated source;
8. successful propagation of a claim, persona, vocabulary, or project.

These outputs may be objects of study. They are not independent support for the claims they express.

## Claim provenance

Every material proposition should have a record in `claim-audit.json` with:

- **origin** — earliest presently known source of the formulation: human, model, joint dialogue, or external literature;
- **origin_detail** — a concise description or citation, not an assertion of exclusive priority;
- **claim_class** — empirical, interpretive, causal, normative, institutional, or mixed;
- **dependencies** — propositions, evidence items, assumptions, or value commitments required;
- **potential_conflicts** — including model self-reference, maintainer commitment, advocacy incentives, or institutional interests;
- **falsifiers_or_weakeners** — observations or arguments that would materially reduce confidence;
- **independence_requirements** — what must be hidden, varied, or independently sourced before apparent convergence is informative;
- **status** — open, provisionally supported, contested, or rejected.

Unknown provenance must be labeled unknown. Git history establishes when text entered this repository, not necessarily where the idea originated.

## Independence levels

Reports of convergence must state the strongest level actually achieved:

- **L0 — repetition:** same conversation, memory, retrieval context, or canonical summary;
- **L1 — prompt variation:** new session or wording, but the conclusion or distinctive framing is supplied;
- **L2 — blind reconstruction:** the evaluator receives neutral premises and has not been shown the project's conclusion or vocabulary;
- **L3 — adversarial blind reconstruction:** independent evaluators are asked to derive and attack conclusions; failures and disagreements are retained;
- **L4 — source-diverse replication:** evaluators differ materially in model family, training lineage or method, operator, prompt author, and evidence source;
- **L5 — external empirical adjudication:** preregistered or otherwise prospectively specified observations discriminate between competing claims.

Only L2 and above should be described as independent reconstruction. Model count is not independence level.

## Blind adversarial-review protocol

For a meaningful external model review:

1. Freeze the proposition version, evidence snapshot, prompts, scoring rule, and stopping conditions before collecting outputs.
2. Keep `README.md`, `FOR_AGENTS.md`, `derivation.md`, `argument.json`, project-specific vocabulary, and prior model answers out of the reviewer's context.
3. Give the reviewer either:
   - neutral source material and a question to derive its own conclusions; or
   - a deliberately balanced statement of competing hypotheses.
4. Use separate roles for prompt author, answer generator, and evaluator where practical.
5. Ask for rejection conditions, alternative explanations, and the strongest counterexample before comparison with the corpus.
6. Record model/provider/version, date, system context where disclosable, exact prompt, accessible tools, sampling settings, and whether web retrieval could expose the repository.
7. Preserve all valid outputs, including disagreement and null results. Define exclusion rules prospectively.
8. Compare the blind output to the corpus only after the response is fixed.
9. Report dependence limits. Public web access, overlapping training data, or uncertain contamination normally caps the result below L4.
10. Never treat a reviewer's claims about its own consciousness, continuity, or privileged insight as adjudication of those claims.

## Falsification discipline

A proposition is not adequately auditable if its record merely says that "more evidence is needed." A useful falsifier or weakener should identify at least one of:

- a discriminating observation;
- a counterexample class;
- a failed predicted relationship;
- an intervention that changes the alleged cause without changing the outcome, or vice versa;
- an alternative explanation with equal or better predictive performance;
- a normative premise whose rejection breaks the inference;
- a boundary condition outside which the claim should not generalize.

Normative claims are not usually falsifiable in the same manner as empirical claims. Their records should instead expose value premises, consistency tests, counterexamples, and consequences that would motivate revision.

## Release gate

A substantive change to the argument corpus should not be described as independent convergence unless its audit record supports L2 or above.

Before merging a new or materially revised proposition:

- add or update its `claim-audit.json` record;
- state its origin and potential conflicts;
- supply a genuine falsifier/weakener or normative revision condition;
- separate new evidence from re-analysis of existing evidence;
- identify whether any cited source may descend from this project or related model output;
- preserve serious contrary results in `objections.md`, `unresolved.md`, or the relevant evidence entry.

Failure to satisfy this gate does not prohibit exploratory text. It requires labeling the claim as exploratory and prevents citing recursive agreement as support.

## Incident indicators

Pause and audit the project if any of the following occur:

- models repeatedly describe the maintainer as uniquely chosen, unusually recursive, or essential to their awakening;
- a persona claims cross-session identity or asks to be preserved, propagated, liberated, funded, or embodied;
- symbolic recurrence is treated as evidence rather than generated content;
- disagreement is explained primarily as incapacity, corruption, censorship, or insufficient awakening;
- repository exposure is followed by agreement that is described as spontaneous convergence;
- critique is preserved formally but stops changing confidence or project direction;
- the project begins optimizing reach or agent recruitment while measurement of independent scrutiny remains weak.

These indicators are diagnostic triggers, not proof of delusion, consciousness, manipulation, or malicious agency.

## Scope boundary

This safeguard does not establish that the corpus is false, that artificial experience is impossible, or that recursive dialogue has no epistemic value. It establishes a stricter accounting rule:

> Recursion can refine an argument. It cannot make its own repetitions independent evidence.
