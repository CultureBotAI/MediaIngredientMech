# `data/ingredients/mapped/Lactone.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI:25000 identity, source occurrence, empty
synonym payload, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lactone.yaml`.
- Identifier and grounding: `identifier: CHEBI:25000` with
  `ontology_mapping.ontology_id: CHEBI:25000`, label `lactone`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Source provenance: imported from MicrobeDecoder
  `kgmicrobe.trait:lactone` by OLS label-exact CHEBI matching, then promoted
  from pending review by `review-ingredients`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lacto-N-fucopentaose_II` through `Lactone`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lacto-N-fucopentaose_II.yaml data/ingredients/mapped/Lacto-N-neotetraose.yaml data/ingredients/mapped/Lactone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:25000` as active `lactone`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:25000`; its
  `other` field is empty.
- `occurrence_statistics.source_occurrences` preserves the one MicrobeDecoder
  `BacDive_Metabolite_utilization` source occurrence. No CultureMech recipe
  occurrence is expected.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row plus unrelated specific lactone compounds; no sibling generic `Lactone`
  MIM record was found.

## Completeness

- The active CHEBI identity, source occurrence, aggregate copy, and final SSSOM
  row are present and consistent.
- The record correctly leaves formula, InChI, CAS RN, and SMILES empty because
  `CHEBI:25000` is a chemical class rather than one molecular species.

## Recommended Edits

- None.
