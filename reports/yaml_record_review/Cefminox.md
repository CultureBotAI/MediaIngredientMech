# `data/ingredients/mapped/Cefminox.yaml`

## Verdict

Pass. The MicrobeDecoder cefminox record is exactly grounded to active
`CHEBI:135817`, and its formula, InChI, SMILES, molecular weight, zero media
occurrence count, source occurrence annotation, SSSOM row, and aggregate copy
agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cefminox.yaml`.
- Identifier and grounding: `identifier: CHEBI:135817`,
  `ontology_mapping.ontology_id: CHEBI:135817`, `ontology_label: cefminox`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:135817` returns one active ChEBI term labelled
  `cefminox` with formula `C16H21N7O7S3`, molecular mass `519.587`, and the
  same InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cefminox.yaml data/ingredients/mapped/Cefoperazone.yaml data/ingredients/mapped/Cefotaxime.yaml data/ingredients/mapped/Cefotaxime_Sodium_Salt.yaml data/ingredients/mapped/Cefotetan.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cefminox.yaml data/ingredients/mapped/Cefoperazone.yaml data/ingredients/mapped/Cefotaxime.yaml data/ingredients/mapped/Cefotaxime_Sodium_Salt.yaml data/ingredients/mapped/Cefotetan.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 external-ontology records in this batch.
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
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active exact `MIM:Cefminox` SSSOM row, the approved
  `mappings/microbedecoder_auto_mapped_review.tsv` row, and matching
  aggregate/docs rows for `CHEBI:135817`.
- Hidden/ignored-inclusive search of `mappings/culturemech_recipe_membership.tsv`
  found no `CHEBI:135817` rows, which matches the explicit 0/0 media
  `occurrence_statistics`.
- The MicrobeDecoder `source_occurrences` annotation preserves the one BacDive
  antibiotic sensitivity mention that caused this ingredient-like trait to be
  imported. That source mention is not a CultureMech recipe occurrence.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, molecular weight, SSSOM
  row, aggregate copy, docs row, zero media occurrence count, and MicrobeDecoder
  source occurrence count are populated and agree.
- `synonyms` is empty, but no local alternate label, rejected label, or
  additional lookup key is required for this exact identity.

## Recommended Edits

- None for this record.
