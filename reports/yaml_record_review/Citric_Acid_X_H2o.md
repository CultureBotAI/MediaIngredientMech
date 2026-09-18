# `data/ingredients/mapped/Citric_Acid_X_H2o.yaml`

## Verdict

Needs curation; major. The live monohydrate identity is exactly grounded to
active `CHEBI:31404`; its CAS RN, formula, InChI, SMILES, 8/8 CultureMech
membership, SSSOM row, and aggregate copy agree. The record still publishes
monoanion labels as monohydrate synonyms and still carries carbon- and
energy-source roles backed only by provisional computational rules.

## Identity

- Reviewed record: `data/ingredients/mapped/Citric_Acid_X_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:31404`,
  `ontology_mapping.ontology_id: CHEBI:31404`,
  `ontology_label: Citric acid monohydrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS lookup for `Citric acid monohydrate` returns one active
  `CHEBI:31404` term labelled `Citric acid monohydrate`.
- PubChem lookup by CAS RN `5949-29-1` returns CID 22230 and the same
  citric-acid-plus-water standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Citric_Acid_X_H2o.yaml data/ingredients/mapped/Citric_Acidh2o.yaml data/ingredients/mapped/Cl.yaml data/ingredients/mapped/Cladomycin.yaml data/ingredients/mapped/Clarified_rumen_fluid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Citric_Acid_X_H2o.yaml data/ingredients/mapped/Citric_Acidh2o.yaml data/ingredients/mapped/Cl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-scoped records in this batch. `Cladomycin` and
  `Clarified_rumen_fluid` were skipped because local `kgmicrobe.compound:` and
  `MICRO:` terms are outside the focused Engine A CHEBI/OBO validation scope.
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
  `reports` found the active exact `MIM:Citric_Acid_X_H2o` SSSOM row, the
  `OK_HYDRATE_TERM` review row, the accepted duplicate-hydrate merge row,
  8 exact CultureMech membership rows, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  this active `CHEBI:31404` monohydrate record and one rejected duplicate
  tombstone for the old source label.
- Hidden/ignored-inclusive exact counting over
  `mappings/culturemech_recipe_membership.tsv` found 8 rows with total count
  8 for `CHEBI:31404`, matching the explicit 8/8 media-recipe
  `occurrence_statistics`.
- The record absorbed the exact old monohydrate source labels from the rejected
  duplicate, and the final SSSOM preserves the Fisher A 104 source label as a
  same-hydrate `other` token.
- The active SSSOM also emits `H2cit`, `citrate(1-)`, and `dihydrogen citrate`
  as final `other` synonyms. Those tokens denote the dihydrogen citrate
  monoanion, not neutral citric acid monohydrate, so they should not resolve to
  `CHEBI:31404`.
- `nutritional_roles.CARBON_SOURCE` and `nutritional_roles.ENERGY_SOURCE` each
  rely only on provisional computational references. Those references explain
  a rule-based guess; they do not cite a medium record or source text that
  establishes citric acid monohydrate as a carbon or energy source.
- The record carries no component or environment claims.

## Completeness

- The exact hydrate ChEBI identifier, CAS RN, formula, InChI, SMILES,
  CultureMech occurrence count, SSSOM row, aggregate copy, and docs row are
  populated and agree.
- The unresolved gaps are the monoanion `other` synonyms and the two
  unsupported nutritional role facets.

## Recommended Edits

- Major: in `data/ingredients/mapped/Citric_Acid_X_H2o.yaml`, remove or retype
  `H2cit`, `citrate(1-)`, and `dihydrogen citrate` so monoanion names no longer
  resolve to the neutral monohydrate in final SSSOM and label-search exports.
- Major: either attach source evidence to `CARBON_SOURCE` and `ENERGY_SOURCE`
  or remove the provisional role facets.
- After the YAML edits, regenerate the curated aggregate, final SSSOM, and docs
  products, then rerun strict validation and the SSSOM invariant checks.
