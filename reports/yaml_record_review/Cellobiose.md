# `data/ingredients/mapped/Cellobiose.yaml`

## Verdict

Needs curation; major issue. The exact ChEBI cellobiose identity, formula,
InChI, SMILES, carbon-source role, 273 CultureMech memberships, SSSOM row, and
aggregate copy pass, but the `ENERGY_SOURCE` role is still only a provisional
computational prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Cellobiose.yaml`.
- Identifier and grounding: `identifier: CHEBI:17057`,
  `ontology_mapping.ontology_id: CHEBI:17057`, `ontology_label: cellobiose`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:17057` returns one active ChEBI term labelled
  `cellobiose` with formula `C12H22O11`, molecular mass `342.297`, and the same
  InChI and SMILES stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cefuroxime.yaml data/ingredients/mapped/Cefuroxime_Sodium.yaml data/ingredients/mapped/Celesticetin.yaml data/ingredients/mapped/Cell_Lysate.yaml data/ingredients/mapped/Cellobiose.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cefuroxime.yaml data/ingredients/mapped/Cefuroxime_Sodium.yaml data/ingredients/mapped/Celesticetin.yaml data/ingredients/mapped/Cell_Lysate.yaml data/ingredients/mapped/Cellobiose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 external-ontology records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active exact `MIM:Cellobiose` SSSOM row, the
  `SYNONYM_ENRICH` and expected kg-microbe registry row-review dispositions,
  the synonym-enrichment `ALREADY_REPRESENTED` row, and matching aggregate/docs
  rows for `CHEBI:17057`.
- `mappings/culturemech_recipe_membership.tsv` contains 273 `CHEBI:17057`
  memberships with 273 total occurrences, matching `occurrence_statistics`.
- The final SSSOM row carries only the curated kg-microbe exact synonyms and
  `CAS:528-50-7` in `other`; the CultureMech role/property `RAW_TEXT` entries
  and the `(alternative)` placeholder in YAML are filtered as non-resolving
  synonym text.
- `CARBON_SOURCE` is backed by imported CultureMech database-entry evidence
  with the original role text preserved in its excerpt.
- `ENERGY_SOURCE` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_energy_source` and is explicitly marked "Provisional ENERGY_SOURCE
  added alongside CARBON_SOURCE; review recommended."

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, SSSOM row, aggregate
  copy, docs row, CultureMech occurrence count, and carbon-source role are
  populated and agree.
- The YAML still preserves imported role/property strings in `synonyms`, but
  the active synonym policy prevents those strings from being exposed in search
  or in the SSSOM `other` field.

## Recommended Edits

- Major: either replace `nutritional_roles.ENERGY_SOURCE` with inspected
  evidence for cellobiose as an energy source in media, or remove the role,
  then rerun strict validation, SSSOM QC, aggregate roundtrip, and
  `git diff --check`.
