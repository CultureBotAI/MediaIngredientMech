# `data/ingredients/mapped/Fluoranthene.yaml`

## Verdict

Pass. The record denotes fluoranthene exactly, its structure agrees with
PubChem, and the final SSSOM row exports only accepted exact fluoranthene
synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Fluoranthene.yaml`.
- Identifier and grounding: `identifier: CHEBI:33083` with matching
  `ontology_mapping.ontology_id`, canonical label `fluoranthene`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by name resolved CID 9154 titled `Fluoranthene` with formula
  `C16H10` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fleroxacin.yaml data/ingredients/mapped/Flucloxacillin.yaml data/ingredients/mapped/Fluoranthene.yaml data/ingredients/mapped/Fluorene.yaml data/ingredients/mapped/Fluorescein.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fluoranthene.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, formula, InChI, SMILES, occurrence counts, synonyms, and
  ingredient type as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fluoranthene` to `CHEBI:33083` with `skos:exactMatch`.
- The final SSSOM `other` tokens are `benzo[j,k]acenaphthylene`,
  `1,2-benzacenaphthylene`, and `benzo[jk]fluorene`, matching accepted exact
  synonyms on the record.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` records
  `benzo[j,k]acenaphthylene` and `1,2-benzacenaphthylene` as already
  represented.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, synonym-enrich review, occurrence membership,
  and ignored historical batch reports.

## Completeness

- The exact fluoranthene identity, structure fields, accepted synonyms,
  ingredient type, occurrence counts, and final SSSOM payload are populated.
- I found no consequential missing role, component, or environment assertion.

## Recommended Edits

- None.
