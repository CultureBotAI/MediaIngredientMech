# `data/ingredients/mapped/Cadmium_Chloride_Hemipentahydrate.yaml`

## Verdict

Pass. The CAS-backed `CHEBI:63938` cadmium dichloride hemipentahydrate identity,
CAS, hydrate formula, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Cadmium_Chloride_Hemipentahydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:63938`,
  `ontology_mapping.ontology_id: CHEBI:63938`,
  `ontology_label: cadmium dichloride hemipentahydrate`,
  `ontology_source: CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:63938` returns the active label
  `cadmium dichloride hemipentahydrate`.
- PubChem resolves CAS `7790-78-5` to formula `Cd2Cl4H10O5`, the same
  hemipentahydrate expressed locally as `2CdCl2.5H2O`, with a matching InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cacl2_X_7_H2o.yaml data/ingredients/mapped/Caco3.yaml data/ingredients/mapped/Cadaverine.yaml data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml data/ingredients/mapped/Cadmium_Chloride_Hemipentahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cadmium_Chloride_Hemipentahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`, `docs/data`,
  and `reports`, excluding bulky backups and generated review-report
  directories, found the active SSSOM row, the exact aggregate copy, and the
  `OK_HYDRATE_TERM` row in `reports/hydrate_grounding.tsv`.
- The 2026-08-24 curation event records why the record keeps
  `mapping_quality: CAS_RN_LOOKUP`: the CAS-to-ChEBI lookup uniquely resolved
  `7790-78-5` to `CHEBI:63938`.
- The SSSOM row maps `MIM:Cadmium_Chloride_Hemipentahydrate` to `CHEBI:63938`
  with `skos:exactMatch`; this is the own-identifier Rule D row and is
  compatible with CAS lookup as the mapping-quality provenance.

## Completeness

- The exact ChEBI identifier, canonical label, CAS, formula, InChI, SMILES,
  ChEBI synonym, single-ingredient classification, SSSOM row, and aggregate
  copy are populated.
- 0/0 occurrence statistics are expected for this CultureBotHT-only compound.

## Recommended Edits

- None for this record.
