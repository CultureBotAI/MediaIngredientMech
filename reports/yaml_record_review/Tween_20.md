# `data/ingredients/mapped/Tween_20.yaml`

## Verdict

Pass. The synonym match to polysorbate 20, CAS RN, polymer structure fields,
CultureMech surfactant role, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Tween_20.yaml`.
- Identifier and grounding: `identifier: CHEBI:53424` with matching
  `ontology_mapping.ontology_id`, label `polysorbate 20`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `9005-64-5`.
- Synonyms: raw CultureMech role/property text.
- Occurrences: 4 CultureMech recipe occurrences.
- Roles: one CultureMech-imported `physicochemical_roles.SURFACTANT` facet.
- KG-Microbe node: `CHEBI:53424`, matching the identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tween_20` through `Tyloxapol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:53424` returns active label `polysorbate 20`,
  CAS xref `9005-64-5`, formula
  `(C2H4O)w.(C2H4O)x.(C2H4O)y.(C2H4O)z.C18H34O6`, the same InChI and SMILES as
  the YAML, and `Tween 20` as a synonym.
- The final SSSOM row correctly has
  `MIM:Tween_20 skos:exactMatch CHEBI:53424` and exports only `CAS:9005-64-5`
  in `other`.

## Issues

None.

## Completeness

- The CHEBI synonym match, CAS RN, polymer structure fields, occurrence count,
  surfactant role, KG-Microbe node, aggregate copy, and final SSSOM row agree.
- The raw `Role:` / `Properties:` CultureMech string is kept out of final SSSOM
  `other`.

## Recommended Edits

None.
