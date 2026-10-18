# `data/ingredients/mapped/Threonine.yaml`

## Verdict

Needs curation. The MicrobeDecoder exact match to `CHEBI:26986`, CultureMech
occurrence count, aggregate row, and final SSSOM row identity pass, but the
related stereo label `DL-threonine` is exported in final SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Threonine.yaml`.
- Identifier and grounding: `identifier: CHEBI:26986` with the same
  `ontology_mapping.ontology_id`, label `threonine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: one `RELATED_SYNONYM`, `DL-threonine`, for a racemate narrower than
  the stereo-unspecified parent.
- Chemical properties: formula `C4H9NO3`, InChI, and molecular weight from
  `ChEBI+PubChem`.
- Occurrences: 22 CultureMech recipe occurrences in 22 media, with 31
  MicrobeDecoder BacDive utilization occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thioridazine_Hydrochloride` through `Threonine`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:26986` with canonical label `threonine`, supporting
  the imported MicrobeDecoder exact-label match.
- The #260 curation event explicitly marked `DL-threonine` as
  `RELATED_SYNONYM` rather than exact because the racemate is narrower than the
  stereo-unspecified parent and is not the active `L-Threonine` sibling.
- Major: the final SSSOM has exactly one row for `MIM:Threonine` and correctly
  points at `CHEBI:26986`, but it publishes `DL-threonine` in `other`, which
  flattens the intentionally related stereo synonym into the exact-synonym
  surface.

## Completeness

- The CHEBI identity, occurrence count, aggregate copy, and final SSSOM row
  identity agree.
- No components or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected MicrobeDecoder import, #260
  synonym addition, active `L-Threonine` sibling, aggregate, and final SSSOM
  rows.

## Recommended Edits

- Major: update the SSSOM synonym export so `RELATED_SYNONYM` values such as
  `DL-threonine` do not publish in exact `other`, or rehome the racemate to a
  bounded exact record if exact upstream grounding is desired. Then rerun
  strict validation, term validation, SSSOM publication, synonym-row review,
  and `scripts/validate_sssom_invariants.py`.
