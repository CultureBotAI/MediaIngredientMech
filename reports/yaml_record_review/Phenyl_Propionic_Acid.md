# `data/ingredients/mapped/Phenyl_Propionic_Acid.yaml`

## Verdict

Needs curation; major. The repaired primary identity now maps exactly to active
`CHEBI:28631` 3-phenylpropionic acid, and final SSSOM synonyms are real
synonyms, but `CARBON_SOURCE` is still supported only by provisional LLM
reasoning.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenyl_Propionic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:28631` with
  `ontology_mapping.ontology_id: CHEBI:28631`, label
  `3-phenylpropionic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 6 CultureMech occurrences across 6 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:28631` resolves `CHEBI:28631`
  `3-phenylpropionic acid`; an exact synonym search for
  `3-Phenylpropanoic acid` also resolves `CHEBI:28631`.
- A local CAS checksum calculation confirmed that `501-52-0` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:Phenyl_Propionic_Acid` exactly to `CHEBI:28631`.

## Evidence

- The #554 fix repaired `kg_microbe_node_id`, so the compatibility node id now
  matches the curated CHEBI identifier after the earlier remap from obsolete
  `CHEBI:501520` to `CHEBI:28631`.
- The CHEBI primary identifier, mapping target, CAS `501-52-0`, structured
  formula, SMILES, and InChI all describe 3-phenylpropionic acid.
- The final SSSOM `other` values,
  `3-Phenylpropanoic acid|CAS:501-52-0`, are valid exact synonyms for the
  current target.
- Major: the `CARBON_SOURCE` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from provisional in-session Claude
  reasoning.

## Completeness

- The identity, structure, and final synonym surface are complete enough for an
  exact CHEBI mapping.
- Nutritional-role evidence remains incomplete while the carbon-source role is
  provisional.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phenyl_Propionic_Acid.yaml`, replace
  `nutritional_roles.CARBON_SOURCE` with source-backed evidence or remove the
  provisional role facet until it is curated.
