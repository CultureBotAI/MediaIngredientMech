# `data/ingredients/mapped/Tubercidin.yaml`

## Verdict

Pass. The MicrobeDecoder exact-label match, exact CHEBI identity, structure
fields, source occurrence count, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Tubercidin.yaml`.
- Identifier and grounding: `identifier: CHEBI:48267` with matching
  `ontology_mapping.ontology_id`, label `tubercidin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: 1 MicrobeDecoder trait occurrence and no CultureMech recipe
  occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tuberactinomycin` through `Tween`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this file with
  `--labels`: passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:48267` returns active label `tubercidin`,
  formula `C11H14N4O4`, and the same InChI and SMILES as the YAML.
- The final SSSOM row correctly has
  `MIM:Tubercidin skos:exactMatch CHEBI:48267` and no `other` synonyms.

## Issues

None.

## Completeness

- The CHEBI identity, structure fields, MicrobeDecoder occurrence count,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
