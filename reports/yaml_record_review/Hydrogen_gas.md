# `data/ingredients/mapped/Hydrogen_gas.yaml`

## Verdict

Needs curation. The exact ChEBI dihydrogen identity passes, but mixture labels,
a typo, and a process-qualified trait label are active synonyms and are
published in the final SSSOM `other` column.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydrogen_gas.yaml`.
- Identifier and grounding: `identifier: CHEBI:18276` with
  `ontology_mapping.ontology_id: CHEBI:18276`, label `dihydrogen`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `H2`, InChI `InChI=1S/H2/h1H`, and SMILES
  `[H][H]`.
- Source occurrences: 243 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydrogen_gas.yaml data/ingredients/mapped/Hydroquinone.yaml data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml data/ingredients/mapped/Hydroxy-l-proline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydrogen_gas.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1501`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1501`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:18276` as the active ChEBI class `dihydrogen`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Hydrogen_gas` to `CHEBI:18276`.
- Major: `H2_CO2` and `H2_methanol` are mixture labels represented by their own
  componentized records, not synonyms of hydrogen gas, but they are stored as
  `EXACT_SYNONYM` and exported in final `other`.
- Major: `Diydrogen` is retained as a typo provenance token and
  `aerobic catabolization: dihydrogen` is process-qualified trait text; neither
  is an exact synonym of dihydrogen, but both are published in final `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, synonym-enrichment review
  row, and decomposed `H2_*` records that use `CHEBI:18276` as a component.

## Completeness

- The active ChEBI identifier, H2 formula, InChI, SMILES, occurrence count,
  aggregate copy, and final exact-match row are present and consistent.
- The record is incomplete until mixture labels, typo text, and process text are
  moved out of the exported exact-synonym surface.

## Recommended Edits

- Major: remove `H2_CO2`, `H2_methanol`, `Diydrogen`, and
  `aerobic catabolization: dihydrogen` from active exported synonyms or keep
  them only as non-exported provenance, regenerate the SSSOM, and rerun strict,
  term, round-trip, id-label, component, and SSSOM validation.
