# `data/ingredients/mapped/Choline_Chloride.yaml`

## Verdict

Pass. The CultureMech choline chloride import is exactly grounded to active
`CHEBI:133341`; its CAS, InChI, SMILES, reviewed exact synonyms, 48/48
CultureMech occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Choline_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:133341`,
  `ontology_mapping.ontology_id: CHEBI:133341`,
  `ontology_label: choline chloride`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct exact OLS lookup for `choline chloride` returns active
  `CHEBI:133341` labelled `choline chloride`, with the record's 19
  `kg_microbe` exact synonyms on the OLS related-synonym surface.
- PubChem lookup of CAS `67-48-1` resolves to CID `6209` with the same standard
  InChI and SMILES stored in `chemical_properties`; PubChem flattens the same
  salt to formula `C5H14ClNO` while the YAML retains ChEBI's dotted
  `C5H14NO.Cl` notation.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Choline_Chloride.yaml data/ingredients/mapped/Cholinium_Dihydrogen_Phosphate.yaml data/ingredients/mapped/Cholinium_Lysinate.yaml data/ingredients/mapped/Chondroitin_Sulfate_A_Sodium_Salt_From_Bovine_Trachea.yaml data/ingredients/mapped/Chromium_Iii_Chloride_Hexahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Choline_Chloride.yaml data/ingredients/mapped/Chondroitin_Sulfate_A_Sodium_Salt_From_Bovine_Trachea.yaml data/ingredients/mapped/Chromium_Iii_Chloride_Hexahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three CHEBI-scoped records in this narrowed run.
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
  `reports` found the active exact `MIM:Choline_Chloride` SSSOM row, OAK/OLS
  row-review confirmation, matching aggregate/docs rows, and no QC report entry
  that flags this record.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found exactly 48
  `CHEBI:133341` recipe rows, matching the refreshed 48/48 occurrence
  statistics.
- The SSSOM `other` column exports all 19 exact synonyms plus `CAS:67-48-1`.
  It correctly omits the raw `Role: Growth factor; Properties: ...`
  CultureMech note because `synonym_policy.py` filters those source notes from
  the resolving synonym surface.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS, InChI, SMILES, exact synonyms, occurrence
  count, SSSOM row, aggregate copy, and docs row are populated and agree.

## Recommended Edits

- None for this record.
