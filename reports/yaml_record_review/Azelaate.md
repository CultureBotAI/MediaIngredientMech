# `data/ingredients/mapped/Azelaate.yaml`

## Verdict

Pass. The bare MicrobeDecoder `azelaate` label is exact-mapped to generic
`CHEBI:132955` `azelaate`, not over-narrowed to the dianion
`CHEBI:78208` `azelaate(2-)`, and the aggregate plus SSSOM rows publish the
same generic anion identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Azelaate.yaml`.
- Identifier and grounding: `identifier: CHEBI:132955` with
  `ontology_mapping.ontology_id: CHEBI:132955`,
  `ontology_label: azelaate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:132955` to non-obsolete `azelaate`, a generic anion
  obtained by deprotonating at least one carboxy group of azelaic acid.
- OLS also has the narrower `CHEBI:78208` `azelaate(2-)` term, but the source
  label `azelaate` does not specify complete deprotonation or charge -2.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azacolutin.yaml data/ingredients/mapped/Azadirachtin.yaml data/ingredients/mapped/Azaserine.yaml data/ingredients/mapped/Azelaate.yaml data/ingredients/mapped/Azelaic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Azelaate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookups for `CHEBI:132955` and `CHEBI:78208` confirmed that the current
  target is the broader azelaate anion and that the structural dianion is more
  specific than the MicrobeDecoder source label.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 509 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `data/custom/microbedecoder/unmapped_labels.tsv` and
  `data/custom/microbedecoder/ingredient_candidates.tsv` record thirteen
  `azelaate` source occurrences in `BacDive_Metabolite_utilization`, matching
  `occurrence_statistics.source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the prior
  MicrobeDecoder auto-mapping review and approval for `Azelaate.yaml`.
- The absence of fixed formula, InChI, SMILES, and molecular weight fields is
  appropriate because `CHEBI:132955` spans multiple protonation states.

## Completeness

- The exact generic anion identifier, source occurrence, SSSOM row, and
  aggregate copy are populated.
- No supplied form, component list, ingredient type, role, or environmental
  context is asserted, and none is required for the underspecified
  MicrobeDecoder trait label.

## Recommended Edits

- None.
