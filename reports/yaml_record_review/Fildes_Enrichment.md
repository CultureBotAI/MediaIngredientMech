# `data/ingredients/mapped/Fildes_Enrichment.yaml`

## Verdict

Pass with minor issues. The record maps exactly to the MICRO Fildes enrichment
term and publishes a clean final SSSOM row, but this blood-digest enrichment is
missing an explicit `ingredient_type`.

## Identity

- Reviewed record: `data/ingredients/mapped/Fildes_Enrichment.yaml`.
- Identifier and grounding: `identifier: MICRO:0001597` with matching
  `ontology_mapping.ontology_id`, label `fildes enrichment`, source `MICRO`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- EBI OLS for MICRO resolves `MICRO:0001597` as `fildes enrichment`, marks it
  non-obsolete, and defines it as a peptic digest of sheep or horse blood used
  as a hemin and NAD source for microorganism cultivation.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fildes_Enrichment.yaml data/ingredients/mapped/Filipin.yaml data/ingredients/mapped/Filtered_Seawater.yaml data/ingredients/mapped/Fish-sperm_Dna.yaml data/ingredients/mapped/Fish_peptone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fildes_Enrichment.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  failed in the local MICRO validation path because the local sqlite adapter
  lacks the `rdfs_label_statement` table; prefix-specific EBI OLS resolved the
  exact MICRO CURIE and label.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  MICRO identifier, synonym, occurrence counts, stale top-level notes, and
  missing `ingredient_type` as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fildes_Enrichment` to `MICRO:0001597` with `skos:exactMatch` and an
  empty `other` column.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `MICRO:0001597` exactly through prefix-specific EBI OLS; the older
  `UNKNOWN_TERM` row in `mappings/ingredient_mappings_oak_ols_review.tsv` was
  a validator-prefix coverage gap, not a bad identifier.
- Minor: this MICRO blood-digest enrichment has no `ingredient_type`, even
  though its ontology definition indicates a complex digest that should be
  typed as a mixture after curator confirmation.
- Minor: top-level `notes` still carry the import-era "curator review needed"
  text that predates the successful MICRO promotion.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, MICRO OLS validation rows, row-review provenance,
  occurrence membership, and ignored historical batch reports.

## Completeness

- The exact MICRO identity, occurrence counts, and final SSSOM identity row are
  populated.
- No role, component, environment, or published synonym payload needs evidence
  in the current record.
- The missing mixture type is the only consequential field gap.

## Recommended Edits

- Minor: set the curator-confirmed `ingredient_type`, likely
  `UNDEFINED_MIXTURE`, in `data/ingredients/mapped/Fildes_Enrichment.yaml`;
  while touching the record, remove stale top-level review notes, sync
  `data/curated/mapped_ingredients.yaml`, and rerun strict validation plus the
  final SSSOM invariant gates.
