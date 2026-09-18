# `data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml`

## Verdict

Needs curation; major issue. The CAS-derived ChEBI identity, disodium salt
specificity, CAS, formula, InChI, SMILES, synonym, SSSOM row, and aggregate
copy pass, but `SELECTIVE_AGENT` is still supported only by a provisional
name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:34609`,
  `ontology_mapping.ontology_id: CHEBI:34609`,
  `ontology_label: carbenicillin disodium`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:34609` returns the active ChEBI
  carbenicillin disodium term with CAS `4800-94-6`, generalized formula
  `C17H16N2O6S.2Na`, and the same InChI/SMILES as the local
  `chemical_properties`.
- PubChem resolves CAS `4800-94-6` to CID `20933`, formula
  `C17H16N2Na2O6S`, and the same InChI as the local record, confirming this is
  the disodium salt and not the parent `Carbenicillin` acid record reviewed
  separately.

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
  review-report directories, found the active
  `MIM:Carbenicillin_Disodium_Salt` SSSOM row with the ChEBI exact target,
  `CAS:4800-94-6`, and the same ChEBI IUPAC synonym as the YAML record,
  matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `CHEBI:34609`, matching `occurrence_statistics` `0/0`.
- The `SELECTIVE_AGENT` role has only `COMPUTATIONAL_PREDICTION` evidence with
  a curator note that explicitly labels it a provisional name-pattern rule.
  The record lacks antibiotic or selective-agent evidence inspected at the
  narrow role level.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, salt-specific
  identity, synonym, 0/0 CultureMech occurrence count, SSSOM row, aggregate
  copy, and docs row are populated.
- No independent source occurrence rows are required for this CultureBotHT
  FEBA/Hans80 panel compound record.

## Recommended Edits

- Major: either replace the provisional `physicochemical_roles.SELECTIVE_AGENT`
  evidence in `data/ingredients/mapped/Carbenicillin_Disodium_Salt.yaml` with
  inspected evidence for this disodium salt or remove the role, then rerun
  strict validation, SSSOM QC, aggregate roundtrip, and `git diff --check`.
