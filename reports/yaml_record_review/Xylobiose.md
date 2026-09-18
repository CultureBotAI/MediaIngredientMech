# `data/ingredients/mapped/Xylobiose.yaml`

## Verdict

Needs curation. The exact `CHEBI:28309` xylobiose identity, structure fields,
CAS RN, aggregate row, and final SSSOM row pass, but the `CARBON_SOURCE` role
is still a provisional ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Xylobiose.yaml`.
- Identifier and grounding: `identifier: CHEBI:28309` with matching
  `ontology_mapping.ontology_id`, label `xylobiose`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `6860-47-5`.
- Chemical fields: formula `C10H18O9` with populated InChI and SMILES strings.
- Synonyms: one CultureBotHT exact synonym and the reviewed ChEBI exact synonym
  `beta-D-xylopyranosyl-(1->4)-D-xylopyranose`.
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

- Fresh OLS4 exact search for `Xylobiose` in ChEBI returns active
  `CHEBI:28309` with label `xylobiose` and the reviewed exact IUPAC synonym.
- The final SSSOM row correctly has
  `MIM:Xylobiose skos:exactMatch CHEBI:28309`.

## Issues

- Major: `nutritional_roles.CARBON_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the ChEBI-ancestry role
  was provisional and still needs review.

## Completeness

- The exact CHEBI mapping, structure fields, CAS RN, aggregate copy, and final
  SSSOM row agree.

## Recommended Edits

- Replace or remove this record's `CARBON_SOURCE` role; keep it only if a
  maintained source supports xylobiose as a carbon source in media.
- Rerun strict validation and SSSOM invariant validation after curation.
