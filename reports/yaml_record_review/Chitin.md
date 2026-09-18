# `data/ingredients/mapped/Chitin.yaml`

## Verdict

Needs curation; major issue. The exact `CHEBI:17029` chitin identity, formula,
InChI, SMILES, exact ChEBI synonym, 12 CultureMech occurrence rows, SSSOM row,
and aggregate copy pass. The record still exports `hydrolysis: crab shell
chitin` as a resolvable synonym, and the `CARBON_SOURCE` role is only a
provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Chitin.yaml`.
- Identifier and grounding: `identifier: CHEBI:17029`,
  `ontology_mapping.ontology_id: CHEBI:17029`, `ontology_label: chitin`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:17029` returns one active ChEBI term labelled
  `chitin` with formula `(C8H13NO5)n.H2O`, the same InChI and SMILES stored in
  `chemical_properties`, and exact synonym
  `(1->4)-2-acetamido-2-deoxy-beta-D-glucan`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chenodeoxycholic_Acid.yaml data/ingredients/mapped/Chitin.yaml data/ingredients/mapped/Chitosan.yaml data/ingredients/mapped/Chloramphenicol.yaml data/ingredients/mapped/Chlorhexidine_Diacetate_Salt_Hydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chenodeoxycholic_Acid.yaml data/ingredients/mapped/Chitin.yaml data/ingredients/mapped/Chitosan.yaml data/ingredients/mapped/Chloramphenicol.yaml data/ingredients/mapped/Chlorhexidine_Diacetate_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records in this batch.
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
  `reports` found the active exact `MIM:Chitin` SSSOM row, the `CONFIRMED`
  row-review disposition, matching aggregate and docs rows for `CHEBI:17029`,
  and an intentionally narrower active unmapped `Chitin from shrimp shells`
  record.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found exactly twelve
  `CHEBI:17029` rows, matching the explicit 12/12 `occurrence_statistics`.
- The `hydrolysis: crab shell chitin` raw text is not filtered by
  `src/mediaingredientmech/synonym_policy.py`: current `docs/data` exports
  still resolve it as a `Chitin` synonym.
- `CARBON_SOURCE` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, exact ChEBI synonym,
  occurrence count, SSSOM row, aggregate copy, and docs row are populated and
  agree.
- The active `Chitin from shrimp shells` record appropriately remains separate
  and narrower, so no identity merge is required.
- The consequential gaps are the leaked `hydrolysis:` source statement and the
  unsupported provisional role.

## Recommended Edits

- Major: either remove `hydrolysis: crab shell chitin` from
  `data/ingredients/mapped/Chitin.yaml` or extend
  `src/mediaingredientmech/synonym_policy.py` so `hydrolysis:` source
  statements stay in provenance without resolving as ingredient synonyms.
- Major: either replace `nutritional_roles.CARBON_SOURCE` with inspected
  evidence for chitin as a carbon source in this media scope, or remove the
  role.
- Regenerate synchronized outputs and rerun strict validation, SSSOM QC,
  aggregate roundtrip, docs generation, and `git diff --check`.
