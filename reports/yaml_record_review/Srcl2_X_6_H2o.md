# `data/ingredients/mapped/Srcl2_X_6_H2o.yaml`

## Verdict

Needs curation - major. The exact strontium dichloride hexahydrate identity,
CAS, and mineral-role evidence pass, but a concentration-qualified stock label
is curated and exported as a hydrate synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Srcl2_X_6_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:36385` with
  `ontology_mapping.ontology_id: CHEBI:36385`, label
  `strontium dichloride hexahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: `cas_rn: 10025-70-4`, formula `Cl2Sr.6H2O`, and
  hexahydrate InChI and SMILES.
- Occurrences: 230 source occurrences across 230 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sporangiomycin` through `Stachyose_Hydrate`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:36385` with label
  `strontium dichloride hexahydrate` and exact synonym
  `strontium dichloride--water (1/6)`, matching the stored CHEBI target.
- PubChem resolves CAS `10025-70-4` to CID `6101868`; the CID has formula
  `Cl2H12O6Sr`, IUPAC name `strontium;dichloride;hexahydrate`, and the same
  hexahydrate InChI as YAML.
- `reports/hydrate_grounding.tsv` records this row as `OK_HYDRATE_TERM`, so
  the hydrate-specific grounding is already recognized by the hydrate audit.
- The CultureMech `Mineral` evidence supports the migrated
  `nutritional_roles.TRACE_ELEMENT` assertion for a strontium salt in media.
- Major: `SrCl2 x 6 H2O (0.1% w/v)` is concentration-qualified source text,
  not a synonym for the dry hexahydrate, but it remains a `HYDRATE_FORM`
  synonym and is exported in final SSSOM `other`.

## Completeness

- Raw `Role: Mineral source; Properties: ...` source labels are correctly
  filtered from final SSSOM.
- The middle-dot and other plain hexahydrate spellings are true same-form
  aliases; the remaining unsafe synonym is only the `0.1% w/v` stock label.

## Recommended Edits

- Major: remove `SrCl2 x 6 H2O (0.1% w/v)` from
  `data/ingredients/mapped/Srcl2_X_6_H2o.yaml` or retype it as non-exported
  source provenance so SSSOM `other` contains only dry-hexahydrate labels.
