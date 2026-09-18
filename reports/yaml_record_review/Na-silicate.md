# `data/ingredients/mapped/Na-silicate.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:60720` sodium silicate identity,
CAS-backed structure, source-backed mineral role, occurrence count, and hydrate
synonym rejection pass, but final SSSOM still publishes a numbered sodium
metasilicate list item as an unconstrained synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-silicate.yaml`.
- Identifier and grounding: `identifier: CHEBI:60720` with
  `ontology_mapping.ontology_id: CHEBI:60720`, label `sodium silicate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 218 CultureMech recipe occurrences across 218 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-orotate` through `Na-silicate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:60720` as active `sodium silicate`,
  with `cas:1344-09-8`, formula `2Na.O3Si`, the stored structure, and the
  accepted broad sodium silicate synonyms.
- The `MINERAL_SOURCE` facet is source-backed by CultureMech original role text
  that explicitly says `Mineral source`.
- The #251 cleanup correctly marks `Na2SiO3 x 5 H2O` as `REJECTED_LABEL`, so
  the sodium-metasilicate pentahydrate label no longer collapses into the
  anhydrous sodium silicate SSSOM row.
- Major: the final SSSOM row `MIM:Na-silicate` publishes
  `(5)  Sodium metasilicate` in `other`. The leading list marker makes this a
  source artifact, not a synonym for `CHEBI:60720`.

## Completeness

- The active ChEBI target, canonical CAS RN, formula, structure, 218/218
  occurrence count, source-backed `MINERAL_SOURCE` role, and hydrate-synonym
  rejection agree.
- The only consequential gap is the numbered source artifact that still reaches
  final SSSOM `other`.

## Recommended Edits

- Major: demote `(5)  Sodium metasilicate` in
  `data/ingredients/mapped/Na-silicate.yaml` so it remains source provenance
  rather than a publishable exact synonym, then rebuild final SSSOM and re-run
  final SSSOM validation plus product label validation.
