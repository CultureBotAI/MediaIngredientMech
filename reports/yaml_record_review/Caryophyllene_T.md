# `data/ingredients/mapped/Caryophyllene_T.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup is exactly grounded to active
`CHEBI:10357`, and the CAS RN, formula, InChI, synonym, SSSOM row, aggregate
copy, and 0/0 occurrence count agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Caryophyllene_T.yaml`.
- Identifier and grounding: `identifier: CHEBI:10357`,
  `ontology_mapping.ontology_id: CHEBI:10357`,
  `ontology_label: (-)-beta-caryophyllene`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:10357` returns one active ChEBI term labelled
  `(-)-beta-caryophyllene` with CAS `87-44-5`, formula `C15H24`, and the same
  InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Caryomycin.yaml data/ingredients/mapped/Caryophyllene_T.yaml data/ingredients/mapped/Casamino_Acids.yaml data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml data/ingredients/mapped/Casein.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caryomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  unavailable for the kgmicrobe placeholder sibling because the local
  kgmicrobe OAK adapter has no `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caryophyllene_T.yaml data/ingredients/mapped/Casamino_Acids.yaml data/ingredients/mapped/Casamino_Acids_Vitamin_Assay.yaml data/ingredients/mapped/Casein.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review-report directories,
  found the active `MIM:Caryophyllene_T` SSSOM row with `CHEBI:10357`,
  `CAS:87-44-5`, the ChEBI synonym-review disposition, and matching
  aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `CHEBI:10357`, matching `occurrence_statistics` `0/0`.
- No role, component, or environment claims are present.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, IUPAC synonym,
  0/0 occurrence count, SSSOM row, aggregate copy, and docs row are populated.

## Recommended Edits

- None for this record.
