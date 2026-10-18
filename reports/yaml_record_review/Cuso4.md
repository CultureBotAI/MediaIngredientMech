# `data/ingredients/mapped/Cuso4.yaml`

## Verdict

Pass. The anhydrous `CHEBI:23414` copper(II) sulfate identity, structure,
187/187 count, CultureMech mineral role, rejected hydrate labels, and final
SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Cuso4.yaml`.
- Identifier and grounding: `identifier: CHEBI:23414`,
  `ontology_mapping.ontology_id: CHEBI:23414`,
  `ontology_label: copper(II) sulfate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `match_level: EXACT` by equality of the record and ontology identifiers.
- Live OLS lookup by `CHEBI:23414` returns active `CHEBI:23414` labelled
  `copper(II) sulfate` with the anhydrous synonyms retained by the record.
- Hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found two sibling hydrate records still sharing
  `CHEBI:23414`; those are the reviewed `Cuso4_X_2_H2o` and `Cuso4_X_4_H2o`
  curation issues, not an identity defect in this anhydrous record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Curcumin.yaml data/ingredients/mapped/Curdlan.yaml data/ingredients/mapped/Cuso4.yaml data/ingredients/mapped/Cuso4_X_2_H2o.yaml data/ingredients/mapped/Cuso4_X_4_H2o.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Curcumin.yaml data/ingredients/mapped/Cuso4.yaml data/ingredients/mapped/Cuso4_X_2_H2o.yaml data/ingredients/mapped/Cuso4_X_4_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI records in this batch. `Curdlan` was intentionally
  skipped because its CAS primary identifier and MeSH parent are outside this
  CHEBI-focused exact-label validation pass.
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

- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the active `MIM:Cuso4` final SSSOM
  row, generated docs rows, and the synonym-enrichment review row for
  `CHEBI:23414`.
- `mappings/culturemech_recipe_membership.tsv` contains 187 `CHEBI:23414`
  rows and a total occurrence sum of 187, matching `occurrence_statistics`
  `187/187`.
- The final SSSOM `other` tokens are anhydrous ChEBI/CAS synonyms; raw role
  payloads and rejected hydrate labels are filtered out.
- The `TRACE_ELEMENT` role is backed by the imported CultureMech role text
  rather than inferred from the compound name or ChEBI class.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, final SSSOM row,
  aggregate copy, occurrence count, and generated docs rows are populated and
  agree.
- The anhydrous/hydrate boundary is explicit on this record: sibling hydrate
  surfaces remain only as `REJECTED_LABEL` provenance.

## Recommended Edits

- None for `data/ingredients/mapped/Cuso4.yaml`; fix the duplicate
  `CHEBI:23414` hydrate siblings in their own records.
