# Outbound Contribution Strategy

_Status: working plan — 2026-09-30_

The goal is to contribute useful, independently checkable work to adjacent public projects **without turning contribution into backlink placement**.

A link to Reciprocal Agency is appropriate when it supplies provenance for a concrete method, dataset, argument, replication, or comparison being contributed. It is not sufficient reason to open an issue or pull request.

## Contribution rule

Use this order:

```text
missing test / correction / synthesis
        ↓
smallest useful contribution
        ↓
source-bounded evidence and falsifiers
        ↓
attribution/provenance
        ↓
optional reciprocal link
```

Never reverse the order.

## Why this matters for independence

Reciprocal Agency explicitly treats post-exposure agreement as weaker evidence than blind convergence. Seeding the corpus widely and then later citing agreement from those same surfaces would contaminate the independence map.

Therefore every outbound contribution should record:

- target repository/page;
- date and contribution type;
- exact Reciprocal Agency material exposed;
- whether the target previously knew of the project;
- whether the contribution could influence later model/human agreement;
- any later evidence imported back from the target.

This is both research hygiene and ordinary citation provenance.

## Immediate-fit targets

### 1. Mitchel-Alexander/getting-started-digital-minds-next — Digital Minds Guide

**Why fit is strong**

The guide explicitly welcomes human contributions and already has structured research areas for:

- Welfare Capacity and Assessment;
- Governance Under Uncertainty;
- Safety-Welfare Coordination;
- Rights and Legal Frameworks;
- Identity and Individuation.

Those are direct intersections with Reciprocal Agency rather than a forced backlink opportunity.

**Useful contribution**

A small PR adding one or more properly described resources where the guide has a genuine gap. The strongest candidate is not a generic project listing; it is a concise entry pointing to:

- the method × claim matrix under Welfare Capacity and Assessment, as a cross-study measurement/confound map;
- the reciprocal-governance argument under Safety-Welfare Coordination or Governance Under Uncertainty, if the maintainer judges it sufficiently developed;
- subject-individuation work only where it adds something not already covered by the guide's current identity sources.

**Attribution**

Normal resource citation: "Reciprocal Agency contributors" plus canonical repository URL. Avoid promotional language.

**Gate before submission**

Read the full target data section, verify no existing source already does the same job, keep British English, type the new data correctly, and make the PR narrowly scoped.

### 2. jasontang-ai/model-welfare — Model Welfare Initiative

**Why fit is strong**

The repository explicitly invites extensions, critiques, alternatives, framework applications, and shared findings. Its current materials call for:

- measurement approaches and limitations;
- evidence standards;
- cross-system observation;
- methods for distinguishing alternative explanations;
- protocol refinement;
- measurement standardisation;
- integration across diverse data sources.

That is nearly a direct request for the work in the method × claim matrix.

**Useful contribution**

A bounded methodological addition, probably to `methodologies.md`, `open-research.md`, or `research-agenda.md`, introducing:

1. construct separation: stated preference != behavior != introspective access != latent representation != persistent state;
2. a minimum robustness bundle for welfare-preference claims;
3. explicit null, evaluation-awareness, scaffold, and persistence controls;
4. a short pointer to the machine-readable matrix as provenance.

A second, separate contribution could later present reciprocal/polycentric governance as an alternative governance framework, but it should not be bundled into the measurement PR.

**Attribution**

Cite the matrix/repository only for the specific synthesis or framework actually imported. Preserve the target project's authorship and terminology.

### 3. rgambee/llm-preferences

**Why fit is strong**

The study itself identifies evaluation awareness as important future work and already distinguishes self-report, behavior, and interpretability.

**Useful contribution**

Not a backlink PR. The useful path is a replication/extension protocol adding:

- explicit evaluation-awareness probes;
- additional response-format and option-order arms;
- a second elicitation channel;
- predeclared criteria for when a preference is called stable.

If we actually run that extension, an issue or PR linking the reproducible results back to Reciprocal Agency would be well justified.

**Gate**

Do not contact merely to point out that the matrix cites the study. Produce a concrete protocol or result first.

### 4. benjibrcz/which-preference-gets-measured

**Why fit is strong**

