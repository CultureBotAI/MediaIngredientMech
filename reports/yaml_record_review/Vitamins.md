# `data/ingredients/mapped/Vitamins.yaml`

## Verdict

Needs curation. The record is synchronized with the aggregate export and still
points at active `CHEBI:33229`, but `CHEBI:33229` is the abstract ChEBI
`vitamin (role)` class rather than a substance or preparation identity for a
media ingredient. The final SSSOM also exports the formulation-qualified
surface form `Vitamins (ATCC)` as an exact `other` synonym for that role.

## Identity

- Reviewed record: `data/ingredients/mapped/Vitamins.yaml`.
- Identifier and grounding: `identifier: CHEBI:33229` with matching
  `ontology_mapping.ontology_id`, label `vitamin (role)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Synonyms: one raw CultureMech occurrence surface form, `Vitamins (ATCC)`.
- Occurrences: three CultureMech recipe occurrences across three media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Vitamins` through `Voso4_X_5_H2o`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the three
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:33229` returns active label `vitamin (role)` and
  defines the term as a biochemical role played by micronutrients.
- The same OLS4 lookup includes `vitamins` as a related synonym of the ChEBI
  role, explaining the restored CultureMech lexical match.
- The final SSSOM row has
  `MIM:Vitamins skos:exactMatch CHEBI:33229` and exports `Vitamins (ATCC)` in
  `other`.

## Issues

- Major: the media ingredient surface `Vitamins` is asserted as an exact match
  to an abstract role class. A vitamin mixture or unspecified vitamin additive
  should not be identical to the biochemical role played by vitamin compounds.
- Major: the final SSSOM row exports `Vitamins (ATCC)` as an exact `other`
  synonym. That parenthetical names a source or formulation context and is not
  a clean synonym for the ChEBI role.

## Completeness

- The aggregate row and final SSSOM row agree with the per-record YAML.
- The record needs a material identity, likely a local stock-solution or
  mixture record, rather than a role-class exact match.

## Recommended Edits

- Remap `Vitamins` away from `CHEBI:33229`; preserve any relation to
  `vitamin (role)` as role semantics instead of an exact ingredient identity if
  that relation is still useful.
- Remove or suppress `Vitamins (ATCC)` from final SSSOM `other`.
- Rebuild SSSOM and rerun strict validation, LinkML term validation, SSSOM
  invariant validation, and the cross-record `other` synonym audit.
