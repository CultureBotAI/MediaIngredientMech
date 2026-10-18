# `data/ingredients/mapped/Aluminium_Sulfate.yaml`

## Verdict

Pass. The exact `CHEBI:74772` aluminium sulfate identity, CultureBotHT CAS
provenance, row-review confirmation, SSSOM row, occurrence count, and aggregate
copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Aluminium_Sulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:74772` with
  `ontology_mapping.ontology_id: CHEBI:74772`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:74772` to
  `aluminium sulfate`.
- `chemical_properties.cas_rn: 10043-01-3` matches the CultureBotHT
  `compounds_to_cas.csv` creation history for this record.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml data/ingredients/mapped/Alpha-toxicarol_Dl.yaml data/ingredients/mapped/Alphaalpha-Trehalose.yaml data/ingredients/mapped/Althiomycin.yaml data/ingredients/mapped/Aluminium_Sulfate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Aluminium_Sulfate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:30915 CHEBI:16551 CHEBI:157683 CHEBI:74772 CHEBI:9643`:
  returned canonical `aluminium sulfate` and related `aluminium sulfates` for
  `CHEBI:74772`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30915 CHEBI:16551 CHEBI:157683 CHEBI:74772 CHEBI:9643`:
  returned the canonical label and definition for `CHEBI:74772`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with the same 104 non-blocking
  plausibility warnings seen at corpus scope.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The creation history records import from CultureBotHT `compounds_to_cas.csv`
  with CAS `10043-01-3` and one CultureBotHT medium.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Aluminium_Sulfate` to `CHEBI:74772` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records that no row
  curation action was required.
- `mappings/ingredient_mappings.sssom.tsv` row 385 maps
  `MIM:Aluminium_Sulfate` to `CHEBI:74772` with `skos:exactMatch`, the
  CultureBotHT provenance, and CAS `10043-01-3`.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, OAK/OLS confirmation rows, generated
  reports, and the distinct aluminium sulfate hydrate records; none conflict
  with this anhydrous aluminium sulfate row.

## Completeness

- CAS, occurrence statistics, mapping evidence, curation history, and
  `ingredient_type` are populated.
- ChEBI does not expose formula or structure metadata on `CHEBI:74772`; no
  incompatible structure has been backfilled from an adjacent hydrate or salt.
- No synonym, role, component, environmental context, discussion, or dataset
  entry is needed.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:74772` row, which
  is consistent with this one-occurrence record being sourced from CultureBotHT
  rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