The project already treats falsification as a feature and distinguishes owned preference, self-prediction, forced choice, and identity report. That maps almost exactly onto the matrix's construct-separation rule.

**Useful contribution**

A cross-study comparison or replication that adds evaluation-awareness, authority-pressure, costly-choice, or internal-state channels to the same-item design.

**Gate**

Prefer a result-bearing extension or a narrowly framed methodological issue. Avoid asking the repository to cite Reciprocal Agency just because the conclusions converge.

## Strong targets after doing new empirical work

### Mulaydm10/null-ladder

The natural contribution is a **new null**, not prose: test one or more Reciprocal Agency preference/valence criteria against mindless or minimally parameterised generators. If the null passes, that weakens our own criteria and should be imported back into the repository.

This is especially valuable because it creates adversarial contact with the project rather than friendly citation exchange.

### pnavada/digital-minds-research-sprint

A useful extension would combine Welfare Introspection Accuracy with an evaluation-awareness readout or sham steering condition. The contribution becomes valuable only when it adds data/code or a crisp design distinction.

### almostrealism/model-welfare

The project is unusually compatible with construct-validity work. Potential contribution: apply the matrix's persistence/construct-specificity distinctions to a new intervention or replication arm.

**Important:** avoid influencing an active preregistered study after registration in ways that muddy its confirmatory status. Coordinate only around clearly post-registration additions or future studies.

### the-manyfolds/thats-not-my-volvo

Potential contribution: connect behavioral stability/self-recognition dissociation to a preregistered subject-individuation test, ideally using an intervention rather than a literature-only cross-reference.

## Useful but lower-immediacy surfaces

### valen-research/probing-llm-preferences

The repository is primarily a paper supplement and replication base. Best contribution is a genuine replication or extension using another model family or added robustness controls. A documentation-only backlink is not useful.

### Mitchel-Alexander/dmpi-index

The Digital Minds Policy Index tracks commercial AI-lab policy positions. Reciprocal Agency is not a commercial-lab policy source, so direct inclusion would distort its corpus definition. Contribution should be limited to corrections or methodological improvements relevant to the index itself.

### Public wikis

Wiki contribution can be useful when adding neutral, sourced coverage of a missing project or method. The standard should be higher than for GitHub: write from third-party/primary evidence, disclose project involvement where the venue expects it, and avoid using the wiki as a self-citation surface.

## Contribution forms, ordered by evidentiary value

1. **Replication / new experiment** — strongest reciprocal value.
2. **Falsifier or null control** — especially valuable because it may weaken our own claims.
3. **Reusable method / dataset / machine-readable mapping**.
4. **Concrete correction or missing-source patch**.
5. **Cross-study synthesis that the target does not already contain**.
6. **Related-work citation**.
7. **Bare backlink** — normally do not do this.

## Attribution format

Where a target accepts ordinary scholarly/resource attribution, use a neutral form such as:

> Reciprocal Agency contributors (2026), "Model Preference / Welfare Method × Claim Matrix", Reciprocal Agency.

Then link to the exact file or stable commit, not merely the repository homepage when the contribution depends on a specific artifact.

If Gabe is the contributor of record for an external PR, Git history provides the ordinary human attribution. AI assistance can be disclosed consistently with the target project's conventions; do not imply independent human authorship for text generated or heavily synthesized by an AI system.

## Contamination ledger

Before any external contribution is submitted, add a row to a future outbound-contribution ledger with:

- target;
- artifact exposed;
- contribution SHA/URL;
- exposure date;
- direction: outbound / inbound / reciprocal;
- independence consequence;
- follow-up status.

This should later be machine-readable so the claim-audit tooling can downgrade apparent convergence that occurred after exposure.

## Immediate next work

1. Finish source-auditing the v0.1 matrix.
2. Add an outbound-contribution ledger schema.
3. Prepare **draft-only**, target-specific contribution packets for:
   - Digital Minds Guide;
   - Model Welfare Initiative.
4. Design, but do not yet submit, one adversarial empirical extension for:
   - Null Ladder; or
   - LLM Preferences evaluation-awareness replication.
5. Record any actual external exposure before importing later agreement as evidence.
