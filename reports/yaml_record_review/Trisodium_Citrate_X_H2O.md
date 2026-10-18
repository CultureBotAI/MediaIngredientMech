# `data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml`

## Verdict

Needs curation, major. The MeSH `trisodium citrate` fallback resolves, but the
source label names a monohydrate while the exact SSSOM row collapses it to a
generic non-hydrate MeSH concept, and both nutritional roles are still
provisional computational evidence.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml`.
- Identifier and grounding: `identifier: mesh:C514290` with matching
  `ontology_mapping.ontology_id`, label `trisodium citrate`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Synonyms: one raw mim-queue label.
- Occurrences: 2 MediaDive-derived occurrences in 2 media.
- Roles: provisional `nutritional_roles.CARBON_SOURCE` and `ENERGY_SOURCE`
  facets.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tris_Base` through `Trithionate`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- The record history shows an automatic MeSH upgrade via name normalization to
  `Trisodium citrate`, and the final row review already classified the
  SSSOM `UNKNOWN_TERM` stamp as missing prefix-validator coverage rather than a
  bad CURIE.
- Fresh CHEBI-scoped OLS4 exact search for `sodium citrate monohydrate`
  returned zero rows, while neighboring sodium citrate dihydrate rows now use
  hydrate-specific `CHEBI:32142`.
- The final SSSOM row has
  `MIM:Trisodium_Citrate_X_H2O skos:exactMatch mesh:C514290`, losing the
  monohydrate state in the source label.

## Issues

### Major: the hydrate label is exact-mapped to generic trisodium citrate

`Trisodium citrate x H2O` denotes a monohydrate, but `mesh:C514290`
represents trisodium citrate without preserving the one-water supplied form.
The exact mapping loses the hydrate boundary in the final SSSOM.

### Major: both nutritional roles are provisional computational evidence

The only role assertions are `COMPUTATIONAL_PREDICTION` entries from a
name-pattern carbon-source rule and a canonical energy-substrate inference.
Neither is curated evidence for this hydrate record.

## Completeness

- The per-record YAML, aggregate copy, and final SSSOM row agree on the
  current generic MeSH mapping.
- The missing work is to model the monohydrate distinctly and either support or
  remove the provisional nutritional roles.

## Recommended Edits

- Replace the exact MeSH mapping with a distinct monohydrate identity, likely a
  `kgmicrobe.compound` registry term with an honest broader mapping to
  trisodium citrate until a form-specific ontology term exists.
- Replace the `CARBON_SOURCE` and `ENERGY_SOURCE` computational predictions
  with curated evidence, or remove `nutritional_roles` until such support is
  added.
