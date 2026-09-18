# `data/ingredients/mapped/Citrate.yaml`

## Verdict

Needs curation; major. The kg-microbe metatraits record is correctly grounded
to active `CHEBI:16947` citrate(3-), and its formula, InChI, SMILES, 63/63
CultureMech membership, SSSOM row, and aggregate copy agree. The record still
publishes `assimilation: citrate` as a resolving SSSOM synonym and still carries
carbon- and energy-source roles backed only by provisional computational
rules.

## Identity

- Reviewed record: `data/ingredients/mapped/Citrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16947`,
  `ontology_mapping.ontology_id: CHEBI:16947`,
  `ontology_label: citrate(3-)`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS lookup for `citrate(3-)` returns active `CHEBI:16947` labelled
  `citrate(3-)`; `CHEBI:30769` citric acid is a separate acid record.
- PubChem lookup by `citrate` returns CID 31348, formula `C6H5O7-3`, and the
  same `/p-3` standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Citraconate.yaml data/ingredients/mapped/Citraconic_Acid.yaml data/ingredients/mapped/Citramalate.yaml data/ingredients/mapped/Citrate.yaml data/ingredients/mapped/Citric_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Citraconate.yaml data/ingredients/mapped/Citraconic_Acid.yaml data/ingredients/mapped/Citramalate.yaml data/ingredients/mapped/Citrate.yaml data/ingredients/mapped/Citric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-scoped records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Citrate` SSSOM row, the OAK/OLS
  row-review confirmation, 63 exact CultureMech membership rows, and matching
  aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:16947` only in this active record.
- Exact counting over `mappings/culturemech_recipe_membership.tsv` found 63
  rows with total count 63 for `CHEBI:16947`, matching the explicit 63/63
  media-recipe `occurrence_statistics`.
- `mappings/ingredient_mappings.sssom.tsv` emits `assimilation: citrate` in the
  final `other` column, and `docs/data/label_index.csv` exposes the same text as
  a resolvable synonym. That token is a kg-microbe trait phrase, not an
  ingredient label.
- `nutritional_roles.CARBON_SOURCE` and `nutritional_roles.ENERGY_SOURCE` each
  rely only on provisional computational references. Those references explain
  a rule-based guess; they do not cite a medium record or source text that
  establishes citrate as a carbon or energy source.
- The record carries no component or environment claims.

## Completeness

- The ChEBI identifier, formula, InChI, SMILES, CultureMech occurrence count,
  SSSOM row, aggregate copy, and docs row are populated and agree.
- The unresolved gaps are the final-SSSOM trait phrase in `other` and the two
  unsupported nutritional role facets.

## Recommended Edits

- Major: in `data/ingredients/mapped/Citrate.yaml`, remove or retype
  `assimilation: citrate` so it remains provenance only and no longer reaches
  `mappings/ingredient_mappings.sssom.tsv` or label-search exports.
- Major: either attach source evidence to `CARBON_SOURCE` and `ENERGY_SOURCE`
  or remove the provisional role facets.
- After the YAML edits, regenerate the curated aggregate, final SSSOM, and docs
  products, then rerun strict validation and the SSSOM invariant checks.
