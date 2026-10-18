# `data/ingredients/mapped/Brain_Heart_Infusion.yaml`

## Verdict

Needs curation, minor. The exact `MICRO:0000193` brain heart infusion identity,
undefined-mixture classification, protein-source role, occurrence count, SSSOM
row, and aggregate copy agree, but top-level `notes` still describe the old
unmapped review state.

## Identity

- Reviewed record: `data/ingredients/mapped/Brain_Heart_Infusion.yaml`.
- Identifier and grounding: `identifier: MICRO:0000193` with
  `ontology_mapping.ontology_id: MICRO:0000193`,
  `ontology_label: brain heart infusion`, `ontology_source: MICRO`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: UNDEFINED_MIXTURE`, and
  `mapping_status: MAPPED`.
- Live OLS exact search for `Brain heart infusion` returns `MICRO:0000193`;
  the local row-review manifest also records that prefix-specific OLS resolves
  this exact CURIE.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bottromycin.yaml data/ingredients/mapped/Bovine_Albumin.yaml data/ingredients/mapped/Bovine_Calf_Serum.yaml data/ingredients/mapped/Bovine_Serum_Albumin.yaml data/ingredients/mapped/Brain_Heart_Infusion.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation is intentionally skipped for this record because
  `MICRO` has no OBO sqlite adapter; prefix-specific EBI OLS validation has
  already resolved `MICRO:0000193`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the prefix-specific MICRO resolution, the
  authoritative exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv`
  row 627, 29 `mappings/culturemech_recipe_membership.tsv` rows for
  `MICRO:0000193`, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Brain_Heart_Infusion` to `MICRO:0000193` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`. The same MICRO identifier is shared by the separately
  tracked Bacto and broth labels, and that duplicate family is already present
  in `mappings/duplicate_identifier_baseline.tsv`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The MICRO identifier, raw synonym, undefined-mixture classification,
  provisional protein-source role, 29/29 occurrence count, SSSOM row, and
  aggregate copy are populated.
- Minor gap: top-level `notes` still say no CAS-RN or CHEBI/NCIT match was
  available and curator review was needed, even though the record is now mapped
  to `MICRO:0000193`.

## Recommended Edits

- Minor: replace the stale import note in
  `data/ingredients/mapped/Brain_Heart_Infusion.yaml` with a current note
  naming the accepted MICRO mapping, then run `just sync-curated` and focused
  strict validation.
