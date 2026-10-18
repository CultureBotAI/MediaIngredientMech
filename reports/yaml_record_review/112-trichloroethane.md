# `data/ingredients/mapped/112-trichloroethane.yaml`

## Verdict

Needs curation. The exact `CHEBI:36018` identity and CAS/formula/InChI/SMILES
fields are sound, but the record has an unattached `kgscan` discussion that is
not a concrete 1,1,2-trichloroethane curation gap.

## Identity

- Reviewed record: `data/ingredients/mapped/112-trichloroethane.yaml`.
- Identifier and grounding: `identifier: CHEBI:36018` with
  `ontology_mapping.ontology_id: CHEBI:36018`, label
  `1,1,2-trichloroethane`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:36018`
  resolves to `1,1,2-trichloroethane`, formula `C2H3Cl3`, SMILES
  `ClCC(Cl)Cl`, the same InChI stored in `chemical_properties`, and CAS RN
  `79-00-5`.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/112-trichloroethane.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/112-trichloroethane.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/11-Biphenyl-2-ol.yaml data/ingredients/mapped/112-trichloroethane.yaml data/ingredients/mapped/1122-Tetrachloroethane.yaml data/ingredients/mapped/12-Propanediol.yaml data/ingredients/mapped/12-dichloropropane.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  matched after excluding the per-record-only `discussions` overlay.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `CHEBI:36018` row with CAS `79-00-5` and the raw absorbed
  `2-trichloroethane` label in `other_label`.

## Evidence

- Current ChEBI verifies the CAS-backed exact identity and stored structure.
- The absorbed `2-trichloroethane` surface is correctly marked `RAW_TEXT`, not
  an exact synonym, so the dropped-locant artifact is preserved only for source
  resolution.
- Minor: `kgscan-47348d9115e1` is an unattached broad literature-gap bundle.
  Its organohalide-respiration and dechlorination sentences are not tied to a
  specific unresolved mapping, synonym, role, or occurrence question here, and
  one cited snippet is unrelated neuropeptide/bioinsecticide context.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the active YAML/aggregate/SSSOM/docs rows,
  expected row-review TSVs, and no duplicate active YAML for `CHEBI:36018`.

## Completeness

- Empty component and role slots are acceptable for this single ChEBI chemical.
- CAS RN, formula, SMILES, and InChI are populated and match current ChEBI.

## Recommended Edits

1. Remove or replace `kgscan-47348d9115e1` with a claim-attached,
   1,1,2-trichloroethane-specific discussion if an actual unresolved gap
   remains.
2. No ChEBI, CAS RN, structure, SSSOM, aggregate, or docs edit is needed for the
   active identity.
