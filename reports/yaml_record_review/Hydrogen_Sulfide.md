# `data/ingredients/mapped/Hydrogen_Sulfide.yaml`

## Verdict

Needs curation. The exact ChEBI hydrogen-sulfide identity passes, but the record
publishes a process-qualified raw label as an exact synonym and still carries
unsupported environmental and reducing-agent assertions.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydrogen_Sulfide.yaml`.
- Identifier and grounding: `identifier: CHEBI:16136` with
  `ontology_mapping.ontology_id: CHEBI:16136`, label `hydrogen sulfide`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `H2S`, InChI `InChI=1S/H2S/h1H2`, and SMILES
  `[H]S[H]`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydrastine_1r_9s.yaml data/ingredients/mapped/Hydro_Methylpteroylglutamylglutamic_Acid.yaml data/ingredients/mapped/Hydrocarbon.yaml data/ingredients/mapped/Hydrogen_Peroxide.yaml data/ingredients/mapped/Hydrogen_Sulfide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydrogen_Sulfide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1454`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1454`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:16136` as the active ChEBI class `hydrogen sulfide` and
  lists the three curated ChEBI synonyms as exact synonyms.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hydrogen_Sulfide` to `CHEBI:16136`.
- Major: `produces: hydrogen sulfide` is a process-qualified trait/source
  label, not an exact synonym of hydrogen sulfide, but it is stored as
  `RAW_TEXT` and exported beside the legitimate ChEBI synonyms in the SSSOM
  `other` column.
- Major: `physicochemical_roles.REDUCING_AGENT` has only provisional
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule.
- Major: the marine hydrothermal vent `ENVIRONMENT_MIMIC` assertion has a
  plausible note, but no cited evidence attached to the context claim.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the CHEBI mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, formula, InChI, SMILES, ChEBI synonyms,
  aggregate copy, and final exact-match row are present and consistent.
- The record is incomplete until the process-qualified raw label is removed
  from the exported exact-synonym surface and the role/context claims are either
  supported with claim-level sources or removed.

## Recommended Edits

- Major: remove `produces: hydrogen sulfide` from active exported synonyms or
  keep it only as non-exported source provenance, regenerate the SSSOM, and
  rerun strict, term, round-trip, id-label, component, and SSSOM validation.
- Major: remove `physicochemical_roles.REDUCING_AGENT` and the marine
  hydrothermal vent environmental context unless inspected sources can support
  those exact hydrogen sulfide claims.
