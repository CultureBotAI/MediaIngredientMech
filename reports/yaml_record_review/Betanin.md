# `data/ingredients/mapped/Betanin.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:3080` Betanin identity, CAS xref,
structure fields, SSSOM row, and aggregate copy pass, but
`chemical_properties.data_source` still names the CultureBotHT CAS table even
though the formula, InChI, and SMILES came from the later ChEBI backfill.

## Identity

- Reviewed record: `data/ingredients/mapped/Betanin.yaml`.
- Identifier and grounding: `identifier: CHEBI:3080` with
  `ontology_mapping.ontology_id: CHEBI:3080`,
  `ontology_label: Betanin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS confirms current `CHEBI:3080` `Betanin`, xref CAS `7659-95-2`, formula
  `C24H26N2O13`, and the same InChI and SMILES stored in the record.
- PubChem resolves CAS `7659-95-2` to the same molecular formula; its current
  InChI and SMILES are not the ChEBI strings stored by the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Betaine_X_H2o.yaml data/ingredients/mapped/Betanin.yaml data/ingredients/mapped/Bg-11_Medium.yaml data/ingredients/mapped/Bg-11_Trace_Metals_Solution.yaml data/ingredients/mapped/Bicarbonate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Betaine_X_H2o.yaml data/ingredients/mapped/Betanin.yaml data/ingredients/mapped/Bicarbonate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three ChEBI-backed records in this batch.
- Engine A term validation is intentionally skipped for the two non-ChEBI
  records here: `MICRO` is omitted by the local justfile's OBO-safe adapter list
  and `kgmicrobe.ingredient` is a local registry prefix.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 587, the OAK/OLS confirmation row
  in `mappings/ingredient_mappings_row_review_manifest.tsv`, and the aggregate
  copy in `data/curated/mapped_ingredients.yaml`.
- The CultureBotHT import supplied CAS `7659-95-2`; ChEBI currently carries
  that same CAS as a database cross-reference on `CHEBI:3080`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact CHEBI identifier, CAS RN, single-ingredient classification,
  formula, InChI, SMILES, SSSOM row, zero occurrence count, and aggregate copy
  are populated.
- Minor gap: `chemical_properties.data_source` should distinguish the original
  CAS table from the ChEBI structure backfill that supplied the formula and
  structure strings.

## Recommended Edits

- Minor: update `data/ingredients/mapped/Betanin.yaml` so the
  `chemical_properties` provenance accurately names ChEBI as the source for the
  formula, InChI, and SMILES; then run `just sync-curated` and focused
  strict/term validation.
