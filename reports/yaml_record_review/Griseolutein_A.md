# `data/ingredients/mapped/Griseolutein_A.yaml`

## Verdict

Pass. The placeholder upgrade to exact `mesh:C018306` griseolutein A still
resolves in prefix-specific OLS, no unsupported roles are asserted, and the
final MeSH registry SSSOM row is clean.

## Identity

- Reviewed record: `data/ingredients/mapped/Griseolutein_A.yaml`.
- Identifier and grounding: `identifier: mesh:C018306` with matching
  `ontology_mapping.ontology_id`, label `griseolutein A`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Granaticin.yaml data/ingredients/mapped/Grasseriomycin.yaml data/ingredients/mapped/Green_House_Soil.yaml data/ingredients/mapped/Grisamine.yaml data/ingredients/mapped/Griseolutein_A.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation was skipped for this MeSH primary because the
  repository's focused term validator does not cover MeSH CURIEs.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `mesh:C018306` under the MeSH ontology as active
  `griseolutein A`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` confirms
  that `mesh:C018306` resolves by prefix-specific OLS query; the final
  `UNKNOWN_TERM` marker on older row-review TSVs came from synonym-review
  dispatcher prefix coverage, not from a bad MeSH CURIE.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Griseolutein_A` to `mesh:C018306` by `skos:exactMatch` with an empty
  `other` payload.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, the external
  prefix-resolution TSV, matching aggregate copies, generated products, the
  final SSSOM row, row-review TSVs, and ignored aggregate backups.

## Completeness

- The exact MeSH identity, promotion history, singleton type, and final SSSOM
  row are populated.
- Chemical structure fields are absent, which is acceptable because this record
  is grounded to MeSH rather than CHEBI or PubChem.
- No role facet is asserted, which is acceptable for this record.

## Recommended Edits

- None.
