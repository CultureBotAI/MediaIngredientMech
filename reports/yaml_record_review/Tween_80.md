# `data/ingredients/mapped/Tween_80.yaml`

## Verdict

Needs curation, major. The CHEBI polysorbate 80 identity, CAS RN, structure
fields, CultureMech surfactant role, aggregate row, and most final SSSOM
synonyms pass, but final SSSOM `other` exports the pH-qualified
`Tween 80 (pH 8.0)` label.

## Identity

- Reviewed record: `data/ingredients/mapped/Tween_80.yaml`.
- Identifier and grounding: `identifier: CHEBI:53426` with matching
  `ontology_mapping.ontology_id`, label `polysorbate 80`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `9005-65-6`.
- Synonyms: raw CultureMech role/property strings, exact polysorbate 80
  synonyms, one BD catalog variant, and one pH-qualified raw label.
- Occurrences: 299 CultureMech recipe occurrences.
- Roles: one CultureMech-backed `physicochemical_roles.SURFACTANT` facet.
- KG-Microbe node: `CHEBI:53426`, matching the identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tween_20` through `Tyloxapol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:53426` returns active label `polysorbate 80`,
  CAS xref `9005-65-6`, formula
  `(C2H4O)w.(C2H4O)x.(C2H4O)y.(C2H4O)z.C24H44O6`, the same InChI and SMILES as
  the YAML, and the exported non-catalog SSSOM `other` labels as CHEBI
  synonyms.
- The final SSSOM row correctly has
  `MIM:Tween_80 skos:exactMatch CHEBI:53426` and exports the structured CAS
  token plus CHEBI synonyms in `other`.

## Issues

### Major: final `other` exports a pH-qualified raw label

`Tween 80 (pH 8.0)` describes a CultureMech recipe surface at a stated pH, not
an exact synonym for polysorbate 80. It should remain provenance, not a
published final SSSOM synonym.

### Minor: `mapping_quality` overstates the lexical match

`Tween 80` is a CHEBI synonym of canonical `polysorbate 80`, not the canonical
label itself. This should be `SYNONYM_MATCH`; the final SSSOM predicate remains
`skos:exactMatch` either way.

## Completeness

- The CHEBI identity, CAS RN, polymer structure fields, occurrence count,
  CultureMech surfactant role, KG-Microbe node, aggregate copy, and own final
  SSSOM row agree apart from the noisy pH-qualified `other` token.
- Raw `Role:` / `Properties:` CultureMech strings are kept out of final SSSOM
  `other`.

## Recommended Edits

- Mark `Tween 80 (pH 8.0)` as non-exportable provenance so final SSSOM `other`
  keeps only true polysorbate 80 synonyms, `Tween 80 (BD)`, and
  `CAS:9005-65-6`.
- Regrade `ontology_mapping.mapping_quality` from `EXACT_MATCH` to
  `SYNONYM_MATCH` so it records that the source label matched a CHEBI synonym.
