# `data/ingredients/mapped/Monomethyl_Succinate.yaml`

## Verdict

Pass. The exact `CHEBI:75146` monomethyl succinate identity, MicrobeDecoder
provenance, structural properties, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Monomethyl_Succinate.yaml`.
- Identifier and grounding: `identifier: CHEBI:75146` with
  `ontology_mapping.ontology_id: CHEBI:75146`, label `monomethyl succinate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: eight MicrobeDecoder `BacDive_Metabolite_utilization` source
  occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Monomethyl_Succinate` through `Moxifloxacin`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:75146` as active `monomethyl
  succinate`.
- A fresh PubChem lookup by name returns formula `C5H8O4` and the same InChI
  stored on the record.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Monomethyl_Succinate` to `CHEBI:75146` with empty `other`.

## Completeness

- The active ChEBI target, structural properties, MicrobeDecoder provenance,
  source occurrence count, and final exact row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
