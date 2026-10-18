# `data/ingredients/mapped/Trisodium_Citrate.yaml`

## Verdict

Needs curation, major. The exact anhydrous CHEBI identity, CAS RN, structure
fields, CultureMech buffer role, occurrence count, aggregate row, and own
SSSOM row pass, but `Na2-citrate` and `Citric Acid` are not synonyms of
trisodium citrate and leak into final SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Trisodium_Citrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:53258` with matching
  `ontology_mapping.ontology_id`, label `sodium citrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `68-04-2`.
- Synonyms: raw CultureMech role/properties strings, ChEBI/kg-microbe sodium
  citrate labels, and two stale merged labels, `Na2-citrate` and
  `Citric Acid`.
- Occurrences: 182 CultureMech recipe occurrences in 182 media.
- Roles: one CultureMech-imported `physicochemical_roles.BUFFER` facet.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tris_Base` through `Trithionate`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 term lookup for `CHEBI:53258` returns `sodium citrate`, formula
  `C6H5O7.3Na`, and the same InChI and SMILES as the YAML.
- Fresh PubChem lookup for CAS `68-04-2` resolves to CID 6224 with
  `CHEBI:53258` and anhydrous trisodium citrate labels.
- Fresh OLS4 search for `Citric Acid` resolves that label to the separate
  protonated parent `CHEBI:30769`.
- The final SSSOM row has
  `MIM:Trisodium_Citrate skos:exactMatch CHEBI:53258` and exports
  `Na2-citrate`, `Citric Acid`, and `CAS:68-04-2` in `other`.

## Issues

### Major: final `other` exports stale merged labels for other citrate forms

`Citric Acid` denotes the protonated parent, not trisodium citrate.
`Na2-citrate` does not denote the trisodium salt represented by `CHEBI:53258`.
Both labels should stay out of final SSSOM synonyms for this subject.

## Completeness

- The anhydrous trisodium-citrate identity, CAS RN, structure fields,
  occurrence count, CultureMech-imported buffer role, aggregate copy, and real
  trisodium-citrate labels agree.
- The only material issue is the stale merged synonym overreach.

## Recommended Edits

- Mark `Citric Acid` and `Na2-citrate` as rejected or non-exportable labels so
  the final SSSOM row keeps only true anhydrous trisodium-citrate synonyms.
