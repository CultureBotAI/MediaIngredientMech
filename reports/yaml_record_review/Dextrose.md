# `data/ingredients/mapped/Dextrose.yaml`

## Verdict

Pass with minor issues. This is an intentional rejected duplicate tombstone:
`Dextrose` was merged into live `D-Glucose`, its own final SSSOM row was
dropped, and the surviving `MIM:D-glucose` row exports `Dextrose` as a synonym.
Some stale pre-merge fields and cross-record bookkeeping remain on or around
the tombstone.

## Identity

- Reviewed record: `data/ingredients/mapped/Dextrose.yaml`.
- Current tombstone identity: `identifier: CHEBI:17634`,
  `ontology_mapping.ontology_id: CHEBI:17634`, canonical label `D-glucose`,
  and `mapping_status: REJECTED`.
- The 2026-08-13 merge history says `Dextrose` was merged into live
  `D-Glucose` because dextrose is D-glucose; the tombstone history also
  records the old `CHEBI:4167` D-glucopyranose grounding and the 2026-08-15
  ontology pointer refresh to `CHEBI:17634`.
- The live survivor is `data/ingredients/mapped/D-glucose.yaml`, also
  `identifier: CHEBI:17634`, with `Dextrose` preserved as a raw label.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dextrose.yaml data/ingredients/mapped/Diacetyl.yaml data/ingredients/mapped/Diallyl_Sulfide.yaml data/ingredients/mapped/Diaminopimelic_Acid.yaml data/ingredients/mapped/Diammonium_molybdate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dextrose.yaml data/ingredients/mapped/Diacetyl.yaml data/ingredients/mapped/Diallyl_Sulfide.yaml data/ingredients/mapped/Diaminopimelic_Acid.yaml data/ingredients/mapped/Diammonium_molybdate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the rejected tombstone, the live `D-glucose.yaml` survivor, and the
  row-review record marking the stale `CHEBI:4167` synonym-enrichment row as
  already represented.
- The final `mappings/ingredient_mappings.sssom.tsv` has no `MIM:Dextrose`
  row, matching the merge history that says this tombstone's SSSOM rows were
  dropped.
- The live `MIM:D-glucose` SSSOM row exports `Dextrose` in `other`.
- Minor: `mappings/other_cross_record_baseline.tsv` still has an `UNREVIEWED`
  row for the `MIM:D-glucose` to `MIM:Dextrose` synonym even though the
  duplicate is tombstoned and the raw label is intentionally carried on the
  survivor.

## Completeness

- The tombstone is complete enough for duplicate lookup: it records its merge
  into D-glucose, carries 0/0 occurrences, and emits no standalone final SSSOM
  row.
- Minor: `chemical_properties`, `nutritional_roles`, and generated
  `docs/data/mapped_ingredients.*` rows still expose pre-merge content from a
  rejected mapped-directory tombstone.

## Recommended Edits

- Minor: retire or mark reviewed the
  `mappings/other_cross_record_baseline.tsv` `UNREVIEWED` row for
  `MIM:D-glucose`/`MIM:Dextrose`.
- Minor: if rejected tombstones are meant to retain only merge pointers and
  raw labels, prune stale role and structure fields from
  `data/ingredients/mapped/Dextrose.yaml` and synchronize
  `data/curated/mapped_ingredients.yaml`.
