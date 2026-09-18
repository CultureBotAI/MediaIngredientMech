# `data/ingredients/mapped/Trigonelline_HCl.yaml`

## Verdict

Pass. The CAS-to-CHEBI hydrochloride identity, exact synonym, CAS RN, ChEBI
structure fields, occurrence count, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Trigonelline_HCl.yaml`.
- Identifier and grounding: `identifier: CHEBI:229203` with matching
  `ontology_mapping.ontology_id`, label `Trigonelline HCl`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `6138-41-6`.
- Synonyms: one reviewed exact synonym,
  `1-methylpyridin-1-ium-3-carboxylic acid;chloride`.
- Occurrences: 10 FEBA recipe occurrences in 10 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Triethanolamine` through `Trimethylamine-N-oxide`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `Trigonelline` returns `CHEBI:229203` with label
  `Trigonelline HCl` and the inspected
  `1-methylpyridin-1-ium-3-carboxylic acid;chloride` exact synonym.
- The YAML CAS RN `6138-41-6`, formula `C7H8NO2.Cl`, and InChI all describe
  the hydrochloride salt rather than the neighboring free-betaine record.
- The final SSSOM row has
  `MIM:Trigonelline_HCl skos:exactMatch CHEBI:229203` and exports only the
  exact synonym plus `CAS:6138-41-6` in `other`.

## Issues

None.

## Completeness

- The CHEBI identity, CAS RN, structure fields, occurrence count, aggregate
  copy, and final SSSOM row agree.

## Recommended Edits

None.
