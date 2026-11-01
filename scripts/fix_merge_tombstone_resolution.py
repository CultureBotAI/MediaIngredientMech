#!/usr/bin/env python3
"""Repair merge tombstones whose post-merge REJECTED events broke _mim_merge_target (#882).

Nine merge tombstones in ``data/ingredients/mapped/`` acquired post-merge
bookkeeping curation events (#739, #755, #757) with ``new_status: REJECTED`` and
no ``representative:`` field. Because ``_mim_merge_target`` in
``culturebotai-claw/scripts/build_unified_ingredient_mapping.py`` checks
``representative:`` first and otherwise walks ``curation_history`` backwards
stopping at the first ``new_status == "REJECTED"`` event, those non-merge
``REJECTED`` events hid the earlier ``MERGED_INTO`` event and caused 33 rows
(3,378 recipe occurrences) in ``UNIFIED_INGREDIENT_MAPPING.tsv`` to emit
``mapping_status=REJECTED`` with no downstream identity.

Before restoring tombstone resolution, wrong-form hydrate/salt/anion synonyms
still sitting on seven of those tombstones must be retyped to ``REJECTED_LABEL``
so restoring tombstone resolution does not collapse distinct hydrates or anions
onto the merge target:

* ``Cocl2_X_6_H2o`` (``CHEBI:53503``): ``CoCl2 x 2 H2O``, ``CoCl2 x 4 H2O``
  (already held on live ``Cocl2_X_2_H2o`` / ``Cocl2_X_4_H2o``);
* ``Na2moo42h2o`` (``CHEBI:75213``): ``Na2MoO4 . H2O``, ``Na2MoO4 · H2O``,
  ``Na2MoO4.H2O``, ``Na2MoO4xH2O`` (monohydrate labels on the dihydrate
  tombstone);
* ``Mgcl2x_6_H2o`` (``CHEBI:86345``): ``MgCl2  x 7 H2O``, ``MgCl2  x 76 H2O``,
  ``MgCl2 x 7 H2O``, ``MgCl2 x 7H2O``, ``MgCl2x7H2O`` (heptahydrate / typo
  hydrate labels on the hexahydrate tombstone; live ``Mgcl2_X_7_H2o`` holds
  the heptahydrate labels);
* ``Trisodium_Citrate_X_2_H2o`` (``CHEBI:32142``): ``Trisodium citrate·3H2O``
  (trihydrate label on the dihydrate tombstone);
* ``Calcium_Chloride`` (``CHEBI:3312``): ``CaCl22H2O`` (dihydrate ``CHEBI:86158``
  label on the anhydrous tombstone; live ``Cacl2_X_2_H2o`` holds ``CaCl22H2O``);
* ``Na-glutamate`` (``CHEBI:64243``): ``(2S)-2-aminopentanedioate``,
  ``L-glutamic acid dianion`` (``CHEBI:29988`` dianion names on the monosodium
  salt tombstone);
* ``Sodium_Citrate`` (``CHEBI:32142``): ``Na2citrate`` (two-sodium shorthand
  with different stoichiometry from the trisodium citrate dihydrate tombstone).

Dry-run by default; pass ``--apply`` to write records.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402

MAPPED_DIR = ROOT / "data" / "ingredients" / "mapped"
UNMAPPED_DIR = ROOT / "data" / "ingredients" / "unmapped"
ISSUE = "#882"
CURATOR = "claude"
LLM_MODEL = "claude-opus-4-6"


@dataclass(frozen=True)
class TombstoneFix:
    slug: str
    representative: str
    target_slug: str
    retired_tokens: tuple[str, ...]
    rationale: str
    added_synonyms: tuple[tuple[str, str, str], ...] = ()


@dataclass(frozen=True)
class UnmappedHydrateSpec:
    slug: str
    identifier: str
    preferred_term: str
    synonyms: tuple[tuple[str, str, str], ...]
    notes: str
    rationale: str


TARGETS: tuple[TombstoneFix, ...] = (
    TombstoneFix(
        slug="Cocl2_X_6_H2o",
        representative="CHEBI:53503",
        target_slug="Cobalt_chloride_hexahydrate",
        retired_tokens=("CoCl2 x 2 H2O", "CoCl2 x 4 H2O"),
        added_synonyms=(("CoCl2.6H2O", "HYDRATE_FORM", "kg_microbe"),),
        rationale=(
            "Set explicit representative CHEBI:53503 (Cobalt_chloride_hexahydrate) so the post-merge "
            "REJECTED_WRONG_FORM_SYNONYMS event (#232/#757) no longer blocks _mim_merge_target, "
            "retype dihydrate/tetrahydrate HYDRATE_FORM tokens to REJECTED_LABEL (already "
            "held on live Cocl2_X_2_H2o and Cocl2_X_4_H2o), and add CoCl2.6H2O as HYDRATE_FORM "
            "so recipes labeled CoCl2.6H2O with stale anhydrous term.id CHEBI:35696 resolve "
            "through label_index.csv to hexahydrate CHEBI:53503"
        ),
    ),
    TombstoneFix(
        slug="Na2moo42h2o",
        representative="CHEBI:75213",
        target_slug="Na2moo4_X_2_H2o",
        retired_tokens=("Na2MoO4 . H2O", "Na2MoO4 · H2O", "Na2MoO4.H2O", "Na2MoO4xH2O"),
        rationale=(
            "Set explicit representative CHEBI:75213 (Na2moo4_X_2_H2o) so the post-merge "
            "REJECTED_WRONG_FORM_SYNONYMS event (#232/#757) no longer blocks _mim_merge_target, "
            "and retype monohydrate HYDRATE_FORM tokens to REJECTED_LABEL so monohydrate "
            "labels do not collapse onto dihydrate CHEBI:75213"
        ),
    ),
    TombstoneFix(
        slug="Mgcl2x_6_H2o",
        representative="CHEBI:86345",
        target_slug="Mgcl2_X_6_H2o",
        retired_tokens=(
            "MgCl2  x 7 H2O",
            "MgCl2  x 76 H2O",
            "MgCl2 x 7 H2O",
            "MgCl2 x 7H2O",
            "MgCl2x7H2O",
        ),
        rationale=(
            "Set explicit representative CHEBI:86345 (Mgcl2_X_6_H2o) so the post-merge "
            "CORRECTED event (#312/#739) no longer blocks _mim_merge_target, and retype "
            "heptahydrate/typo HYDRATE_FORM tokens to REJECTED_LABEL (heptahydrate labels "
            "are held on live Mgcl2_X_7_H2o)"
        ),
    ),
    TombstoneFix(
        slug="Trisodium_Citrate_X_2_H2o",
        representative="CHEBI:32142",
        target_slug="Na3-citrate_X_2_H2o",
        retired_tokens=("Trisodium citrate·3H2O",),
        rationale=(
            "Set explicit representative CHEBI:32142 (Na3-citrate_X_2_H2o) so the post-merge "
            "REJECTED_WRONG_FORM_SYNONYMS event (#232/#757) no longer blocks _mim_merge_target, "
            "and retype trihydrate HYDRATE_FORM token to REJECTED_LABEL so it does not "
            "collapse onto dihydrate CHEBI:32142"
        ),
    ),
    TombstoneFix(
        slug="Calcium_Chloride",
        representative="CHEBI:3312",
        target_slug="Cacl2",
        retired_tokens=("CaCl22H2O",),
        rationale=(
            "Set explicit representative CHEBI:3312 (Cacl2) so the post-merge "
            "REJECTED_WRONG_FORM_SYNONYMS event (#232/#757) no longer blocks _mim_merge_target, "
            "and retype dihydrate HYDRATE_FORM token CaCl22H2O to REJECTED_LABEL (held on "
            "live Cacl2_X_2_H2o)"
        ),
    ),
    TombstoneFix(
        slug="Na-glutamate",
        representative="CHEBI:64243",
        target_slug="Sodium_L-glutamate",
        retired_tokens=("(2S)-2-aminopentanedioate", "L-glutamic acid dianion"),
        rationale=(
            "Set explicit representative CHEBI:64243 (Sodium_L-glutamate) so the post-merge "
            "REJECTED_WRONG_FORM_SYNONYMS event (#232/#757) no longer blocks _mim_merge_target, "
            "and retype L-glutamate(2-) CHEBI:29988 dianion EXACT_SYNONYM tokens to REJECTED_LABEL "
            "(https://www.ebi.ac.uk/chebi/CHEBI:29988)"
        ),
    ),
    TombstoneFix(
        slug="Sodium_Citrate",
        representative="CHEBI:32142",
        target_slug="Na3-citrate_X_2_H2o",
        retired_tokens=("Na2citrate",),
        rationale=(
            "Set explicit representative CHEBI:32142 (Na3-citrate_X_2_H2o) so the post-merge "
            "REJECTED_WRONG_FORM_SYNONYMS event (#232/#757) no longer blocks _mim_merge_target, "
            "and retype Na2citrate to REJECTED_LABEL because its two-sodium stoichiometry "
            "differs from the trisodium citrate dihydrate target"
        ),
    ),
    TombstoneFix(
        slug="Nah2po4h2o",
        representative="CHEBI:114249",
        target_slug="Sodium_phosphate_monobasic_monohydrate",
        retired_tokens=(),
        rationale=(
            "Set explicit representative CHEBI:114249 (Sodium_phosphate_monobasic_monohydrate) so the post-merge "
            "CORRECTED event (#312/#755) no longer blocks _mim_merge_target"
        ),
    ),
    TombstoneFix(
        slug="Cinnamic_Acid",
        representative="CHEBI:35697",
        target_slug="Trans-cinnamic_Acid",
        retired_tokens=(),
        rationale=(
            "Set explicit representative CHEBI:35697 (Trans-cinnamic_Acid) so the post-merge "
            "CORRECTED event (#312/#755) no longer blocks _mim_merge_target"
        ),
    ),
)

# 0819 and 0820 were retired by Hydroxystreptomycin and Isophthalate.
# The #1021 inventory includes ignored backups and Git history through 0850;
# these two new records must not reuse those historical identities.
UNMAPPED_HYDRATE_SPECS: tuple[UnmappedHydrateSpec, ...] = (
    UnmappedHydrateSpec(
        slug="Na2moo4_X_H2o",
        identifier="UNMAPPED_0851",
        preferred_term="Na2MoO4 x H2O",
        synonyms=(
            ("Na2MoO4 x H2O", "RAW_TEXT", "CultureMech"),
            ("Na2MoO4 . H2O", "HYDRATE_FORM", "kg_microbe"),
            ("Na2MoO4 · H2O", "HYDRATE_FORM", "kg_microbe"),
            ("Na2MoO4 × H2O", "HYDRATE_FORM", "kg_microbe"),
            ("Na2MoO4.H2O", "HYDRATE_FORM", "kg_microbe"),
            ("Na2MoO4xH2O", "HYDRATE_FORM", "kg_microbe"),
        ),
        notes=(
            "Sodium molybdate monohydrate surface forms split out from anhydrous Na2moo4 "
            "(CHEBI:75215) and dihydrate Na2moo42h2o / Na2moo4_X_2_H2o (CHEBI:75213) so "
            "recipes carrying stale anhydrous term.id CHEBI:75215 resolve to UNMAPPED "
            "rather than collapsing monohydrate onto anhydrous or dihydrate (#882)."
        ),
        rationale=(
            "Create unmapped sodium molybdate monohydrate record holding the 6 monohydrate "
            "surface forms retired from Na2moo4 and Na2moo42h2o so label_index.csv keeps "
            "them unmapped instead of falling back to stale anhydrous term.id CHEBI:75215"
        ),
    ),
    UnmappedHydrateSpec(
        slug="Trisodium_Citrate_X_3_H2o",
        identifier="UNMAPPED_0852",
        preferred_term="Trisodium citrate x 3 H2O",
        synonyms=(
            ("Trisodium citrate x 3 H2O", "RAW_TEXT", "CultureMech"),
            ("Trisodium citrate·3H2O", "HYDRATE_FORM", "kg_microbe"),
            ("Trisodium citrate・3H2O", "HYDRATE_FORM", "CultureMech"),
        ),
        notes=(
            "Trisodium citrate trihydrate surface forms split out from dihydrate "
            "Trisodium_Citrate_X_2_H2o / Na3-citrate_X_2_H2o (CHEBI:32142) so recipes "
            "carrying stale anhydrous term.id CHEBI:53258 resolve to UNMAPPED rather "
            "than collapsing trihydrate onto anhydrous or dihydrate (#882)."
        ),
        rationale=(
            "Create unmapped trisodium citrate trihydrate record holding the 3 trihydrate "
            "surface forms retired from Trisodium_Citrate_X_2_H2o so label_index.csv keeps "
            "them unmapped instead of falling back to stale anhydrous term.id CHEBI:53258"
        ),
    ),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write changes to disk")
    args = parser.parse_args(argv)

    updated = 0
    for spec in TARGETS:
        path = MAPPED_DIR / f"{spec.slug}.yaml"
        target_path = MAPPED_DIR / f"{spec.target_slug}.yaml"
        if not path.exists():
            raise SystemExit(f"Missing tombstone record: {path}")
        if not target_path.exists():
            raise SystemExit(f"Missing target record: {target_path}")

        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        target_record = yaml.safe_load(target_path.read_text(encoding="utf-8"))
        if record.get("mapping_status") != "REJECTED":
            raise SystemExit(f"{spec.slug}: expected REJECTED, got {record.get('mapping_status')}")
        if target_record.get("mapping_status") != "MAPPED":
            raise SystemExit(
                f"{spec.target_slug}: expected MAPPED target, got {target_record.get('mapping_status')}"
            )
        if target_record.get("identifier") != spec.representative:
            raise SystemExit(
                f"{spec.target_slug}: expected identifier {spec.representative}, "
                f"got {target_record.get('identifier')}"
            )

        changes_made: list[str] = []
        if record.get("representative") != spec.representative:
            record["representative"] = spec.representative
            changes_made.append(f"representative={spec.representative}")

        retired: list[str] = []
        for syn in record.get("synonyms") or []:
            text = syn.get("synonym_text")
            if text in spec.retired_tokens and syn.get("synonym_type") != "REJECTED_LABEL":
                retired.append(f"{text!r} ({syn.get('synonym_type')} -> REJECTED_LABEL)")
                syn["synonym_type"] = "REJECTED_LABEL"
        if retired:
            changes_made.append("retired wrong-form synonyms: " + ", ".join(retired))

        existing_syns = {
            (syn.get("synonym_text") or "").strip() for syn in (record.get("synonyms") or [])
        }
        added: list[str] = []
        for syn_text, syn_type, syn_source in spec.added_synonyms:
            if syn_text not in existing_syns:
                record.setdefault("synonyms", []).append(
                    {
                        "synonym_text": syn_text,
                        "synonym_type": syn_type,
                        "source": syn_source,
                    }
                )
                added.append(f"{syn_text!r} ({syn_type})")
        if added:
            changes_made.append("added synonyms: " + ", ".join(added))

        if not changes_made:
            print(f"SKIP   {spec.slug}: already repaired")
            continue

        # Preserve every prior repair event; a necessary later repair appends
        # its own evidence. The no-change branch above makes reruns idempotent.
        # Do NOT set new_status="REJECTED" on non-merge events (#882).
        record_curation_event(
            record,
            curator=CURATOR,
            action="REPAIRED_TOMBSTONE_RESOLUTION",
            changes=f"{spec.rationale} ({ISSUE}).",
            previous_status="REJECTED",
            new_status=None,
            llm_assisted=True,
            llm_model=LLM_MODEL,
        )
        print(f"REPAIR {spec.slug} -> {spec.representative} ({spec.target_slug}): {'; '.join(changes_made)}")
        if args.apply:
            write_validated_ingredient(record, path)
        updated += 1

    created = 0
    for hspec in UNMAPPED_HYDRATE_SPECS:
        upath = UNMAPPED_DIR / f"{hspec.slug}.yaml"
        if upath.exists():
            print(f"SKIP   unmapped/{hspec.slug}.yaml: already exists")
            continue
        urecord: dict = {
            "identifier": hspec.identifier,
            "preferred_term": hspec.preferred_term,
            "synonyms": [
                {"synonym_text": text, "synonym_type": stype, "source": ssource}
                for text, stype, ssource in hspec.synonyms
            ],
            "mapping_status": "UNMAPPED",
            "occurrence_statistics": {
                "total_occurrences": 0,
                "media_count": 0,
            },
            "curation_history": [],
            "notes": hspec.notes,
            "ingredient_type": "SINGLE_INGREDIENT",
        }
        record_curation_event(
            urecord,
            curator=CURATOR,
            action="CREATED_AS_UNMAPPED",
            changes=f"{hspec.rationale} ({ISSUE}).",
            previous_status=None,
            new_status="UNMAPPED",
            llm_assisted=True,
            llm_model=LLM_MODEL,
        )
        print(f"CREATE unmapped/{hspec.slug}.yaml ({hspec.identifier}: {hspec.preferred_term!r})")
        if args.apply:
            write_validated_ingredient(urecord, upath)
        created += 1

    print(
        f"\n{'Applied' if args.apply else 'Dry-run:'} "
        f"{updated} tombstone repair(s), {created} unmapped hydrate record(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
