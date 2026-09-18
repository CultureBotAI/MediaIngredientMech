# `data/ingredients/mapped/Fumaric_Acid.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The exact fumaric acid
identity, CAS-backed structure fields, supported CultureMech carbon-source
role, ChEBI synonyms, and final SSSOM payload pass, but `ENERGY_SOURCE` is
still only a provisional computational prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Fumaric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:18012` with matching
  `ontology_mapping.ontology_id`, canonical label `fumaric acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:18012`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `110-17-8` resolved to CID 444972 titled
  `Fumaric Acid` with formula `C4H4O4` and the same InChI recorded under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fumaric_Acid.yaml data/ingredients/mapped/Fumarprotocetraric_Acid.yaml data/ingredients/mapped/Fungichromin.yaml data/ingredients/mapped/Furaltadone_Hydrochloride.yaml data/ingredients/mapped/Furaxone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fumaric_Acid.yaml data/ingredients/mapped/Fumarprotocetraric_Acid.yaml data/ingredients/mapped/Fungichromin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18012 CHEBI:144157 CHEBI:31639`:
  returned the active ChEBI label, formula, InChI, SMILES, mass, and synonyms
  for `CHEBI:18012`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, exact mapping, structure fields, CAS RN, kg-microbe node
  ID, ingredient type, synonyms, occurrence counts, supported carbon-source
  role, and computational energy-source role as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fumaric_Acid` to `CHEBI:18012` with `skos:exactMatch`, exports valid
  ChEBI synonyms plus `CAS:110-17-8`, and correctly omits the raw
  `(disodium salt)` and `Role:` / `Properties:` tokens.
- `nutritional_roles.CARBON_SOURCE` is backed by CultureMech `DATABASE_ENTRY`
  evidence for the original `Role: Carbon source` import surface.
- Major: `nutritional_roles.ENERGY_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence added alongside the carbon-source role
  and the evidence note explicitly says the role is provisional.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` only records that
  the raw disodium-salt candidate text was already present in the YAML; the
  synonym policy filters that parenthetical form out of the final SSSOM row.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM row, CultureMech recipe memberships, row-review entries, and a
  fumaric-acid component in a local decomposed ingredient.

## Completeness

- The exact fumaric acid identity, supported carbon-source role, structure
  fields, CAS RN, occurrence counts, and final SSSOM identity row are populated.
- No component, environment, unsafe final synonym, or missing structure gap
  remains for the current ChEBI identity.

## Recommended Edits

- Major: either replace `nutritional_roles.ENERGY_SOURCE` in
  `data/ingredients/mapped/Fumaric_Acid.yaml` with inspected source-backed
  evidence for fumaric acid in media, or remove the unsupported role; then sync
  `data/curated/mapped_ingredients.yaml` and rerun strict validation.
