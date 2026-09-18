# `data/ingredients/mapped/Trimethylamine-hcl.yaml`

## Verdict

Needs curation, major. The exact CHEBI hydrochloride identity, CAS RN,
CultureMech carbon-source role, occurrence count, aggregate row, and own SSSOM
row pass, but `Methylamine-HCl` is not a synonym of trimethylamine
hydrochloride and is exported in final SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Trimethylamine-hcl.yaml`.
- Identifier and grounding: `identifier: CHEBI:64700` with matching
  `ontology_mapping.ontology_id`, label `trimethylamine hydrochloride`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `593-81-7`.
- Synonyms: two raw CultureMech role strings, two raw CultureMech spelling
  variants, eight trimethylamine-hydrochloride kg-microbe synonyms, and the
  wrong `Methylamine-HCl` kg-microbe synonym.
- Occurrences: 63 CultureMech recipe occurrences in 63 media.
- Roles: one CultureMech-imported `nutritional_roles.CARBON_SOURCE` facet.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trimethylamine-hcl` through `Tris_Acetate_Stock_Solution`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 term lookup for `CHEBI:64700` returns `trimethylamine
  hydrochloride`, CAS xref `cas:593-81-7`, formula `C3H9N.HCl`, and the same
  InChI and SMILES as the YAML.
- The same ChEBI term lists the formula abbreviations, IUPAC hydrochloride
  labels, `Trimethylammonium chloride`, and
  `trimethylamine monohydrochloride`, but not `Methylamine-HCl`.
- A fresh CHEBI-scoped OLS4 exact search for `Methylamine-HCl` returned zero
  rows.
- The final SSSOM row has
  `MIM:Trimethylamine-hcl skos:exactMatch CHEBI:64700` and exports the wrong
  `Methylamine-HCl` token in `other`.

## Issues

### Major: final `other` exports a methylamine salt as a synonym

`Methylamine-HCl` drops two methyl groups relative to trimethylamine
hydrochloride and does not resolve to `CHEBI:64700`; it should not be an active
synonym or a final SSSOM `other` token for this subject.

## Completeness

- The CHEBI identity, CAS RN, structure fields, occurrence count,
  CultureMech-imported carbon-source role, aggregate copy, and remaining
  trimethylamine-hydrochloride labels agree.
- The only issue is the wrong methylamine label surviving from the duplicate
  merge and kg-microbe synonym import.

## Recommended Edits

- Mark `Methylamine-HCl` as a rejected label or otherwise make it
  non-exportable, then regenerate the final SSSOM row without that `other`
  token.
