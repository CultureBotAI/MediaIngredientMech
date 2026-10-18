# `data/ingredients/mapped/D-mannose.yaml`

## Verdict

Needs curation. The `CHEBI:16024` D-mannose identity, CultureMech carbon role,
12/12 occurrence count, PubChem-backed CAS payload, and final SSSOM synonyms
pass, but the `ENERGY_SOURCE` role is still only a provisional computational
assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/D-mannose.yaml`.
- Identifier and grounding: `identifier: CHEBI:16024` with
  `ontology_mapping.ontology_id: CHEBI:16024`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:16024` to `D-mannose` with formula `C6H12O6`,
  charge `0`, and `D-manno-hexose` as an exact synonym.
- PubChem resolves `CAS:530-26-7` to `D-Mannose`, formula `C6H12O6`, and
  InChIKey `WQZGKKKJIJFFOK-QTVWNMPRSA-N`, supporting the CAS value published
  in SSSOM `other`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-histidine.yaml data/ingredients/mapped/D-limonene.yaml data/ingredients/mapped/D-malate.yaml data/ingredients/mapped/D-mannitol.yaml data/ingredients/mapped/D-mannose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-histidine.yaml data/ingredients/mapped/D-malate.yaml data/ingredients/mapped/D-mannitol.yaml data/ingredients/mapped/D-mannose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-file CHEBI subset. `D-limonene` was skipped because its `cas:`
  fallback crashes the OAK SQL label lookup with
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27947 CHEBI:15588 CHEBI:16899 CHEBI:16024`:
  returned formula, charge, mass, and synonyms for `CHEBI:16024`.
- `curl -L ... /compound/name/530-26-7/property/.../JSON`: PubChem resolved
  the record's CAS value to `D-Mannose`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` contains 12 rows for
  `CHEBI:16024`, matching `occurrence_statistics.media_count: 12` and
  `total_occurrences: 12`.
- The `CARBON_SOURCE` role has CultureMech `DATABASE_ENTRY` evidence with the
  original role text and is supported as a media-formulation role for this
  ingredient.
- The `ENERGY_SOURCE` role is supported only by a `COMPUTATIONAL_PREDICTION`
  evidence object whose curator note calls it provisional and recommends
  review.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-mannose` to `CHEBI:16024` with `skos:exactMatch`, canonical object
  label `D-mannose`, CHEBI object source, and the same-subject tokens
  `D-manno-hexose|CAS:530-26-7` in `other`.
- The raw CultureMech `Cross-references:` and `Role:` / `Properties:` strings
  are filtered and do not leak into the final SSSOM row.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`
  surfaces found no second primary record or parent-mapping record for
  `CHEBI:16024`.
- CAS, molecular formula, occurrence statistics, and the duplicate-merge /
  CAS-conflict history are populated.
- No mixture decomposition is required for the free D-mannose record.

## Recommended Edits

- In `data/ingredients/mapped/D-mannose.yaml`, remove the provisional
  `ENERGY_SOURCE` role or replace its `COMPUTATIONAL_PREDICTION` evidence with
  inspected claim-level evidence.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-mannose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
