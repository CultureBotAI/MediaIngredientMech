# `data/ingredients/mapped/D-_-turanose.yaml`

## Verdict

Needs curation, with major final-SSSOM synonym and role-evidence issues. The
CAS-resolved active `CHEBI:32528` identity, structure fields, 0/0 occurrence
count, and canonical IUPAC synonym pass, but final SSSOM exports
`D-turanose (turanose)`, a backfilled display string that is not a real
resolving synonym for the subject.

## Identity

- Reviewed record: `data/ingredients/mapped/D-_-turanose.yaml`.
- Current identifier and grounding: `identifier: CHEBI:32528`,
  `ontology_mapping.ontology_id: CHEBI:32528`,
  `ontology_label: turanose`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:32528` returns active `CHEBI:32528` labelled
  `turanose`, CAS xref `547-25-1`, formula `C12H22O11`, matching
  InChI/SMILES strings, and the exact IUPAC synonym
  `alpha-D-glucopyranosyl-(1->3)-D-fructose`.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:32528` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml data/ingredients/mapped/D-_-pantolactone.yaml data/ingredients/mapped/D-_-tagatose.yaml data/ingredients/mapped/D-_-turanose.yaml data/ingredients/mapped/D-apiose.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-_-pantolactone.yaml data/ingredients/mapped/D-_-tagatose.yaml data/ingredients/mapped/D-_-turanose.yaml data/ingredients/mapped/D-apiose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 with no failures for the four CHEBI-primary records in this batch.
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

- The record's formula, InChI, SMILES, and CAS RN agree with active
  `CHEBI:32528`; the explicit 2026-08-24 regrade preserves the CAS-to-CHEBI
  lookup method behind the mapping.
- The hidden/ignored-inclusive membership search found no `CHEBI:32528` rows in
  `mappings/culturemech_recipe_membership.tsv`, matching the record's 0/0
  `occurrence_statistics`.
- The final SSSOM row publishes
  `MIM:D-_-turanose skos:exactMatch CHEBI:32528`. Its IUPAC synonym and
  `CAS:547-25-1` `other` tokens are safe.
- A hidden/ignored-inclusive search over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found `D-turanose (turanose)` only in this record, its
  generated final SSSOM row, and ignored aggregate backups. The token is a
  parenthetical display string, not an OLS synonym of `CHEBI:32528`, and should
  not be exported in final SSSOM `other`.
- The `CARBON_SOURCE` facet is supported only by
  `COMPUTATIONAL_PREDICTION` from CHEBI ancestry and its own `curator_note`
  calls it provisional.

## Completeness

- No parent mappings, supplied-form assertions, components, or source
  occurrences are asserted, so there are no unsupported secondary claims beyond
  the bad raw synonym and provisional nutritional role.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry, including the bad raw synonym.

## Recommended Edits

- In `data/ingredients/mapped/D-_-turanose.yaml`, remove the
  `sssom_other_backfill` raw synonym `D-turanose (turanose)`; then synchronize
  `data/curated/mapped_ingredients.yaml` and regenerate final SSSOM so it
  leaves the `other` column.
- Either replace the computational `CARBON_SOURCE` evidence with direct
  CultureBotHT or source-backed media-role evidence for this ingredient, or
  remove the role facet; then rerun strict validation and the final SSSOM
  build.
