# `data/ingredients/mapped/Trans-2-Pentenoic_Acid.yaml`

## Verdict

Pass. The CAS-to-CHEBI identity, exact synonym, CAS RN, PubChem structure,
aggregate row, and final SSSOM row for trans-2-pentenoic acid are
synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Trans-2-Pentenoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:38366` with matching
  `ontology_mapping.ontology_id`, label `trans-pent-2-enoic acid`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `13991-37-2`.
- Synonyms: exact ChEBI synonym `(2E)-pent-2-enoic acid`.
- Occurrences: no MediaDive/media occurrence count.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trace_Mineral_Solution` through `Trans-aconitic_Acid`: exited 0 and wrote
  zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 search for `trans-pent-2-enoic acid` returns `CHEBI:38366`, the
  same term reached by the CAS xref.
- Fresh PubChem lookup for CAS `13991-37-2` returns formula `C5H8O2` and the
  same E double-bond InChI as the YAML.
- The final SSSOM row has
  `MIM:Trans-2-Pentenoic_Acid skos:exactMatch CHEBI:38366` and exports only the
  exact synonym plus `CAS:13991-37-2` in `other`.

## Completeness

- The CHEBI identity, CAS RN, structure fields, exact synonym, aggregate copy,
  and final SSSOM row agree.
- No roles, components, environmental contexts, or bad final SSSOM tokens are
  asserted.

## Recommended Edits

- None.
