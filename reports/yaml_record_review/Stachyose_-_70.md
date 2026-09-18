# `data/ingredients/mapped/Stachyose_-_70.yaml`

## Verdict

Needs curation - major. The record exact-maps a `70%` stachyose preparation to
pure `CHEBI:17164`, exports sibling hydrate text as a synonym, and still has a
provisional carbon-source role.

## Identity

- Reviewed record: `data/ingredients/mapped/Stachyose_-_70.yaml`.
- Identifier and grounding: `identifier: CHEBI:17164` with
  `ontology_mapping.ontology_id: CHEBI:17164`, label `stachyose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: `cas_rn: 470-55-3` and formula `C24H42O21`.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sporangiomycin` through `Stachyose_Hydrate`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:17164` with label `stachyose` and
  the long glycoside exact synonym retained in YAML.
- PubChem resolves CAS `470-55-3` to CID `439531`, with formula `C24H42O21`
  and the same stereospecific InChI stored on this record.
- Major: the preferred term `Stachyose - 70%` denotes a purity-qualified
  supplied product, not pure CHEBI stachyose. If the CAS evidence was for the
  solute, that should not be used to erase the 70% formulation boundary.
- Major: the final SSSOM `other` column publishes `Stachyose hydrate`, which is
  a distinct sibling `Stachyose_Hydrate` subject with its own CAS and only a
  `skos:closeMatch` to anhydrous stachyose.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by
  `COMPUTATIONAL_PREDICTION` from CHEBI carbohydrate ancestry, with the
  provisional curator note.

## Completeness

- The anhydrous CAS, formula, and CHEBI synonym are internally consistent for
  stachyose itself, but the active record needs a bounded decision about what
  the `70%` source label denotes.

## Recommended Edits

- Major: re-evaluate whether `Stachyose - 70%` should merge into an anhydrous
  stachyose record as source provenance, become a distinct local preparation,
  or be retired in favor of the hydrate record; then update the exact mapping
  and regenerated SSSOM row accordingly.
- Major: remove `Stachyose hydrate` from this record's exported synonym set so
  the anhydrous/purity-qualified row does not claim its sibling hydrate as a
  same-subject alias.
- Major: remove `nutritional_roles.CARBON_SOURCE` or replace the provisional
  carbohydrate-ancestry assertion with source evidence that uses this supplied
  stachyose form as a carbon source.
