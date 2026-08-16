#!/usr/bin/env python3
"""Cover the CultureMech labels MIM cannot resolve (#260 follow-up).

`docs/data/label_index.csv` becomes CultureMech's grounding source under the #260
direction, so every label CultureMech uses that the index does not contain is a
lookup miss. 44 such labels were found. Most are notation damage on labels MIM
already has — subscript-stripped (`H BO` for H₃BO₃, `Na WO .2H O`) or misspelt
(`NaMoO4·2H2O`, `Distiled water`) — and those belong in a normalisation pass, not
here. This script handles the 16 that name something real.

**Nine are synonyms, not new records.** That is the finding that reshaped this
task. `L-glutathione reduced` is CHEBI:16856, which `Glutathione` already holds;
`Peptic digest of soybean meal` is the USP descriptor for soy peptone, which
`Soy peptone` holds; `RbCl` is `rubidium chloride`. In MIM the `identifier` IS
the ontology CURIE, so a second record on a held CURIE is a duplicate by
construction — the `Butane-1,4-diol` defect. Adding the surface form as a synonym
is what actually fixes the lookup: `export_lists` emits a `match_type=synonym`
row per synonym, so the label resolves without minting anything.

**CultureMech's own groundings are not used.** They were checked and three are
wrong in ways that would have propagated: `Sodium sulfide` → CHEBI:85357, an
unrelated organic acid; `DL-Tyrosine` and `DL-threonine` → the L-enantiomers,
dropping the racemate. Filed as CultureBotAI/CultureMech#276. Every term below
was resolved independently against OLS4 and checked against the corpus for an
existing holder first.

## New records (7)

    Neutral red                 CHEBI:86370   free
    Pyridoxine dihydrochloride  CHEBI:189426  free — a distinct ChEBI term from
                                              CHEBI:30961 pyridoxine hydrochloride
    DL-Tyrosine                 CHEBI:18186   tyrosine, stereo-unspecified
    Defibrinated sheep blood    MICRO:0001570 MICRO models this exactly
    Defibrinated horse blood    MICRO:0001572 likewise
    R2A agar                    MICRO:0000543 likewise
    Marine agar 2216            minted        MICRO has no 2216 term

`DL-Tyrosine` follows the corpus's own racemate precedent — 15 `DL-` records sit
on the stereo-unspecified ChEBI parent (`DL-aspartic acid`→CHEBI:22660,
`DL-methionine`→CHEBI:16811). It is graded CLOSE_MATCH rather than the EXACT the
precedent often uses: the label names a racemate and the term does not, so the
two are not the same thing, and `skos:closeMatch` says so.

`DL-threonine` would take CHEBI:26986 by the same rule, but `Threonine` already
holds it — so it is a synonym instead. Same reasoning, opposite outcome, decided
entirely by whether the CURIE was free.

`R2A agar` is a named medium and MICRO has the class, so `MAPPING_SEMANTICS` §3
**step 1** applies and it is grounded rather than minted — matching `Brucella
agar` (MICRO:0000595) and `Bacto Tryptic Soy Agar` (MICRO:0000114). The
CultureMech medium id is recorded as a cross-reference, not as the mapping.

`Marine agar 2216` has no ontology term at any granularity (MICRO has `ZoBell
marine agar` and `216L marine agar`, neither verified to be Difco 2216), so §3
**step 3** applies and it is minted under the #288 convention, cross-referenced
to `CultureMech:007629`. `Marine broth 2216` — already in the corpus as
UNMAPPED_0434 — is promoted the same way, because minting the agar and leaving
its broth twin unmapped would be an arbitrary split.

A CultureMech id cannot be the `identifier`: MIM's primary key is an ontology
CURIE or a registry mint, and `CultureMech:` is neither. It is carried as
evidence, which is where a cross-reference belongs.

## Synonyms onto existing records (9)

    Peptic digest of soybean meal        -> Soy peptone         FOODON:03315720
    Sodium sulfide                       -> Na2S                CHEBI:76208
    L-glutathione reduced                -> Glutathione         CHEBI:16856
    Acid hydrolysate of casein           -> Casein hydrolysate  MICRO:0001366
    RbCl                                 -> rubidium chloride   CHEBI:78672
    DL-threonine                         -> Threonine           CHEBI:26986
    Defibrinated rabbit blood            -> Rabbit blood        MICRO:0001229
    Natural seawater (filtered, 95% ...) -> Filtered Seawater   MICRO:0001773
    Whole eggs                           -> Whole egg           UNMAPPED_0577

The last one attaches to an UNMAPPED record and does not ground it — but
`label_index.csv` carries UNMAPPED rows too, and the contract already states that
a row is an answer about identity regardless of status. Resolving `Whole eggs`
and `Whole egg` to the same record is the useful part.

`Defibrinated rabbit blood` is a synonym rather than a record because MICRO has
`defibrinated sheep blood` and `defibrinated horse blood` but no rabbit
equivalent, and `Rabbit blood` already holds MICRO:0001229.

**Occurrences are not imported.** MIM's counts are over MIM's own ingest;
CultureMech's counts are over its corpus. Copying them would double-count.

    python scripts/add_culturemech_gap_labels.py            # dry-run
    python scripts/add_culturemech_gap_labels.py --apply
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
from export_individual_records import (  # noqa: E402
    collect_existing_filenames, sanitize_filename,
)
from promote_resolved_unmapped import (  # noqa: E402
    CONFIDENCE, OBJECT_SOURCE, PREDICATE, REGISTRY_SOURCE, is_registry_mint,
)

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
DATE = "2026-08-15"
STAMP = f"{DATE}T00:00:00+00:00"
CURATOR = "add_culturemech_gap_labels"
ISSUE = "#260"

# `promote_resolved_unmapped.OBJECT_SOURCE` has no MICRO entry, so a MICRO
# promotion through that path emits an empty object_source. Every MICRO row
# already in the SSSOM file uses `obo:micro.owl`; filed separately rather than
# edited here, and overridden locally so these rows are correct.
SOURCE = {**OBJECT_SOURCE, "MICRO": "obo:micro.owl"}

# `ingredient_type` is set explicitly on every record written here. Leaving it
# unset was a review finding: `auto_classify_ingredient_type` only runs when
# someone invokes it, so an unset value is not "pending", it is missing. The
# values follow the corpus's own convention rather than the label's grammar —
# `Rabbit blood`, `Horse serum` and `Filtered Seawater` are all UNDEFINED_MIXTURE
# because a biological preparation has no defined composition, and `Brucella
# agar` / `Bacto Tryptic Soy Agar` are UNDEFINED_MIXTURE because a compounded
# medium built on peptone and yeast extract does not have one either.
#
# label -> (term, ontology_label, source, quality, ingredient_type, why)
NEW = {
    "Neutral red": (
        "CHEBI:86370", "neutral red", "CHEBI", "EXACT_MATCH", "SINGLE_INGREDIENT",
        "the phenazine pH-indicator dye used in MacConkey-type and clostridial "
        "media. ChEBI names it exactly and no MIM record holds the term. "
        "CHEBI:86372 'neutral red base' and CHEBI:86373 'neutral red(1+)' are the "
        "free base and cation; media recipes weigh out the dye itself"),
    "Pyridoxine dihydrochloride": (
        "CHEBI:189426", "Pyridoxine dihydrochloride", "CHEBI", "EXACT_MATCH", "SINGLE_INGREDIENT",
        "a distinct ChEBI term from CHEBI:30961 'pyridoxine hydrochloride', which "
        "`Pyridoxine hydrochloride` already holds (1942 occurrences). The two are "
        "different salts of the same vitamer, so folding this label onto the "
        "mono-hydrochloride record would assert a stoichiometry the label denies"),
    "DL-Tyrosine": (
        "CHEBI:18186", "tyrosine", "CHEBI", "CLOSE_MATCH", "SINGLE_INGREDIENT",
        "ChEBI has no racemic tyrosine term — a search returns only derivatives "
        "(DL-tyrosine betaine, racemetirosine) — so the stereo-unspecified parent "
        "is the closest available, which is what the corpus's other 15 `DL-` "
        "records do (DL-aspartic acid->CHEBI:22660, DL-methionine->CHEBI:16811). "
        "Graded CLOSE_MATCH, not the EXACT those often use: the label names a "
        "racemate and the term does not distinguish stereochemistry at all, so "
        "skos:closeMatch is the honest predicate. NOT CHEBI:17895 L-tyrosine, "
        "which is what CultureMech asserts (CultureMech#276) — that silently "
        "discards the D-enantiomer"),
    "Defibrinated sheep blood": (
        "MICRO:0001570", "defibrinated sheep blood", "MICRO", "EXACT_MATCH", "UNDEFINED_MIXTURE",
        "MICRO models the defibrinated preparation as its own class, separate "
        "from MICRO:0001230 'sheep blood'. Defibrination removes fibrin so the "
        "blood stays liquid in agar, so the preparation is the thing weighed out "
        "and the specific term is right under MAPPING_SEMANTICS §3 step 1"),
    "Defibrinated horse blood": (
        "MICRO:0001572", "defibrinated horse blood", "MICRO", "EXACT_MATCH", "UNDEFINED_MIXTURE",
        "as for sheep — MICRO has the defibrinated class distinct from "
        "MICRO:0001234 'horse blood'"),
    "R2A agar": (
        "MICRO:0000543", "R2A agar", "MICRO", "EXACT_MATCH", "UNDEFINED_MIXTURE",
        "Reasoner & Geldreich's low-nutrient agar for heterotrophic plate counts. "
        "A named medium, but MICRO has the class, so §3 step 1 grounds it rather "
        "than minting — matching `Brucella agar` (MICRO:0000595) and `Bacto "
        "Tryptic Soy Agar` (MICRO:0000114). MICRO:0000541 'R2A medium' is the "
        "broth; this label says agar. Cross-reference: CultureMech:002706 "
        "(data/normalized_yaml/bacterial/r2a_agar.yaml)"),
}

# label -> (mint, culturemech_id, why); minted because no ontology term exists
MINT = {
    "Marine agar 2216": (
        "kgmicrobe.ingredient:marine_agar_2216", "CultureMech:007629",
        "Difco/BD Marine Agar 2216, ZoBell's seawater formulation. MICRO has "
        "`ZoBell marine agar` (MICRO:0000112) and `216L marine agar` "
        "(MICRO:0000064), but neither is verified to be the 2216 formulation and "
        "grounding to a maybe-equivalent named medium is how wrong identities "
        "enter. No ChEBI/FOODON term covers a compounded medium either, so §3 "
        "step 3 mints it under the #288 convention, as `Trace element solution "
        "see Medium No. 187` already is"),
    "Marine broth 2216": (
        "kgmicrobe.ingredient:marine_broth_2216", "CultureMech:008094",
        "the broth twin of Marine Agar 2216, already in the corpus as an UNMAPPED "
        "record. Minted alongside its agar rather than left unmapped: the two "
        "differ only by the gelling agent, and splitting them would be arbitrary"),
}

# surface form -> (holder preferred_term, expected CURIE, synonym_type, why)
SYNONYM = {
    "Peptic digest of soybean meal": (
        "Soy peptone", "FOODON:03315720", "EXACT_SYNONYM",
        "the USP/compendial descriptor for soy peptone — the same product the "
        "record already lists as `Soybean peptone`, `Peptone from soymeal`, "
        "`Soytone` and `Phytone peptone`. Names the manufacturing process rather "
        "than a different substance"),
    "Sodium sulfide": (
        "Na2S", "CHEBI:76208", "EXACT_SYNONYM",
        "the systematic name of the formula this record already carries; the "
        "record's own synonym list has `disodium sulfide` and `sodium sulphide`. "
        "NOT CHEBI:85357, which CultureMech asserts (CultureMech#276) — that term "
        "is 3-[(1E,4R)-4-hydroxycyclohex-2-en-1-ylidene]pyruvic acid, an organic "
        "acid with no sodium and no sulfur"),
    "L-glutathione reduced": (
        "Glutathione", "CHEBI:16856", "EXACT_SYNONYM",
        "CHEBI:16856 'glutathione' IS the reduced form (GSH) — the record already "
        "lists `Reduced glutathione` and `GSH`, and the oxidised form is a "
        "separate record on CHEBI:17858. The `L-` and `reduced` qualifiers add "
        "nothing the term does not already fix"),
    "Acid hydrolysate of casein": (
        "Casein hydrolysate", "MICRO:0001366", "EXACT_SYNONYM",
        "names the hydrolysis route to the same product. Acid hydrolysis destroys "
        "tryptophan where enzymatic does not, but MICRO has one casein-hydrolysate "
        "class and no acid/enzymatic split, so this is a surface variant of it"),
    "RbCl": (
        "rubidium chloride", "CHEBI:78672", "ABBREVIATION",
        "the molecular formula as a surface form. The corpus routinely carries "
        "both (`Na2S`/`sodium sulfide`, `Na2SO4`/`sodium sulfate`)"),
    "DL-threonine": (
        "Threonine", "CHEBI:26986", "RELATED_SYNONYM",
        "the racemate under the stereo-unspecified parent — the same treatment "
        "`DL-Tyrosine` gets in this batch, except that CHEBI:26986 is already held "
        "by this record, so it is a synonym rather than a new one. RELATED rather "
        "than EXACT because the racemate is narrower than the parent. NOT "
        "CHEBI:16857 L-threonine, which CultureMech asserts (CultureMech#276)"),
    "Defibrinated rabbit blood": (
        "Rabbit blood", "MICRO:0001229", "RELATED_SYNONYM",
        "MICRO has `defibrinated sheep blood` and `defibrinated horse blood` as "
        "classes but no rabbit equivalent, and MICRO:0001229 `rabbit blood` is "
        "already held here. So unlike its sheep and horse siblings this one cannot "
        "become a record — the granularity available in the ontology decides"),
    "Natural seawater (filtered, 95% strength)": (
        "Filtered Seawater", "MICRO:0001773", "RELATED_SYNONYM",
        "the filtered-seawater term with a dilution stated. `95% strength` is a "
        "preparation detail belonging to the recipe, not a different substance, "
        "and no ontology distinguishes seawater by dilution"),
    "Whole eggs": (
        "Whole egg", "UNMAPPED_0577", "ALTERNATE_FORM",
        "a plural of the record's own label. This does not ground the record — it "
        "stays UNMAPPED — but label_index carries UNMAPPED rows, so both surface "
        "forms now resolve to the same record instead of one of them missing"),
}


def evidence(note: str) -> dict:
    return {"evidence_type": "MANUAL_CURATION",
            "source": f"MIM curation ({ISSUE})", "notes": note}


def history(action: str, changes: str, **extra) -> dict:
    return {"timestamp": STAMP, "curator": CURATOR, "action": action,
            "changes": changes, "llm_assisted": False, **extra}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    mapped = yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
    unmapped = yaml.safe_load(UNMAPPED.read_text(encoding="utf-8")) or {}
    all_recs = (mapped.get("ingredients") or []) + (unmapped.get("ingredients") or [])
    by_label = {}
    for r in all_recs:
        by_label.setdefault(str(r.get("preferred_term") or ""), r)
    taken = {str(r.get("identifier")) for r in all_recs}
    index = collect_existing_filenames(ROOT / "data" / "ingredients")

    created, minted, syns, skipped = [], [], [], []
    new_records: list[dict] = []
    rows: list[str] = []

    def sssom_row(slug: str, label: str, term: str, term_label: str,
                  source: str, grade: str) -> None:
        rows.append("\t".join([
            f"MIM:{slug}", label, PREDICATE[grade], term, term_label, source,
            "semapv:ManualMappingCuration",
            f"MIM:curation ({ISSUE})|MIM:curator={CURATOR}", DATE,
            CONFIDENCE[grade], "", "", f"manual:{CURATOR}|{DATE}"]) + "\n")

    # ---- new records on ontology terms -------------------------------------
    for label, (term, term_label, src, grade, itype, why) in NEW.items():
        if label in by_label:
            skipped.append(f"{label}: a record already carries this label")
            continue
        if term in taken:
            # The Butane-1,4-diol defect: identifier IS the CURIE, so this would
            # be a duplicate primary key, not a new mapping.
            holder = next(r for r in all_recs if str(r.get("identifier")) == term)
            skipped.append(f"{label}: {term} already held by "
                           f"{holder.get('preferred_term')!r} — would duplicate")
            continue
        note = f"Created to cover a CultureMech label MIM could not resolve ({ISSUE}): {why}."
        rec = {
            "identifier": term,
            "preferred_term": label,
            "ontology_mapping": {
                "ontology_id": term, "ontology_label": term_label,
                "ontology_source": src, "mapping_quality": grade,
                "evidence": [evidence(note)]},
            "synonyms": [],
            "mapping_status": "MAPPED",
            "ingredient_type": itype,
            "occurrence_statistics": {"total_occurrences": 0, "media_count": 0},
            "curation_history": [history(
                "CREATED_FROM_CULTUREMECH_GAP", note, new_status="MAPPED")],
        }
        new_records.append(rec)
        taken.add(term)
        sssom_row(sanitize_filename(label), label, term, term_label,
                  SOURCE.get(src, ""), grade)
        created.append(f"{label[:34]:<36} {term:<16} {term_label[:28]:<30} {grade}")

    # ---- mints (no ontology term at any granularity) ------------------------
    for label, (mint, cm_id, why) in MINT.items():
        note = (f"Minted under the #288 named-preparation convention ({ISSUE}): {why}. "
                f"Cross-reference: {cm_id}. A CultureMech id cannot be the identifier "
                f"— MIM's primary key is an ontology CURIE or a registry mint — so it "
                f"is carried here as evidence.")
        rec = by_label.get(label)
        if rec is None:
            rec = {
                "identifier": mint, "preferred_term": label,
                "ontology_mapping": {}, "synonyms": [],
                "mapping_status": "MAPPED",
                "occurrence_statistics": {"total_occurrences": 0, "media_count": 0},
                "curation_history": [],
            }
            new_records.append(rec)
            action, prev = "CREATED_FROM_CULTUREMECH_GAP", None
        elif rec.get("mapping_status") == "UNMAPPED":
            action, prev = "PROMOTED_TO_MAPPED", "UNMAPPED"
        else:
            skipped.append(f"{label}: already {rec.get('mapping_status')}")
            continue
        if mint in taken and rec.get("identifier") != mint:
            skipped.append(f"{label}: {mint} already held")
            continue
        old = rec.get("identifier")
        rec["identifier"] = mint
        rec["mapping_status"] = "MAPPED"
        # UNDEFINED_MIXTURE, not DEFINED_MEDIUM: Marine 2216 is built on peptone
        # and yeast extract, so its composition is not defined however precisely
        # the recipe is published. Matches `Brucella agar` and `Bacto Tryptic Soy
        # Agar`; DEFINED_MEDIUM in the corpus is reserved for media that really
        # are chemically defined.
        rec["ingredient_type"] = "UNDEFINED_MIXTURE"
        rec["ontology_mapping"] = {
            "ontology_id": mint, "ontology_label": label,
            "ontology_source": "kgmicrobe.ingredient",
            "mapping_quality": "FALLBACK_REGISTRY",
            "evidence": [evidence(note)]}
        rec.setdefault("curation_history", []).append(
            history(action, f"{old} -> {mint} (FALLBACK_REGISTRY). {note}",
                    **({"previous_status": prev, "new_status": "MAPPED"} if prev else
                       {"new_status": "MAPPED"})))
        taken.add(mint)
        slug = index.for_record(rec) or sanitize_filename(label)
        # FALLBACK_REGISTRY -> skos:closeMatch against its own mint. That single
        # self-referential row IS the registry row; Rule B1 fires only on
        # narrowMatch, so no sibling exactMatch is wanted.
        sssom_row(slug, label, mint, label,
                  REGISTRY_SOURCE["kgmicrobe.ingredient"], "FALLBACK_REGISTRY")
        minted.append(f"{label[:34]:<36} {mint:<44} xref {cm_id}")

    # ---- synonyms onto existing records ------------------------------------
    for surface, (holder_label, expect, syn_type, why) in SYNONYM.items():
        rec = by_label.get(holder_label)
        if rec is None:
            skipped.append(f"{surface}: holder {holder_label!r} not found")
            continue
        if str(rec.get("identifier")) != expect:
            skipped.append(f"{surface}: {holder_label!r} is on "
                           f"{rec.get('identifier')}, expected {expect}")
            continue
        existing = {str(s.get("synonym_text", "")).lower()
                    for s in (rec.get("synonyms") or [])}
        if surface.lower() in existing:
            skipped.append(f"{surface}: already a synonym of {holder_label!r}")
            continue
        rec.setdefault("synonyms", []).append({
            "synonym_text": surface, "synonym_type": syn_type,
            "source": f"CultureMech label unresolvable via label_index ({ISSUE})"})
        note = (f"Added {surface!r} as a {syn_type} ({ISSUE}): {why}. CultureMech uses "
                f"this surface form and label_index did not contain it, so the lookup "
                f"missed. No new record: {expect} is this record's identifier, and in "
                f"MIM the identifier IS the ontology CURIE, so a second record on it "
                f"would be a duplicate primary key rather than added coverage.")
        rec.setdefault("curation_history", []).append(
            history("ADDED_SYNONYM_FOR_CULTUREMECH_GAP", note))
        om = rec.get("ontology_mapping")
        if om:
            om.setdefault("evidence", []).append(evidence(note))
        syns.append(f"{surface[:42]:<44} -> {holder_label[:24]:<26} {expect}")

    if args.apply and (created or minted or syns):
        # New MAPPED records go into mapped_ingredients.yaml, and a promoted
        # record MOVES there. reconcile_sssom reads only that file, so anything
        # MAPPED left in the unmapped collection is curated but unpublished —
        # the #370 defect.
        for rec in new_records:
            mapped["ingredients"].insert(0, rec)
        um = unmapped.get("ingredients") or []
        movers = [r for r in um if r.get("mapping_status") == "MAPPED"]
        if movers:
            unmapped["ingredients"] = [r for r in um if r not in movers]
            mapped["ingredients"] = movers + mapped["ingredients"]
            print(f"  moved {len(movers)} promoted record(s) to mapped_ingredients.yaml (#370)")
        for coll, path in ((mapped, MAPPED), (unmapped, UNMAPPED)):
            recs = coll.get("ingredients") or []
            coll["total_count"] = len(recs)
            coll["mapped_count"] = sum(1 for r in recs if r.get("mapping_status") == "MAPPED")
            coll["unmapped_count"] = sum(1 for r in recs if r.get("mapping_status") == "UNMAPPED")
            save_yaml(coll, path)

        lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
        hdr = next(i for i, l in enumerate(lines) if l.startswith("subject_id"))
        ncols = len(lines[hdr].rstrip("\n").split("\t"))
        padded = []
        for r in rows:
            cells = r.rstrip("\n").split("\t")[:ncols]
            padded.append("\t".join(cells + [""] * (ncols - len(cells))) + "\n")
        lines[hdr + 1:hdr + 1] = padded
        SSSOM.write_text("".join(lines), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(created)} created, {len(minted)} minted, {len(syns)} synonym(s), "
          f"{len(rows)} SSSOM row(s)\n")
    print(f"  new records on ontology terms ({len(created)}):")
    for c in created:
        print(f"     {c}")
    print(f"\n  minted, no ontology term available ({len(minted)}):")
    for m in minted:
        print(f"     {m}")
    print(f"\n  synonyms onto records that already hold the term ({len(syns)}):")
    for s in syns:
        print(f"     {s}")
    for s in skipped:
        print(f"  SKIPPED {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
