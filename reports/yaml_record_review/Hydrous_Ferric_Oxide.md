# `data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml`

## Verdict

Needs curation. The source label is hydrous ferric oxide, but the record and
final SSSOM exact-match the anhydrous ChEBI `ferric oxide` class and export
anhydrous iron oxide synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml`.
- Identifier and grounding: `identifier: CHEBI:50819` with
  `ontology_mapping.ontology_id: CHEBI:50819`, label `ferric oxide`, source
  `CHEBI`, `mapping_quality: LEXICAL_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `Fe2O3`, InChI `InChI=1S/2Fe.3O`, and SMILES
  `[O]=[Fe][O][Fe]=[O]`.
- Source occurrences: 50 CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydrogen_gas.yaml data/ingredients/mapped/Hydroquinone.yaml data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml data/ingredients/mapped/Hydroxy-l-proline.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1501`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1501`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:50819` as the active ChEBI class `ferric oxide` and
  lists only anhydrous iron(III) oxide labels as exact synonyms.
- Major: hydrous ferric oxide is a hydrated oxide form, but the record stores
  the anhydrous `Fe2O3` structure and publishes an exact `skos:exactMatch` to
  `CHEBI:50819`.
- The final SSSOM exports the anhydrous synonyms `diiron trioxide`,
  `iron(3+) oxide`, and `iron(III) oxide` on the hydrous source subject.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and synonym-enrichment
  row.

## Completeness

- The CultureMech occurrence count, aggregate copy, and final SSSOM row are
  present.
- The record is incomplete until the hydrous source form is modeled distinctly
  from anhydrous ferric oxide.

## Recommended Edits

- Major: remap hydrous ferric oxide to a distinct local registry identifier, or
  to an exact external hydrous-ferric-oxide term if one is found, and keep
  `CHEBI:50819` only as a broader or related anhydrous oxide target if that
  relationship is chemically justified; then regenerate the SSSOM and rerun
  strict, term, round-trip, id-label, component, and SSSOM validation.
