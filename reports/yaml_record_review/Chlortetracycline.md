# `data/ingredients/mapped/Chlortetracycline.yaml`

## Verdict

Pass. The MicrobeDecoder chlortetracycline import is exactly grounded to active
`CHEBI:27644`, and its formula, InChI, SMILES, absorbed raw spelling,
MicrobeDecoder source occurrence, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Chlortetracycline.yaml`.
- Identifier and grounding: `identifier: CHEBI:27644`,
  `ontology_mapping.ontology_id: CHEBI:27644`,
  `ontology_label: chlortetracycline`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct ChEBI and exact OLS lookups for `CHEBI:27644` return one active term
  labelled `chlortetracycline`. ChEBI publishes formula `C22H23ClN2O8`, mass
  `478.885`, and the same SMILES and standard InChI stored in
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chloridazon.yaml data/ingredients/mapped/Chlorogenic_Acid.yaml data/ingredients/mapped/Chlororaphin.yaml data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml data/ingredients/mapped/Chlortetracycline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chloridazon.yaml data/ingredients/mapped/Chlorogenic_Acid.yaml data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml data/ingredients/mapped/Chlortetracycline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 4 CHEBI-grounded records in this batch. `Chlororaphin` was
  intentionally skipped because its `kgmicrobe.compound` placeholder CURIE is a
  local registry ID outside Engine A's OBO prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Chlortetracycline` SSSOM row, the
  MicrobeDecoder import-review approval, and matching aggregate and docs rows
  for `CHEBI:27644`.
- Hidden/ignored-inclusive search of `data/custom/microbedecoder` found
  `kgmicrobe.trait:chlortetracycline` in `BacDive_Metabolite_production` with
  count 1, matching the explicit `source_occurrences` entry.
- Hidden/ignored-inclusive search also found the absorbed raw
  `kgmicrobe.trait:chlortetracyclin` label in
  `BacDive_Antibiotic_resistance|BacDive_Antibiotic_sensitivity` with count
  13, matching the curation history entry that merged `UNMAPPED_0664` as a
  `RAW_TEXT` synonym for the same antibiotic.
- Hidden/ignored-inclusive search of `mappings/culturemech_recipe_membership.tsv`
  plus `data` found no CultureMech membership rows for `CHEBI:27644`, matching
  the explicit 0/0 media-recipe `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, source occurrence,
  absorbed raw spelling, SSSOM row, aggregate copy, and docs row are populated
  and agree.

## Recommended Edits

- None for this record.
