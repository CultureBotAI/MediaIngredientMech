# `data/ingredients/mapped/Tes.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:39035` identity, CAS RN, occurrence
count, aggregate row, and final SSSOM object pass, but `BUFFER` is still a
provisional name-pattern role and the final SSSOM publishes catalog and dry
preparation labels as `other` synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Tes.yaml`.
- Identifier and grounding: `identifier: CHEBI:39035` with
  `ontology_mapping.ontology_id: CHEBI:39035`, label `TES`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `7365-44-8`.
- Occurrences: 20 CultureMech recipe occurrences across 20 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tertiomycin_B` through `Tetrachloroethene`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:39035` as `TES` and lists `TES
  buffer` as a synonym.
- Fresh PubChem lookup by CAS `7365-44-8` resolves CID 81831, confirms the
  `C6H15NO6S` TES formula and InChI, and lists CAS `7365-44-8`.
- `mappings/culturemech_recipe_membership.tsv` has 20 `CHEBI:39035` rows,
  agreeing with `total_occurrences: 20` and `media_count: 20`.
- Major: the final SSSOM exact CHEBI row for `MIM:Tes` publishes
  `TES buffer(Sigma T 1375)` and `TES (Dry Buffer)` in `other`. Those are
  vendor/catalog or dry-preparation surfaces, not exact synonyms on
  `CHEBI:39035`.
- Major: `physicochemical_roles.BUFFER` cites only
  `reference_type: COMPUTATIONAL_PREDICTION` from a curated name pattern and
  explicitly notes that review is recommended.

## Completeness

- The CHEBI identity, CAS RN, occurrence count, aggregate row, and final SSSOM
  object all agree.
- The role and synonym payload are incomplete until the provisional buffer role
  is reviewed and non-synonym raw surfaces stop exporting in `other`.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureMech import,
  duplicate merge, residual-alias backfill, occurrence refresh, aggregate, final
  SSSOM, and row-review rows.

## Recommended Edits

- Major: remove `TES buffer(Sigma T 1375)` and `TES (Dry Buffer)` as active
  synonyms from `data/ingredients/mapped/Tes.yaml`, or retype them as
  provenance that the SSSOM builder will not export for the TES subject.
- Major: replace the provisional name-pattern `BUFFER` role with source-backed
  evidence for TES as a buffer, or remove the role if no maintained source
  supports it.
- Major: regenerate `mappings/ingredient_mappings.sssom.tsv` so the exact
  CHEBI row for `MIM:Tes` no longer publishes the catalog or dry-preparation
  labels in `other`.
