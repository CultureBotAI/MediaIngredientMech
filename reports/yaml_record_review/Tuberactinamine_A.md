# `data/ingredients/mapped/Tuberactinamine_A.yaml`

## Verdict

Pass. The exact MeSH fallback identity, single-ingredient classification,
aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Tuberactinamine_A.yaml`.
- Identifier and grounding: `identifier: mesh:C108556` with matching
  `ontology_mapping.ontology_id`, label `tuberactinamine A`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: none.
- Occurrences: no CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tryptoneyeastbeef_(tyb)` through `Tuberactinamine_A`: exited 0 and wrote
  zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch.
  The lower-case `mesh:C108556` CURIE is covered by the exact OLS search below
  and by the existing unknown-term triage row that classifies its stale final
  validation stamp as missing-prefix-validator coverage.

## Evidence

- Fresh exact OLS4 search for `Tuberactinamine A` returns active
  `mesh:C108556` as the exact label match. The old low-confidence CHEBI
  candidates in the import evidence are adjacent `A...` compounds, not exact
  tuberactinamine A matches.
- The final SSSOM row correctly has
  `MIM:Tuberactinamine_A skos:exactMatch mesh:C108556` and no `other`
  synonyms.

## Issues

None.

## Completeness

- The MeSH fallback identity, single-ingredient classification, aggregate copy,
  and final SSSOM row agree.

## Recommended Edits

None.
