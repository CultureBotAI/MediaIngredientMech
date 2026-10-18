# `data/ingredients/mapped/Triptolide.yaml`

## Verdict

Pass. The exact CHEBI identity, CAS RN, ChEBI structure fields, aggregate row,
and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Triptolide.yaml`.
- Identifier and grounding: `identifier: CHEBI:9747` with matching
  `ontology_mapping.ontology_id`, label `Triptolide`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `38748-32-2`.
- Synonyms: none.
- Occurrences: 0 recipe occurrences in 0 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trimethylamine-hcl` through `Tris_Acetate_Stock_Solution`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 term lookup for `CHEBI:9747` returns `Triptolide`, CAS xref
  `cas:38748-32-2`, formula `C20H24O6`, and the same InChI and SMILES as the
  YAML.
- The final SSSOM row has `MIM:Triptolide skos:exactMatch CHEBI:9747` and
  exports only `CAS:38748-32-2` in `other`.

## Issues

None.

## Completeness

- The CHEBI identity, CAS RN, structure fields, aggregate copy, and final SSSOM
  row agree.

## Recommended Edits

None.
