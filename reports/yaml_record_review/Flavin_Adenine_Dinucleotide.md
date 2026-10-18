# `data/ingredients/mapped/Flavin_Adenine_Dinucleotide.yaml`

## Verdict

Pass. The record denotes flavin adenine dinucleotide exactly, its CAS RN
resolves to the same PubChem compound, and the final SSSOM payload contains
only the exact ChEBI row plus the same-substance CAS alias.

## Identity

- Reviewed record: `data/ingredients/mapped/Flavin_Adenine_Dinucleotide.yaml`.
- Identifier and grounding: `identifier: CHEBI:24040` with matching
  `ontology_mapping.ontology_id`, canonical label
  `flavin adenine dinucleotide`, source `CHEBI`, `mapping_quality:
  EXACT_MATCH`, `mapping_status: MAPPED`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `146-14-5` resolved to CID 643975 titled
  `Flavin Adenine Dinucleotide`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Flavensomycin.yaml data/ingredients/mapped/Flavin_Adenine_Dinucleotide.yaml data/ingredients/mapped/Flavofungin.yaml data/ingredients/mapped/Flavomycin.yaml data/ingredients/mapped/Flavone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Flavin_Adenine_Dinucleotide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, occurrence counts, and ingredient type as the
  per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Flavin_Adenine_Dinucleotide` to `CHEBI:24040` with
  `skos:exactMatch`.
- The final SSSOM `other` column contains only `CAS:146-14-5`, matching
  `chemical_properties.cas_rn`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` records the ChEBI row
  as `CONFIRMED_NO_ACTION`.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, OAK/OLS confirmation, occurrence membership, and
  an existing `Fad` synonym/duplicate record using the same CAS RN.

## Completeness

- The exact ChEBI identity, CAS RN, ingredient type, occurrence counts, and
  final SSSOM CAS alias are populated.
- I found no consequential missing role, component, environment, or synonym
  payload.

## Recommended Edits

- None.
