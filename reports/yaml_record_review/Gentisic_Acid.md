# `data/ingredients/mapped/Gentisic_Acid.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The exact `CHEBI:17189`
gentisic acid identity, acid/base synonyms, CAS RN, structure fields, and final
SSSOM aliases pass, but `nutritional_roles.CARBON_SOURCE` is still only a
provisional in-session LLM prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Gentisic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17189` with matching
  `ontology_mapping.ontology_id`, canonical label
  `2,5-dihydroxybenzoic acid`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:17189` as active 2,5-dihydroxybenzoic acid with CAS xref
  `490-79-9`, formula `C7H6O4`, and InChI/SMILES matching the YAML.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gentisic_Acid.yaml data/ingredients/mapped/Geomycin.yaml data/ingredients/mapped/Gepotidacin.yaml data/ingredients/mapped/Geraniol.yaml data/ingredients/mapped/Ginger.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gentisic_Acid.yaml data/ingredients/mapped/Gepotidacin.yaml data/ingredients/mapped/Geraniol.yaml data/ingredients/mapped/Ginger.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI/NCIT-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact mapping, 3 CultureMech occurrences, CAS RN, structure
  fields, single-ingredient type, acid/base synonyms, and provisional
  carbon-source role as the per-record YAML.
- OLS4 lists `Gentisic acid`, `2,5-Dihydroxybenzoate`, `Gentisate`,
  `5-hydroxysalicylic acid`, and `Hydroquinonecarboxylic acid` as synonyms of
  `CHEBI:17189`.
- The final SSSOM row maps `MIM:Gentisic_Acid` to `CHEBI:17189` by
  `skos:exactMatch` and exports only OLS4 synonyms plus `CAS:490-79-9` in
  `other`. The bare raw `(sodium salt)` token is filtered as expected.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by a
  `COMPUTATIONAL_PREDICTION` assigned by in-session Claude reasoning with no
  external API, and the curator note says the role is provisional.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM and row-review rows, generated indexes, old batch validation reports,
  and ignored aggregate backups.

## Completeness

- The gentisic acid identity, CAS RN, structure fields, synonyms, occurrence
  count, and final SSSOM row are populated.
- The carbon-source role needs curator review before it can be treated as
  supported.

## Recommended Edits

- Major: replace `CARBON_SOURCE` with source-backed evidence or remove the role,
  then rerun strict validation.
