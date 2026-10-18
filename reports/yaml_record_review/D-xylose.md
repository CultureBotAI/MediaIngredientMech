# `data/ingredients/mapped/D-xylose.yaml`

## Verdict

Needs curation. The record is an exact active ChEBI match for D-xylose, its
CultureMech carbon-source role is source-backed, its 28/28 occurrence count is
traceable, and its final SSSOM `other` payload is only `CAS:58-86-6`, but the
`ENERGY_SOURCE` role is still a provisional computational assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/D-xylose.yaml`.
- Identifier and grounding: `identifier: CHEBI:65327` with
  `ontology_mapping.ontology_id: CHEBI:65327`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:65327` to active `D-xylose` with formula
  `C5H10O5`, charge `0`, mass, and the 3-star ChEBI subset marker.
- The record's `chemical_properties.cas_rn: 58-86-6` is kept out of active
  synonyms and is published in the final SSSOM row only as structured
  `CAS:58-86-6` payload.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DAMPA.yaml data/ingredients/mapped/DCMU.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DAMPA.yaml data/ingredients/mapped/DCMU.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed through `D` and then failed on `DAMPA` because its `cas:` fallback
  hit the known OAK SQL label-lookup error:
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DCMU.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-file CHEBI subset after skipping `DAMPA`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:65327 CHEBI:37492 CHEBI:75228 CHEBI:116509`:
  returned formula, charge, mass, synonyms, and xrefs for `CHEBI:65327`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 28 rows for
  `CHEBI:65327`, matching `occurrence_statistics.media_count: 28` and
  `total_occurrences: 28`.
- The `CARBON_SOURCE` role has CultureMech `DATABASE_ENTRY` evidence with the
  original role text and is supported as a media-formulation role for this
  ingredient.
- The `ENERGY_SOURCE` role is supported only by a `COMPUTATIONAL_PREDICTION`
  evidence object whose curator note calls it provisional and recommends
  review.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-xylose` to `CHEBI:65327` with `skos:exactMatch`, canonical object
  label `D-xylose`, CHEBI object source, and only `CAS:58-86-6` in `other`.
- The raw CultureMech `Cross-references:` and `Role:` / `Properties:` strings
  are filtered and do not leak into the final SSSOM row.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over `data`, `mappings`,
  `docs`, `reports`, `.claude`, `.github`, `scripts`, `src`, and `tests` found
  no second primary record or parent-mapping record for `CHEBI:65327`; the term
  appears in the D-xylose record, synchronized/generated projections, review
  surfaces, and as the D-xylose component of `NLDM_metabolites`.
- The CAS value, molecular formula, occurrence statistics, and duplicate-merge
  history are populated.
- No mixture decomposition is required for free D-xylose.

## Recommended Edits

- In `data/ingredients/mapped/D-xylose.yaml`, remove the provisional
  `ENERGY_SOURCE` role or replace its `COMPUTATIONAL_PREDICTION` evidence with
  inspected claim-level evidence.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
