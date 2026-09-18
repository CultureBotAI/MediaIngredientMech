# `data/ingredients/mapped/Terephthalate.yaml`

## Verdict

Pass. The resolved MicrobeDecoder surface `Terephthalate` is intentionally
grounded to active fully deprotonated `CHEBI:30043`, the structure fields match
that dianion, and the final SSSOM exact row is synchronized and synonym-clean.

## Identity

- Reviewed record: `data/ingredients/mapped/Terephthalate.yaml`.
- Identifier and grounding: `identifier: CHEBI:30043` with
  `ontology_mapping.ontology_id: CHEBI:30043`, label `terephthalate(2-)`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C8H4O4`, ChEBI/PubChem InChI and SMILES, and
  molecular weight `164.116`.
- Occurrences: zero CultureMech recipe occurrences and 1 MicrobeDecoder
  metabolite-utilization row.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Teicoplanin` through `Tertiomycin_A`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:30043` as `terephthalate(2-)` and
  includes `terephthalate` as a synonym of that term.
- The structured `MIM curation (#213)` evidence explicitly records the decision
  to map the bare anion label to the fully deprotonated conjugate base instead
  of the monoanion.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Terephthalate`,
  points at `CHEBI:30043`, names `obo:chebi.owl`, and publishes no unsafe
  `other` synonyms.

## Completeness

- The CHEBI identity, structure fields, aggregate row, MicrobeDecoder source
  occurrence, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder promotion,
  aggregate, final SSSOM, generated, and research-validation rows.

## Recommended Edits

- None.
