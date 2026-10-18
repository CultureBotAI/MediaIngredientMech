# `data/ingredients/mapped/Xylotetraose.yaml`

## Verdict

Needs curation. The exact `CHEBI:62972` xylotetraose identity, structure
fields, aggregate row, and final SSSOM row pass, but the `CARBON_SOURCE` role
is still a provisional ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Xylotetraose.yaml`.
- Identifier and grounding: `identifier: CHEBI:62972` with matching
  `ontology_mapping.ontology_id`, label `xylotetraose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `22416-58-6`.
- Chemical fields: formula `C20H34O17` with populated InChI and SMILES strings.
- Synonyms: one reviewed ChEBI exact synonym.
- Occurrences: zero.
- Role: `CARBON_SOURCE` with provisional ChEBI-ancestry evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xylitol` through `Xylotetraose`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the four
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:62972` returns active label `xylotetraose`,
  formula `C20H34O17`, matching structure strings, and exact synonym
  `beta-D-xylopyranosyl-(1->4)-beta-D-xylopyranosyl-(1->4)-beta-D-xylopyranosyl-(1->4)-D-xylopyranose`.
- The final SSSOM row correctly has
  `MIM:Xylotetraose skos:exactMatch CHEBI:62972`.

## Issues

- Major: `nutritional_roles.CARBON_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the ChEBI-ancestry role
  was provisional and still needs review.

## Completeness

- The exact CHEBI mapping, structure fields, aggregate copy, and final SSSOM row
  agree.

## Recommended Edits

- Replace or remove this record's `CARBON_SOURCE` role; keep it only if a
  maintained source supports xylotetraose as a carbon source in media.
- Rerun strict validation and SSSOM invariant validation after curation.
