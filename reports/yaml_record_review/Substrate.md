# `data/ingredients/mapped/Substrate.yaml`

## Verdict

Needs curation - major. `NCIT:C120264` now resolves and exact-matches the
stored label, but the record models a functional reaction placeholder as a
`SINGLE_INGREDIENT`.

## Identity

- Reviewed record: `data/ingredients/mapped/Substrate.yaml`.
- Identifier and grounding: `identifier: NCIT:C120264` with
  `ontology_mapping.ontology_id: NCIT:C120264`, label `Substrate`, source
  `NCIT`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 5 occurrences across 5 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Substrate` through `Sucrose-6-monophosphate_Dipotassium_Salt`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this NCIT record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh prefix-specific OLS4 lookup resolves active `NCIT:C120264` with label
  `Substrate`, matching the stored target and the existing external-prefix
  OLS triage row.
- The NCIT definition describes any chemical that can be consumed or modified
  in a chemical reaction or biological process; it is a role-like placeholder,
  not an exact orderable medium ingredient.
- The final SSSOM row exact-matches `NCIT:C120264` and leaves `other` empty.

## Completeness

- The NCIT CURIE, aggregate row, 5/5 CultureMech occurrence count, and final
  SSSOM row agree.
- An ignored/hidden search of local curated, mapping, generated, report, source,
  and documentation paths found only the `mim-queue` import provenance, the
  five recipe-membership rows, and generated/triage products for this record;
  it found no narrower curated identity for `mediadive.ingredient:672`.

## Recommended Edits

- Major: inspect the five CultureMech `Substrate` occurrences behind
  `NCIT:C120264` and either split them to concrete ingredients, reject the
  placeholder if it is not a supplied ingredient, or remodel it as a deliberate
  generic class instead of `ingredient_type: SINGLE_INGREDIENT`.
