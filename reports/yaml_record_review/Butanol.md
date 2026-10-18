# `data/ingredients/mapped/Butanol.yaml`

## Verdict

Needs curation, minor. The CAS-backed `CHEBI:28885` butan-1-ol identity, CAS,
`1-Butanol` alias, structure fields, SSSOM row, and aggregate copy agree, but
the occurrence statistics were not refreshed after the `1-Butanol` CultureMech
alias was folded into the record.

## Identity

- Reviewed record: `data/ingredients/mapped/Butanol.yaml`.
- Identifier and grounding: `identifier: CHEBI:28885` with
  `ontology_mapping.ontology_id: CHEBI:28885`,
  `ontology_label: butan-1-ol`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS search for `butan-1-ol` returns `CHEBI:28885`, whose CAS xref,
  formula, InChI, and SMILES match the populated local claims.
- PubChem resolves CAS `71-36-3` to CID 263 with formula `C4H10O` and the same
  standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Butan-1-amine.yaml data/ingredients/mapped/Butane-14-diol.yaml data/ingredients/mapped/Butanol.yaml data/ingredients/mapped/Butyl_Stearate.yaml data/ingredients/mapped/Butyl_Vinyl_Ether.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Butan-1-amine.yaml data/ingredients/mapped/Butane-14-diol.yaml data/ingredients/mapped/Butanol.yaml data/ingredients/mapped/Butyl_Stearate.yaml data/ingredients/mapped/Butyl_Vinyl_Ether.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the synonym-enrichment row, the authoritative exact
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 639, the
  `1-Butanol` residual grounding and triage rows, and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Butanol` to `CHEBI:28885` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`; its `other` field publishes `1-Butanol|CAS:71-36-3`.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact ChEBI identifier, CAS, CultureMech alias, single-ingredient
  classification, formula, InChI, SMILES, SSSOM row, and aggregate copy are
  populated.
- Minor gap: `occurrence_statistics` still says 0/0 even though the later alias
  backfill found four `1-Butanol` CultureMech residual mentions that are still
  present in `mappings/culturemech_residual_groundings.tsv` and
  `mappings/culturemech_residual_triage.tsv`.
- No roles, components, or environmental contexts are required for this
  single-compound record.

## Recommended Edits

- Minor: refresh `data/ingredients/mapped/Butanol.yaml` occurrence statistics
  from the maintained CultureMech occurrence table after the `1-Butanol` alias
  is represented in the membership export; then run `just sync-curated` and
  focused strict/term/SSSOM validation.
