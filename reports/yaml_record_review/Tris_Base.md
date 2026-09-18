# `data/ingredients/mapped/Tris_Base.yaml`

## Verdict

Needs curation, major. The exact CHEBI identity, CAS RN, structure fields,
CultureMech buffer role, occurrence count, aggregate row, and own SSSOM row
pass, but salt, concentration-qualified, pH-qualified, and wrong-compound
labels leak into final SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Tris_Base.yaml`.
- Identifier and grounding: `identifier: CHEBI:9754` with matching
  `ontology_mapping.ontology_id`, label `tris`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `77-86-1`.
- Synonyms: four raw CultureMech role strings, ChEBI/kg-microbe synonyms for
  Tris base, and multiple merged source aliases.
- Occurrences: 212 CultureMech recipe occurrences in 210 media.
- Roles: one CultureMech-imported `physicochemical_roles.BUFFER` facet.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tris_Base` through `Trithionate`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 term lookup for `CHEBI:9754` returns `tris`, CAS xref
  `cas:77-86-1`, formula `C4H11NO3`, and the same InChI and SMILES as the
  YAML.
- The same ChEBI term confirms the unqualified Tris base labels including
  `Tris`, `Tris base`, `Tris buffer`, `Tris-base`, `Trizma`, `Trometamol`,
  and `Tromethamine`.
- The final SSSOM row has `MIM:Tris_Base skos:exactMatch CHEBI:9754`, filters
  the raw `Role:` strings, but still exports non-identity payloads including
  `Tris buffer 1M`, `Tris hydrochloride`, `Tris-HCl buffer`, `Tris HCl`,
  `Trizma Base pH`, `Trizma Base pH 8.2`, a Japanese-middle-dot Tris-HCl
  label, and `nitrilotriacetic acid trisodium salt`.

## Issues

### Major: final `other` exports salts, preparation labels, and a wrong compound

`Tris hydrochloride`, `Tris-HCl buffer`, `Tris HCl`, and the
Japanese-middle-dot Tris-HCl label denote the hydrochloride salt or buffer,
not the neutral `CHEBI:9754` Tris base molecule. `Tris buffer 1M` and the
`Trizma Base pH` labels carry concentration or pH preparation context.
`nitrilotriacetic acid trisodium salt` is an entirely different compound.

## Completeness

- The neutral CHEBI identity, CAS RN, structure fields, occurrence count,
  CultureMech-imported buffer role, aggregate copy, and real Tris synonyms
  agree.
- The only material issue is active synonym overreach from the duplicate merge
  and synonym imports.

## Recommended Edits

- Mark the Tris-HCl, concentration-qualified, pH-qualified, and
  nitrilotriacetic-acid salt labels as non-exportable or rejected so the final
  SSSOM row keeps only true `CHEBI:9754` synonyms.
