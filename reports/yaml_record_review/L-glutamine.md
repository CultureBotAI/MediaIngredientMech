# `data/ingredients/mapped/L-glutamine.yaml`

## Verdict

Pass. The CultureMech exact CHEBI:18050 identity, CAS RN, PubChem structure,
claim-level nitrogen-source role, occurrence count, reviewed synonyms, and
final SSSOM row are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-glutamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:18050` with
  `ontology_mapping.ontology_id: CHEBI:18050`, label `L-glutamine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `56-85-9`, molecular formula `C5H10N2O3`,
  InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-glutamate-gamma-3-carboxy-4-nitroanilide.yaml data/ingredients/mapped/L-glutamic_Acid.yaml data/ingredients/mapped/L-glutamine.yaml data/ingredients/mapped/L-histidine.yaml data/ingredients/mapped/L-histidine_2-naphthylamide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-glutamic_Acid.yaml data/ingredients/mapped/L-glutamine.yaml data/ingredients/mapped/L-histidine.yaml data/ingredients/mapped/L-histidine_2-naphthylamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the four OBO-backed ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:18050` as active `L-glutamine` and lists CAS
  `56-85-9`.
- PubChem resolves CAS RN `56-85-9` to CID `5961` with formula `C5H10N2O3` and
  the same InChI as the YAML record.
- `nutritional_roles.NITROGEN_SOURCE` has `DATABASE_ENTRY` evidence from the
  CultureMech database role text for this ingredient, matching the migrated
  role enum.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:18050`; its
  `other` field contains exact ChEBI or kg-microbe synonyms plus
  `CAS:56-85-9`, with no raw cross-reference text.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and the row-review confirmation.

## Completeness

- The active ChEBI identity, CAS RN, structure, occurrence count, role,
  aggregate copy, and final SSSOM row are present and consistent.

## Recommended Edits

- None.
