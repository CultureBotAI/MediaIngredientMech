# `data/ingredients/mapped/Totarol.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, PubChem structure, aggregate row, and
final SSSOM row for totarol are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Totarol.yaml`.
- Identifier and grounding: `identifier: CHEBI:69241` with matching
  `ontology_mapping.ontology_id`, label `totarol`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `511-15-9`.
- Synonyms: none.
- Occurrences: no MediaDive/media occurrence count.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tomato_Juice` through `Trace_Element_Solution`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 search for `totarol` returns `CHEBI:69241` with label `totarol`.
- Fresh PubChem lookup for CAS `511-15-9` returns formula `C20H30O` and the
  same InChI as the YAML.
- The final SSSOM row has `MIM:Totarol skos:exactMatch CHEBI:69241`, uses
  `obo:chebi.owl`, and exports only `CAS:511-15-9` in `other`.

## Completeness

- The CHEBI identity, CAS RN, structure fields, aggregate copy, and final SSSOM
  row agree.
- No components, media roles, environmental contexts, or final synonym tokens
  require curation.

## Recommended Edits

- None.
