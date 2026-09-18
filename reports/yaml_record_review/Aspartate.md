# `data/ingredients/mapped/Aspartate.yaml`

## Verdict

Pass. The record intentionally maps the bare MicrobeDecoder `aspartate` surface
to stereo-agnostic `CHEBI:29995` `aspartate(2-)`, preserves the regrounding
rationale from #319, and keeps the aggregate and SSSOM surfaces consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Aspartate.yaml`.
- Identifier and grounding: `identifier: CHEBI:29995` with
  `ontology_mapping.ontology_id: CHEBI:29995`,
  `ontology_label: aspartate(2-)`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:29995` to non-obsolete `aspartate(2-)` with exact
  synonym `aspartate`, formula `C4H5NO4`, and the same dianion InChI and SMILES
  stored on the record.
- Separate sibling records already model the stereospecific MicrobeDecoder
  residues `D-aspartate` and `L-aspartate`, so this bare record does not claim a
  D or L form.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Asparagine.yaml data/ingredients/mapped/Aspartate.yaml data/ingredients/mapped/Astaxanthin.yaml data/ingredients/mapped/Astromicin.yaml data/ingredients/mapped/Atorvastatin_Calcium_Salt_Trihydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Aspartate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:29995` resolved the expected non-obsolete term and
  confirmed the `aspartate` exact synonym, formula, InChI, and SMILES.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 490 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `data/custom/microbedecoder/unmapped_labels.tsv` preserves the raw
  `kgmicrobe.trait:aspartate` import label with count 431 in
  `BacDive_Metabolite_utilization`.
- `mappings/culturemech_recipe_membership.tsv` has 12 `CHEBI:29995`
  memberships, matching `occurrence_statistics`.
- The `MIM curation (#319)` evidence on the record explains why the original
  `CHEBI:132943` parent was narrowed to the dianion while preserving an
  explicitly recorded counterargument.

## Completeness

- The exact identifier, label, mapping quality, chemistry fields, source
  occurrence, CultureMech occurrence count, aggregate copy, and SSSOM row are
  populated.
- `synonyms` is correctly empty: the raw source was the preferred term itself.
- No hydrate, salt, stereochemical, role, component, or literature evidence
  fields are needed for this import-only record.

## Recommended Edits

- None.
