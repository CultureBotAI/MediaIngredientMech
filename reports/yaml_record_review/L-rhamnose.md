# `data/ingredients/mapped/L-rhamnose.yaml`

## Verdict

Pass with minor issues. The CultureMech exact CHEBI:62345 identity,
carbon-source role, occurrence count, reviewed synonym, and final SSSOM row
pass, but the PubChem chemistry block was never backfilled beyond
provenance-only metadata.

## Identity

- Reviewed record: `data/ingredients/mapped/L-rhamnose.yaml`.
- Identifier and grounding: `identifier: CHEBI:62345` with
  `ontology_mapping.ontology_id: CHEBI:62345`, label `L-rhamnose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Role facets: `nutritional_roles.CARBON_SOURCE` with
  `DATABASE_ENTRY` evidence from the imported CultureMech role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-proline_2-naphthylamide.yaml data/ingredients/mapped/L-pyroglutamic_Acid_2-naphthylamide.yaml data/ingredients/mapped/L-rhamnose.yaml data/ingredients/mapped/L-serine.yaml data/ingredients/mapped/L-serine_2-naphthylamide.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-proline_2-naphthylamide.yaml data/ingredients/mapped/L-pyroglutamic_Acid_2-naphthylamide.yaml data/ingredients/mapped/L-rhamnose.yaml data/ingredients/mapped/L-serine.yaml data/ingredients/mapped/L-serine_2-naphthylamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:62345` as active `L-rhamnose`.
- PubChem resolves `L-rhamnose` to CID `25310` with formula `C6H12O5`.
- `nutritional_roles.CARBON_SOURCE` is backed by `DATABASE_ENTRY` evidence
  whose curator note preserves the original CultureMech role text, `Carbon
  Source`, matching the facet.
- The exact OLS search for final synonym `L-rhamnoses` returns CHEBI:62345, so
  the unusual plural kg-microbe token does not cross an identity boundary.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:62345`; its
  `other` field contains only the reviewed exact synonym `L-rhamnoses`.
- Minor: `chemical_properties` still contains only `data_source` and
  `retrieval_date`, even though the ChEBI identity now has a PubChem-resolvable
  formula and structure.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, the CAS-anchored monohydrate sibling, and the
  alpha-L-rhamnose sibling.

## Completeness

- The active ChEBI identity, carbon-source role, occurrence count, aggregate
  copy, final synonym, and final SSSOM row are present and consistent.
- The CAS history is not represented as an active CAS field, and no suspect CAS
  token is exported in final SSSOM.

## Recommended Edits

- Minor: backfill `chemical_properties` for
  `data/ingredients/mapped/L-rhamnose.yaml` from the exact ChEBI/PubChem
  structure the next time this record is touched, then sync the aggregate copy.
