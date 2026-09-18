# `data/ingredients/mapped/Hydro_Methylpteroylglutamylglutamic_Acid.yaml`

## Verdict

Needs curation. The local exact registry row preserves the KG-Microbe placeholder
text, but the `skos:narrowMatch` to NCIT `Glutamic Acid` is only a bad
stem-substring parent and a separate MIM record already carries the exact MeSH
identity for the same KG-Microbe source ID.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Hydro_Methylpteroylglutamylglutamic_Acid.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:hydro_methylpteroylglutamylglutamic_acid`
  with `ontology_mapping.ontology_id: NCIT:C1115`, label `Glutamic Acid`,
  source `NCIT`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydrastine_1r_9s.yaml data/ingredients/mapped/Hydro_Methylpteroylglutamylglutamic_Acid.yaml data/ingredients/mapped/Hydrocarbon.yaml data/ingredients/mapped/Hydrogen_Peroxide.yaml data/ingredients/mapped/Hydrogen_Sulfide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation was run for the four CHEBI records in this
  batch and skipped for `Hydro_Methylpteroylglutamylglutamic_Acid` because its
  parent target is an NCIT CURIE outside the local CHEBI/OBO subset used for
  per-record label checks.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1454`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1454`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `NCIT:C1115` as active `Glutamic Acid`, so the CURIE itself is
  valid.
- OLS4 search for `Hydro Methylpteroylglutamylglutamic Acid` returns
  `mesh:C052093`, `7-hydro-8-methylpteroylglutamylglutamic acid`; the hidden
  and ignored-inclusive search also found
  `data/ingredients/mapped/7-Hydro-8-methylpteroylglutamylglutamic_Acid.yaml`,
  an exact MeSH-grounded record created from the same
  `kgmicrobe.compound:hydro_methylpteroylglutamylglutamic_acid` source ID.
- Major: `Glutamic Acid` was selected only by a stem-substring backfill even
  though the subject string names a pteroylglutamylglutamic acid derivative,
  not a narrower glutamic-acid class.
- The final SSSOM publishes a `skos:narrowMatch` row from
  `MIM:Hydro_Methylpteroylglutamylglutamic_Acid` to `NCIT:C1115` plus the
  expected exact local `kgmicrobe.compound` registry row.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate rows, final SSSOM rows, docs projections, NCIT prefix-validation
  row, and row-review manifest entries.

## Completeness

- The exact local registry companion row is present and structurally consistent.
- The record is incomplete until the invalid NCIT parent is removed and the
  duplicate/abbreviated placeholder relationship to the existing exact
  `mesh:C052093` record is resolved.

## Recommended Edits

- Major: remove the `NCIT:C1115` parent `narrowMatch`, merge or reject this
  local placeholder against
  `data/ingredients/mapped/7-Hydro-8-methylpteroylglutamylglutamic_Acid.yaml`
  as appropriate, regenerate the SSSOM, and rerun strict, round-trip, id-label,
  duplicate-id, component, and SSSOM validation.
