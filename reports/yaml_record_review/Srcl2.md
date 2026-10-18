# `data/ingredients/mapped/Srcl2.yaml`

## Verdict

Needs curation - major. The anhydrous strontium dichloride identity, CAS, and
mineral-role evidence pass, but `SrCl` is curated and exported as an exact
synonym even though it is not the dichloride formula.

## Identity

- Reviewed record: `data/ingredients/mapped/Srcl2.yaml`.
- Identifier and grounding: `identifier: CHEBI:36383` with
  `ontology_mapping.ontology_id: CHEBI:36383`, label `strontium dichloride`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: `cas_rn: 10476-85-4`, formula `2Cl.Sr`, and the expected
  strontium dication plus two chloride anions in InChI and SMILES.
- Occurrences: 244 source occurrences across 244 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sporangiomycin` through `Stachyose_Hydrate`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:36383` with label
  `strontium dichloride` and exact synonym `strontium chloride`, matching the
  anhydrous mapping.
- PubChem resolves CAS `10476-85-4` to CID `5362485`; the CID has formula
  `Cl2Sr`, IUPAC name `strontium dichloride`, and the same ionic InChI as YAML.
- The CultureMech `Mineral source` evidence supports the migrated
  `nutritional_roles.TRACE_ELEMENT` assertion for a strontium mineral in media.
- Major: `SrCl` is not a true synonym for `SrCl2` or `CHEBI:36383`, but it is
  retained as an `EXACT_SYNONYM` and is exported in final SSSOM `other`.

## Completeness

- Raw `Role: Mineral source; Properties: ...` source labels are correctly
  filtered from final SSSOM.
- The only unsupported active synonym or final SSSOM payload found is `SrCl`.

## Recommended Edits

- Major: remove `SrCl` from `data/ingredients/mapped/Srcl2.yaml` or retype it
  as rejected provenance so the final SSSOM no longer publishes it as a
  synonym for strontium dichloride.
