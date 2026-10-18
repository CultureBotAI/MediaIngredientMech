# `data/ingredients/mapped/Cinerubin_R.yaml`

## Verdict

Pass. The MicrobeDecoder cinerubin R import is exactly grounded to active
`CHEBI:214436`; its formula, InChI, SMILES, MicrobeDecoder source occurrence,
SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cinerubin_R.yaml`.
- Identifier and grounding: `identifier: CHEBI:214436`,
  `ontology_mapping.ontology_id: CHEBI:214436`,
  `ontology_label: Cinerubin R`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS search returns active `CHEBI:214436` labelled `Cinerubin R`; sibling
  hits `Cinerubin B` and `Cinerubin Y` are distinct variants.
- PubChem lookup by `Cinerubin R` returns formula `C42H51NO15` and the same
  standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cimicifugoside_H1.yaml data/ingredients/mapped/Cinerubin_A.yaml data/ingredients/mapped/Cinerubin_R.yaml data/ingredients/mapped/Cinnamic_Acid.yaml data/ingredients/mapped/Cinnamycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cinerubin_R.yaml data/ingredients/mapped/Cinnamic_Acid.yaml data/ingredients/mapped/Cinnamycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three CHEBI-scoped records in this batch.
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
  `reports` found the active exact `MIM:Cinerubin_R` SSSOM row, the
  MicrobeDecoder import-review approval, and matching aggregate/docs rows.
- Hidden/ignored-inclusive search of `data/custom/microbedecoder` found
  `kgmicrobe.trait:cinerubin_r` in `BacDive_Metabolite_production` with count
  1, matching the explicit `source_occurrences` entry.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:214436` rows,
  matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, source occurrence, SSSOM
  row, aggregate copy, and docs row are populated and agree.

## Recommended Edits

- None for this record.
