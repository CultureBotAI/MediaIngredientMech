# `data/ingredients/mapped/Azithromycin.yaml`

## Verdict

Pass. The MicrobeDecoder label is exact-mapped to non-obsolete `CHEBI:2955`
`azithromycin`, the ChEBI/PubChem formula, InChI, and SMILES match the active
ChEBI term, the source occurrences are traceable, and the aggregate plus SSSOM
rows agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Azithromycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:2955` with
  `ontology_mapping.ontology_id: CHEBI:2955`,
  `ontology_label: azithromycin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:2955` to non-obsolete `azithromycin` with CAS
  `83905-01-5`, formula `C38H72N2O12`, and the same standard InChI and SMILES
  stored locally.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azithromycin.yaml data/ingredients/mapped/Azlocillin.yaml data/ingredients/mapped/Azlocillin_Sodium_Salt.yaml data/ingredients/mapped/Azomycin.yaml data/ingredients/mapped/Aztreonam.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Azithromycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:2955` confirmed the active azithromycin identity and
  structural annotations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 511 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `data/custom/microbedecoder/unmapped_labels.tsv` and
  `data/custom/microbedecoder/ingredient_candidates.tsv` record 21
  `azithromycin` occurrences in
  `BacDive_Antibiotic_resistance|BacDive_Antibiotic_sensitivity`, matching the
  record's source occurrence.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the prior
  MicrobeDecoder auto-mapping review and approval for `Azithromycin.yaml`.
- The ChEBI structural annotations match the local formula, InChI, SMILES, and
  molecular weight.

## Completeness

- The exact identifier, formula, InChI, SMILES, source occurrence, SSSOM row,
  and aggregate copy are populated.
- No supplied form, component list, nutritional role, physicochemical role,
  cellular metabolic role, or environmental context is asserted, and none is
  required for this imported MicrobeDecoder antibiotic trait label.

## Recommended Edits

- None.
