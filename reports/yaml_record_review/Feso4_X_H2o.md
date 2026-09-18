# `data/ingredients/mapped/Feso4_X_H2o.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The record denotes
iron(II) sulfate monohydrate exactly and its final SSSOM synonym payload is
hydrate-specific, but `nutritional_roles.IRON_SOURCE` is still only a
provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Feso4_X_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:75834` with matching
  `ontology_mapping.ontology_id`, canonical label
  `iron(2+) sulfate monohydrate`, source `CHEBI`, `mapping_quality:
  EXACT_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- `mappings/hydrate_review.tsv` marks the named monohydrate and `CHEBI:75834`
  mapping as correct and high-confidence.
- PubChem lookup by CAS RN `17375-41-6` resolved to CID 62712 with formula
  `FeH2O5S` and the same monohydrate InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Feso4_X_H2o.yaml data/ingredients/mapped/Fetal_Bovine_Serum.yaml data/ingredients/mapped/Fibrin.yaml data/ingredients/mapped/Fidaxomicin.yaml data/ingredients/mapped/Fig.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Feso4_X_H2o.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  monohydrate ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence
  counts, and role evidence as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Feso4_X_H2o` to `CHEBI:75834` with `skos:exactMatch`.
- The final SSSOM `other` tokens are spelling variants of `FeSO4.H2O`, exact
  monohydrate names, monohydrate trade names curated from the ChEBI collision
  routing pass, `iron(2+) sulfate--water (1/1)`, and `CAS:17375-41-6`; all
  denote the same monohydrate or its CAS RN.
- Major: the `IRON_SOURCE` role was created by `infer_roles_from_name_lists`
  and has only `COMPUTATIONAL_PREDICTION` evidence with a curator note calling
  the name-pattern rule provisional.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, OAK/OLS row-review provenance, hydrate review
  rows, final external-prefix validation, occurrence membership, and ignored
  historical batch reports.

## Completeness

- The exact monohydrate identity, hydrate-specific CAS RN, structure fields,
  ingredient type, occurrence counts, and accepted hydrate synonyms are
  populated.
- No component or environment assertion is expected for this single hydrated
  salt.
- The one consequential gap is evidence for the nutritional role.

## Recommended Edits

- Major: either replace `nutritional_roles.IRON_SOURCE` in
  `data/ingredients/mapped/Feso4_X_H2o.yaml` with source-backed role evidence
  or remove the role, sync `data/curated/mapped_ingredients.yaml`, and rerun
  strict validation plus the final SSSOM invariant gates.
