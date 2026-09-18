# `data/ingredients/mapped/Gentamicin_Sulfate_Salt.yaml`

## Verdict

Needs curation, with a major unsupported-role issue. The CAS-backed identity
for `CHEBI:5312` gentamicin sulfate and final SSSOM CAS xref pass, but
`physicochemical_roles.SELECTIVE_AGENT` is still only a provisional
name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Gentamicin_Sulfate_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:5312` with matching
  `ontology_mapping.ontology_id`, canonical label `gentamicin sulfate`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:5312` as active gentamicin sulfate with CAS xref
  `1405-41-0`, formula `C19H37N5O7R2.H2O4S`, and SMILES matching the YAML.

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
  the same ChEBI CAS lookup, CAS RN, structure fields, single-ingredient type,
  and provisional selective-agent role as the per-record YAML.
- Issue `#317` intentionally regraded the mapping to `CAS_RN_LOOKUP` because
  CAS `1405-41-0` uniquely resolved through the ChEBI xref to `CHEBI:5312`
  gentamicin sulfate.
- The final SSSOM row maps `MIM:Gentamicin_Sulfate_Salt` to `CHEBI:5312` by
  `skos:exactMatch`, exports only `CAS:1405-41-0` in `other`, and records the
  expected `SYNONYM_ENRICH` row review.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by a
  `COMPUTATIONAL_PREDICTION` whose reference text is an inferred curated
  media-role name pattern and whose curator note says the role is provisional.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the final
  SSSOM row, row-review rows, generated indexes, old batch validation reports,
  and ignored aggregate backups.

## Completeness

- The gentamicin sulfate identity, CAS RN, structure fields, and final SSSOM
  row are populated.
- The selective-agent role needs curator review before it can be treated as
  supported.

## Recommended Edits

- Major: replace `SELECTIVE_AGENT` with source-backed evidence or remove the
  role, then rerun strict validation.
