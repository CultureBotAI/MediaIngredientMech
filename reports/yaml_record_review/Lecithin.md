# `data/ingredients/mapped/Lecithin.yaml`

## Verdict

Pass. The MicrobeDecoder exact CHEBI:61995 identity, source occurrence count,
empty synonym payload, and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lecithin.yaml`.
- Identifier and grounding: `identifier: CHEBI:61995` with
  `ontology_mapping.ontology_id: CHEBI:61995`, label `lecithin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Source provenance: imported from MicrobeDecoder
  `kgmicrobe.trait:lecithin` by OLS label-exact CHEBI matching, then promoted
  from pending review by `review-ingredients`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lecithin` through `Leucodin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Lecithin.yaml data/ingredients/mapped/Lentilan_From_Mushroom.yaml data/ingredients/mapped/Leucodin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the three CHEBI-primary records. The local KG-Microbe and NCIT
  records were outside this CHEBI-focused term-validation subset.

## Evidence

- EBI OLS4 resolves `CHEBI:61995` as active `lecithin`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:61995`; its
  `other` field is empty.
- `occurrence_statistics.source_occurrences` preserves the eight MicrobeDecoder
  `BacDive_Metabolite_utilization` source occurrences. No CultureMech recipe
  occurrence is expected.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same lecithin identity.

## Completeness

- The active CHEBI identity, source occurrence count, aggregate copy, and final
  SSSOM row are present and consistent.
- The record correctly leaves formula, InChI, CAS RN, and SMILES empty because
  `CHEBI:61995` denotes a lipid-rich mixture rather than one molecular species.

## Recommended Edits

- None.
