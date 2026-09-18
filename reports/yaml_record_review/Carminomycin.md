# `data/ingredients/mapped/Carminomycin.yaml`

## Verdict

Pass. The MicrobeDecoder label is exactly grounded to active `CHEBI:31359`
carminomycin, and its formula, InChI, SMILES, occurrence metadata, SSSOM row,
and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Carminomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:31359`,
  `ontology_mapping.ontology_id: CHEBI:31359`,
  `ontology_label: carminomycin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:31359` returns the active carminomycin term with
  formula `C26H27NO10`, CAS `39472-31-6`, and the same InChI/SMILES as the
  local `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carcinomycin.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carcinomycin.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  validated `Carboxymethyl_Cellulose`, then stopped on `Carcinomycin` because
  the local kgmicrobe adapter has no `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Carminomycin` SSSOM row
  with the exact ChEBI target and matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `CHEBI:31359`, matching `occurrence_statistics` `0/0`.
- The MicrobeDecoder import source is retained as
  `kgmicrobe.trait:carminomycin`; no synonym, role, component, or environment
  claims are present.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, molecular weight,
  MicrobeDecoder source occurrence, SSSOM row, aggregate copy, and docs row are
  populated.
- `cas_rn` is empty even though ChEBI has a carminomycin CAS xref, but this
  record was not created from a CAS source and does not need a CAS to support
  the exact OLS label mapping.

## Recommended Edits

- None for this record.
