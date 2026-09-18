# `data/ingredients/mapped/Capso.yaml`

## Verdict

Pass. The CultureMech record is exactly grounded to active `CHEBI:183882`
CAPSO, and its CAS, formula, InChI, SMILES, buffer role, occurrence count,
SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Capso.yaml`.
- Identifier and grounding: `identifier: CHEBI:183882`,
  `ontology_mapping.ontology_id: CHEBI:183882`,
  `ontology_label: 3-(cyclohexylamino)-2-hydroxy-1-propanesulfonic acid`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:183882` returns the active CAPSO chemical label,
  CAS `73463-39-5`, and formula `C9H19NO4S`.
- PubChem resolves CAS `73463-39-5` to CID `2733480` with formula
  `C9H19NO4S` and the same InChI/SMILES as the local `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Caprolactam.yaml data/ingredients/mapped/Caps_Buffer.yaml data/ingredients/mapped/Capsaicin.yaml data/ingredients/mapped/Capso.yaml data/ingredients/mapped/Carbenicillin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caprolactam.yaml data/ingredients/mapped/Caps_Buffer.yaml data/ingredients/mapped/Capsaicin.yaml data/ingredients/mapped/Capso.yaml data/ingredients/mapped/Carbenicillin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 files.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The current `mappings/culturemech_recipe_membership.tsv` rows contain three
  distinct recipes and three occurrences, matching `occurrence_statistics`.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Capso` SSSOM row with the
  curated ChEBI synonym plus `CAS:73463-39-5`, matching aggregate/docs rows.
- The `BUFFER` role was extracted from CultureMech's raw role text and is
  attached at 1.0 confidence with a `DATABASE_ENTRY` evidence object.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, synonyms,
  single-ingredient classification, buffer role, 3/3 occurrence count, SSSOM
  row, aggregate copy, and docs row are populated.
- Raw role text is retained in YAML for auditability but is not exported as an
  SSSOM synonym.

## Recommended Edits

- None for this record.
