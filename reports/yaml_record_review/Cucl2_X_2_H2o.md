# `data/ingredients/mapped/Cucl2_X_2_H2o.yaml`

## Verdict

Needs curation; major. The exact `CHEBI:86318` copper(II) chloride dihydrate
identity, structure, role evidence, and 2488/2488 count pass, but the final
SSSOM still exports `CuCl 2`, an anhydrous formula surface, as if it were a
real synonym for the dihydrate.

## Identity

- Reviewed record: `data/ingredients/mapped/Cucl2_X_2_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86318`,
  `ontology_mapping.ontology_id: CHEBI:86318`,
  `ontology_label: copper(II) chloride dihydrate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `match_level: EXACT` by equality of the
  record and ontology identifiers.
- Live OLS lookup by `CHEBI:86318` returns active `CHEBI:86318` labelled
  `copper(II) chloride dihydrate` with dihydrate-specific synonyms.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using `CHEBI:86318` as a
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
  `scripts`, `tests`, and `reports` found the active `MIM:Cucl2_X_2_H2o`
  final SSSOM row, generated docs rows, synonym-enrichment review rows, and
  `mappings/hydrate_review.tsv` row classifying the dihydrate record as `OK`.
- `mappings/culturemech_recipe_membership.tsv` contains 2488 `CHEBI:86318`
  rows and a total occurrence sum of 2488, matching `occurrence_statistics`
  `2488/2488`.
- The CAS RN, formula, InChI, and SMILES are dihydrate-specific and agree with
  the exact CHEBI identity.
- The `TRACE_ELEMENT` role is backed by an imported CultureMech role excerpt
  rather than inferred from the compound name or ChEBI class.
- Major: the final SSSOM `other` field includes `CuCl 2`. Live OLS for
  `CHEBI:86318` does not list that surface, and the label denotes anhydrous
  `CuCl2` rather than `CuCl2 x 2 H2O`.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, role evidence, final
  SSSOM row, aggregate copy, occurrence count, and generated docs rows are
  populated and agree apart from the unsafe `CuCl 2` synonym.
- Other final SSSOM aliases are dihydrate names, ChEBI hydrate synonyms, the
  `Coppertrace` synonym present in OLS for `CHEBI:86318`, or the structured
  `CAS:10125-13-0` value from `chemical_properties.cas_rn`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Cucl2_X_2_H2o.yaml`, mark `CuCl 2` as a
  rejected anhydrous label or move it to parent-only provenance so it no longer
  publishes as a synonym for the dihydrate.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
