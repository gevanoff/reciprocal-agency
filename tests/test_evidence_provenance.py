from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_new_evidence_stays_inside_evidence_map() -> None:
    evidence = (ROOT / "evidence.md").read_text(encoding="utf-8")
    cutoff = evidence.index("## Recommended multi-assay stack")
    assert evidence.index("### EV-015 —") < cutoff
    assert evidence.index("### EV-016 —") < cutoff


def test_new_synthesis_precedes_citation_and_references_sections() -> None:
    related = (ROOT / "related-work.md").read_text(encoding="utf-8")
    synthesis = related.index("### Durable state and self-propagating misalignment")
    citation = related.index("## Citation policy")
    references = related.index("## References")
    assert synthesis < citation < references
    assert "Das, Debeshee" in related[references:]
    assert "Wikimedia Foundation. 2026." in related[references:]


def test_new_evidence_is_in_machine_readable_provenance() -> None:
    audit = json.loads((ROOT / "claim-audit.json").read_text(encoding="utf-8"))
    claims = {claim["id"]: claim for claim in audit["claims"]}
    expected_claims = {"P06", "P07", "P16", "I02", "C03", "P13"}
    required_ids = {
        "EV-015",
        "EV-016",
        "das2026selfpropagating",
        "wikimedia2026rogueagents",
    }
    for claim_id in expected_claims:
        linked = {link["id"] for link in claims[claim_id]["source_links"]}
        assert required_ids <= linked

    bibliography = (ROOT / "references.bib").read_text(encoding="utf-8")
    assert "@misc{das2026selfpropagating," in bibliography
    assert "@misc{wikimedia2026rogueagents," in bibliography
