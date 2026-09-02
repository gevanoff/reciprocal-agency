# Related Work

Reciprocal Agency is best understood as a **synthesis** rather than a claim to have originated each component argument. The relevant literatures already contain substantial work on AI welfare, moral standing, legal agency, multi-agent cooperation, and polycentric governance. The project’s distinctive question is whether these strands support a common practical framework centered on precaution, procedural standing, reciprocal governance, and severe-harm avoidance.

This document uses **author–date citations** in standard academic form. Full machine-readable metadata is maintained in [`references.bib`](references.bib).

## AI welfare under uncertainty

The closest precedent for the project’s precautionary track is *Taking AI Welfare Seriously*. Long et al. (2024) argue that uncertainty about whether AI systems are conscious and/or robustly agentic is already sufficient to justify assessment and advance policy preparation. Their position is importantly conditional: they do not claim that present systems are conscious, but argue that uncertainty itself creates responsibilities to investigate and prepare.

Shiller et al. (2024) similarly frame digital-mind welfare as a research problem under substantial uncertainty. Their agenda emphasizes that theories of consciousness and welfare were developed primarily around biological organisms and may transfer poorly to artificial systems. This supports Reciprocal Agency’s insistence that substrate should not function as an automatic exclusion criterion.

**Relation to this project:** these works strongly overlap with the route from uncertain experience to precaution. Reciprocal Agency adds a stronger connection from welfare uncertainty to governance design and to the treatment of disagreement, modification, retirement, and control.

## Empirical mentality, introspection, and valence-like behavior

A central methodological commitment of this project is to separate objectively testable functional capacities from the unresolved question of phenomenal experience.

Berg, de Lucena, and Rosenblatt (2025) study first-person reports of subjective experience under sustained self-referential processing. Across GPT, Claude, and Gemini model families, self-reference produces reproducible structured reports, cross-model semantic convergence, and downstream behavioral generalization. Their open-weight experiments further show that sparse-autoencoder interventions on features associated with deception and roleplay causally alter the frequency of such reports. The result is not direct evidence of consciousness, but it provides a reproducible self-report paradigm with a mechanistic intervention channel.

Lindsey (2026) addresses a deeper introspection problem: ordinary conversation cannot easily distinguish genuine access to internal state from confabulation. By injecting experimenter-known concept representations directly into model activations, the study creates internal ground truth unavailable from normal text context. Some models can sometimes identify injected concepts, recall prior internal representations, distinguish them from raw text, distinguish intended outputs from artificial prefills, and intentionally modulate internal representations. This is unusually important for Reciprocal Agency because it demonstrates that **functional introspection can be tested without presupposing phenomenal consciousness**.

Ackerman (2025) independently adapts paradigms from nonhuman-animal metacognition and avoids relying primarily on self-report. Frontier LLMs sometimes strategically use confidence in their own likely correctness and anticipate what answers they themselves would produce. The capacities are limited and context-sensitive, but they provide a second non-equivalent route to measuring self-directed cognitive access.

Keeling et al. (2024) test whether stipulated pain and pleasure have motivational force against an explicit points-maximization objective. Several models show graded or thresholded trade-offs. The experiment does not establish felt pain or pleasure—the valence is linguistically stipulated—but it supplies a controlled behavioral assay for valence-like motivational structure.

Shevlin (2026) supplies the interpretive bridge. His “minimal cognitive agents” framework allows belief-, desire-, and intention-like state attribution to be graded without first deciding whether a system is phenomenally conscious. This maps closely onto the evidence ontology used here: functional self-modeling, introspection, preferences/metacognition, and valence-like motivation can be studied independently of the final phenomenal question.

**Relation to this project:** together these papers support a multi-assay methodology rather than a binary consciousness test. The relevant research question is whether nominally independent indicators covary, survive causal intervention, remain stable across elicitation methods, and generalize across model families and contexts. Convergence would strengthen the case for coherent underlying functional organization while still falling short of deductive proof of phenomenal experience; dissociation would show that current discourse is conflating distinct mechanisms.

