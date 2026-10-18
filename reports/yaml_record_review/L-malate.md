# `data/ingredients/mapped/L-malate.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder synonym promotion to active
CHEBI:15589, dianion structure, source occurrence count, empty final synonym
payload, and final SSSOM row are consistent; only stale importer notes still
say the record lacked a CHEBI/NCIT match.

## Identity

- Reviewed record: `data/ingredients/mapped/L-malate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15589` with
  `ontology_mapping.ontology_id: CHEBI:15589`, label `(S)-malate(2-)`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C4H4O5`, dianion InChI and SMILES,
  and molecular weight from ChEBI plus PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-lysine_Hcl.yaml data/ingredients/mapped/L-lyxose.yaml data/ingredients/mapped/L-malate.yaml data/ingredients/mapped/L-methionine.yaml data/ingredients/mapped/L-norleucine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-lysine_Hcl.yaml data/ingredients/mapped/L-lyxose.yaml data/ingredients/mapped/L-malate.yaml data/ingredients/mapped/L-methionine.yaml data/ingredients/mapped/L-norleucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:15589` as active `(S)-malate(2-)`.
- PubChem resolves `L-malate` to CID `5459792` with formula `C4H4O5-2` and
  the same InChI as the YAML record.
- The resolved-unmapped promotion records the Edison identity research and
  local CHEBI verification that `L-malate` is a ChEBI synonym of
  `(S)-malate(2-)`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:15589` with an
  empty `other` field, so no raw MicrobeDecoder text or sodium-malate sibling
  synonym is exported.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, and the separate sodium malate sibling.
- Minor: the top-level `notes` and original import history still say there was
  no CHEBI/NCIT match and curator review was needed. That was true at import,
  but the record was later promoted to CHEBI:15589.

## Completeness

- The ChEBI identity, synonym-grade mapping, structure, source occurrence
  count, aggregate copy, and final SSSOM row are present and consistent.

## Recommended Edits

- Minor: update the stale top-level `notes` in
  `data/ingredients/mapped/L-malate.yaml` and the aggregate copy the next time
  the record is touched so the current review text does not imply that the
  CHEBI search is still unresolved.
