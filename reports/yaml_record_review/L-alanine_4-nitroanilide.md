# `data/ingredients/mapped/L-alanine_4-nitroanilide.yaml`

## Verdict

Needs curation. The local registry fallback shape and exact final SSSOM row are
internally consistent, but live OLS now returns a plausible MeSH candidate for
the label that postdates the #213 fallback review.

## Identity

- Reviewed record: `data/ingredients/mapped/L-alanine_4-nitroanilide.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:l-alanine_4-nitroanilide` with matching
  `ontology_mapping.ontology_id`, label `L-alanine 4-nitroanilide`, source
  `kgmicrobe.compound`, `mapping_quality: FALLBACK_REGISTRY`, `mapping_status:
  MAPPED`, and no chemical properties block.
- This record intentionally denotes an exact local compound identity rather
  than a broad ChEBI 4-nitroanilide class.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-_-erythrulose.yaml data/ingredients/mapped/L-_-sorbose.yaml data/ingredients/mapped/L-alaninamide.yaml data/ingredients/mapped/L-alanine.yaml data/ingredients/mapped/L-alanine_4-nitroanilide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 ChEBI records; Engine A was
  intentionally skipped for this `kgmicrobe.compound` fallback.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- The #213 curation evidence explains why the record was minted as a
  self-referential `kgmicrobe.compound` fallback instead of being overclaimed as
  a 4-nitroanilide functional-group class.
- The final SSSOM publishes exactly one `skos:exactMatch` row to
  `kgmicrobe.compound:l-alanine_4-nitroanilide` with no `other` synonym noise.
- Major: live EBI OLS4 exact search for `L-alanine 4-nitroanilide` now returns
  `mesh:C004813` with label `alanine-4-nitroanilide`. A curator needs to
  inspect that MeSH entry to determine whether it preserves the L-alanine
  stereochemistry; if it does, this local fallback should be regrounded, and if
  it does not, the negative search evidence should be refreshed.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM row, docs
  projections, MicrobeDecoder source rows, and older generated review warnings
  from before local `kgmicrobe.compound` CURIEs were allowed.

## Completeness

- The local identifier, exact fallback SSSOM row, MicrobeDecoder source
  occurrence count, empty occurrence count, and aggregate copy are present and
  consistent.
- The ontology search status is incomplete until the new MeSH candidate is
  accepted or rejected with inspected evidence.

## Recommended Edits

- Major: inspect `mesh:C004813`; either reground
  `data/ingredients/mapped/L-alanine_4-nitroanilide.yaml` to that term or record
  why it is broader than the L-specific MIM subject and keep the local fallback.
- Rerun strict, term, round-trip, component, and SSSOM validation after that
  decision.
