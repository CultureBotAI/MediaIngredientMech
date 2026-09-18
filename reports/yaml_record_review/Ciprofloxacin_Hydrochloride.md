# `data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml`

## Verdict

Needs curation; major. The CAS-backed identity is consistent with active
`CHEBI:59936` ciprofloxacin hydrochloride hydrate, and the formula, InChI,
SMILES, SSSOM row, zero occurrence count, and aggregate copy agree. The record
still carries an active `SELECTIVE_AGENT` role supported only by the
`infer_roles_from_name_lists` computational placeholder.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:59936`,
  `ontology_mapping.ontology_id: CHEBI:59936`,
  `ontology_label: ciprofloxacin hydrochloride hydrate`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- The stored CAS RN `86393-32-0`, formula `C17H18FN3O3.H2O.HCl`, InChI, and
  SMILES all describe the hydrochloride hydrate rather than the anhydrous
  `CHEBI:310388` sibling.
- Live exact OLS lookup for `ciprofloxacin hydrochloride hydrate` returns one
  active `CHEBI:59936` term labelled `ciprofloxacin hydrochloride hydrate`.
- PubChem lookup by `86393-32-0` returns CID 62998 and the same hydrate-plus-HCl
  InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cinoxacin.yaml data/ingredients/mapped/Ciprofloxacin.yaml data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml data/ingredients/mapped/Cis-aconitate.yaml data/ingredients/mapped/Cisplatin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cinoxacin.yaml data/ingredients/mapped/Ciprofloxacin.yaml data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml data/ingredients/mapped/Cis-aconitate.yaml data/ingredients/mapped/Cisplatin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-scoped records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Ciprofloxacin_Hydrochloride` SSSOM row,
  the OAK/OLS row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:59936` only in this active record.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:59936`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The `physicochemical_roles.SELECTIVE_AGENT` assertion has only a
  `COMPUTATIONAL_PREDICTION` reference from a curated name-pattern rule. That
  source can explain why the role was guessed, but it is not evidence that this
  ingredient was observed as a selective agent in a supported medium record.
- The record carries no component or environment claims.

## Completeness

- The exact ChEBI identifier, formula, CAS RN, InChI, SMILES, exact synonym,
  SSSOM row, aggregate copy, and docs row are populated and agree.
- The active role facet is the only consequential unsupported claim.

## Recommended Edits

- Major: in
  `data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml`, either attach
  source evidence that specifically supports the `SELECTIVE_AGENT` role for
  ciprofloxacin hydrochloride hydrate or remove the provisional role facet.
- After that YAML change, regenerate the curated aggregate, final SSSOM, and
  docs products, then rerun strict validation and the SSSOM invariant checks.
