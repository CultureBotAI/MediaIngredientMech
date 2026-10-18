# `data/ingredients/mapped/Carnosic_Acid.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed record is exactly grounded to active
`CHEBI:65585` carnosic acid, and its CAS, formula, InChI, SMILES, synonym,
SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Carnosic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:65585`,
  `ontology_mapping.ontology_id: CHEBI:65585`,
  `ontology_label: carnosic acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:65585` returns the active carnosic acid term
  with CAS `3650-09-7`, formula `C20H28O4`, and the same InChI/SMILES as the
  local `chemical_properties`.
- PubChem resolves CAS `3650-09-7` to CID `65126` with formula `C20H28O4` and
  the same InChI as the local record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carnitine_Hydrochloride.yaml data/ingredients/mapped/Carnosic_Acid.yaml data/ingredients/mapped/Carotenoid.yaml data/ingredients/mapped/Carrageenan.yaml data/ingredients/mapped/Carrot.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carnitine_Hydrochloride.yaml data/ingredients/mapped/Carnosic_Acid.yaml data/ingredients/mapped/Carotenoid.yaml data/ingredients/mapped/Carrageenan.yaml data/ingredients/mapped/Carrot.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Carnosic_Acid` SSSOM row
  with the exact ChEBI target, `CAS:3650-09-7`, and the same ChEBI IUPAC
  synonym as the YAML record, matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` table has 0 rows
  for `CHEBI:65585`, matching `occurrence_statistics` `0/0`.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, synonym, 0/0
  CultureMech occurrence count, SSSOM row, aggregate copy, and docs row are
  populated.
- No role, component, or environment claims are present.

## Recommended Edits

- None for this record.
