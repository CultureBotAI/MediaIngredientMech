#!/usr/bin/env python3
"""Correct stale/empty ``ontology_label`` values to the canonical OBO label.

``OntologyMapping.ontology_label`` is meant to carry the *ontology's* canonical
label, while ``preferred_term`` holds the curated media-ingredient surface form
(a formula, catalog name, or common name). Many CHEBI records, however, have the
surface form copied into ``ontology_label`` too — e.g. ``CHEBI:17905`` carried
``ontology_label: "2-Mercaptoethanesulfonate"`` when CHEBI's canonical label is
``coenzyme M``. The 2026-05-23 backfill only filled *empty* labels; it never
corrected stale-but-nonempty ones.

This script resolves the canonical label from the same local OAK sqlite adapters
the repo already uses (``~/.data/oaklib/<onto>.db``) and overwrites
``ontology_label`` wherever it differs. ``preferred_term`` is never touched.

Safety guards (mirrors ``backfill_ontology_labels.py``):
  * skip records whose ``ontology_source`` disagrees with the CURIE prefix
    (the documented id/source-mismatch class — fix the record first);
  * never overwrite with a junk IRI-fragment label (e.g. ``CHEBI_8150``, the
    string OAK returns for obsolete/stub terms) or an empty string;
  * only prefixes with a populated local adapter are processed; others are left
    untouched (``micro.db`` is currently a 0-byte stub, so MICRO is skipped).

Every change is recorded as a ``CORRECTED`` curation event. Idempotent: a second
run finds nothing to do.

Usage::

    python scripts/correct_stale_ontology_labels.py            # writes in place
    python scripts/correct_stale_ontology_labels.py --dry-run  # report only
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.utils.yaml_handler import save_yaml

DATA = Path("data/curated/mapped_ingredients.yaml")

# Prefixes with a local OAK sqlite adapter whose labels we trust. MICRO is
# excluded on purpose: ~/.data/oaklib/micro.db is a 0-byte stub, so every MICRO
# id would resolve to nothing and look (wrongly) like a missing term.
OAK_DBS = {
    "CHEBI": "chebi.db",
    "FOODON": "foodon.db",
    "ENVO": "envo.db",
    "UBERON": "uberon.db",
    "BTO": "bto.db",
}
REGISTRY_PREFIXES = {"kgmicrobe.compound", "kgmicrobe.ingredient", "cas", "registry", "mesh"}


def make_resolver():
    """Return f(curie) -> canonical label or None, lazily opening adapters."""
    from oaklib import get_adapter

    adapters: dict = {}
    base = Path.home() / ".data" / "oaklib"

    def resolve(curie: str) -> str | None:
        prefix = curie.split(":", 1)[0]
        db = OAK_DBS.get(prefix)
        if not db or not (base / db).exists() or (base / db).stat().st_size == 0:
            return None
        try:
            if prefix not in adapters:
                adapters[prefix] = get_adapter(f"sqlite:///{base / db}")
            label = adapters[prefix].label(curie)
        except Exception as e:  # missing cache / adapter failure
            print(f"  warning: could not resolve {curie} ({e})", file=sys.stderr)
            return None
        if not label:
            return None
        # IRI-fragment fallback (e.g. "CHEBI_8150") = obsolete/stub, not a label.
        local = curie.split(":", 1)[1]
        if label.replace("_", ":") == curie or label == f"{prefix}_{local}":
            return None
        return label

    return resolve


def needs_correction(om: dict, resolve) -> str | None:
    """Return the canonical label an OntologyMapping should adopt, or None to skip.

    Pure (modulo ``resolve``) so it can be unit-tested with a stub resolver.
    Returns None when: the id has no trusted adapter, the source disagrees with
    the prefix (id/source-mismatch class), the canonical label is unresolvable/
    junk, or the label is already byte-canonical.
    """
    oid = om.get("ontology_id")
    if not oid or oid.split(":", 1)[0] not in OAK_DBS:
        return None
    prefix = oid.split(":", 1)[0]
    source = (om.get("ontology_source") or "").strip()
    if source and prefix.lower() not in REGISTRY_PREFIXES and source.upper() != prefix.upper():
        return None
    canonical = resolve(oid)
    if not canonical:
        return None
    if (om.get("ontology_label") or "").strip() == canonical.strip():
        return None
    return canonical


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--limit", type=int, default=0, help="show N samples in dry-run")
    args = parser.parse_args()

    data = yaml.safe_load(DATA.read_text())
    resolve = make_resolver()

    corrected, filled, samples = 0, 0, []
    for r in data["ingredients"]:
        om = r.get("ontology_mapping") or {}
        canonical = needs_correction(om, resolve)
        if not canonical:
            continue
        current = om.get("ontology_label") or ""
        was_empty = current.strip() == ""
        if len(samples) < (args.limit or 12):
            samples.append((om["ontology_id"], current, canonical))
        if not args.dry_run:
            om["ontology_label"] = canonical
            record_curation_event(
                r,
                curator="correct_stale_ontology_labels.py",
                action="CORRECTED",
                changes=(
                    f"ontology_label {'(empty)' if was_empty else repr(current)} -> "
                    f"{canonical!r}: synced to canonical {om['ontology_id'].split(':',1)[0]} "
                    f"label (preferred_term {r.get('preferred_term')!r} unchanged)."
                ),
            )
        corrected += 1
        filled += int(was_empty)

    print(f"Records needing correction: {corrected}  (of which empty->filled: {filled})")
    for oid, cur, canon in samples:
        print(f"  {oid:16s} {('(empty)' if cur.strip()=='' else repr(cur)):42s} -> {canon!r}")
    if corrected > len(samples):
        print(f"  ... and {corrected - len(samples)} more")

    if not args.dry_run and corrected:
        save_yaml(data, DATA, backup=False, validate=True, target_class="IngredientCollection")
        print(f"\nSaved {DATA}")
    elif args.dry_run:
        print("\n[dry-run] no changes written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
