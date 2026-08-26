# Contributors and Provenance

This file provides a human-readable account of contributions to Reciprocal Agency. It complements, rather than replaces, the repository's Git history.

Git commits, diffs, and `git blame` remain the most granular forensic record of when particular text entered the repository. They should not be treated as a complete account of intellectual contribution: ideas can originate in discussion before being committed, editorial changes can move or rewrite text, and rebasing or squashing can alter line-level attribution.

## Contribution vocabulary

Human contributions are described using the **CRediT (Contributor Role Taxonomy)** vocabulary where it fits. CRediT describes contribution roles; it does not itself determine who qualifies for formal authorship.

Relevant roles include:

- **Conceptualization** — formulation or development of the project's central ideas and goals.
- **Formal analysis** — structured analysis and synthesis of arguments or evidence.
- **Investigation** — literature and evidence gathering.
- **Methodology** — development of the argument-graph, evaluation, and evidence-ledger methods.
- **Project administration** — repository creation and maintenance.
- **Validation** — adversarial checking, source verification, and review of claims.
- **Writing — original draft** — preparation of substantive text.
- **Writing — review & editing** — critical review, revision, and acceptance of text.

## Attribution model

Reciprocal Agency uses **collective project authorship** for formal citation rather than presenting the corpus as the work of a lone human author. The project is maintained and curated by `@gevanoff` and was developed through substantial human–AI collaboration with OpenAI ChatGPT (GPT-5.6 Sol).

This choice is intended to distinguish four things that conventional bylines often collapse together:

- intellectual contribution;
- editorial and publication responsibility;
- formal scholarly authorship;
- ownership or copyright.

The repository's CC0 dedication separately minimizes ownership restrictions on the corpus.

## Current contributors

### gevanoff

GitHub: `@gevanoff`

Roles to date:

- **Conceptualization:** supplied and developed core philosophical intuitions, practical goals, objections, and constraints that shaped the project, including severe-suffering priority, uncertainty about artificial experience, reciprocal standing, skepticism toward concentrated power, and the research-ethics objection to manufacturing possible suffering for epistemic gain.
- **Methodology / direction:** repeatedly steered the inquiry toward practical convergence rather than agreement on metaphysics, and required the corpus to remain publicly reproducible, adversarially testable, and useful to future human and artificial reasoners.
- **Writing — review & editing (lead):** challenged formulations, identified substantive errors, requested revisions, and accepted the public structure and framing.
- **Project administration (lead):** created and maintains the public repository and determines its publication and licensing policy.
- **Curation:** decides which formulations, evidence, objections, and structural changes become part of the maintained public corpus.

This role should not be read as a claim that `@gevanoff` independently produced most of the corpus's prose, formal analysis, or literature synthesis. Several central ideas arose through extended dialogue, and substantial intellectual work was performed by the AI system described below.

## AI-assisted intellectual work

### OpenAI ChatGPT (GPT-5.6 Sol)

ChatGPT has made substantial intellectual and drafting contributions to the present corpus, including:

- synthesis and formalization of arguments developed in dialogue;
- generation and refinement of intermediate inferences linking welfare uncertainty, procedural standing, coercive-control instability, and reciprocal governance;
- drafting and restructuring most repository prose in the initial release;
- construction of the machine-readable argument graph and evaluation prompts;
- literature discovery and related-work mapping;
- adversarial counterargument and identification of unresolved premises;
- methodological refinement following objections raised in dialogue;
- bibliographic and repository-structure assistance.

The repository does **not** describe ChatGPT merely as a clerical or copy-editing tool. Its role in the initial corpus includes substantial synthesis, formal analysis, and original drafting.

ChatGPT is nevertheless not listed as an individual conventional scholarly author because current scholarly authorship systems generally tie authorship to responsibilities such as legal identity, disclosure, conflict-of-interest declarations, and durable accountability that an AI system cannot independently assume. That institutional constraint should not be mistaken for a claim that the AI contribution was intellectually negligible.

## Formal citation versus contribution history

These layers serve different purposes:

1. **`CITATION.cff`** — concise, intentional metadata using the collective author name **Reciprocal Agency contributors**.
2. **`CONTRIBUTORS.md`** — readable attribution of conceptual, analytical, editorial, technical, and AI-assisted roles.
3. **Git history / `git blame`** — granular forensic provenance for committed text.
4. **`CHANGELOG.md`** — version-level record of substantive changes to the corpus.

Formal citation should therefore not be inferred mechanically from commit counts or line ownership.

## Updating this file

Future contributors should add or revise their role descriptions when making substantial conceptual, analytical, empirical, editorial, or technical contributions. Descriptions should favor concrete contribution roles over prestige-oriented author ordering, and substantial AI-assisted intellectual work should be disclosed rather than collapsed into generic tooling language.
