# `data/ingredients/mapped/Citric_Acid.yaml`

## Verdict

Needs curation; major. The CultureMech citric acid identity is exactly grounded
to active `CHEBI:30769`; its CAS RN, formula, InChI, SMILES, 110/113
CultureMech membership, SSSOM row, and aggregate copy agree. The record still
exports the separate `Citrate` anion record as an exact synonym for the acid
and carries carbon- and energy-source roles backed only by provisional
computational rules.

## Identity

- Reviewed record: `data/ingredients/mapped/Citric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30769`,
  `ontology_mapping.ontology_id: CHEBI:30769`,
  `ontology_label: citric acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS lookup for `citric acid` returns active `CHEBI:30769` labelled
  `citric acid`; `CHEBI:16947` citrate(3-), `CHEBI:31404` citric acid
  monohydrate, and `CHEBI:53258` sodium citrate are distinct active siblings.
- PubChem lookup by CAS RN `77-92-9` returns CID 311, formula `C6H8O7`, and the
  same standard InChI stored in `chemical_properties`.

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
  `reports` found the active exact `MIM:Citric_Acid` SSSOM row, the OAK/OLS
  synonym-enrichment rows, a cross-record `Citrate` baseline row, 110 exact
  CultureMech membership rows, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:30769` only in this active acid record; it also found separate
  monohydrate records that preserve the same ChEBI parent as a close or hidden
  hydrate relationship rather than exact synonyms.
- Exact counting over `mappings/culturemech_recipe_membership.tsv` found 110
  rows with total count 113 for `CHEBI:30769`, matching the explicit 113/110
  media-recipe `occurrence_statistics`.
- `synonyms` still includes `Citrate` as an active exact synonym from the 2026
  manual backfill, and the final SSSOM row publishes `Citrate` in `other`.
  `Citrate` is already an active preferred term for
  `data/ingredients/mapped/Citrate.yaml` grounded to `CHEBI:16947`
  citrate(3-), so this synonym collapses two distinct acid/anion records in
  label search and final SSSOM output.
- The bare `(trisodium salt)` and `Properties:` CultureMech imports are
  filtered before final SSSOM export, and the two hidden hydrate labels are
  correctly typed as `REJECTED_LABEL`.
- `nutritional_roles.CARBON_SOURCE` and `nutritional_roles.ENERGY_SOURCE` each
  rely only on provisional computational references. Those references explain
  a rule-based guess; they do not cite a medium record or source text that
  establishes citric acid as a carbon or energy source.
- The record carries no component or environment claims.

## Completeness

- The exact ChEBI identifier, CAS RN, formula, InChI, SMILES, curated ChEBI
  synonyms other than `Citrate`, CultureMech occurrence count, SSSOM row,
  aggregate copy, and docs row are populated and agree.
- The unresolved gaps are the cross-record anion synonym and the two
  unsupported nutritional role facets.

## Recommended Edits

- Major: in `data/ingredients/mapped/Citric_Acid.yaml`, remove or retype the
  `Citrate` synonym so the final SSSOM no longer exports an active preferred
  term for `CHEBI:16947` as an exact `CHEBI:30769` acid synonym.
- Major: either attach source evidence to `CARBON_SOURCE` and `ENERGY_SOURCE`
  or remove the provisional role facets.
- After the YAML edits, regenerate the curated aggregate, final SSSOM, and docs
  products, then rerun strict validation and the SSSOM invariant checks.
