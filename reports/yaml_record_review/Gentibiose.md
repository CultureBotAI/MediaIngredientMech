# `data/ingredients/mapped/Gentibiose.yaml`

## Verdict

Needs curation, with a major unsupported-role issue and a minor preferred-term
typo. The CAS-backed `CHEBI:28066` gentiobiose identity, structure fields, and
exported CAS/IUPAC aliases pass, but `nutritional_roles.CARBON_SOURCE` is still
only a provisional ChEBI-ancestry prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Gentibiose.yaml`.
- Identifier and grounding: `identifier: CHEBI:28066` with matching
  `ontology_mapping.ontology_id`, canonical label `gentiobiose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:28066` as active gentiobiose with CAS xref `554-91-6`,
  formula `C12H22O11`, the exported
  `beta-D-glucopyranosyl-(1->6)-D-glucopyranose` synonym, and InChI/SMILES
  matching the YAML.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Geneticin_G418.yaml data/ingredients/mapped/Gentamicin.yaml data/ingredients/mapped/Gentamicin_C2b.yaml data/ingredients/mapped/Gentamicin_Sulfate_Salt.yaml data/ingredients/mapped/Gentibiose.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Geneticin_G418.yaml data/ingredients/mapped/Gentamicin.yaml data/ingredients/mapped/Gentamicin_C2b.yaml data/ingredients/mapped/Gentamicin_Sulfate_Salt.yaml data/ingredients/mapped/Gentibiose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI identity, CAS RN, structure fields, IUPAC synonym,
  single-ingredient type, and provisional carbon-source role as the per-record
  YAML.
- The final SSSOM row maps `MIM:Gentibiose` to `CHEBI:28066` by
  `skos:exactMatch` and exports only the ChEBI IUPAC synonym plus
  `CAS:554-91-6` in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by a
  `COMPUTATIONAL_PREDICTION` from ChEBI carbohydrate ancestry whose curator
  note says the role is provisional.
- Minor: `preferred_term` is `Gentibiose`, while ChEBI spells the disaccharide
  `gentiobiose` and OLS4 does not list `Gentibiose` as a synonym. The final
  SSSOM `other` field stays clean, but the preferred term and subject label
  should be corrected.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM row, row-review rows, generated indexes, old batch validation reports,
  and ignored aggregate backups.

## Completeness

- The exact gentiobiose identity, CAS RN, structure fields, curated synonym,
  and final SSSOM row are populated.
- The carbon-source role needs curator review and the stored preferred term
  needs spelling cleanup.

## Recommended Edits

- Major: replace `CARBON_SOURCE` with source-backed evidence or remove the role,
  then rerun strict validation.
- Minor: change `preferred_term` from `Gentibiose` to `Gentiobiose`; regenerate
  final SSSOM and rerun SSSOM invariants so the subject label updates too.
