# `data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml`

## Verdict

Needs curation. The local stock-solution identity and final local registry rows
are synchronized, but this named stock still lacks component-level
representation and its `VITAMIN_SOURCE` role is only a provisional
name-pattern prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:thiamine_vitamin_solution`, close parent
  `MICRO:0000460`, source `MICRO`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, `kg_microbe_node_id:
  kgmicrobe.ingredient:thiamine_vitamin_solution`, and `ingredient_type:
  STOCK_SOLUTION`.
- Synonyms: raw CultureMech label `Thiamine Vitamin Solution`.
- Occurrences: 14 CultureMech recipe occurrences in 14 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thiamine-hcl_X_2_H2o` through `Thiamine_monophosphate`: exited 0 and wrote
  zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this local/MICRO row
  because its exact `kgmicrobe.ingredient` ID and close `MICRO` parent are
  outside the CHEBI-focused term-validator subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- The `ingredient_mapping_review_2026-05-05` curation event correctly moved
  this formulation variant off exact `MICRO:0000460` and retained that generic
  vitamin-solution term only as a close match.
- The unknown-term triage for the final SSSOM accepts the
  `kgmicrobe.ingredient:thiamine_vitamin_solution` exact registry row as an
  expected local identity and marks the `MICRO:0000460` unknown-term result as
  a prefix-dispatch coverage gap, not a bad CURIE.
- Major: `nutritional_roles.VITAMIN_SOURCE` has only
  `reference_type: COMPUTATIONAL_PREDICTION` evidence inferred from a curated
  name-pattern rule and the curator note explicitly marks the role as
  provisional.

## Completeness

- The final SSSOM has both expected rows for
  `MIM:Thiamine_Vitamin_Solution`: a `skos:closeMatch` row to
  `MICRO:0000460` and an exact local registry row preserving
  `kgmicrobe.ingredient:thiamine_vitamin_solution`.
- Major: the record is a `STOCK_SOLUTION`, but it does not assert any
  components or a `component_assertion`; the exact formula behind the thiamine
  vitamin solution remains unrepresented.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureMech import,
  local-identity correction, unknown-term triage, aggregate, and final SSSOM
  rows.

## Recommended Edits

- Major: in `data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml`, curate
  the stock recipe into `components` plus `component_assertion` if the
  underlying source defines its ingredients. If the source really only names an
  opaque stock, annotate that bounded absence explicitly.
- Major: replace or remove the provisional `VITAMIN_SOURCE` role evidence.
  Then rerun strict validation, SSSOM publication, unknown-term triage,
  component partonomy validation, and `scripts/validate_sssom_invariants.py`.
