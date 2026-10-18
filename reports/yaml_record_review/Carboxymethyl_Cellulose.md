# `data/ingredients/mapped/Carboxymethyl_Cellulose.yaml`

## Verdict

Needs curation; major issue. The merged carboxymethylcellulose record is
grounded to active `CHEBI:234035` for the sodium salt, and its CAS-specific
form, supplied form, occurrence count, SSSOM row, and aggregate copy agree, but
`CARBON_SOURCE` is still supported only by a provisional name-pattern
prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Carboxymethyl_Cellulose.yaml`.
- Identifier and grounding: `identifier: CHEBI:234035`,
  `ontology_mapping.ontology_id: CHEBI:234035`,
  `ontology_label: carboxymethylcellulose sodium salt`,
  `ontology_source: CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, `kg_microbe_node_id: CHEBI:234035`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:234035` returns the active
  carboxymethylcellulose sodium salt term with CAS `9004-32-4`, matching the
  local `chemical_properties.cas_rn`.
- The history documents why a mixed plain/sodium-salt CultureMech surface set
  was resolved by CAS and supplier form to the sodium salt rather than the
  parent `CHEBI:85146` term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carcinomycin.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carcinomycin.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  validated `Carboxymethyl_Cellulose`, then stopped on `Carcinomycin` because
  the local kgmicrobe adapter has no `rdfs_label_statement` table.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Carboxymethyl_Cellulose.yaml data/ingredients/mapped/Carminate.yaml data/ingredients/mapped/Carminomycin.yaml data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 4 external-ontology records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the active `MIM:Carboxymethyl_Cellulose`
  SSSOM row with `CHEBI:234035`, `CAS:9004-32-4`, and the expected backfilled
  surface forms, matching aggregate/docs rows.
- The current `mappings/culturemech_recipe_membership.tsv` rows contain seven
  distinct recipes and seven occurrences, matching `occurrence_statistics`.
- The sodium-salt supplied form is anchored to the Sigma-Aldrich `C-5013`
  product named in the DSMZ 1111 preparation note, while the source-label
  conflict with plain carboxymethylcellulose is preserved in curation history.
- The `CARBON_SOURCE` role has only `COMPUTATIONAL_PREDICTION` evidence with a
  curator note that explicitly labels it a provisional name-pattern rule. No
  inspected source is attached to the nutritional role.

## Completeness

- The exact ChEBI identifier, salt CAS, merged surface forms, supplied form,
  7/7 occurrence count, SSSOM row, aggregate copy, and docs row are populated.
- Raw synonym strings from CultureMech and the merge audit retain the source
  spellings that led to this record and do not create duplicate live records.

## Recommended Edits

- Major: either replace the provisional `nutritional_roles.CARBON_SOURCE`
  evidence in `data/ingredients/mapped/Carboxymethyl_Cellulose.yaml` with
  inspected evidence for this sodium-salt record and source scope, or remove
  the role, then rerun strict validation, SSSOM QC, aggregate roundtrip, and
  `git diff --check`.
