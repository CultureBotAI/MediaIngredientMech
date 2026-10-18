# `data/ingredients/mapped/Xylitol.yaml`

## Verdict

Needs curation. The exact `CHEBI:17151` xylitol identity, corrected CAS RN,
structure fields, aggregate row, and final SSSOM row pass, but the
`CARBON_SOURCE` role is still a provisional ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Xylitol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17151` with matching
  `ontology_mapping.ontology_id`, label `xylitol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `87-99-0`.
- Chemical fields: formula `C5H12O5` with populated InChI and SMILES strings.
- Synonyms: seven clean kg-microbe synonyms for xylitol.
- Occurrences: two CultureMech recipe occurrences across two media.
- Role: `CARBON_SOURCE` with provisional ChEBI-ancestry evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xylitol` through `Xylotetraose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the four
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:17151` returns active label `xylitol`, CAS
  `87-99-0`, formula `C5H12O5`, matching structure strings, and synonym
  coverage for the kg-microbe synonym set.
- The final SSSOM row correctly has
  `MIM:Xylitol skos:exactMatch CHEBI:17151`.

## Issues

- Major: `nutritional_roles.CARBON_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the ChEBI-ancestry role
  was provisional and still needs review.

## Completeness

- The exact CHEBI mapping, corrected CAS RN, structure fields, occurrence
  count, aggregate copy, and final SSSOM row agree.

## Recommended Edits

- Replace or remove this record's `CARBON_SOURCE` role; keep it only if a
  maintained source supports xylitol as a carbon source in media.
- Rerun strict validation and SSSOM invariant validation after curation.
