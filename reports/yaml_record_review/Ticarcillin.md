# `data/ingredients/mapped/Ticarcillin.yaml`

## Verdict

Pass. The exact CHEBI identity, MicrobeDecoder occurrence accounting,
aggregate row, and final SSSOM row for ticarcillin are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Ticarcillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:9587` with matching
  `ontology_mapping.ontology_id`, label `ticarcillin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: 4 MicrobeDecoder hits across the BacDive antibiotic resistance
  and sensitivity columns.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Ticarcillin` through `TitaniumIII_Chloride`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 search for `ticarcillin` returns `CHEBI:9587` with label
  `ticarcillin`, matching the stored MicrobeDecoder exact lexical import.
- The PubChem-backed formula, SMILES, InChI, and molecular weight are the
  neutral ticarcillin structure rather than the disodium salt or a penicillin
  parent.
- The final SSSOM row has `MIM:Ticarcillin skos:exactMatch CHEBI:9587`, uses
  `obo:chebi.owl`, carries the expected MicrobeDecoder and reviewed curator
  sources, and leaves `other` empty.

## Completeness

- The CHEBI identity, structure fields, MicrobeDecoder source count, aggregate
  copy, and final SSSOM row agree.
- No CAS RN, components, media roles, environmental contexts, or final
  synonym/export tokens require curation.

## Recommended Edits

- None.
