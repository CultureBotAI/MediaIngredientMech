# `data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml`

## Verdict

Pass with minor issues. The exact CultureMech residual grounding to the NCIT
hydroxocobalamin hydrochloride term and final SSSOM row pass, but the record is
missing `ingredient_type`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml`.
- Identifier and grounding: `identifier: NCIT:C217966` with
  `ontology_mapping.ontology_id: NCIT:C217966`, label
  `Hydroxocobalamin Hydrochloride`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Source occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydrogen_gas.yaml data/ingredients/mapped/Hydroquinone.yaml data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml data/ingredients/mapped/Hydroxy-l-proline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation was run for the four CHEBI records in this
  batch and skipped for `Hydroxocobalamin_hydrochloride` because its exact
  target is an NCIT CURIE outside the local CHEBI/OBO subset used for
  per-record label checks.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1501`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1501`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `NCIT:C217966` as the active NCIT class
  `Hydroxocobalamin Hydrochloride`.
- The CultureMech source label exact-matches the NCIT label after
  case-normalization and the final SSSOM publishes one `skos:exactMatch` row
  from `MIM:Hydroxocobalamin_hydrochloride` to `NCIT:C217966`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, and docs projections.
- Minor: the exact residual-grounding record is missing `ingredient_type`,
  leaving it out of the otherwise standard chemical/ingredient classifier
  surface.

## Completeness

- The active NCIT identifier, occurrence count, claim-level grounding evidence,
  aggregate copy, and final SSSOM row are present and consistent.
- No unsupported roles or noisy final synonyms are asserted.

## Recommended Edits

- Minor: classify `Hydroxocobalamin_hydrochloride` with the maintained
  ingredient-type workflow, then rerun strict, round-trip, id-label, component,
  and SSSOM validation.