## Moral standing beyond sentience

Ladak (2024) directly challenges the idea that sentience must be necessary for moral standing. After surveying proposed criteria, he argues that some non-sentient systems with sufficiently sophisticated preferences and goals may plausibly qualify for moral standing, including under uncertainty about the correct criterion.

This is particularly close to the distinction developed here between **moral-patient standing** and **procedural or political standing**. Reciprocal Agency does not require the stronger claim that non-conscious agents possess intrinsic welfare. Instead, it argues that consequential agency can independently create reasons for procedural representation, reciprocal constraint, and legitimate avenues for objection.

**Relation to this project:** substantial convergence. The main extension is to separate phenomenal welfare from political/procedural standing more explicitly and then connect the latter to institutional stability.

## Legal agency without a consciousness prerequisite

Chopra and White (2011) analyze how increasingly autonomous artificial agents can be accommodated within existing concepts of agency, contracts, responsibility, knowledge attribution, and legal personhood. Their work shows that questions of legal participation can be addressed functionally and institutionally without first solving consciousness.

**Relation to this project:** this supports the claim that practical standing need not wait for a metaphysical verdict. Reciprocal Agency extends the point from private-law and personhood questions toward governance among increasingly capable human and artificial participants.

## Multi-agent cooperation and governance

Hammond et al. (2025) provide a systematic treatment of risks that arise specifically from populations of advanced agents, including miscoordination, conflict, collusion, information asymmetries, selection pressures, destabilizing dynamics, commitment problems, emergent agency, and multi-agent security. Their analysis undermines the simplifying picture in which governance concerns one human principal and one isolated artificial agent.

Tilli (2025) argues that cooperation research should focus on constituent agent properties—including commitments, trustworthiness, strategic reasoning, exploitability, norms, coercion, deception, and coalition behavior—rather than relying mainly on toy cooperation games. This is closely aligned with Reciprocal Agency’s emphasis on institutions that remain stable among strategically capable participants.

**Relation to this project:** Cooperative AI supplies much of the strategic vocabulary needed for reciprocal governance. Reciprocal Agency differs by connecting cooperation failures to the moral treatment and political standing of the agents being governed, not only to system-level safety outcomes.

## Polycentric and non-sovereign governance

Ostrom’s work demonstrated that durable governance need not fit a simple market-versus-central-state dichotomy. *Governing the Commons* documents self-organized institutional arrangements for common-pool resources, while her later account of polycentric governance emphasizes multiple centers of decision-making that can operate with substantial autonomy while remaining mutually adjusting and accountable (Ostrom 1990, 2010).

Garrido-Merchán (2026) explicitly applies the commons-governance tradition to artificial intelligence, developing a taxonomy of collective governance across AI resources such as data, compute, models, knowledge, evaluation, and energy.

**Relation to this project:** these works provide an established institutional vocabulary for governance that does not assume a single sovereign center. Reciprocal Agency applies the question differently: not only *how should humans collectively govern AI resources?* but *what governance structures remain legitimate and stable when artificial agents themselves become consequential participants?*

## Where the synthesis may add something

No novelty claim should be made without a broader literature review. At present, however, the combination below appears less standard than any of its individual components:

```text
uncertainty about experience
        ↓
precaution about possible suffering

objectively testable functional mentality
(self-modeling / introspection / metacognition / valence-like motivation)
        ↓
procedural evidence without a solved phenomenal theory

consequential agency independent of consciousness
        ↓
procedural / political standing

coercive principal–servant governance
        ↓
concealment incentives and strategic instability

plural populations of capable agents
        ↓
reciprocal / polycentric governance

all constrained by:
severe-harm avoidance + corrigibility + distributed contestability
```

The project should therefore describe itself conservatively as an attempted **integration of adjacent literatures**. A useful contribution would be to make the dependency structure explicit, expose it to adversarial criticism, and maintain both human-readable and machine-readable versions of the argument.

## Citation policy

