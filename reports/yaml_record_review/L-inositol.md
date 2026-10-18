# `data/ingredients/mapped/L-inositol.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder synonym promotion to active
CHEBI:27374, formula, occurrence counts, empty final synonym payload, and final
SSSOM row are consistent; only stale importer notes still say the record
lacked a CHEBI/NCIT match.

## Identity

- Reviewed record: `data/ingredients/mapped/L-inositol.yaml`.
- Identifier and grounding: `identifier: CHEBI:27374` with
  `ontology_mapping.ontology_id: CHEBI:27374`, label `1L-chiro-inositol`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C6H12O6`, InChI, SMILES, and
  molecular weight from ChEBI plus PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-inositol.yaml data/ingredients/mapped/L-isoleucine.yaml data/ingredients/mapped/L-leucine.yaml data/ingredients/mapped/L-leucylglycine_2-naphthylamide.yaml data/ingredients/mapped/L-lysine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-inositol.yaml data/ingredients/mapped/L-isoleucine.yaml data/ingredients/mapped/L-leucine.yaml data/ingredients/mapped/L-leucylglycine_2-naphthylamide.yaml data/ingredients/mapped/L-lysine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:27374` as active `1L-chiro-inositol`, lists
  `L-inositol` as an exact synonym, and lists CAS `551-72-4`.
- PubChem lookup for `1L-chiro-inositol` returns formula `C6H12O6`, matching
  the YAML formula.
- The MicrobeDecoder import records one `BacDive_Metabolite_utilization`
  source occurrence and the refreshed CultureMech occurrence table records one
  medium occurrence.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:27374` with an
  empty `other` field, so no raw MicrobeDecoder text is exported.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy,
  MicrobeDecoder source rows, final SSSOM row, docs projections, and the
  resolved-unmapped grounding row that supports the promotion.
- Minor: the top-level `notes` and original import history still say there was
  no CHEBI/NCIT match and curator review was needed. That was true at import,
  but the record was later promoted to CHEBI:27374.

## Completeness

- The ChEBI identity, synonym-grade mapping, formula, occurrence counts,
  aggregate copy, and final SSSOM row are present and consistent.

## Recommended Edits

- Minor: update the stale top-level `notes` in
  `data/ingredients/mapped/L-inositol.yaml` and the aggregate copy the next
  time the record is touched so the current review text does not imply that
  the CHEBI search is still unresolved.
