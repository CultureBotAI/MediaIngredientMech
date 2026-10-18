# `data/ingredients/mapped/Cinnamic_Acid.yaml`

## Verdict

Needs curation, major. The record validates and its CAS was normalized
correctly, but CAS `140-10-3` resolves to trans-cinnamic acid while the record
is exact-mapped to the generic parent `CHEBI:27386` cinnamic acid; this
duplicates the existing active `Trans-cinnamic_Acid` record for `CHEBI:35697`.

## Identity

- Reviewed record: `data/ingredients/mapped/Cinnamic_Acid.yaml`.
- Current identifier and grounding: `identifier: CHEBI:27386`,
  `ontology_mapping.ontology_id: CHEBI:27386`,
  `ontology_label: cinnamic acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup confirms active generic `CHEBI:27386` `cinnamic acid`, but
  it also returns active `CHEBI:35697` `trans-cinnamic acid`, the E isomer of
  cinnamic acid.
- PubChem lookup of the record's CAS `140-10-3` resolves to formula `C9H8O2`
  with a standard InChI ending in `/b7-6+`, i.e. the trans-specific double-bond
  isomer. The YAML still stores the non-isomeric generic InChI from
  `CHEBI:27386`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cimicifugoside_H1.yaml data/ingredients/mapped/Cinerubin_A.yaml data/ingredients/mapped/Cinerubin_R.yaml data/ingredients/mapped/Cinnamic_Acid.yaml data/ingredients/mapped/Cinnamycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cinerubin_R.yaml data/ingredients/mapped/Cinnamic_Acid.yaml data/ingredients/mapped/Cinnamycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three CHEBI-scoped records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Cinnamic_Acid` row to `CHEBI:27386`,
  the row-review confirmation for that generic target, and matching
  aggregate/docs rows.
- Hidden/ignored-inclusive search over the same tree found an existing active
  `data/ingredients/mapped/Trans-cinnamic_Acid.yaml` record mapped to
  `CHEBI:35697` with 3/3 CultureMech occurrence rows, so the CAS-supported
  trans-specific identity is already represented elsewhere.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:27386` rows,
  matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The generic SSSOM row, zero occurrence count, aggregate copy, and docs row are
  synchronized.
- The active record is chemically inconsistent because its CAS-RN and
  PubChem-resolved structure are trans-specific while its identifier,
  ontology_id, formula-derived InChI, and exact synonym are generic.

## Recommended Edits

- Merge, redirect, or otherwise retire
  `data/ingredients/mapped/Cinnamic_Acid.yaml` in favor of the existing
  `data/ingredients/mapped/Trans-cinnamic_Acid.yaml`, preserving any
  CultureBotHT provenance that still matters and avoiding a second exact row
  for the same trans-cinnamic acid CAS identity.
- Rerun strict validation, term validation, duplicate-identifier/CAS audits,
  aggregate/roundtrip verification, and `scripts/validate_sssom_invariants.py`.
