# `data/ingredients/mapped/Caco3.yaml`

## Verdict

Needs curation, major. The exact calcium carbonate identity, `CHEBI:3311` row,
CAS, formula, occurrence count, and aggregate copy agree, but the generic
`Optional ingredient` note is still exported as a synonym of calcium carbonate.

## Identity

- Reviewed record: `data/ingredients/mapped/Caco3.yaml`.
- Identifier and grounding: `identifier: CHEBI:3311`,
  `ontology_mapping.ontology_id: CHEBI:3311`,
  `ontology_label: calcium carbonate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:3311` returns the active label
  `calcium carbonate`.
- PubChem resolves CAS `471-34-1` to calcium carbonate, matching the local
  `CO3.Ca` formula, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cacl2_X_7_H2o.yaml data/ingredients/mapped/Caco3.yaml data/ingredients/mapped/Cadaverine.yaml data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml data/ingredients/mapped/Cadmium_Chloride_Hemipentahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Caco3.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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

- Hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active SSSOM row in
  `mappings/ingredient_mappings.sssom.tsv`, the exact aggregate copy in
  `data/curated/mapped_ingredients.yaml`, the current `docs/data` export rows,
  and four active records that still publish `Optional ingredient`.
- The SSSOM row maps `MIM:Caco3` to `CHEBI:3311` with `skos:exactMatch` and
  carries `CAS:471-34-1`, matching the YAML identity and current CAS.
- Major gap: `Optional ingredient` is not a name for calcium carbonate, but it
  is present in this record, in the SSSOM `other` field, and in
  `docs/data/label_index.csv` as a conflict across `Caco3`, `Cellulose`,
  `D-Fructose`, and `Na-acetate`.

## Completeness

- The ChEBI identifier, CAS, calcium carbonate synonyms, single-ingredient
  classification, formula, InChI, SMILES, mineral-source role, 320/320
  occurrence count, SSSOM row, and aggregate copy are populated.
- The record is incomplete until generic source annotations such as
  `Optional ingredient` and `(if required)` are either non-published provenance
  or explicitly rejected labels.

## Recommended Edits

- Major: convert `Optional ingredient` and `(if required)` from resolving
  `RAW_TEXT` synonyms into non-resolving provenance on
  `data/ingredients/mapped/Caco3.yaml`, regenerate the SSSOM/docs exports so
  `Optional ingredient` is removed from `MIM:Caco3`, then run
  `just sync-curated`, focused strict/term validation, `just qc-sssom`, and
  `just qc-flat-coverage`.
