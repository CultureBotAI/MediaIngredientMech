# `data/ingredients/mapped/Stachyose_Hydrate.yaml`

## Verdict

Needs curation - major. The CAS hydrate correctly remains distinct from
anhydrous stachyose, but the final SSSOM is missing the local
`kgmicrobe.compound` identity row tracked by the hydrate audit and the
carbon-source role is still provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Stachyose_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:54261-98-2` with
  `ontology_mapping.ontology_id: CHEBI:17164`, label `stachyose`, source
  `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: `cas_rn: 54261-98-2`, `pubchem_cid: 4287569`, and
  formula `C24H42O21`.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sporangiomycin` through `Stachyose_Hydrate`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 lookup found no exact ChEBI `Stachyose hydrate` term, while
  OLS4 resolves the parent `CHEBI:17164` as `stachyose`.
- PubChem resolves CAS `54261-98-2` to CID `4287569`, whose synonym list
  includes `stachyose hydrate`. That CID is distinct from CAS `470-55-3`,
  which resolves to CID `439531` for the anhydrous `CHEBI:17164` stachyose
  sibling.
- `MIM curation (#342)` correctly downgraded the parent relation from
  `NARROW_MATCH` to `CLOSE_MATCH`, because an unspecified hydrate is distinct
  from and not a subclass of the anhydrous parent.
- Major: `reports/hydrate_grounding.tsv` still marks this record
  `CAS_MISSING_ANCHOR_ROWS`. The final SSSOM has a close parent row and a CAS
  identity row, but no exact `kgmicrobe.compound:stachyose_hydrate` registry
  sibling row for the local hydrate identity mentioned in the August curation
  history.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by
  `COMPUTATIONAL_PREDICTION` from a name-list rule, with the provisional
  curator note.

## Completeness

- The close parent mapping and CAS identity preserve the anhydrous/hydrate
  boundary, and the final SSSOM row does not export anhydrous stachyose
  synonyms on the hydrate subject.
- The exact water stoichiometry remains unresolved, as already recorded in
  `mappings/hydrate_review.tsv`.

## Recommended Edits

- Major: add the missing local `kgmicrobe.compound:stachyose_hydrate` identity
  row through the maintained YAML/SSSOM generation path so the final SSSOM
  records both the close CHEBI parent and the local hydrate identity.
- Major: remove `nutritional_roles.CARBON_SOURCE` or replace the provisional
  name-list assertion with source evidence that uses stachyose hydrate as a
  carbon source.
