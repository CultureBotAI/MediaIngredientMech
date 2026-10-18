# `data/ingredients/mapped/Azaserine.yaml`

## Verdict

Pass. The MicrobeDecoder label is exact-mapped to non-obsolete `CHEBI:74846`
`azaserine`, the stored formula, InChI, and SMILES describe the same structure,
the source occurrence is traceable, and the aggregate plus SSSOM rows agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Azaserine.yaml`.
- Identifier and grounding: `identifier: CHEBI:74846` with
  `ontology_mapping.ontology_id: CHEBI:74846`,
  `ontology_label: azaserine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search resolves `Azaserine` to non-obsolete `CHEBI:74846`.
- PubChem lookup for azaserine CAS `115-02-6` resolves to title `Azaserine`,
  formula `C5H7N3O4`, and the same standard InChI recorded locally.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azacolutin.yaml data/ingredients/mapped/Azadirachtin.yaml data/ingredients/mapped/Azaserine.yaml data/ingredients/mapped/Azelaate.yaml data/ingredients/mapped/Azelaic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Azaserine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `Azaserine` and PubChem lookup for azaserine CAS `115-02-6`
  confirmed the exact identity and structure.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 508 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `data/custom/microbedecoder/unmapped_labels.tsv` and
  `data/custom/microbedecoder/ingredient_candidates.tsv` record one
  `azaserine` source occurrence in `BacDive_Metabolite_production`, matching
  `occurrence_statistics.source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the prior
  MicrobeDecoder auto-mapping review and approval for `Azaserine.yaml`.
- The structural fields were populated from `ChEBI+PubChem` and match
  PubChem's azaserine formula and standard InChI.

## Completeness

- The exact identifier, formula, InChI, SMILES, source occurrence, SSSOM row,
  and aggregate copy are populated.
- No supplied form, component list, nutritional role, physicochemical role,
  cellular metabolic role, or environmental context is asserted, and none is
  required for this imported MicrobeDecoder metabolite-production label.

## Recommended Edits

- None.
