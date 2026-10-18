# `data/ingredients/mapped/Toyocamycin.yaml`

## Verdict

Pass. The exact CHEBI identity, MicrobeDecoder occurrence accounting,
aggregate row, and final SSSOM row for toyocamycin are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Toyocamycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:134606` with matching
  `ontology_mapping.ontology_id`, label `toyocamycin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: 1 MicrobeDecoder hit in the BacDive metabolite production
  column.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tomato_Juice` through `Trace_Element_Solution`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `toyocamycin` returns `CHEBI:134606` with label
  `toyocamycin`, matching the stored MicrobeDecoder exact lexical import.
- The PubChem-backed formula, SMILES, InChI, and molecular weight encode the
  toyocamycin structure.
- The final SSSOM row has `MIM:Toyocamycin skos:exactMatch CHEBI:134606`,
  uses `obo:chebi.owl`, carries the expected MicrobeDecoder and reviewed
  curator sources, and leaves `other` empty.

## Completeness

- The CHEBI identity, structure fields, MicrobeDecoder source count, aggregate
  copy, and final SSSOM row agree.
- No CAS RN, components, media roles, environmental contexts, or final
  synonym/export tokens require curation.

## Recommended Edits

- None.
