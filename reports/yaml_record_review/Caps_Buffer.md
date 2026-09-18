# `data/ingredients/mapped/Caps_Buffer.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:191088` CAPS buffer identity, CAS,
structure fields, synonyms, occurrence count, SSSOM row, and aggregate copy
pass, but the `BUFFER` role still uses provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Caps_Buffer.yaml`.
- Identifier and grounding: `identifier: CHEBI:191088`,
  `ontology_mapping.ontology_id: CHEBI:191088`,
  `ontology_label: Cyclohexylaminopropanesulfonic acid`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:191088` returns active label
  `Cyclohexylaminopropanesulfonic acid`, CAS `1135-40-6`, and formula
  `C9H19NO3S`.
- PubChem resolves CAS `1135-40-6` to CID `70815` with formula `C9H19NO3S` and
  the same InChI/SMILES as the local `chemical_properties`.

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

- The current `mappings/culturemech_recipe_membership.tsv` rows contain five
  distinct recipes and five occurrences, matching `occurrence_statistics`.
- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Caps_Buffer` SSSOM row with
  the curated ChEBI synonyms plus `CAS:1135-40-6`, matching aggregate/docs rows.
- The `BUFFER` role is plausible for a CultureMech `CAPS buffer` label, but
  its evidence is still `COMPUTATIONAL_PREDICTION` from a curated name-pattern
  rule and says review is recommended.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, synonyms,
  single-ingredient classification, 5/5 occurrence count, SSSOM row, aggregate
  copy, and docs row are populated.
- No raw CultureMech role/property text is exported as an SSSOM synonym.

## Recommended Edits

- In `data/ingredients/mapped/Caps_Buffer.yaml`, replace the provisional
  `BUFFER` role evidence with claim-level evidence from the CultureMech source
  label or remove the role until source-backed evidence is available.
- Regenerate `data/curated/mapped_ingredients.yaml`, docs data, and any role
  exports that consume the aggregate; prove the cleanup with strict validation
  and round-trip verification.
