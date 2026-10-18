# `data/ingredients/mapped/Bacteriochlorophyll_A.yaml`

## Verdict

Pass. The MicrobeDecoder label is exact-mapped to non-obsolete `CHEBI:30033`
`bacteriochlorophyll a`, the Alpha raw synonym was merged correctly, the
ChEBI/PubChem structure fields match, and the SSSOM row plus aggregate copy
are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Bacteriochlorophyll_A.yaml`.
- Identifier and grounding: `identifier: CHEBI:30033` with
  `ontology_mapping.ontology_id: CHEBI:30033`,
  `ontology_label: bacteriochlorophyll a`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:30033` to non-obsolete `bacteriochlorophyll a` with CAS
  `17499-98-8`, formula `C55H74MgN4O6`, and the same InChI and SMILES stored
  locally.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacitracin.yaml data/ingredients/mapped/Bacl2.yaml data/ingredients/mapped/Bacl2_X_2_H2o.yaml data/ingredients/mapped/Bacteriochlorophyll_A.yaml data/ingredients/mapped/Bacteriocin_Isk_1.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Bacteriochlorophyll_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:30033` confirmed the exact bacteriochlorophyll a
  identity and structure.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 524 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `data/custom/microbedecoder/unmapped_labels.tsv` and
  `data/custom/microbedecoder/ingredient_candidates.tsv` record three
  `bacteriochlorophyll a` occurrences and 20 `bacteriochlorophyll alpha`
  occurrences in `BacDive_Metabolite_production`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the prior
  MicrobeDecoder auto-mapping review and approval for this record.
- The #213 duplicate merge correctly kept `Bacteriochlorophyll Alpha` as raw
  MicrobeDecoder source text while retaining the existing `CHEBI:30033`
  identity.

## Completeness

- The exact identifier, raw synonym, formula, InChI, SMILES, MicrobeDecoder
  occurrence, SSSOM row, and aggregate copy are populated.
- No supplied form, component list, role, or environmental context is required
  for this imported MicrobeDecoder metabolite-production label.

## Recommended Edits

- None.
