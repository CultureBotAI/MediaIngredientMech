"""Read-only canonical-label check of the exact isolated proposal payloads.

This supplements strict LinkML validation. It records database provenance and
after-payload hashes; it does not validate substance identity or grant release.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sqlite3
import sys

import yaml

ROOT = Path(__file__).resolve().parent.parent
CACHE = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-generation-20261031T213407Z/ontology-cache/oaklib")
DATABASES = {
    "CHEBI": Path("/Users/marcin/.data/oaklib/chebi.db"),
    "NCIT": Path("/Users/marcin/.data/oaklib/ncit.db"),
    **{name.upper(): CACHE / f"{name}.db" for name in ("mesh", "foodon", "envo", "bto", "uberon")},
}


def run(proposal_files: list[Path]) -> dict:
    observations = []
    databases = {}
    connections = {}
    for path in proposal_files:
        document = json.loads(path.read_text())
        for proposal in document["proposals"]:
            capture = proposal["after_capture"]
            if capture["root"] != "artifact":
                raise ValueError("This helper only accepts isolated artifact payloads")
            after = ROOT / capture["path"]
            digest = hashlib.sha256(after.read_bytes()).hexdigest()
            if digest != capture["sha256"]:
                raise ValueError(f"after payload changed: {after}")
            value = yaml.safe_load(after.read_text())
            mapping = value.get("ontology_mapping")
            if not mapping:
                observations.append({"proposal_id": proposal["proposal_id"], "status": "NO_ONTOLOGY_MAPPING", "after_sha256": digest})
                continue
            curie, label = mapping["ontology_id"], mapping["ontology_label"]
            prefix, local = curie.split(":", 1)
            prefix = prefix.upper()
            database = DATABASES.get(prefix)
            row = {"proposal_id": proposal["proposal_id"], "after_sha256": digest, "ontology_id": curie, "ontology_label": label}
            if prefix in ('KGMICROBE.INGREDIENT', 'KGMICROBE.COMPOUND', 'KGMICROBE.PREP', 'CAS') and mapping.get('mapping_quality') == 'FALLBACK_REGISTRY':
                row['status'] = 'REGISTRY_SELF_CONSISTENT' if curie == value['identifier'] and label == value['preferred_term'] else 'REGISTRY_SELF_MISMATCH'
                row['limitation'] = 'Local identity row consistency only; this does not independently establish registry applicability or source identity.'
            elif database is None or not database.is_file():
                row["status"] = "UNAVAILABLE_ADAPTER"
            else:
                if prefix not in connections:
                    connections[prefix] = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
                    with database.open("rb") as handle:
                        sha = hashlib.file_digest(handle, "sha256").hexdigest()
                    databases[prefix] = {"path": str(database), "sha256": sha, "mode": "SQLite mode=ro"}
                result = connections[prefix].execute(
                    "SELECT predicate,value,object FROM statements WHERE subject=? "
                    "AND predicate IN ('rdfs:label','owl:deprecated','IAO:0100001')",
                    (f"{prefix}:{local}",),
                ).fetchall()
                canonical = {v for p, v, o in result if p == "rdfs:label"}
                deprecated = any(p == "owl:deprecated" and str(v).lower() in ("true", "1") for p, v, o in result)
                row.update(statements=result, status="OK_CANONICAL" if label in canonical and not deprecated else "MISMATCH_OR_DEPRECATED")
            observations.append(row)
    for connection in connections.values():
        connection.close()
    return {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "proposal_inputs": [{"path": str(p), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in proposal_files],
        "databases": databases,
        "results": observations,
        "scientific_approval_established": False,
        "limitations": "Canonical labels and deprecation flags only. Source/form identity, all synonyms, roles, downstream compatibility and full publication payload require separate review.",
    }


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit("usage: validate_proposal_labels.py NEW_RECEIPT PROPOSALS_JSON...")
    destination = Path(sys.argv[1])
    if destination.exists():
        raise FileExistsError(destination)
    report = run([Path(p) for p in sys.argv[2:]])
    destination.write_text(json.dumps(report, indent=2) + "\n")
    failures = [r for r in report["results"] if r["status"] not in ("OK_CANONICAL", "NO_ONTOLOGY_MAPPING", "REGISTRY_SELF_CONSISTENT")]
    print(json.dumps({"checked": len(report["results"]), "failures": failures}, indent=2))
    raise SystemExit(bool(failures))
