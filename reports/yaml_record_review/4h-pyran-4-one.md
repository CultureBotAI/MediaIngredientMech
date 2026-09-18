# `data/ingredients/mapped/4h-pyran-4-one.yaml`

## Verdict

Pass, none. The exact `CHEBI:37966` 4H-pyran-4-one identity, canonical label,
microbedecoder provenance, chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4h-pyran-4-one.yaml`.
- Identifier and grounding: `identifier: CHEBI:37966` with
  `ontology_mapping.ontology_id: CHEBI:37966`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:37966` is active and resolves to
  `4H-pyran-4-one`.
- The current ChEBI page reports formula `C5H4O2`, the stored SMILES, and the
  stored InChI for `CHEBI:37966`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-vinylphenol.yaml data/ingredients/mapped/4_Carbon_Mix.yaml data/ingredients/mapped/4h-pyran-4-one.yaml data/ingredients/mapped/5-Aminolevulinic_Acid.yaml data/ingredients/mapped/5-Azacytidine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4h-pyran-4-one.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- The active ChEBI term, formula, SMILES, and InChI all support the exact
  4H-pyran-4-one identity.
- The raw microbedecoder source row in
  `data/custom/microbedecoder/unmapped_labels.tsv` records
  `kgmicrobe.trait:4h_pyran_4_one` with count 1 in
  `BacDive_Metabolite_production`, matching `source_occurrences`.
- The occurrence statistics correctly keep the upstream microbedecoder count
  separate from verified CultureMech recipe counts, which remain
  `total_occurrences: 0` and `media_count: 0`.
- The SSSOM row maps `MIM:4h-pyran-4-one` to `CHEBI:37966` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and no `other` synonym payload.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy,
  microbedecoder source row, SSSOM row, generated docs, source review row, and
  ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence counts, and
  `ingredient_type` are populated.
- No synonyms, roles, components, environment, or discussion entries need
  review.

## Recommended Edits

No YAML edit is required for this record.
