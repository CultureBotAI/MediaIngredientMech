# `data/ingredients/mapped/Carbon_dioxide_gas.yaml`

## Verdict

Pass. The manually curated gas label is grounded to active `CHEBI:16526`
carbon dioxide, and its synonyms, formula, InChI, SMILES, occurrence count,
SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Carbon_dioxide_gas.yaml`.
- Identifier and grounding: `identifier: CHEBI:16526`,
  `ontology_mapping.ontology_id: CHEBI:16526`,
  `ontology_label: carbon dioxide`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:16526` returns the active carbon dioxide term
  with CAS `124-38-9`, formula `CO2`, InChI `InChI=1S/CO2/c2-1-3`, and SMILES
  `O=C=O`.
- PubChem resolves CAS `124-38-9` to CID `280` with formula `CO2`, the same
  InChI, and an equivalent linear carbon dioxide SMILES string.

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
  review-report directories, found the active `MIM:Carbon_dioxide_gas` SSSOM
  row with the enriched ChEBI synonyms plus matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain 771
  distinct recipes summing to 775 occurrences, matching
  `occurrence_statistics`.
- The manual `CO2`, `carbon dioxide`, and `Carbon dioxide` aliases name the
  same ChEBI molecule, and OLS confirms the kg-microbe-enriched `CO(2)`,
  `E 290`, `E-290`, `E290`, `R-744`, `[CO2]`, `carbonic anhydride`,
  `dioxidocarbon`, and `methanedione` labels on `CHEBI:16526`.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, synonym set, 775/771
  occurrence count, SSSOM row, aggregate copy, and docs row are populated.
- The record has no role or component assertions requiring extra evidence.

## Recommended Edits

- None for this record.
