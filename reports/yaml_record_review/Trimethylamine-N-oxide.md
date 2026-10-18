# `data/ingredients/mapped/Trimethylamine-N-oxide.yaml`

## Verdict

Pass. The CAS-to-CHEBI identity, exact synonym, CAS RN, ChEBI structure fields,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Trimethylamine-N-oxide.yaml`.
- Identifier and grounding: `identifier: CHEBI:15724` with matching
  `ontology_mapping.ontology_id`, label `trimethylamine N-oxide`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `1184-78-7`.
- Synonyms: one reviewed exact synonym, `N,N-dimethylmethanamine oxide`.
- Occurrences: 0 recipe occurrences in 0 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Triethanolamine` through `Trimethylamine-N-oxide`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `trimethylamine N-oxide` returns `CHEBI:15724`
  with label `trimethylamine N-oxide` and the exported
  `N,N-dimethylmethanamine oxide` exact synonym.
- Fresh OLS4 term lookup for `CHEBI:15724` reports the CAS xref
  `cas:1184-78-7`, formula `C3H9NO`, InChI
  `InChI=1S/C3H9NO/c1-4(2,3)5/h1-3H3`, and SMILES `C[N+](C)(C)[O-]`.
- The final SSSOM row has
  `MIM:Trimethylamine-N-oxide skos:exactMatch CHEBI:15724` and exports only
  the exact synonym plus `CAS:1184-78-7` in `other`.

## Issues

None.

## Completeness

- The CHEBI identity, CAS RN, structure fields, aggregate copy, and final SSSOM
  row agree.
- The zero occurrence count is consistent across the per-record and aggregate
  copies.

## Recommended Edits

None.
