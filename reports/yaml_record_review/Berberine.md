# `data/ingredients/mapped/Berberine.yaml`

## Verdict

Needs curation, major. The `CHEBI:31271` berberine chloride identity, CAS
`633-65-8`, synonym recovery, SSSOM row, and aggregate copy pass, but the stored
formula, InChI, and SMILES still describe the berberine cation from the
pre-#320 grounding rather than the chloride salt.

## Identity

- Reviewed record: `data/ingredients/mapped/Berberine.yaml`.
- Identifier and grounding: `identifier: CHEBI:31271` with
  `ontology_mapping.ontology_id: CHEBI:31271`,
  `ontology_label: Berberine chloride (TN)`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- OLS search in `chebi` returns `CHEBI:31271` for `Berberine chloride` and lists
  both `Berberine chloride` and `berberine chloride` as synonyms.
- PubChem resolves CAS `633-65-8` to berberine chloride, formula
  `C20H18ClNO4`, and a chloride-containing InChI, while the stored structure is
  PubChem's chloride-free berberine cation structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Benzylhydrazine_Hydrochloride.yaml data/ingredients/mapped/Berberine.yaml data/ingredients/mapped/Bergapten.yaml data/ingredients/mapped/Bergenin.yaml data/ingredients/mapped/Beryllium_Sulfate_Tetrahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Berberine.yaml data/ingredients/mapped/Bergapten.yaml data/ingredients/mapped/Bergenin.yaml data/ingredients/mapped/Beryllium_Sulfate_Tetrahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-backed records in the batch.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 564 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The 2026-08-13 `reground_cas_specific_form` event intentionally moved the
  record from `CHEBI:16118` berberine to `CHEBI:31271` because CAS `633-65-8`
  denotes the chloride salt.
- The 2026-09-02 curation events recovered all SSSOM `other` surface forms as
  `RAW_TEXT` synonyms, and the current SSSOM row still carries those synonyms
  plus `CAS:633-65-8`.

## Completeness

- The exact CHEBI identifier, CAS registry number, recovered synonyms, SSSOM
  row, and aggregate copy are populated.
- Major gap: the `chemical_properties` block is stale after the CAS-specific
  form repair and omits the chloride counterion.
- Minor method gap: this was a CAS-specific regrounding, so
  `mapping_quality` should be `CAS_RN_LOOKUP` rather than `SYNONYM_MATCH` under
  `MAPPING_SEMANTICS.md`.

## Recommended Edits

- Major: update `chemical_properties.molecular_formula`, `inchi`, and `smiles`
  in `data/ingredients/mapped/Berberine.yaml` to the CAS `633-65-8` berberine
  chloride structure, then run `just sync-curated`.
- Minor: change `ontology_mapping.mapping_quality` to `CAS_RN_LOOKUP` in the
  same maintained record so the grade preserves the CAS method used in #320.
