# `data/ingredients/mapped/Tetramethyl_Ammonium.yaml`

## Verdict

Pass. The 2026-09 whole-substance remint from the tetramethylammonium cation to
a local compound with active `CHEBI:35273` as a broad parent is synchronized,
the cation-only chemistry was cleared, and the final SSSOM has the expected
parent and exact local registry rows.

## Identity

- Reviewed record: `data/ingredients/mapped/Tetramethyl_Ammonium.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:tetramethyl_ammonium` with
  `ontology_mapping.ontology_id: CHEBI:35273`, label
  `quaternary ammonium salt`, source `CHEBI`, `mapping_quality:
  NARROW_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- Chemical properties: intentionally empty after the 2026-09 cation-overclaim
  repair.
- Occurrences: 4 CultureMech recipe occurrences across 4 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetracycline` through `Tetramethyl_Ammonium_Chloride`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:35273` as `quaternary ammonium salt`.
- `mappings/culturemech_recipe_membership.tsv` has four
  `kgmicrobe.compound:tetramethyl_ammonium` rows, agreeing with
  `total_occurrences: 4` and `media_count: 4`.
- The final SSSOM publishes the expected `skos:narrowMatch` row to
  `CHEBI:35273` and an exact local registry sibling row to
  `kgmicrobe.compound:tetramethyl_ammonium`.
- The raw `Role:`/`Properties:` strings and rejected cation labels in the YAML
  do not leak into either final SSSOM row's `other` field.

## Completeness

- The local whole-substance identity, CHEBI parent, occurrence count, aggregate
  row, cleared chemistry, and final SSSOM rows agree.
- The record has no components, roles, or environmental contexts needing
  narrower evidence.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected salt-ion repair, aggregate,
  occurrence-membership, final SSSOM, tests, and generated rows.

## Recommended Edits

- None.
