# `data/ingredients/mapped/Xylan_From_Beechwood.yaml`

## Verdict

Needs curation. The CAS-backed `CHEBI:15447` xylan identity, structure fields,
CAS RN, aggregate row, and final SSSOM row pass, but the `CARBON_SOURCE` role
is still a provisional ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Xylan_From_Beechwood.yaml`.
- Identifier and grounding: `identifier: CHEBI:15447` with matching
  `ontology_mapping.ontology_id`, label `(1->4)-beta-D-xylan`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `9014-63-5`.
- Chemical fields: formula `(C5H8O4)n.H2O` with populated InChI and SMILES
  strings.
- Synonyms: one reviewed ChEBI exact synonym,
  `(1->4)-beta-D-xylopyranan`.
- Occurrences: two CultureMech recipe occurrences across two media.
- Role: `CARBON_SOURCE` with provisional ChEBI-ancestry evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Xanthocidin` through `Xylan_From_Beechwood`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the four
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:15447` returns active label
  `(1->4)-beta-D-xylan`, CAS `9014-63-5`, formula `(C5H8O4)n.H2O`, matching
  structure strings, and exact synonym `(1->4)-beta-D-xylopyranan`.
- The final SSSOM row correctly has
  `MIM:Xylan_From_Beechwood skos:exactMatch CHEBI:15447`.

## Issues

- Major: `nutritional_roles.CARBON_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the ChEBI-ancestry role
  was provisional and still needs review.

## Completeness

- The CAS-backed CHEBI mapping, structure fields, CAS RN, occurrence count,
  aggregate copy, and final SSSOM row agree.

## Recommended Edits

- Replace or remove this record's `CARBON_SOURCE` role; keep it only if a
  maintained source supports beechwood xylan as a carbon source in media.
- Rerun strict validation and SSSOM invariant validation after curation.
