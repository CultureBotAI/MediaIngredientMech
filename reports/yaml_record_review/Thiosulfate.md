# `data/ingredients/mapped/Thiosulfate.yaml`

## Verdict

Needs curation. The exact `CHEBI:26977` identity, occurrence count, aggregate
row, and final SSSOM row pass, but the `ELECTRON_DONOR` role is still only a
provisional in-session LLM assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Thiosulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:26977` with the same
  `ontology_mapping.ontology_id`, label `thiosulfate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: related ChEBI thiosulfate ester and plural labels from the
  kg-microbe enrichment sweep.
- Occurrences: six CultureMech recipe occurrences in six media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thioridazine_Hydrochloride` through `Threonine`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:26977` with canonical label `thiosulfate` and the
  stored thiosulfate ester and plural related labels.
- The final SSSOM has exactly one exact row for `MIM:Thiosulfate`, points at
  `CHEBI:26977`, keeps the reviewed
  `OAK+OLS:chebi|CONFIRMED|2026-07-07` validation token, and publishes the
  stored ChEBI-related labels in `other`.
- Major: `cellular_metabolic_roles.ELECTRON_DONOR` has only
  `reference_type: COMPUTATIONAL_PREDICTION` evidence assigned by in-session
  Claude reasoning, and the curator note explicitly marks the role as
  provisional.

## Completeness

- The CHEBI identity, occurrence count, aggregate copy, and final SSSOM row
  agree.
- No components or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureMech import, duplicate
  merge, row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- Major: in `data/ingredients/mapped/Thiosulfate.yaml`, either verify
  `ELECTRON_DONOR` against inspected database or literature evidence and
  replace the provisional `COMPUTATIONAL_PREDICTION`, or remove the role. Then
  rerun strict validation, term validation, SSSOM publication, and
  `scripts/validate_sssom_invariants.py`.
