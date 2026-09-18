# `data/ingredients/mapped/Choline.yaml`

## Verdict

Pass. The CultureMech choline import is exactly grounded to active
`CHEBI:15354`; its CAS, formula, InChI, SMILES, reviewed exact synonyms, 4/4
CultureMech occurrence count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Choline.yaml`.
- Identifier and grounding: `identifier: CHEBI:15354`,
  `ontology_mapping.ontology_id: CHEBI:15354`,
  `ontology_label: choline`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct exact OLS lookup for `Choline` returns active `CHEBI:15354` labelled
  `choline`; the six `kg_microbe` exact synonyms in the YAML are present in
  OLS related synonyms.
- PubChem lookup of CAS `62-49-7` resolves to the same formula and standard
  InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chocolate_agar.yaml data/ingredients/mapped/Cholesterol_Lipid_Concentrate.yaml data/ingredients/mapped/Cholic_Acid.yaml data/ingredients/mapped/Cholin_Acetate.yaml data/ingredients/mapped/Choline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cholesterol_Lipid_Concentrate.yaml data/ingredients/mapped/Cholic_Acid.yaml data/ingredients/mapped/Choline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  `reports` found the active exact `MIM:Choline` SSSOM row, OAK/OLS row-review
  confirmation, matching aggregate/docs rows, and no QC report entry that flags
  this record.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found exactly four
  `CHEBI:15354` recipe rows, matching the refreshed 4/4 occurrence statistics.
- The SSSOM `other` column exports the six exact synonyms plus `CAS:62-49-7`.
  It correctly omits the raw `Cross-references: KEGG:chol` CultureMech note
  because `synonym_policy.py` filters those cross-reference notes from the
  resolving synonym surface.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, reviewed exact
  synonyms, occurrence count, SSSOM row, aggregate copy, and docs row are
  populated and agree.

## Recommended Edits

- None for this record.
