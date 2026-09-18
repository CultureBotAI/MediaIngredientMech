# `data/ingredients/mapped/L-serine_2-naphthylamide.yaml`

## Verdict

Pass. The MicrobeDecoder exact-label promotion to active CHEBI:90603, ChEBI
structure, empty synonym payload, source occurrence count, and final SSSOM row
are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-serine_2-naphthylamide.yaml`.
- Identifier and grounding: `identifier: CHEBI:90603` with
  `ontology_mapping.ontology_id: CHEBI:90603`, label
  `L-serine 2-naphthylamide`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C13H14N2O2`, InChI, SMILES, and
  molecular weight from ChEBI plus PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-proline_2-naphthylamide.yaml data/ingredients/mapped/L-pyroglutamic_Acid_2-naphthylamide.yaml data/ingredients/mapped/L-rhamnose.yaml data/ingredients/mapped/L-serine.yaml data/ingredients/mapped/L-serine_2-naphthylamide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-proline_2-naphthylamide.yaml data/ingredients/mapped/L-pyroglutamic_Acid_2-naphthylamide.yaml data/ingredients/mapped/L-rhamnose.yaml data/ingredients/mapped/L-serine.yaml data/ingredients/mapped/L-serine_2-naphthylamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:90603` as active
  `L-serine 2-naphthylamide`.
- PubChem resolves `L-serine 2-naphthylamide` to CID `688575` with formula
  `C13H14N2O2` and the same InChI as the YAML record.
- The MicrobeDecoder import grounded
  `kgmicrobe.trait:l_serine_2_naphthylamide` by exact OLS label match and
  records one `BacDive_Metabolite_utilization` source occurrence; the later
  `review-ingredients` event promoted the held mapping back to `MAPPED`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:90603` with an
  empty `other` field, so no unreviewed synonyms are exported.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy,
  MicrobeDecoder source rows, final SSSOM row, and docs projections.

## Completeness

- The active ChEBI identity, structure, source occurrence count, empty synonym
  list, aggregate copy, and final SSSOM row are present and consistent.
- The empty CultureMech `occurrence_statistics` count is expected for this
  MicrobeDecoder-only import because its evidence is captured under
  `source_occurrences`.

## Recommended Edits

- None.
