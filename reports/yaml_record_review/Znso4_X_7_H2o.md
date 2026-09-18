# `data/ingredients/mapped/Znso4_X_7_H2o.yaml`

## Verdict

Needs curation. The exact `CHEBI:32312` zinc sulfate heptahydrate identity,
CAS, structure, source-backed `TRACE_ELEMENT` role, aggregate row, and final
SSSOM predicate pass, but one exported heptahydrate synonym uses the impossible
`Zn2SO4` formula.

## Identity

- Reviewed record: `data/ingredients/mapped/Znso4_X_7_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:32312` with matching
  `ontology_mapping.ontology_id`, canonical label
  `zinc sulfate heptahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `7446-20-0`.
- Structure: formula `7H2O.O4S.Zn` with populated InChI and SMILES for the
  heptahydrate.
- Synonyms: raw CultureMech `Role: Mineral source` provenance strings, many
  formulaic heptahydrate variants, and exact heptahydrate labels.
- Role: source-backed `TRACE_ELEMENT` evidence from the CultureMech original
  `Mineral source` role.
- Occurrences: 2,410 CultureMech occurrences across 2,407 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` passed for this CHEBI-primary
  record with `--labels`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `zinc sulfate heptahydrate` in CHEBI returned the
  active `CHEBI:32312` label `zinc sulfate heptahydrate`.

## Evidence

- The final SSSOM row correctly exports
  `MIM:Znso4_X_7_H2o skos:exactMatch CHEBI:32312`.
- Raw `Role:` and `Properties:` strings from the YAML are filtered from final
  SSSOM.
- The final `other` field exports only heptahydrate labels except for one
  variant whose formula starts with `Zn2SO4`.

## Issues

- Major: the final SSSOM `other` field exports an impossible
  `Zn2SO4`-prefixed heptahydrate formula as an exact synonym for zinc sulfate
  heptahydrate.

## Completeness

- The exact CHEBI identifier, CAS, structure fields, single-ingredient type,
  CultureMech role evidence, aggregate copy, and final SSSOM predicate agree.
- The exported synonym payload needs a one-token cleanup.

## Recommended Edits

- Remove or suppress the `Zn2SO4`-prefixed hydrate synonym from final SSSOM
  `other`.
- Rebuild SSSOM and rerun strict validation plus SSSOM invariant validation.
