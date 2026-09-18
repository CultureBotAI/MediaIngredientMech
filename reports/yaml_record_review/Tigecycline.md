# `data/ingredients/mapped/Tigecycline.yaml`

## Verdict

Pass. The exact CHEBI identity, MicrobeDecoder occurrence accounting,
aggregate row, and final SSSOM row for tigecycline are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Tigecycline.yaml`.
- Identifier and grounding: `identifier: CHEBI:149836` with matching
  `ontology_mapping.ontology_id`, label `tigecycline`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: 1 MicrobeDecoder hit in the BacDive antibiotic sensitivity
  column.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Ticarcillin` through `TitaniumIII_Chloride`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `tigecycline` returns `CHEBI:149836` with label
  `tigecycline`; the related conjugate-acid term is a narrower charged species
  rather than the neutral record subject.
- The PubChem-backed formula, SMILES, InChI, and molecular weight encode the
  neutral tigecycline structure.
- The final SSSOM row has `MIM:Tigecycline skos:exactMatch CHEBI:149836`, uses
  `obo:chebi.owl`, carries the expected MicrobeDecoder and reviewed curator
  sources, and leaves `other` empty.

## Completeness

- The CHEBI identity, structure fields, MicrobeDecoder source count, aggregate
  copy, and final SSSOM row agree.
- No CAS RN, components, media roles, environmental contexts, or final
  synonym/export tokens require curation.

## Recommended Edits

- None.
