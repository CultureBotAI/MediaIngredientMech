# `data/ingredients/mapped/Benzoin.yaml`

## Verdict

Pass. The exact `CHEBI:17682` benzoin identity, microbedecoder provenance,
formula, InChI, SMILES, SSSOM row, and aggregate copy all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Benzoin.yaml`.
- Identifier and grounding: `identifier: CHEBI:17682` with
  `ontology_mapping.ontology_id: CHEBI:17682`, `ontology_label: benzoin`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- OLS search in `chebi` returns `CHEBI:17682` as the `benzoin` class.
- PubChem resolves benzoin to formula `C14H12O2` and the same standard InChI
  stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Benzoin.yaml data/ingredients/mapped/Benzothiazole.yaml data/ingredients/mapped/Benzyl_Alcohol.yaml data/ingredients/mapped/Benzyl_Isothiocyanate.yaml data/ingredients/mapped/Benzylcyanide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Benzoin.yaml data/ingredients/mapped/Benzothiazole.yaml data/ingredients/mapped/Benzyl_Alcohol.yaml data/ingredients/mapped/Benzyl_Isothiocyanate.yaml data/ingredients/mapped/Benzylcyanide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 558 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/microbedecoder_auto_mapped_review.tsv` row 78 approved the
  `CHEBI:17682` mapping after local OAK resolution and case-insensitive
  canonical-label agreement.
- The current OLS and PubChem checks agree with the exact CHEBI grounding and
  the stored `ChEBI+PubChem` structure fields.

## Completeness

- The exact CHEBI identifier, single-ingredient classification, formula, InChI,
  SMILES, SSSOM row, and aggregate copy are populated.
- `occurrence_statistics` correctly preserves a zero medium count with one
  microbedecoder source occurrence.
- No role, component list, or supplied-form split is required for this
  single-compound record.

## Recommended Edits

- None.
