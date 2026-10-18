# `data/ingredients/mapped/Furfuryl_Alcohol.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed furfuryl alcohol row maps to the exact active
ChEBI chemical, its CAS resolves to the same PubChem structure, and the final
SSSOM row publishes only real same-subject aliases.

## Identity

- Reviewed record: `data/ingredients/mapped/Furfuryl_Alcohol.yaml`.
- Identifier and grounding: `identifier: CHEBI:207496` with matching
  `ontology_mapping.ontology_id`, canonical label `furfuryl alcohol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:207496` as an active term with formula `C5H6O2`,
  InChI `InChI=1S/C5H6O2/c6-4-5-2-1-3-7-5/h1-3,6H,4H2`, SMILES
  `OCc1ccco1`, CAS xref `98-00-0`, and exact synonym `furan-2-ylmethanol`.
- PubChem lookup by CAS RN `98-00-0` resolved to CID 7361 with formula
  `C5H6O2` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Furazolidone.yaml data/ingredients/mapped/Furfuryl_Alcohol.yaml data/ingredients/mapped/Fusaric_Acid.yaml data/ingredients/mapped/Fusidate.yaml data/ingredients/mapped/Fusidic_Acid_Sodium_Salt.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Furazolidone.yaml data/ingredients/mapped/Furfuryl_Alcohol.yaml data/ingredients/mapped/Fusaric_Acid.yaml data/ingredients/mapped/Fusidate.yaml data/ingredients/mapped/Fusidic_Acid_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CultureBotHT source, structure fields, CAS RN, curated
  synonym, and ingredient type as the per-record YAML.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the exact ChEBI
  row, and the row-review manifest marks it `CONFIRMED_NO_ACTION`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Furfuryl_Alcohol` to `CHEBI:207496` with `skos:exactMatch` and exports
  `furan-2-ylmethanol|CAS:98-00-0` in `other`; the first token is a ChEBI
  exact synonym and the second is the record's CAS RN.
- The record has no inferred nutritional, physicochemical, component,
  source-occurrence, or environment claim that would need independent support.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, and OAK/OLS row-review provenance.

## Completeness

- The exact furfuryl alcohol identity, single-ingredient type, structure
  fields, CAS RN, CultureBotHT provenance, curated synonym, and final SSSOM row
  are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