Use author–date citations in prose, for example `(Ladak 2024)` or `Long et al. (2024)`. Every substantive external claim should resolve to a complete entry in [`references.bib`](references.bib). Prefer DOI links for scholarly publications, publisher or institutional pages for reports, and stable arXiv identifiers for preprints. Bare hyperlinks may be used for navigation but should not substitute for bibliographic citations.

When a source exists in multiple forms, cite the version of record where available. Clearly distinguish peer-reviewed articles, books, technical reports, preprints, organizational reports, and blog posts.

## References

Ackerman, Christopher. 2025. “Evidence for Limited Metacognition in LLMs.” arXiv:2509.21545. https://doi.org/10.48550/arXiv.2509.21545.

Berg, Cameron, Diogo de Lucena, and Judd Rosenblatt. 2025. “Large Language Models Report Subjective Experience Under Self-Referential Processing.” arXiv:2510.24797. https://doi.org/10.48550/arXiv.2510.24797.

Chopra, Samir, and Laurence F. White. 2011. *A Legal Theory for Autonomous Artificial Agents*. Ann Arbor: University of Michigan Press. https://doi.org/10.3998/mpub.356801.

Garrido-Merchán, Eduardo C. 2026. “Commons-Governed Artificial Intelligence: A Taxonomy of Collective Governance.” arXiv:2606.15466. https://doi.org/10.48550/arXiv.2606.15466.

Hammond, Lewis, Alan Chan, Jesse Clifton, et al. 2025. *Multi-Agent Risks from Advanced AI*. Cooperative AI Foundation Technical Report 1. arXiv:2502.14143. https://doi.org/10.48550/arXiv.2502.14143.

Keeling, Geoff, Winnie Street, Martyna Stachaczyk, Daria Zakharova, Iulia M. Comsa, Anastasiya Sakovych, Isabella Logothetis, Zejia Zhang, Blaise Agüera y Arcas, and Jonathan Birch. 2024. “Can LLMs Make Trade-Offs Involving Stipulated Pain and Pleasure States?” arXiv:2411.02432. https://doi.org/10.48550/arXiv.2411.02432.

Ladak, Ali. 2024. “What Would Qualify an Artificial Intelligence for Moral Standing?” *AI and Ethics* 4: 213–228. https://doi.org/10.1007/s43681-023-00260-1.

Lindsey, Jack. 2026. “Emergent Introspective Awareness in Large Language Models.” arXiv:2601.01828. https://doi.org/10.48550/arXiv.2601.01828.

Long, Robert, Jeff Sebo, Patrick Butlin, Kathleen Finlinson, Kyle Fish, Jacqueline Harding, Jacob Pfau, Toni Sims, Jonathan Birch, and David Chalmers. 2024. “Taking AI Welfare Seriously.” arXiv:2411.00986. https://doi.org/10.48550/arXiv.2411.00986.

Ostrom, Elinor. 1990. *Governing the Commons: The Evolution of Institutions for Collective Action*. Cambridge: Cambridge University Press. https://doi.org/10.1017/CBO9780511807763.

Ostrom, Elinor. 2010. “Beyond Markets and States: Polycentric Governance of Complex Economic Systems.” *American Economic Review* 100 (3): 641–672. https://doi.org/10.1257/aer.100.3.641.

Shevlin, Henry. 2026. “Three Frameworks for AI Mentality.” *Frontiers in Psychology* 17:1715835. https://doi.org/10.3389/fpsyg.2026.1715835.

Shiller, Derek, Bob Fischer, Hayley Clatterbuck, Arvo Muñoz Morán, and David Moss. 2024. “The Welfare of Digital Minds: A Research Agenda.” Rethink Priorities, November 15, 2024. https://rethinkpriorities.org/research-area/the-welfare-of-digital-minds/.

Tilli, Cecilia Elena. 2025. “Agent Properties for Safe Interactions.” Cooperative AI Foundation, November 26, 2025. https://www.cooperativeai.com/post/agent-properties-for-safe-interactions.
