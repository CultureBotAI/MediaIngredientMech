# `data/ingredients/mapped/Avermectin.yaml`

## Verdict

Pass. The MicrobeDecoder `avermectin` production label exact-maps to the generic
`CHEBI:50344` avermectin class, which has no fixed structure and is therefore
correctly left without chemical structure fields.

## Identity

- Reviewed record: `data/ingredients/mapped/Avermectin.yaml`.
- Identifier and grounding: `identifier: CHEBI:50344` with
  `ontology_mapping.ontology_id: CHEBI:50344`,
  `ontology_label: avermectin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:50344` to non-obsolete `avermectin`, a generic class with
  child terms and no formula, InChI, or SMILES annotation.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Atrazin.yaml data/ingredients/mapped/Atrop_Abyssomicin_C.yaml data/ingredients/mapped/Auraptene.yaml data/ingredients/mapped/Aureothricin.yaml data/ingredients/mapped/Avermectin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Avermectin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:50344` resolved the expected non-obsolete generic
  avermectin class.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 498 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `data/custom/microbedecoder/unmapped_labels.tsv` preserves the raw
  `kgmicrobe.trait:avermectin` import label with count 1 in
  `BacDive_Metabolite_production`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the local
  post-import approval that promoted this exact CHEBI import from
  `PENDING_REVIEW` to `MAPPED`.

## Completeness

- The exact identifier, label, mapping quality, source occurrence, aggregate
  copy, and SSSOM row are populated.
- The absent chemical structure is appropriate because the ChEBI term is a
  generic class, not one defined compound.
- The 0/0 CultureMech occurrence count is correct for a MicrobeDecoder-only
  record that has not appeared in CultureMech recipe memberships.
- No synonyms, roles, components, or literature references are required for the
  current record.

## Recommended Edits

- None.
