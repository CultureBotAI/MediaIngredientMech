#!/usr/bin/env python3
"""Correct the records damaged by the microbedecoder comma-stripping bug (#308).

Every correction below was verified against OLS4 before being written here; the
`verified` field on each entry records what was checked. Two distinct kinds:

**Label restoration.** The CHEBI term is *right* -- lexical matching recovered
the correct compound despite the truncated input -- but `preferred_term` is a
chemically impossible string (`5-trimethoxybenzoate`: three methoxy groups, one
locant) and that string is what gets exported downstream as the node label. The
corrupted form is preserved as a RAW_TEXT synonym, so the surface form the
source actually emitted is not lost; only the record's *preferred* label changes.

**Re-grounding.** `5-didehydro-D-gluconic Acid` was published as
`skos:exactMatch` to CHEBI:17426 `5-dehydro-D-gluconic acid`. That is a
different compound from CHEBI:18281 `2,5-didehydro-D-gluconic acid` (C6H10O7
mono-keto vs C6H8O7 di-keto). An exactMatch licenses node substitution
downstream, so this one is a live data defect, not a cosmetic one.

Deliberately NOT handled here -- each needs a curator call, not a mechanical fix:
  2-dimethylsuccinic_Acid  `2,2-` vs `2,3-` are both real; split-keep-last from
                           `2,3-` would have yielded `3-`, not `2-`, so `2,2-`
                           is more likely -- but "more likely" is not evidence.
  2-tetrachloroethane      probably `1,1,2,2-`, unverified.
  4-Diamino-6 / 4-diol     too little of the original string survives.

    python scripts/apply_locant_corrections.py            # dry-run
    python scripts/apply_locant_corrections.py --apply
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

# `data/curated/*.yaml` is the source of truth; `data/ingredients/<status>/*.yaml`
# is GENERATED from it by scripts/export_individual_records.py. Editing the
# per-record files directly looks like it works and is silently reverted by the
# next `just export-individual`, so every write here goes to the collection and
# the per-record view is regenerated afterwards.
COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
STAMP = "2026-08-08T00:00:00+00:00"
CURATOR = "apply_locant_corrections"
ISSUE = "#308"

# slug -> correction. `verified` is the OLS4 check that licensed the change.
LABEL_FIXES = {
    "2-dichloroethane": {
        "identifier": "CHEBI:27789",
        "preferred_term": "1,2-dichloroethane",
        "verified": "OLS4 CHEBI:27789 label='1,2-dichloroethane', not obsolete; "
                    "'1,2-dichloroethane' is a hasExactSynonym",
    },
    "3-trichloropropane": {
        "identifier": "CHEBI:34036",
        "preferred_term": "1,2,3-trichloropropane",
        "verified": "OLS4 CHEBI:34036 label='1,2,3-Trichloropropane', not obsolete",
    },
    "4-dihydroxy-biphenyl": {
        "identifier": "CHEBI:34367",
        "preferred_term": "4,4'-dihydroxybiphenyl",
        "stale_rationale": "the recorded CLOSE_MATCH rationale reads 'the label lost the "
                           "second locant'. The label no longer lacks it, so that wording is "
                           "stale; CLOSE_MATCH still stands because 4,4'-dihydroxybiphenyl and "
                           "biphenyl-4,4'-diol are alternative names, not an exact label match.",
        "verified": "OLS4 CHEBI:34367 label=\"biphenyl-4,4'-diol\", not obsolete; "
                    "4,4'-dihydroxybiphenyl is the same compound under an "
                    "alternative name, so mapping_quality CLOSE_MATCH is left as is",
    },
    "5-trimethoxybenzoate": {
        "identifier": "CHEBI:58989",
        "preferred_term": "3,4,5-trimethoxybenzoate",
        "stale_rationale": "the recorded CLOSE_MATCH rationale reads 'CLOSE_MATCH for the lost "
                           "locants'. The locants are no longer lost, so the stated reason no "
                           "longer holds and the grade is now a curator call.",
        "verified": "OLS4 CHEBI:58989 label='3,4,5-trimethoxybenzoate', not obsolete. "
                    "The corrected preferred_term now equals the ontology label "
                    "exactly; mapping_quality is left at CLOSE_MATCH because "
                    "re-grading is a separate curator call",
    },
    "2-6-dihydroxybenzoic_Acid": {
        "identifier": "cas:0303-07-1",
        "preferred_term": "2,6-dihydroxybenzoic acid",
        "verified": "CAS 303-07-1 is 2,6-dihydroxybenzoic acid; the record is "
                    "cas-primary (FALLBACK_REGISTRY) and its identifier is unchanged. "
                    "Here the comma became a hyphen ('2-6-') rather than being "
                    "dropped, so this row is the same bug via a different path",
    },
}

REGROUND = {
    "slug": "5-didehydro-D-gluconic_Acid",
    "preferred_term": "2,5-didehydro-D-gluconic acid",
    "from_id": "CHEBI:17426",
    "to_id": "CHEBI:18281",
    "to_label": "2,5-didehydro-D-gluconic acid",
    "verified": "OLS4: CHEBI:17426 label='5-dehydro-D-gluconic acid' (C6H10O7); "
                "CHEBI:18281 label='2,5-didehydro-D-gluconic acid' (C6H8O7), "
                "not obsolete, hasExactSynonym 'D-threo-hexo-2,5-diulosonic acid'. "
                "Distinct compounds; no existing record claims CHEBI:18281",
}


def load_collection() -> dict:
    return yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}


def find(coll: dict, identifier: str) -> dict | None:
    """Locate a record by primary identifier.

    Matching on `identifier` rather than on the slug: the slug is a sanitised
    filename of the *generated* view, and these are precisely the records whose
    labels are being changed, so a name-based lookup would be matching on the
    thing under repair.
    """
    for rec in coll.get("ingredients", []):
        if rec.get("identifier") == identifier:
            return rec
    return None


def ensure_raw_synonym(rec: dict, text: str) -> bool:
    """Keep the corrupted surface form as a synonym before replacing it.

    Without this the record would silently stop recording what the source
    actually emitted, and a later re-ingest of the same corrupt TSV would look
    like a brand new ingredient rather than a known-bad string.
    """
    syns = rec.setdefault("synonyms", [])
    if any(str(s.get("synonym_text", "")).strip() == text for s in syns):
        return False
    syns.append({"synonym_text": text, "synonym_type": "RAW_TEXT",
                 "source": "microbedecoder (comma-truncated)"})
    return True


SUPERSEDED = f"SUPERSEDED ({ISSUE}): "


def supersede_evidence(rec: dict, why: str) -> int:
    """Mark pre-existing evidence notes that the correction has falsified.

    Appending a new note is not enough. The re-grounded record kept a note
    reading "'didehydro' is a typo for 'dehydro'; same compound as
    5-dehydro-D-gluconic acid" -- which is exactly the mistake being corrected --
    sitting above the correction as evidence[0]. Whoever reads the record next
    reads the false claim first. Idempotent: already-marked notes are skipped.
    """
    n = 0
    for ev in (rec.get("ontology_mapping") or {}).get("evidence") or []:
        note = str(ev.get("notes", ""))
        # Skip notes this correction itself wrote. The issue tag lives in
        # `source` ("MIM curation (#308)"), not in `notes`, so checking only the
        # note text marked our own correction as superseded by itself.
        if note.startswith(SUPERSEDED) or ISSUE in note or ISSUE in str(ev.get("source", "")):
            continue
        ev["notes"] = f"{SUPERSEDED}{why} Original note follows. {note}"
        n += 1
    return n


def add_event(rec: dict, action: str, changes: str) -> None:
    rec.setdefault("curation_history", []).append({
        "timestamp": STAMP, "curator": CURATOR, "action": action,
        "changes": changes, "llm_assisted": False,
    })


def fix_label(coll: dict, slug: str, spec: dict) -> str | None:
    rec = find(coll, spec["identifier"])
    if rec is None:
        return f"{slug}: no record with identifier {spec['identifier']} -- skipped"
    old = rec.get("preferred_term")
    new = spec["preferred_term"]
    if old == new:
        # Label already restored by an earlier run. Superseding the stale
        # rationale was added afterwards, so it still has to run for those.
        n = supersede_evidence(rec, spec["stale_rationale"]) if spec.get("stale_rationale") else 0
        return (f"{slug}: already corrected; superseded {n} stale rationale note(s)"
                if n else None)
    added = ensure_raw_synonym(rec, str(old))
    # Some records justify their mapping_quality by the very truncation being
    # repaired ("CLOSE_MATCH for the lost locants"). Restoring the label leaves
    # that reasoning self-contradictory, so say so on the record rather than
    # silently leaving a grade whose stated basis no longer exists.
    if spec.get("stale_rationale"):
        supersede_evidence(rec, spec["stale_rationale"])
    rec["preferred_term"] = new
    add_event(rec, "CORRECTED_TRUNCATED_LABEL",
              f"preferred_term {old!r} -> {new!r}. The source label lost its locant "
              f"list to a comma-splitting bug in the microbedecoder ingest ({ISSUE}); "
              f"{old!r} is not a possible chemical name. The ontology mapping was "
              f"already correct and is unchanged."
              + (" Original surface form retained as a RAW_TEXT synonym." if added else "")
              + f" Verified: {spec['verified']}.")
    return f"{slug}: preferred_term {old!r} -> {new!r}"


def fix_regrounding(coll: dict, apply: bool) -> list[str]:
    spec = REGROUND
    rec = find(coll, spec["from_id"])
    done = find(coll, spec["to_id"])
    out = []
    if rec is None and done is not None:
        # Already re-grounded by an earlier run. The identifier move is
        # idempotent, but superseding the falsified evidence was added later, so
        # it still has to be applied to records corrected before that.
        n = supersede_evidence(done, "this record was re-grounded from CHEBI:17426 to "
                               "CHEBI:18281; the claim below that 'didehydro' is a typo for "
                               "'dehydro' denoting the same compound is false -- they are "
                               "distinct compounds.")
        return [f"{spec['slug']}: already re-grounded"
                + (f"; superseded {n} falsified evidence note(s)" if n else "")]
    if rec is None:
        return [f"{spec['slug']}: no record with identifier {spec['from_id']} -- skipped"]
    if done is not None:
        return [f"{spec['slug']}: {spec['to_id']} is already a primary identifier -- "
                f"this is a merge, not a re-grounding; skipped"]

    old_label = rec.get("preferred_term")
    ensure_raw_synonym(rec, str(old_label))
    supersede_evidence(
        rec,
        "this record was re-grounded from CHEBI:17426 to CHEBI:18281; the claim "
        "below that 'didehydro' is a typo for 'dehydro' denoting the same compound "
        "is false -- they are distinct compounds.")
    rec["identifier"] = spec["to_id"]
    rec["preferred_term"] = spec["preferred_term"]
    om = rec.setdefault("ontology_mapping", {})
    om["ontology_id"] = spec["to_id"]
    om["ontology_label"] = spec["to_label"]
    om["ontology_source"] = "CHEBI"
    om["mapping_quality"] = "EXACT_MATCH"
    om.setdefault("evidence", []).append({
        "evidence_type": "DATABASE_MATCH",
        "source": f"MIM curation ({ISSUE})",
        "notes": f"Re-grounded from {spec['from_id']} after the source label was found "
                 f"to be comma-truncated. {spec['verified']}.",
    })
    add_event(rec, "REGROUNDED_AFTER_TRUNCATED_LABEL",
              f"identifier/ontology_id {spec['from_id']} -> {spec['to_id']}; "
              f"preferred_term {old_label!r} -> {spec['preferred_term']!r}. The previous "
              f"mapping asserted skos:exactMatch to a different compound "
              f"(5-dehydro- vs 2,5-didehydro-, C6H10O7 vs C6H8O7), which licenses "
              f"node substitution downstream. Verified: {spec['verified']}.")
    out.append(f"{spec['slug']}: {spec['from_id']} -> {spec['to_id']}, "
               f"preferred_term {old_label!r} -> {spec['preferred_term']!r}")
    return out


def sync_sssom(apply: bool) -> list[str]:
    """Bring the published rows back in step with the corrected records.

    `subject_label` mirrors the record's `preferred_term`, so changing a label
    without touching SSSOM makes `reconcile_sssom` see the *same* row as both a
    GAP (record with no row) and an ORPHAN (row with no record) -- and `--apply`
    resolves an orphan by deleting it, which would drop five published mappings.
    Caught by tests/test_sssom_currency.py.

    `subject_id` is deliberately NOT touched. The MIM: subject encodes the slug,
    renaming subjects en masse is what #299 had to revert, and the slug did not
    change here -- only the human-readable label did.
    """
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    out = []

    # subject-id prefix -> (new subject_label, new object_id or None, new object_label or None)
    edits: dict[str, tuple[str, str | None, str | None]] = {
        f"MIM:{REGROUND['slug']}": (REGROUND["preferred_term"],
                                    REGROUND["to_id"], REGROUND["to_label"]),
    }
    for slug, spec in LABEL_FIXES.items():
        # A registry (cas:) row states the record's own label on both sides, so
        # its object_label tracks the correction too; an ontology row's
        # object_label belongs to the ontology and must not be rewritten.
        registry = not spec["identifier"].startswith("CHEBI:")
        edits[f"MIM:{slug}"] = (spec["preferred_term"], None,
                                spec["preferred_term"] if registry else None)

    for i, line in enumerate(lines):
        subject = line.split("\t", 1)[0]
        if subject not in edits:
            continue
        new_subj_label, new_obj_id, new_obj_label = edits[subject]
        cells = line.rstrip("\n").split("\t")
        before = "\t".join(cells[:5])
        cells[1] = new_subj_label
        if new_obj_id:
            cells[3] = new_obj_id
        if new_obj_label:
            cells[4] = new_obj_label
        after = "\t".join(cells[:5])
        if after == before:
            continue
        lines[i] = "\t".join(cells) + "\n"
        out.append(f"sssom:{i + 1}: {before}  ->  {after}")
    if apply and out:
        SSSOM.write_text("".join(lines), encoding="utf-8")
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="Write changes (default: dry-run).")
    args = ap.parse_args(argv)

    coll = load_collection()
    changes = [c for slug, spec in LABEL_FIXES.items()
               if (c := fix_label(coll, slug, spec))]
    changes += fix_regrounding(coll, args.apply)
    if args.apply and changes:
        save_yaml(coll, COLLECTION)
    # Always run: the record edits are idempotent, but a re-run after a partial
    # apply still needs SSSOM brought into step.
    changes += sync_sssom(args.apply)

    mode = "APPLIED" if args.apply else "DRY RUN (re-run with --apply)"
    print(f"{mode} -- {len(changes)} change(s)\n")
    for c in changes:
        print(f"  {c}")
    print("\nNot corrected (need a curator call, see the module docstring): "
          "2-dimethylsuccinic_Acid, 2-tetrachloroethane, 4-Diamino-6, 4-diol")
    return 0


if __name__ == "__main__":
    sys.exit(main())
