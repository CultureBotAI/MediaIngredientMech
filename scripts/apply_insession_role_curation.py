#!/usr/bin/env python3
"""Apply in-session (Claude) role curation for high-impact role-less records.

These roles were assigned by in-session Claude reasoning (NOT an external API call)
over the role-less MAPPED records with occurrence >= 2 — the cases the deterministic
synonym / CHEBI-ancestry / name-list passes could not reach. Only chemically/
biologically unambiguous assignments are included; nucleosides, osmolytes, pH-adjusters
(NaOH), enzymes, soils and other ambiguous/no-clean-enum cases were deliberately skipped.

Each is written PROVISIONAL: confidence 0.6, reference_type COMPUTATIONAL_PREDICTION,
curator "claude_in_session_curation" — easy to find, review, and revert. Idempotent:
records that already carry a facet role are skipped. Every assignment is gated by
scripts/audit_role_plausibility.py (run after applying).

Usage:
    python scripts/apply_insession_role_curation.py [--dry-run]
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.utils.role_facets import add_role
from mediaingredientmech.utils.role_iteration import FACET_ROLE_SLOTS, iter_role_assignments

# role -> identifiers (applied to every role-less MAPPED record with that identifier;
# the listed ids are same-substance, so the role holds for all their surface forms).
ASSIGNMENTS = {
    "TRACE_ELEMENT": [
        "CHEBI:53503", "CHEBI:53542", "CHEBI:53437", "CHEBI:86149", "cas:7718-98-1",
        "CHEBI:53438", "CHEBI:131378", "CHEBI:30729", "cas:12054-85-2", "CHEBI:35458",
        "CHEBI:53471", "CHEBI:46502", "CHEBI:38267", "CHEBI:86209",
        "MICRO:0001349", "mesh:D014131", "MICRO:0000455",
    ],
    "ELECTRON_DONOR": ["CHEBI:32150", "CHEBI:132112", "CHEBI:26977", "CHEBI:86466"],
    "REDUCING_AGENT": ["CHEBI:61278", "CHEBI:114786", "CHEBI:26709"],
    "PH_INDICATOR": ["CHEBI:86155", "CHEBI:86154"],
    "REDOX_INDICATOR": ["CHEBI:78019", "CHEBI:6872"],
    "SELECTIVE_AGENT": ["CHEBI:41688", "CHEBI:27641"],
    "VITAMIN_SOURCE": ["CHEBI:17836"],
    "COFACTOR_PROVIDER": ["CHEBI:50385", "CHEBI:17905", "CHEBI:15846", "CHEBI:15346"],
    "NITROGEN_SOURCE": ["CHEBI:16199", "CHEBI:63076", "CHEBI:91241"],
    "BUFFER": [
        "CHEBI:114249", "CHEBI:34683", "CHEBI:37583", "cas:16788-57-1",
        "CHEBI:17201", "cas:202185-84-0", "CHEBI:91263",
    ],
    "CARBON_SOURCE": [
        "CHEBI:30742", "CHEBI:45296", "CHEBI:131383", "CHEBI:17824", "CHEBI:15882",
        "CHEBI:18135", "CHEBI:28488", "CHEBI:113455", "CHEBI:30764", "CHEBI:18026",
        "CHEBI:30745", "CHEBI:28631", "CHEBI:17879", "CHEBI:18101", "CHEBI:17189",
        "CHEBI:35697", "CHEBI:132748", "CHEBI:35899", "CHEBI:18139",
    ],
    "ELECTRON_ACCEPTOR": ["CHEBI:17045", "CHEBI:17300", "CHEBI:132103", "cas:7791-07-3"],
    "SURFACTANT": ["CHEBI:53425", "CHEBI:53423", "CHEBI:141517", "CHEBI:75456", "CHEBI:75937"],
    "PROTEIN_SOURCE": ["NCIT:C113696", "MICRO:0001362"],
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    # invert to identifier -> role (assert no id assigned two roles by mistake)
    id_role: dict[str, str] = {}
    for role, ids in ASSIGNMENTS.items():
        for ident in ids:
            assert ident not in id_role, f"{ident} assigned twice ({id_role[ident]} & {role})"
            id_role[ident] = role

    curator = IngredientCurator(
        data_path=Path("data/curated/mapped_ingredients.yaml"),
        curator_name="claude_in_session_curation",
    )
    curator.load()

    applied = 0
    seen_ids = set()
    for record in curator.records:
        ident = record.get("identifier")
        if ident not in id_role:
            continue
        if record.get("mapping_status") != "MAPPED" or any(
            iter_role_assignments(record, slots=FACET_ROLE_SLOTS)
        ):
            continue
        role = id_role[ident]
        seen_ids.add(ident)
        if not args.dry_run:
            add_role(
                curator,
                record,
                role,
                confidence=0.6,
                reference_text="Assigned by in-session Claude reasoning (no external API)",
                reference_type="COMPUTATIONAL_PREDICTION",
                curator_note="Provisional in-session LLM role assignment; review recommended.",
            )
        applied += 1
        print(f"  {role:18s} <- {ident} {record['preferred_term'][:40]!r}")

    missing = sorted(set(id_role) - seen_ids)
    if missing:
        print(f"\nNOTE: {len(missing)} listed ids matched no role-less MAPPED record "
              f"(already roled / not found): {missing}")
    if not args.dry_run:
        curator.save()
        print(f"\nSaved; applied {applied} role(s).")
    else:
        print(f"\n[dry-run] would apply {applied} role(s).")


if __name__ == "__main__":
    main()
