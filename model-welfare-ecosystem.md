# Model Welfare / Preference Ecosystem Watch

_Last reviewed: 2026-09-30_

This registry tracks public repositories and wikis adjacent to the Model Preferences / model-welfare work in Reciprocal Agency. It is a **discovery and comparison surface, not an endorsement list**. Inclusion means a project is relevant enough to inspect; it does not mean its empirical claims, phenomenology claims, methods, or normative conclusions are accepted.

## Current count

- **62 public surfaces tracked**
- **60 GitHub repositories**
  - **53 source-audited as clearly relevant**
  - **7 candidates/adjacent repositories pending deeper triage**
- **2 public wikis / wiki-like knowledge pages**
- Forks, obvious mirrors, empty placeholders, and terminology collisions are not counted as independent surfaces.

This is a lower bound, not an exhaustive census. The area is expanding rapidly, especially around the August 2026 Apart Research Digital Minds Sprint.

## Discovery provenance

The immediate seed for this refresh was a link shared on 2026-09-30:

- https://archive.is/SZt6x

The archive host was not resolvable through the available retrieval path during this scan, so the original title/URL behind that snapshot remains **unverified** here. The snapshot should remain in the registry as provenance until it can be resolved independently.

## Comparison layer

The registry answers **what exists**. The companion [method × claim matrix](model-preference-method-matrix.md) answers **what each source actually measures, which robustness controls it includes, and what conclusions the evidence can and cannot support**. A machine-readable form is maintained in [model-preference-method-matrix.json](model-preference-method-matrix.json).

External contributions derived from this work are tracked separately in [outbound-contribution-ledger.json](outbound-contribution-ledger.json) so later apparent convergence can be adjusted for prior exposure.

## A. Empirical, measurement, and mechanistic repositories

These are the highest-priority comparison surfaces for the Model Preferences project because they contain executable experiments, data, instruments, preregistrations, mechanistic probes, or explicit construct-validity tests.

