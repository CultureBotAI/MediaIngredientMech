# `data/ingredients/mapped/Vitamin_Solution_Thermophilic_Formulation.yaml`

## Verdict

Needs curation. The local named-formulation identity, generic `MICRO:0000460`
close match, aggregate row, and paired final SSSOM rows pass, but the
`VITAMIN_SOURCE` role is still a provisional name-pattern inference.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Vitamin_Solution_Thermophilic_Formulation.yaml`.
- Identifier and exact local identity:
  `kgmicrobe.ingredient:vitamin_solution_~28thermophilic_formulation~29`.
- Parent grounding: `ontology_mapping.ontology_id: MICRO:0000460`, label
  `vitamin solution`, source `MICRO`, and `mapping_quality: CLOSE_MATCH`.
- `mapping_status: MAPPED` and `ingredient_type: STOCK_SOLUTION`.
- Synonyms: one raw `communitymech-unmapped` surface form,
  `Vitamin solution (thermophilic formulation)`.
- Occurrences: zero.
- Role: `VITAMIN_SOURCE` with provisional curated name-pattern evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vitamin_K1` through `Vitamins-solution`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI-primary record in this
  batch; this local `kgmicrobe.ingredient` row has no OBO adapter for that
  focused check.

## Evidence

- Fresh OLS4 exact-label search for `vitamin solution` in `MICRO` found the
  active `MICRO:0000460` class with label `vitamin solution`, supporting the
  close parent.
- The final SSSOM exports both the intended parent row,
  `MIM:Vitamin_Solution_Thermophilic_Formulation skos:closeMatch MICRO:0000460`,
  and an exact local registry row preserving
  `kgmicrobe.ingredient:vitamin_solution_~28thermophilic_formulation~29`.
- The `2026-05-05` curation history explains why a thermophilic named
  formulation is not identical to the generic vitamin solution class.

## Issues

- Major: `nutritional_roles.VITAMIN_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the curated name-pattern
  rule is provisional and still needs review.

## Completeness

- The local exact identity, MICRO close match, aggregate copy, and paired final
  SSSOM rows agree.

## Recommended Edits

- Replace or remove this record's `VITAMIN_SOURCE` role; keep it only if a
  maintained source supports the thermophilic named formulation as a vitamin
  source.
- Rerun strict validation and SSSOM invariant validation after curation.
