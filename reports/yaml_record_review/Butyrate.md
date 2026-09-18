# `data/ingredients/mapped/Butyrate.yaml`

## Verdict

Pass. The exact `CHEBI:17968` butyrate identity, anion structure fields,
MicrobeDecoder provenance, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Butyrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17968` with
  `ontology_mapping.ontology_id: CHEBI:17968`,
  `ontology_label: butyrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS search for `Butyrate` returns `CHEBI:17968` as the exact
  deprotonated conjugate base of butyric acid, matching the local anion rather
  than the neutral acid.
- PubChem resolves `Butyrate` to CID 104775 with the same standard InChI and
  anion SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Butyrate.yaml data/ingredients/mapped/Butyric_Acid.yaml data/ingredients/mapped/Butyricin_7423.yaml data/ingredients/mapped/Butyrolactam.yaml data/ingredients/mapped/CCCP.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Butyrate.yaml data/ingredients/mapped/Butyric_Acid.yaml data/ingredients/mapped/Butyricin_7423.yaml data/ingredients/mapped/Butyrolactam.yaml data/ingredients/mapped/CCCP.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the MicrobeDecoder source provenance for
  `kgmicrobe.trait:butyrate`, the MicrobeDecoder auto-mapped review approval,
  the authoritative exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv`
  row 642, and the aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Butyrate` to `CHEBI:17968` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, MicrobeDecoder occurrence, single-ingredient
  classification, formula, InChI, SMILES, molecular weight, SSSOM row, and
  aggregate copy are populated.
- `occurrence_statistics.total_occurrences: 0` and `media_count: 0` are
  consistent with a MicrobeDecoder-only import that has no CultureMech recipe
  memberships.
- No roles, components, or environmental contexts are required for this
  single-compound production/utilization label.

## Recommended Edits

- None.
