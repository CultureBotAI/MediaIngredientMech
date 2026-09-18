# `data/ingredients/mapped/Chloramphenicol.yaml`

## Verdict

Needs curation; major issue. The exact `CHEBI:17698` chloramphenicol identity,
CAS, formula, InChI, SMILES, ChEBI exact synonym, 9/9 CultureMech occurrence
count, SSSOM row, and aggregate copy pass, but the `SELECTIVE_AGENT` role is
only a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Chloramphenicol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17698`,
  `ontology_mapping.ontology_id: CHEBI:17698`,
  `ontology_label: chloramphenicol`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:17698` returns one active ChEBI term labelled
  `chloramphenicol` with CAS `56-75-7`, formula `C11H12Cl2N2O5`, exact synonym
  `2,2-dichloro-N-[(1R,2R)-2-hydroxy-1-(hydroxymethyl)-2-(4-nitrophenyl)ethyl]acetamide`,
  and the same InChI and SMILES stored in `chemical_properties`.

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
  `reports` found the active exact `MIM:Chloramphenicol` SSSOM row, the
  `CONFIRMED` row-review disposition, CultureMech residual rows for the
  backfilled raw surface forms, and matching aggregate and docs rows for
  `CHEBI:17698`.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found exactly nine
  `CHEBI:17698` rows, matching the explicit 9/9 `occurrence_statistics`.
- The active SSSOM row includes CAS `56-75-7` and the ChEBI-reviewed exact
  synonym already present in YAML.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, ChEBI exact synonym,
  raw CultureMech surface forms, occurrence count, SSSOM row, aggregate copy,
  and docs row are populated and agree.
- The record has no component or environment claims that need additional
  evidence.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: either replace `physicochemical_roles.SELECTIVE_AGENT` with inspected
  evidence for chloramphenicol as a selective agent in this media scope, or
  remove the role.
- Regenerate synchronized outputs and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
