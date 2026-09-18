# `data/ingredients/mapped/D-_-pantolactone.yaml`

## Verdict

Pass. The CAS-resolved active `CHEBI:16719` identity, structure fields, 0/0
occurrence count, and final SSSOM synonym payload all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/D-_-pantolactone.yaml`.
- Current identifier and grounding: `identifier: CHEBI:16719`,
  `ontology_mapping.ontology_id: CHEBI:16719`,
  `ontology_label: (R)-pantolactone`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:16719` returns active `CHEBI:16719` labelled
  `(R)-pantolactone`, CAS xref `599-04-2`, formula `C6H10O3`, and matching
  InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:16719` as its primary
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
  `CHEBI:16719`; the explicit 2026-08-24 regrade preserves the CAS-to-CHEBI
  lookup method behind the mapping.
- The hidden/ignored-inclusive membership search found no `CHEBI:16719` rows in
  `mappings/culturemech_recipe_membership.tsv`, matching the record's 0/0
  `occurrence_statistics`.
- The final SSSOM row publishes
  `MIM:D-_-pantolactone skos:exactMatch CHEBI:16719`. Its `other` column
  contains the live exact IUPAC synonym and `CAS:599-04-2`.

## Completeness

- No nutritional roles, parent mappings, supplied-form assertions, components,
  or source occurrences are asserted, so there are no unsupported secondary
  claims.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry.

## Recommended Edits

- No curation edits are needed.
