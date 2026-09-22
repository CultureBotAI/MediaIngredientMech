"""Build the frozen #232 parent-name synonym decisions from the reviewed baseline.

Each decision retypes one synonym on a salt, hydrate or merge-tombstone record
that carries the name of the parent it is a form OF -- the free acid's IUPAC
name on a monopotassium salt, the anhydrous ChEBI label on a heptahydrate, a
sibling hydrate's formula string. MAPPING_SEMANTICS Section 3 keeps those
distinct, so the label index resolved the parent's name to the wrong record.

The criterion is decidable and re-derived from ChEBI here: the synonym is a
name ChEBI gives ANOTHER mapped record's term and not this record's own term, or
a formula string whose water count differs from this record's own. Nothing else
about the record is adjudicated.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from mediaingredientmech.export.reviewed_sssom import read_sssom, row_sha256  # noqa: E402
from mediaingredientmech.utils.oaklib_cache import require_db  # noqa: E402

ISSUE = "https://github.com/CultureBotAI/MediaIngredientMech/issues/232"
_NAMES = ("rdfs:label", "oio:hasExactSynonym", "oio:hasRelatedSynonym", "oio:hasBroadSynonym", "oio:hasNarrowSynonym")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def json_sha256(value: object) -> str:
    return sha256_bytes(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())


def yaml_bytes(record: dict) -> bytes:
    return yaml.safe_dump(record, default_flow_style=False, sort_keys=False, allow_unicode=True, width=80).encode()


def waters(text: str):
    m = re.search(r"(?:x|·|・|\.|\*|×)\s*(\d+)\s*H2O", text, re.I) or re.search(r"(\d+)H2O", text)
    if m:
        return int(m.group(1))
    return 0 if re.search(r"anhydrous", text, re.I) else None


def main() -> None:
    con = sqlite3.connect(require_db("CHEBI"))
    marks = ",".join("?" for _ in _NAMES)

    def names(curie: str) -> set[str]:
        if not curie.startswith("CHEBI:"):
            return set()
        return {(v or "").casefold() for (v,) in con.execute(f"select value from statements where subject=? and predicate in ({marks})", (curie, *_NAMES))}  # noqa: S608

    def label(curie: str) -> str:
        r = con.execute("select value from statements where subject=? and predicate='rdfs:label'", (curie,)).fetchone()
        return r[0] if r else curie

    mapped = {}
    for path in sorted((ROOT / "data/ingredients/mapped").glob("*.yaml")):
        d = yaml.safe_load(path.read_text())
        if d.get("mapping_status") == "MAPPED" and str(d.get("identifier", "")).startswith("CHEBI:"):
            mapped[str(path.relative_to(ROOT))] = d["identifier"]
    other_names: dict[str, str] = {}
    for rel, ident in mapped.items():
        for n in names(ident):
            other_names.setdefault(n, ident)

    retirements = json.loads((HERE / "retirements.json").read_text())
    positions = json.loads((HERE / "sssom_row_positions.json").read_text())
    sssom_path = ROOT / "mappings/ingredient_mappings.sssom.tsv"
    _, _, rows = read_sssom(sssom_path)
    timestamp = datetime.now(timezone.utc).isoformat()
    records = []
    for rel in sorted(retirements):
        path = ROOT / rel
        raw = path.read_bytes()
        before = yaml.safe_load(raw)
        own = str(before["identifier"])
        own_names = names(own)
        my_w = waters(before.get("preferred_term", "")) or waters(path.stem.replace("_", " "))
        wanted = {n.casefold() for n in retirements[rel]}
        decisions = []
        for position, synonym in enumerate(before.get("synonyms") or []):
            text = (synonym.get("synonym_text") or "").strip()
            if text.casefold() not in wanted or synonym.get("synonym_type") == "REJECTED_LABEL":
                continue
            w = waters(text)
            if w is not None and my_w is not None and w != my_w:
                reason = (f"'{text}' names a different hydration state ({w} H2O) from this record's own ({my_w} H2O); "
                          "Section 3 keeps hydrates distinct, so it cannot resolve here.")
                basis = {"kind": "hydrate_count", "token_waters": w, "record_waters": my_w}
            else:
                owner = other_names.get(text.casefold())
                if owner is None or text.casefold() in own_names:
                    raise ValueError(f"criterion no longer holds for {rel}: {text!r}")
                reason = (f"'{text}' is a ChEBI name of {owner} ({label(owner)}), the parent compound this record is a form of, "
                          f"and not a name of the record's own term {own}; Section 3 keeps the form distinct.")
                basis = {"kind": "chebi_name_of_other_term", "chebi_owner": owner, "chebi_owner_label": label(owner), "record_term": own}
            mentions = [
                {"curation_history_position": i, "event": ev}
                for i, ev in enumerate(before.get("curation_history") or [])
                if text.casefold() in json.dumps(ev, ensure_ascii=False).casefold()
            ]
            decisions.append({
                "synonym_position": position,
                "before_synonym": copy.deepcopy(synonym),
                "disposition": "REJECTED_LABEL",
                "reason": reason,
                "basis": basis,
                "source_evidence": {
                    "source_synonym_json_pointer": f"/synonyms/{position}",
                    "source_metadata_preserved": synonym.get("source"),
                    "source_history_mentions": mentions,
                },
            })
        if len(decisions) != len(retirements[rel]):
            raise ValueError(f"{rel}: planned {len(retirements[rel])} retirements, found {len(decisions)} live synonyms")
        after = copy.deepcopy(before)
        for dec in decisions:
            after["synonyms"][dec["synonym_position"]]["synonym_type"] = "REJECTED_LABEL"
        sssom_rows = [
            {"data_row_position": p["data_row_position"], "row": rows[p["data_row_position"] - 1], "row_sha256": row_sha256(rows[p["data_row_position"] - 1])}
            for p in positions.get(rel, [])
        ]
        for entry in sssom_rows:
            if entry["row"]["subject_id"] != "MIM:" + path.stem:
                raise ValueError(f"row position drifted for {rel}")
        records.append({
            "source_record": rel,
            "identifier": own,
            "preferred_term": before["preferred_term"],
            "before_yaml_sha256": sha256_bytes(raw),
            "before_record_sha256": json_sha256(before),
            "before_record": before,
            "decisions": decisions,
            "after_record_sha256": None,   # filled by apply.py, which owns the curation event
            "after_yaml_sha256": None,
            "sssom_rows": sssom_rows,
        })
    plan = {
        "schema_version": 1,
        "issue": ISSUE,
        "baseline_git_commit": subprocess.run(["git", "rev-parse", "origin/main"], capture_output=True, text=True, cwd=ROOT).stdout.strip(),
        "curation_timestamp": timestamp,
        "review_scope": (
            f"Exact {sum(len(r['decisions']) for r in records)} parent-compound or sibling-hydrate names on "
            f"{len(records)} salt, hydrate or merge-tombstone records, {sum(len(r['sssom_rows']) for r in records)} of which publish "
            "the token in a full SSSOM row. This review retypes a name that belongs to a different substance and does not approve "
            "identities, remaining synonyms, roles or chemical equivalences. No alias is added."
        ),
        "criterion": "ChEBI assigns the name to another mapped record's term and not to this record's own term, or the formula's water count differs from this record's.",
        "baseline_sssom": {"path": "mappings/ingredient_mappings.sssom.tsv", "sha256": sha256_bytes(sssom_path.read_bytes()), "row_count": len(rows)},
        "evidence_contract": {
            "mapping_semantics": "MAPPING_SEMANTICS.md Section 3: hydrates, anhydrous forms and salts are distinct substances; a reviewed non-name remains REJECTED_LABEL",
            "schema": "src/mediaingredientmech/schema/mediaingredientmech.yaml: IngredientSynonym and SynonymTypeEnum.REJECTED_LABEL",
            "decision_basis": "Direct comparison of each synonym against ChEBI's name lists for the record's own term and for every other mapped record's term, plus hydrate water counts. No external biological claim is inferred.",
        },
        "records": records,
    }
    (HERE / "decisions.json").write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"records": len(records), "decisions": sum(len(r["decisions"]) for r in records), "sssom_rows": sum(len(r["sssom_rows"]) for r in records)}))


if __name__ == "__main__":
    main()
