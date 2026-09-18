# `data/ingredients/mapped/Cucl2_X_5_H2o.yaml`

## Verdict

Needs curation; major. The current YAML is an exact lexical match to active
`CHEBI:91245` copper(II) chloride pentahydrate and its 39/39 count agrees with
current membership rows, but the hydrate audit records this MediaDive label as
probably meant to be the dihydrate, and the `TRACE_ELEMENT` role is still only
computationally supported.

## Identity

- Reviewed record: `data/ingredients/mapped/Cucl2_X_5_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:91245`,
  `ontology_mapping.ontology_id: CHEBI:91245`,
  `ontology_label: copper(II) chloride pentahydrate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `match_level: EXACT` by equality of the
  record and ontology identifiers.
- Live OLS lookup by `CHEBI:91245` returns active `CHEBI:91245` labelled
  `copper(II) chloride pentahydrate`.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using `CHEBI:91245` as a
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cucl2_X_2_H2o.yaml data/ingredients/mapped/Cucl2_X_5_H2o.yaml data/ingredients/mapped/Cucl2_X_6_H2o.yaml data/ingredients/mapped/Cumene_Hydroperoxide.yaml data/ingredients/mapped/Curamycin_A.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cucl2_X_2_H2o.yaml data/ingredients/mapped/Cucl2_X_5_H2o.yaml data/ingredients/mapped/Cumene_Hydroperoxide.yaml data/ingredients/mapped/Curamycin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-exact records in this batch.
  `Cucl2_X_6_H2o` was intentionally skipped because its local
  `kgmicrobe.compound` primary identifier and close ChEBI parent are outside
  this CHEBI-focused exact-label validation pass.
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
  `scripts`, `tests`, and `reports` found the active `MIM:Cucl2_X_5_H2o`
  final SSSOM row, generated docs rows, and the OAK/OLS row-review
  confirmation for `CHEBI:91245`.
- `mappings/culturemech_recipe_membership.tsv` contains 39 `CHEBI:91245`
  rows and a total occurrence sum of 39, matching `occurrence_statistics`
  `39/39`.
- Major: `mappings/hydrate_review.tsv` marks `CuCl2 x 5 H2O` as
  `NEEDS_SOURCE` with `MEDIADIVE_UPSTREAM`: the record faithfully transcribes
  MediaDive compound 838, but the audit concluded the source probably intended
  `CuCl2 x 2 H2O`; the exact `skos:exactMatch CHEBI:91245` row cannot hold if
  that upstream label is corrected to the dihydrate.
- Major: `nutritional_roles.TRACE_ELEMENT` uses
  `reference_type: COMPUTATIONAL_PREDICTION` with `reference_text: Inferred
  from curated media-role name pattern`. No inspected source is attached to the
  role-level claim.
- The final SSSOM `other` tokens are pentahydrate labels or ChEBI synonyms for
  `CHEBI:91245`.

## Completeness

- The ChEBI identifier, formula, InChI, SMILES, final SSSOM row, aggregate
  copy, occurrence count, and generated docs rows are populated and agree with
  the current source label.
- The record needs upstream source confirmation before the pentahydrate
  identity should be trusted as graph-facing exact identity.

## Recommended Edits

- Major: confirm MediaDive compound 838 against its original source; correct it
  upstream if it actually meant copper(II) chloride dihydrate, then refresh the
  CultureMech and MIM products so this record either disappears into
  `CHEBI:86318` or remains with provenance justifying the pentahydrate label.
- Major: replace the provisional `TRACE_ELEMENT` evidence with a source-backed
  `DATABASE_ENTRY` if the label is retained.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