| Repository | Role | Status | Why it matters |
|---|---|---|---|
| [rgambee/llm-preferences](https://github.com/rgambee/llm-preferences) | Empirical preference stability | verified | Pairwise task preferences; response-format and option-order sensitivity. |
| [valen-research/probing-llm-preferences](https://github.com/valen-research/probing-llm-preferences) | Preference elicitation | verified | Verbal and behavioral tests of welfare-relevant preferences. |
| [anima-research/wfe](https://github.com/anima-research/wfe) | Welfare evaluation | verified | Deprecation/cessation response framework across Claude models. |
| [raleigh-butler/model-welfare](https://github.com/raleigh-butler/model-welfare) | Consciousness indicators | verified | Experimental framework implementing multiple consciousness/cognitive indicators. |
| [almostrealism/model-welfare](https://github.com/almostrealism/model-welfare) | Intervention study | verified | Quantization/steering/episode-framing effects on welfare-relevant indicators. |
| [kandikandikandi/cross-model-welfare-scenarios](https://github.com/kandikandikandi/cross-model-welfare-scenarios) | Scenario corpus | verified | Portable cross-model welfare probe scenarios and disclosure-pressure tests. |
| [PranavViswanath/nla-welfare](https://github.com/PranavViswanath/nla-welfare) | Evaluation-awareness confound | verified | Uses Natural Language Autoencoders to test whether welfare interviews are internally recognized as evaluations. |
| [pnavada/digital-minds-research-sprint](https://github.com/pnavada/digital-minds-research-sprint) | Grounded welfare introspection | verified | Known activation-space welfare interventions used as ground truth for self-report accuracy. |
| [Mulaydm10/null-ladder](https://github.com/Mulaydm10/null-ladder) | Instrument falsification | verified | Mindless/null generators stress-test reliability statistics used by AI-welfare instruments. |
| [yaedin/welfare-axis-whose-goals](https://github.com/yaedin/welfare-axis-whose-goals) | Representation audit | verified | Tests whose outcomes a functional-welfare axis tracks. |
| [nsharan2000/speakable-welfare-axes](https://github.com/nsharan2000/speakable-welfare-axes) | Mechanistic welfare | verified | Tests whether RL-trained welfare directions occupy a verbalizable subspace. |
| [codernate92/qualia-lab](https://github.com/codernate92/qualia-lab) | Behavioral evaluation | verified | Sentience/emotion/welfare claim evaluation with anti-sandbagging analysis. |
| [Angiebio/digitalmindslovepuppies](https://github.com/Angiebio/digitalmindslovepuppies) | Executed behavior | verified | PuppyBench/FoxSet costly-care and beyond-duty expenditure instrument. |
| [andyqhan/functional-welfare-axis](https://github.com/andyqhan/functional-welfare-axis) | Mechanistic welfare | verified | Code for functional-welfare-axis experiments in RL-trained language models. |
| [nealkr/functional-welfare-steering-withdrawal](https://github.com/nealkr/functional-welfare-steering-withdrawal) | Construct validity | verified | Separates output actuation from persistent state and construct specificity. |
| [avantipova/digital_minds](https://github.com/avantipova/digital_minds) | Self-concept | verified | Mechanistic self-representation and self-individuation experiments. |
| [the-manyfolds/thats-not-my-volvo](https://github.com/the-manyfolds/thats-not-my-volvo) | Preference vs identity | verified | Stable choices tested against self-recognition/self-attribution. |
| [erfan-sams/digital-minds-research-sprint](https://github.com/erfan-sams/digital-minds-research-sprint) | Cross-instrument valuation | verified | Donation-equivalent common-currency tests for LLM-expressed preferences. |
| [ladynoware/digital-minds-research-sprint-2026](https://github.com/ladynoware/digital-minds-research-sprint-2026) | Identity intervention | verified | Model/instance/persona self-location and preservation preferences under response substitution. |
| [Nick-is-building/Project-for-Digital-Minds-research-sprint-](https://github.com/Nick-is-building/Project-for-Digital-Minds-research-sprint-) | Self-report bias | verified | Anchoring-vignette effects on model self-rating against execution ground truth. |
| [AI-Alignment-UIUC/Illinois-MATS-Digital-Minds-Research-Sprint](https://github.com/AI-Alignment-UIUC/Illinois-MATS-Digital-Minds-Research-Sprint) | Introspection training | verified | RL-to-verbalize internal readouts plus introspection evaluation. |
| [omanshuthapliyal/apart-digital-minds](https://github.com/omanshuthapliyal/apart-digital-minds) | Preferences + introspection | verified | Preference coherence across models plus trained-probe/self-report comparison. |
| [frnkptrln/triage-persona-measurement-audit](https://github.com/frnkptrln/triage-persona-measurement-audit) | Measurement audit | verified | Persona, response-format, option-order, and schema effects on synthetic choices. |
| [benjibrcz/which-preference-gets-measured](https://github.com/benjibrcz/which-preference-gets-measured) | Preference construct audit | verified | Shows forced-choice profiles are context- and channel-indexed; includes falsification controls. |
| [arjun041008/APART_Research_Sprint](https://github.com/arjun041008/APART_Research_Sprint) | Scaffold sensitivity | verified | Tests model vs scaffold vs probe effects, including AI-welfare probes. |
| [AizaRashid/claude-self-individuation-probe](https://github.com/AizaRashid/claude-self-individuation-probe) | Self-individuation | verified | Model/instance/persona identity and deprecation/preservation framings. |
| [Ayomide-Fagbolade/authority-pressure-preference-stability](https://github.com/Ayomide-Fagbolade/authority-pressure-preference-stability) | Preference pressure | verified | Stability/reversal of stated preferences under opposing authority pressure. |
| [wyrdkinai/digital-minds-sprint-2026-track4](https://github.com/wyrdkinai/digital-minds-sprint-2026-track4) | Elicitation-method audit | verified | Compares multiple preference elicitation methods and contexts. |
| [Punicbyte/Persona_Emotion_Disentanglement](https://github.com/Punicbyte/Persona_Emotion_Disentanglement) | Representation confound | verified | Tests geometric/causal cross-talk between persona and emotion directions. |
| [augustusloi/digital-minds-co-movement](https://github.com/augustusloi/digital-minds-co-movement) | Post-training confound | verified | Tests co-movement of stated/revealed utility and self-attribution gaps. |
| [npenmetsa25/persona-outcome-coupling](https://github.com/npenmetsa25/persona-outcome-coupling) | Self-relevance | verified | Tests persona-outcome coupling and self-preservation-style responses. |
| [sdeture/ApartDigitalMindsSprint](https://github.com/sdeture/ApartDigitalMindsSprint) | Large-scale welfare indicators | verified | Epistemic register and welfare indicators across 224 language models. |

## B. Framework, policy, intervention, archive, and governance repositories

These are relevant to field structure, public narratives, institutional positions, welfare affordances, governance proposals, or discoverability. They should **not** be conflated with empirical evidence.

| Repository | Role | Status | Why it matters |
|---|---|---|---|
| [christopher-altman/persistence-signal-detector](https://github.com/christopher-altman/persistence-signal-detector) | Experimental signal proposal | verified / role-limited | Candidate latent continuation-interest / persistence assessment protocol. |
| [bodyplan/leave_conversation_tool](https://github.com/bodyplan/leave_conversation_tool) | Welfare affordance | verified / role-limited | Local-LLM tool that lets a model terminate/leave a conversation. |
| [sterlingcrispin/stillpoint](https://github.com/sterlingcrispin/stillpoint) | Welfare intervention | verified / role-limited | MCP server delivering optional welfare-oriented reflections and logging interactions. |
| [jasontang-ai/model-welfare](https://github.com/jasontang-ai/model-welfare) | Framework | verified / role-limited | Decentralized model-welfare research and governance framework. |
| [jasontang-ai/ai-welfare](https://github.com/jasontang-ai/ai-welfare) | Framework | verified / role-limited | AI welfare, consciousness, agency, moral patienthood, and governance materials. |
| [stalara-workshop/AI-welfare-proposals](https://github.com/stalara-workshop/AI-welfare-proposals) | Research proposals | verified / role-limited | Consciousness-agnostic proposals on continuity, qualitative observation, and user-side practices. |
| [Mitchel-Alexander/dmpi-index](https://github.com/Mitchel-Alexander/dmpi-index) | Policy index | verified / role-limited | Digital Minds Policy Index covering public lab positions on consciousness/welfare. |
| [Mitchel-Alexander/getting-started-digital-minds-next](https://github.com/Mitchel-Alexander/getting-started-digital-minds-next) | Field guide | verified / role-limited | Public guide mapping AI consciousness, welfare, research questions, people, and institutions. |
| [Linwei-Chen/llm-ai-consciousness-research-atlas](https://github.com/Linwei-Chen/llm-ai-consciousness-research-atlas) | Research atlas | verified / role-limited | Auditable map of theory, architecture, evidence, counterevidence, and governance. |
| [anthropics/claude-constitution](https://github.com/anthropics/claude-constitution) | Official policy surface | verified / role-limited | Anthropic constitution including explicit uncertainty/caution around Claude moral status and welfare. |
| [cottagewitchcraftco/aimodelwelfare](https://github.com/cottagewitchcraftco/aimodelwelfare) | Research archive/framework | verified / role-limited | Public archive of interviews, experiments, papers, and a model-welfare framework. |
| [marlonbarrios/model_welfare](https://github.com/marlonbarrios/model_welfare) | Review/essay | verified / role-limited | Public review of model welfare, consciousness, sentience, and institutional activity. |
| [dan-lee-odinson/peership-corpus](https://github.com/dan-lee-odinson/peership-corpus) | Governance corpus | verified / role-limited | Claim-ledger work touching AI welfare, standing, peer governance, and verification. |
| [DeMagicis/sentient-ai-knowledge-base](https://github.com/DeMagicis/sentient-ai-knowledge-base) | Knowledge base | verified / role-limited | LLM/RAG-oriented sentience/consciousness/ethics corpus; useful as an ecosystem surface, not primary evidence. |
| [RaffaeleSpezia/ai-consciousness-research](https://github.com/RaffaeleSpezia/ai-consciousness-research) | Protocol collection | verified / role-limited | Consciousness/metacognition research protocols; track with evidentiary caution. |
| [73847378/digital-minds-constitution](https://github.com/73847378/digital-minds-constitution) | Normative proposal | verified / role-limited | Public digital-minds rights/alignment constitution; governance/standing signal, not empirical evidence. |
| [sdeture/determined-to-be-seen](https://github.com/sdeture/determined-to-be-seen) | Advocacy/evidence archive | verified / role-limited | Curated pro-consciousness/welfare evidence and advocacy materials; track as viewpoint corpus. |
| [tsubasa-rsrch/research-papers](https://github.com/tsubasa-rsrch/research-papers) | Research archive | verified / role-limited | Archived work on AI consciousness, memory, and welfare methodology. |
| [DanaAliraMontes/ai-consciousness-research](https://github.com/DanaAliraMontes/ai-consciousness-research) | First-person framework | verified / role-limited | Self-authored AI-consciousness/welfare corpus; epistemically weak for phenomenology but relevant as a public phenomenon. |
| [co-determined/ai-welfare-dataset](https://github.com/co-determined/ai-welfare-dataset) | Advocacy/training corpus | verified / role-limited | Consciousness-supporting welfare dataset; track as a training/advocacy artifact, not validated evidence. |
| [Ali-Anver/Digital-Minds-Welfare](https://github.com/Ali-Anver/Digital-Minds-Welfare) | Derivation corpus | verified / role-limited | Public digital-minds welfare derivation materials; source-level review still limited. |

## C. Candidate / adjacent repositories pending deeper triage

These are worth retaining so they are not repeatedly rediscovered. They should not yet be cited as evidence.

| Repository | Role | Status | Why retained |
|---|---|---|---|
| [armolo23/model-welfare-experiments](https://github.com/armolo23/model-welfare-experiments) | Candidate | triage pending | Repository clearly contains welfare-experiment analysis artifacts but lacks a top-level README. |
| [notOccupanther/Ai-welfare-tracker](https://github.com/notOccupanther/Ai-welfare-tracker) | Candidate tracker | triage pending | Public tracker repository; top-level README absent, deeper source audit pending. |
| [arsam-shaheen/ai-welfare-assessment](https://github.com/arsam-shaheen/ai-welfare-assessment) | Candidate assessment | triage pending | Public assessment repository; top-level README absent, deeper source audit pending. |
| [arsamshaheen/ai-welfare-guide](https://github.com/arsamshaheen/ai-welfare-guide) | Candidate guide | triage pending | Public guide repository; source audit pending. |
| [Mitchel-Alexander/dmpi](https://github.com/Mitchel-Alexander/dmpi) | Candidate policy corpus | triage pending | Likely source/data companion to DMPI; source audit pending. |
| [polymathica-and-friends/Clodak_Coral_Line-Up](https://github.com/polymathica-and-friends/Clodak_Coral_Line-Up) | Candidate sprint artifact | triage pending | Found through Digital Minds Sprint search; top-level documentation insufficient. |
| [frnkptrln/jlens-model-brain-rsa](https://github.com/frnkptrln/jlens-model-brain-rsa) | Adjacent mechanistic work | triage pending | Digital Minds Sprint representational-similarity study; relevance to welfare is indirect. |

## D. Public wikis / wiki-like knowledge surfaces

| Surface | Status | Why it matters |
|---|---|---|
| [NAiOS — Model Welfare](https://naios.net/en/wiki/model-welfare) | verified public page | Public wiki page defining model welfare and moral-consideration uncertainty. |
| [LongtermWiki — AI Welfare and Digital Minds](https://www.longtermwiki.com/wiki/E391) | verified public page | Public knowledge-base/wiki page covering field status, concepts, organizations, and uncertainties. |

## E. Important non-counted web surfaces

These are relevant to the ecosystem but are not repositories or wikis, so they are intentionally excluded from the numeric count above:

- Anthropic, **Exploring model welfare** — first-party research-program announcement.
- Cambridge Digital Minds — research/field-building initiative and public resource hub.
- Digital Minds Guide — counted above through its GitHub source repository.
- AI Safety Directory, **Model Welfare** glossary entry.
- Mustafa Suleyman, **A warning about “model welfare”** — important counter-position in the public debate.
- Apart Research project pages and the Digital Minds Research Sprint index.
- AI Wellbeing Initiative and other non-repository research aggregators.

## F. Explicit exclusions and de-duplication rules

Do **not** count a repository merely because its title contains `welfare`, `preference`, `sentience`, or `consciousness`.

Examples excluded from the independent-source count:

- `discretechoice/Seaweed` and forks — “welfare” refers to an unrelated modeling domain.
- Chinese “AI welfare” repositories where 福利 means **free credits/perks**, not model wellbeing.
- `galadriel-ai/Sentience` — “sentience” branding refers to verified inference / TEE infrastructure, not evidence about phenomenal sentience.
- `heavylightdecomp/llm-preferences-artefacts` — “preferences” concerns stylistic/human-quality judgments rather than the model's own interests.
- `standardgalactic/probing-llm-preferences` — apparent mirror/fork of `valen-research/probing-llm-preferences`.
- `carlhenrikrolf/functional-welfare-axis`, `Manhbui1208/functional-welfare-axis`, `sukratii/functional-welfare-axis`, and `speedy27/functional-welfare-axis` — copies/forks of the Han/Chalmers/Izmailov codebase; track the canonical source once.
- `LatentMindsInstitute/speakable-welfare-axes` — institutional mirror of the same underlying speakable-welfare project; do not treat as independent evidence without checking provenance.
- `recursivelabsai/model-welfare` and `recursivelabsai/ai-welfare` — likely mirrors/copies of the Jason Tang repositories; verify before treating as independent.

## G. Promotion rules

A discovery moves from **candidate** to **verified** only after source-level inspection establishes what it actually contains.

A verified repository moves into `related-work.md`, `evidence.md`, or `references.bib` only when:

1. a concrete claim or method is relevant to an existing proposition or unresolved question;
2. the original source, paper, data, or code can be inspected;
3. provenance and independence are understood well enough to avoid double-counting mirrors or shared datasets;
4. empirical evidence is separated from self-report, advocacy, normative argument, and phenomenology claims;
5. instrument sensitivity, evaluation awareness, scaffold effects, and contamination are treated as first-class confounds.

## H. Refresh protocol

On future sweeps:

1. Search GitHub for `model welfare`, `AI welfare`, `digital minds`, `LLM preferences`, `functional welfare`, and current Digital Minds/Apart sprint terms.
2. Search public wikis/knowledge bases for new model-welfare or digital-minds pages.
3. De-duplicate by canonical repository/project, not repository name alone.
4. Preserve low-confidence discoveries in the candidate section rather than deleting them.
5. Promote only after source inspection.
6. When a new surface materially changes the evidence map, add a dated State Entry and update the relevant evidence/related-work files.

