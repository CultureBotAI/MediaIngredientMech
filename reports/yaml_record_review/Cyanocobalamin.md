# `data/ingredients/mapped/Cyanocobalamin.yaml`

## Verdict

Needs curation; major. The exact `CHEBI:17439` cyanocobalamin identity,
structure fields, CAS RN, 265/275 CultureMech count, and vitamin role pass, but
the final SSSOM `other` field still exports kg-microbe OCR fragments and
generic Vitamin B12/vitamer strings that are not exact synonyms of the specific
cyanocobalamin molecule.

## Identity

- Reviewed record: `data/ingredients/mapped/Cyanocobalamin.yaml`.
- Current identifier and grounding: `identifier: CHEBI:17439`,
  `ontology_mapping.ontology_id: CHEBI:17439`,
  `ontology_label: cyanocob(III)alamin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:17439` returns active `CHEBI:17439` labelled
  `cyanocob(III)alamin` with CAS `68-19-9`, formula `C63H88CoN14O14P`,
  matching InChI/SMILES strings, and exact cyanocob(III)alamin synonyms.
- Live exact OLS searches for Vitamin B12 and cyanocobalamin show active
  `CHEBI:176843` for the broader `vitamin B12` vitamer class in addition to
  `CHEBI:17439` for the specific cyanocobalamin compound.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:17439` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cuso4_X_5_H2o.yaml data/ingredients/mapped/Cuso4_X_6_H2o.yaml data/ingredients/mapped/Cyanocobalamin.yaml data/ingredients/mapped/Cyanuric_acid.yaml data/ingredients/mapped/Cyclodextrin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cuso4_X_5_H2o.yaml data/ingredients/mapped/Cuso4_X_6_H2o.yaml data/ingredients/mapped/Cyanocobalamin.yaml data/ingredients/mapped/Cyanuric_acid.yaml data/ingredients/mapped/Cyclodextrin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI exact records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- The record's CAS RN, formula, InChI, and SMILES match live `CHEBI:17439`.
- `mappings/culturemech_recipe_membership.tsv` contains 265 distinct recipes
  and 275 total occurrences for `CHEBI:17439`, matching
  `occurrence_statistics.media_count` and `.total_occurrences`.
- The `VITAMIN_SOURCE` role has `DATABASE_ENTRY` evidence from CultureMech
  vitamin source occurrences, not only a name-pattern prediction.
- Major: `mappings/ingredient_mappings.sssom.tsv` exports three truncated or
  source-artifact kg-microbe tokens in `other`: the bare `Cyanocobalamin (B )`
  fragment, the bare `Cyanocobalamin (Vitamin B )` fragment, and the
  `Cyanocobalamin in` text with a non-breaking space in the raw YAML value.
- Major: the same final SSSOM row exports three numbered Vitamin B12 strings
  with non-breaking spaces. Those are citation or list artifacts, not synonym
  text.
- Major: generic `Vitamin B12`, singular and plural `vitamin B12 vitamer`, and
  `vitamins B12` strings are broader-class labels. The repo has an active
  `Vitamin_B12` record mapped to `CHEBI:176843`, and
  `mappings/culturemech_ambiguous_identifiers.tsv` records that several B12
  source labels normalize ambiguously to `CHEBI:17439|CHEBI:176843`.

## Completeness

- The core cyanocobalamin identity is sound, but the kg-microbe synonym sweep
  and SSSOM backfill left cross-record B12 labels and OCR/listing fragments
  active as graph-facing `other` labels.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the duplicated B12 labels in the
  final SSSOM and generated label indexes; they are not merely dormant YAML
  text.

## Recommended Edits

- Major: remove the truncated and numbered B12 artifacts from
  `data/ingredients/mapped/Cyanocobalamin.yaml` so final SSSOM no longer
  publishes them.
- Major: remove or downgrade broader `Vitamin B12`/vitamer-family strings from
  this specific cyanocobalamin record; keep family-level strings on
  `data/ingredients/mapped/Vitamin_B12.yaml` where they match `CHEBI:176843`.
- Rebuild SSSOM and docs, then rerun strict validation, LinkML term validation,
  SSSOM QC, aggregate roundtrip, and the cross-record `other` synonym audit.
