# `data/ingredients/mapped/Trans-2-methyl-2-butenoic_Acid.yaml`

## Verdict

Pass. The CAS-to-ChEBI identity for tiglic acid, exact synonym, CAS RN, PubChem
structure, aggregate row, and final SSSOM row are synchronized.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Trans-2-methyl-2-butenoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:9592` with matching
  `ontology_mapping.ontology_id`, label `tiglic acid`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `80-59-1`.
- Synonyms: exact ChEBI synonym `(2E)-2-methylbut-2-enoic acid`.
- Occurrences: no MediaDive/media occurrence count.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trace_Mineral_Solution` through `Trans-aconitic_Acid`: exited 0 and wrote
  zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `tiglic acid` returns `CHEBI:9592`, whose exact
  synonym `(2E)-2-methylbut-2-enoic acid` matches the YAML synonym.
- Fresh PubChem lookup for CAS `80-59-1` returns formula `C5H8O2` and the same
  E double-bond InChI as the YAML.
- The final SSSOM row has
  `MIM:Trans-2-methyl-2-butenoic_Acid skos:exactMatch CHEBI:9592` and exports
  only the exact synonym plus `CAS:80-59-1` in `other`.

## Completeness

- The CHEBI identity, CAS RN, structure fields, exact synonym, aggregate copy,
  and final SSSOM row agree.
- No roles, components, environmental contexts, or bad final SSSOM tokens are
  asserted.

## Recommended Edits

- None.
