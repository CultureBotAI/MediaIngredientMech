# `data/ingredients/mapped/5-Fluoroorotic_Acid_Hydrate.yaml`

## Verdict

Needs curation, major. The CAS primary identity, PubChem hydrate chemistry,
`skos:closeMatch` relation to anhydrous `CHEBI:74498`, and registry SSSOM row
pass, but an unqualified anhydrous systematic name is still exported as an
exact synonym of the hydrate.

## Identity

- Reviewed record:
  `data/ingredients/mapped/5-Fluoroorotic_Acid_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:207291-81-4` with
  `ontology_mapping.ontology_id: CHEBI:74498`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:74498` is active and resolves to
  `5-fluoroorotic acid`, the anhydrous parent.
- The stored PubChem CID `16212749`, formula `C5H5FN2O5`, SMILES
  `C1(=C(NC(=O)NC1=O)C(=O)O)F.O`, and dot-disconnected InChI consistently
  model 5-fluoroorotic acid hydrate rather than anhydrous 5-fluoroorotic acid.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-Deoxy-5-fluorocytidine.yaml data/ingredients/mapped/5-Fluorodihydropyrimidine-24-dione.yaml data/ingredients/mapped/5-Fluoroorotic_Acid_Hydrate.yaml data/ingredients/mapped/5-Hydroxydodecanoate.yaml data/ingredients/mapped/5-Hydroxymethylfurfural.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/5-Fluoroorotic_Acid_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the ChEBI parent mapping.

## Evidence

- The 2026-08-13 regrade correctly moved the ontology relationship from
  `NARROW_MATCH` to `CLOSE_MATCH`: the hydrate has its own CAS primary
  identifier, and the SSSOM builder emits both a `skos:closeMatch` row to
  anhydrous `CHEBI:74498` and a `skos:exactMatch` registry row to
  `cas:207291-81-4`.
- The `UNKNOWN_TERM` status on the CAS registry row is expected; the
  unknown-term triage marks the CAS CURIE as an expected registry identifier,
  not a broken OAK/OLS ontology target.
- Major: `5-fluoro-2,6-dioxo-1,2,3,6-tetrahydropyrimidine-4-carboxylic acid`
  is an unqualified name for anhydrous 5-fluoroorotic acid. Keeping it as an
  `EXACT_SYNONYM` on the hydrate blurs the hydrate/anhydrous distinction and
  exports that blur through the SSSOM `other` column and generated
  `label_index`.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `docs`
  found the active YAML, aggregate copy, parent and registry SSSOM rows,
  hydrate review TSV, unknown-term triage TSV, synonym-enrichment review TSV,
  stale advisory rows, generated docs, and ignored aggregate backups.

## Completeness

- CAS, PubChem CID, formula, InChI, SMILES, and `ingredient_type` are
  populated for the hydrate.
- No roles, components, environment, or discussion entries need review.

## Recommended Edits

1. Remove or reject
   `5-fluoro-2,6-dioxo-1,2,3,6-tetrahydropyrimidine-4-carboxylic acid` as an
   exact synonym of `5-Fluoroorotic acid hydrate` in
   `data/ingredients/mapped/5-Fluoroorotic_Acid_Hydrate.yaml` and
   `data/curated/mapped_ingredients.yaml`, then regenerate SSSOM and docs so
   the anhydrous name no longer publishes as a hydrate synonym.
