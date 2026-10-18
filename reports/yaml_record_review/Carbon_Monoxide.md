# `data/ingredients/mapped/Carbon_Monoxide.yaml`

## Verdict

Pass. The MicrobeDecoder label is exactly grounded to active `CHEBI:17245`
carbon monoxide, and its formula, InChI, SMILES, occurrence count, SSSOM row,
and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Carbon_Monoxide.yaml`.
- Identifier and grounding: `identifier: CHEBI:17245`,
  `ontology_mapping.ontology_id: CHEBI:17245`,
  `ontology_label: carbon monoxide`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:17245` returns the active carbon monoxide term
  with formula `CO`, CAS `630-08-0`, InChI `InChI=1S/CO/c1-2`, and SMILES
  `[C-]#[O+]`.
- PubChem resolves CAS `630-08-0` to CID `281` with formula `CO`, molecular
  weight `28.010`, and the same InChI/SMILES as the local
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml data/ingredients/mapped/Carbomycin.yaml data/ingredients/mapped/Carbon_Monoxide.yaml data/ingredients/mapped/Carbon_Source_Solution.yaml data/ingredients/mapped/Carbon_dioxide_gas.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml data/ingredients/mapped/Carbomycin.yaml data/ingredients/mapped/Carbon_Monoxide.yaml data/ingredients/mapped/Carbon_Source_Solution.yaml data/ingredients/mapped/Carbon_dioxide_gas.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  validated `Carbenicillin_Disodium_Salt`, `Carbomycin`, and
  `Carbon_Monoxide`, then stopped on `Carbon_Source_Solution` because the
  local kgmicrobe adapter has no `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml data/ingredients/mapped/Carbomycin.yaml data/ingredients/mapped/Carbon_Monoxide.yaml data/ingredients/mapped/Carbon_dioxide_gas.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  review-report directories, found the active `MIM:Carbon_Monoxide` SSSOM row
  with the exact ChEBI target and matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain two
  distinct recipes and two occurrences, matching `occurrence_statistics`.
- The MicrobeDecoder import source is retained as
  `kgmicrobe.trait:carbon_monoxide`; no synonym, role, component, or
  environment claims are present.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, molecular weight, 2/2
  occurrence count, SSSOM row, aggregate copy, and docs row are populated.
- `cas_rn` is empty even though ChEBI has a carbon monoxide CAS xref, but this
  record was not created from a CAS source and does not need a CAS to support
  the exact OLS label mapping.

## Recommended Edits

- None for this record.
