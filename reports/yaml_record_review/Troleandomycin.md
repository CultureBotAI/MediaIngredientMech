# `data/ingredients/mapped/Troleandomycin.yaml`

## Verdict

Pass. The MicrobeDecoder exact-label match, exact CHEBI identity, structure
fields, source occurrence count, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Troleandomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:45735` with matching
  `ontology_mapping.ontology_id`, label `troleandomycin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: 25 MicrobeDecoder trait occurrences; no CultureMech recipe
  occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Triton_X-100` through `Tryptamine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 term lookup for `CHEBI:45735` returns `troleandomycin`, formula
  `C41H67NO15`, and the same InChI and SMILES as the YAML.
- The final SSSOM row has
  `MIM:Troleandomycin skos:exactMatch CHEBI:45735` and exports no `other`
  tokens.

## Issues

None.

## Completeness

- The CHEBI identity, MicrobeDecoder occurrence count, structure fields,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
