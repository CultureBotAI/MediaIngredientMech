# `data/ingredients/mapped/Charcoal.yaml`

## Verdict

Pass. The CultureMech charcoal record is exactly grounded to active
`CHEBI:91090`, and its generic ChEBI mixture identity, five CultureMech
occurrences, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Charcoal.yaml`.
- Identifier and grounding: `identifier: CHEBI:91090`,
  `ontology_mapping.ontology_id: CHEBI:91090`,
  `ontology_label: charcoal`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:91090` returns one active ChEBI term labelled
  `charcoal`; its definition describes a black porous residue mixture
  consisting of carbon and remaining ash after pyrolysis of animal or vegetable
  matter.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chaninin.yaml data/ingredients/mapped/Charcoal.yaml data/ingredients/mapped/Chartreusin.yaml data/ingredients/mapped/Chaulmoogric_Acid.yaml data/ingredients/mapped/Chelated_Iron_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Charcoal.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed. The same focused validator also passed for `Chartreusin` and
  `Chaulmoogric_Acid`; `Chaninin` and `Chelated_Iron_Solution` were skipped
  because their kg-microbe CURIEs are local registry IDs outside Engine A's OBO
  prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Charcoal` SSSOM row, the `CONFIRMED`
  row-review disposition, and matching aggregate and docs rows for
  `CHEBI:91090`.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found exactly five
  `CHEBI:91090` rows, matching the explicit 5/5 `occurrence_statistics`.
- The record has no CAS, formula, InChI, or SMILES assertion, which is
  appropriate for the generic ChEBI mixture term.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, source occurrence count, SSSOM row, aggregate
  copy, and docs row are populated and agree.
- No component or structure split is required for this exact ChEBI mixture
  identity.

## Recommended Edits

- None for this record.
