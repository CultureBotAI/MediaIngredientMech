# `data/ingredients/mapped/Cefazolin.yaml`

## Verdict

Pass. The restored MicrobeDecoder cefazolin record is exactly grounded to
active `CHEBI:474053`, and its formula, InChI, SMILES, molecular weight, zero
media occurrence count, source occurrence annotation, SSSOM row, and aggregate
copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cefazolin.yaml`.
- Identifier and grounding: `identifier: CHEBI:474053`,
  `ontology_mapping.ontology_id: CHEBI:474053`,
  `ontology_label: cefazolin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:474053` returns one active ChEBI term labelled
  `cefazolin` with formula `C14H14N8O4S3`, molecular mass `454.519`, and the
  same InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cefazolin.yaml data/ingredients/mapped/Cefazolin_Sodium_Salt.yaml data/ingredients/mapped/Cefepime.yaml data/ingredients/mapped/Cefixime.yaml data/ingredients/mapped/Cefmetazole.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cefazolin.yaml data/ingredients/mapped/Cefazolin_Sodium_Salt.yaml data/ingredients/mapped/Cefepime.yaml data/ingredients/mapped/Cefixime.yaml data/ingredients/mapped/Cefmetazole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  backups, found the active exact `MIM:Cefazolin` SSSOM row, the
  high-accession demotion/regrounding audit rows, the approved
  `mappings/microbedecoder_auto_mapped_review.tsv` row, and matching
  aggregate/docs rows for `CHEBI:474053`.
- Hidden/ignored-inclusive search of `mappings/culturemech_recipe_membership.tsv`
  found no `CHEBI:474053` rows, which matches the explicit 0/0 media
  `occurrence_statistics`.
- The MicrobeDecoder `source_occurrences` annotation preserves the 108 BacDive
  antibiotic resistance or sensitivity mentions that caused this
  ingredient-like trait to be imported. Those source mentions are not
  CultureMech recipe occurrences.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, molecular weight, SSSOM
  row, aggregate copy, docs row, zero media occurrence count, and MicrobeDecoder
  source occurrence count are populated and agree.
- `synonyms` is empty, but no local alternate label, rejected label, or
  additional lookup key is required for this exact identity.

## Recommended Edits

- None for this record.
