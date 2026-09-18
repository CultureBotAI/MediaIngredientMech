# `data/ingredients/mapped/Gamma-cyclodextrin.yaml`

## Verdict

Pass. `CHEBI:495056` now resolves publicly as the exact active
gamma-cyclodextrin term, the record is structurally consistent with ChEBI, the
MicrobeDecoder approval row is present, and the final SSSOM row has no leaked
`other` synonyms.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Gamma-cyclodextrin.yaml`.
- Identifier and grounding: `identifier: CHEBI:495056` with matching
  `ontology_mapping.ontology_id`, canonical label `gamma-cyclodextrin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:495056` as active gamma-cyclodextrin with formula
  `C48H80O40`, InChI and SMILES matching the YAML, mass `1297.128`, and CAS
  xref `17465-86-0`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gamma-cyclodextrin.yaml data/ingredients/mapped/Garden_Soil.yaml data/ingredients/mapped/Gardimycin.yaml data/ingredients/mapped/Gelatine.yaml data/ingredients/mapped/Gelrite.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gamma-cyclodextrin.yaml data/ingredients/mapped/Gelatine.yaml data/ingredients/mapped/Gelrite.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI identifier, exact mapping, MicrobeDecoder source occurrence
  count, ChEBI/PubChem structure fields, ingredient type, and empty synonym set
  as the per-record YAML.
- `mappings/microbedecoder_auto_mapped_review.tsv` explicitly approved
  `Gamma-cyclodextrin.yaml` after an OAK round-trip and specificity check; the
  YAML curation history preserves both the earlier false-positive demotion and
  the later restoration for `CHEBI:495056`.
- The final SSSOM row maps `MIM:Gamma-cyclodextrin` to `CHEBI:495056` by
  `skos:exactMatch`, keeps the same gamma-cyclodextrin object label, records
  the manual MicrobeDecoder approval, and leaves the `other` field empty.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copies, the
  restored MicrobeDecoder regrounding rows, the final SSSOM row, generated
  indexes, and ignored aggregate backups.

## Completeness

- The exact gamma-cyclodextrin identity, structure fields, MicrobeDecoder
  provenance, ingredient type, and final SSSOM row are populated.

## Recommended Edits

- None.
