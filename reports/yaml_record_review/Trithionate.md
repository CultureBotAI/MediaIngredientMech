# `data/ingredients/mapped/Trithionate.yaml`

## Verdict

Pass. The MicrobeDecoder synonym match, exact CHEBI identity, structure
fields, source occurrence count, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Trithionate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15987` with matching
  `ontology_mapping.ontology_id`, label `trithionate(2-)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: one raw MicrobeDecoder label.
- Occurrences: 7 MicrobeDecoder trait occurrences; no CultureMech recipe
  occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tris_Base` through `Trithionate`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 term lookup for `CHEBI:15987` returns `trithionate(2-)`,
  `Trithionate` as an exact synonym, formula `O6S3`, and the same InChI and
  SMILES as the YAML.
- The final SSSOM row correctly has
  `MIM:Trithionate skos:exactMatch CHEBI:15987`: the object is the record's own
  identifier, so an exact identity row is correct even though the mapping was
  found through a synonym.

## Issues

None.

## Completeness

- The CHEBI identity, MicrobeDecoder occurrence count, structure fields,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
