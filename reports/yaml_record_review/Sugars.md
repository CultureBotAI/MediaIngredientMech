# `data/ingredients/mapped/Sugars.yaml`

## Verdict

Pass. The plural class label is deliberately modeled as a local
`kgmicrobe.compound:sugars` subject with a parent `CHEBI:16646` carbohydrate
`NARROW_MATCH`, and the final SSSOM preserves the mandatory sibling registry
row.

## Identity

- Reviewed record: `data/ingredients/mapped/Sugars.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:sugars` with
  `ontology_mapping.ontology_id: CHEBI:16646`, label `carbohydrate`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: 0 CultureMech media occurrences plus 13 MicrobeDecoder source
  occurrences from `bergey:substrates`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sucrose` through `Sugars`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for the CHEBI parent.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:16646` with label `carbohydrate`.
  ChEBI carries `carbohydrates` as an exact IUPAC synonym, but not bare
  `sugar`, agreeing with the curation decision to treat `Sugars` as narrower
  than the available CHEBI parent.
- The 2026-08-15 `decompose_py_media_and_ground_categories` event records the
  manual category grounding from `Sugars` to the local
  `kgmicrobe.compound:sugars` identity plus `CHEBI:16646` parent.
- The final SSSOM has both required rows: `MIM:Sugars skos:narrowMatch
  CHEBI:16646` and the sibling `skos:exactMatch` registry row to
  `kgmicrobe.compound:sugars`.

## Completeness

- The local identity, parent CHEBI mapping, source occurrence, aggregate row,
  and final SSSOM rows agree.
- No unsupported active role, component, or final SSSOM payload was found.

## Recommended Edits

- None.
