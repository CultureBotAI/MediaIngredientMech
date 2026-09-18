# `data/ingredients/mapped/Cuso4_X_2_H2o.yaml`

## Verdict

Needs curation; major. The record names a copper sulfate hydrate but still uses
the anhydrous `CHEBI:23414` primary identifier, active anhydrous synonyms,
anhydrous InChI/SMILES values, a shared 187/187 occurrence count, and only
computational support for its `TRACE_ELEMENT` role.

## Identity

- Reviewed record: `data/ingredients/mapped/Cuso4_X_2_H2o.yaml`.
- Current identifier and grounding: `identifier: CHEBI:23414`,
  `ontology_mapping.ontology_id: CHEBI:23414`,
  `ontology_label: copper(II) sulfate`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:23414` returns active `CHEBI:23414` labelled
  `copper(II) sulfate`, the anhydrous copper sulfate parent.
- Live exact OLS search for `CuSO4 x 2 H2O` found no exact CHEBI class, so this
  label cannot be made exact by simply swapping to a current CHEBI hydrate
  term.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found that `Cuso4`, `Cuso4_X_2_H2o`, and
  `Cuso4_X_4_H2o` all still share `CHEBI:23414` as their primary identifier.

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
  `scripts`, `tests`, and `reports` found `mappings/hydrate_review.tsv`
  classifying `CuSO4 x 2 H2O` as `WRONG_TERM_ANHYDROUS`,
  `MATCHES_ANHYDROUS_WRONGLY`, and `MEDIADIVE_UPSTREAM`.
- The same hydrate audit reports that the exact source label belongs to
  upstream MediaDive compound 719 and occurs in 7 CultureMech source rows, not
  the shared 187 rows now keyed to `CHEBI:23414`.
- Major: the final SSSOM publishes `MIM:Cuso4_X_2_H2o skos:exactMatch
  CHEBI:23414`; a hydrated source label should not publish as exact to
  anhydrous copper(II) sulfate.
- Major: final SSSOM `other` still exposes anhydrous-parent tokens
  `cupric sulfate anhydrous` and `copper(2+) sulfate` on the hydrate record.
- Major: `chemical_properties.molecular_formula` was corrected to
  `Cu.O4S.2H2O`, but the active InChI and SMILES still encode the anhydrous
  salt with no water of hydration.
- Major: `nutritional_roles.TRACE_ELEMENT` is still a
  `COMPUTATIONAL_PREDICTION` from a curated name pattern.

## Completeness

- The record has already removed the anhydrous CAS and rejected sibling hydrate
  labels, but its primary identifier, ontology row, SSSOM `other`, occurrence
  count, and structure fields still collapse the dihydrate-looking source label
  onto the anhydrous parent.

## Recommended Edits

- Major: confirm MediaDive compound 719 against its original source; if it
  actually meant the pentahydrate, correct it upstream and refresh
  CultureMech/MIM products.
- Major: if the source label must remain as written, mint a local
  `kgmicrobe.compound` identifier, map `CHEBI:23414` only as a close anhydrous
  parent, remove anhydrous synonyms from resolving `other`, and clear or
  replace the anhydrous InChI/SMILES.
- Major: recompute the occurrence statistics after the identity is split so
  this record no longer inherits all 187 `CHEBI:23414` rows.
- Major: replace the provisional `TRACE_ELEMENT` role evidence with a
  source-backed `DATABASE_ENTRY` if the local record is retained.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, duplicate-identifier audit, and `git diff --check`.
