# `data/ingredients/mapped/Wheat_Arabinoxylan.yaml`

## Verdict

Needs curation. The CAS-backed `CHEBI:28427` arabinoxylan identity, structure
fields, aggregate row, and final SSSOM row pass, but the `CARBON_SOURCE` role
is still a provisional ChEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Wheat_Arabinoxylan.yaml`.
- Identifier and grounding: `identifier: CHEBI:28427` with matching
  `ontology_mapping.ontology_id`, label `arabinoxylan`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `9040-27-1`.
- Chemical fields: polymer formula `2(C10H16O8)n.(C15H24O12)n.(C5H8O4)n` with
  a populated SMILES string.
- Synonyms: none.
- Occurrences: zero.
- Role: `CARBON_SOURCE` with provisional ChEBI-ancestry evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Wc_Trace_Elements_Solution` through
  `Wolfes_Mineral_Mix_minus_Nitrilotriacetic_acid`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on this CHEBI-primary
  record exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:28427` returns active label `arabinoxylan`, CAS
  `9040-27-1`, KEGG cross-reference `C01889`, and the same polymer formula and
  SMILES string as the local record.
- The final SSSOM row correctly has
  `MIM:Wheat_Arabinoxylan skos:exactMatch CHEBI:28427`.

## Issues

- Major: `nutritional_roles.CARBON_SOURCE` rests on
  `COMPUTATIONAL_PREDICTION` evidence whose note says the ChEBI-ancestry role
  was provisional and still needs review.

## Completeness

- The CAS-backed CHEBI mapping, structure fields, CAS RN, aggregate copy, and
  final SSSOM row agree.

## Recommended Edits

- Replace or remove this record's `CARBON_SOURCE` role; keep it only if a
  maintained source supports wheat arabinoxylan as a carbon source in media.
- Rerun strict validation and SSSOM invariant validation after curation.
