# `data/ingredients/mapped/Tributyrin.yaml`

## Verdict

Pass. The exact CHEBI identity, MicrobeDecoder occurrence accounting,
aggregate row, and final SSSOM row for tributyrin are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Tributyrin.yaml`.
- Identifier and grounding: `identifier: CHEBI:35020` with matching
  `ontology_mapping.ontology_id`, label `tributyrin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: 8 MicrobeDecoder hits in the BacDive metabolite utilization
  column.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tribenuron-methyl` through `Tricine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `tributyrin` returns `CHEBI:35020` with label
  `tributyrin`.
- The PubChem-backed formula, SMILES, InChI, and molecular weight encode the
  triester of glycerol and butyric acid.
- The final SSSOM row has `MIM:Tributyrin skos:exactMatch CHEBI:35020`, uses
  `obo:chebi.owl`, carries the expected MicrobeDecoder and reviewed curator
  sources, and leaves `other` empty.

## Completeness

- The CHEBI identity, structure fields, MicrobeDecoder source count, aggregate
  copy, and final SSSOM row agree.
- No CAS RN, roles, components, environmental contexts, or bad final SSSOM
  tokens are asserted.

## Recommended Edits

- None.
