# `data/ingredients/mapped/Chondroitin_Sulfate_A_Sodium_Salt_From_Bovine_Trachea.yaml`

## Verdict

Needs curation, major. The CAS fallback identity and registry rows are
internally synchronized, and no exact CHEBI term exists for the full
bovine-trachea supplied form, but the active CHEBI parent is now too broad:
CHEBI exposes more specific sodium and sulfate-A chondroitin terms than the
current generic `CHEBI:37397` parent.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Chondroitin_Sulfate_A_Sodium_Salt_From_Bovine_Trachea.yaml`.
- Identifier and grounding: `identifier: cas:39455-18-0`,
  `ontology_mapping.ontology_id: CHEBI:37397`,
  `ontology_label: chondroitin sulfate`, `ontology_source: CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS search for
  `chondroitin sulfate A sodium salt from bovine trachea` found 0 CHEBI terms,
  so the record still needs a local registry identity.
- Live exact OLS search for `chondroitin sulfate sodium` returns active
  `CHEBI:753835`; a broader `chondroitin sulfate` search also returns active
  `CHEBI:18250` `chondroitin 4'-sulfate`, whose synonyms include
  `Chondroitin sulfate A`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Choline_Chloride.yaml data/ingredients/mapped/Cholinium_Dihydrogen_Phosphate.yaml data/ingredients/mapped/Cholinium_Lysinate.yaml data/ingredients/mapped/Chondroitin_Sulfate_A_Sodium_Salt_From_Bovine_Trachea.yaml data/ingredients/mapped/Chromium_Iii_Chloride_Hexahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Choline_Chloride.yaml data/ingredients/mapped/Chondroitin_Sulfate_A_Sodium_Salt_From_Bovine_Trachea.yaml data/ingredients/mapped/Chromium_Iii_Chloride_Hexahydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three CHEBI-scoped records in this narrowed run.
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
  `reports` found the active narrow parent SSSOM row to `CHEBI:37397`, the
  exact CAS and Rule B1 registry rows, the synonym-enrichment no-op row, the
  expected CAS/local unknown-term triage rows, and matching aggregate/docs
  rows.
- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found no existing `CHEBI:753835`, `CHEBI:81720`, or
  `chondroitin sulfate sodium` representation, so the narrower sodium parent
  is not already modeled elsewhere in this repository.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `cas:39455-18-0` or
  `CHEBI:37397` rows, matching the explicit 0/0 media-recipe occurrence
  statistics.
- PubChem lookup of CAS `39455-18-0` found no CID; the record accordingly
  carries only a CAS-RN under `chemical_properties`.
- The record carries no role, component, or environment claims.

## Completeness

- The supplied-form identity, fallback CAS row, local kg-microbe registry row,
  zero occurrence count, SSSOM rows, aggregate copy, and docs rows are
  synchronized.
- The CHEBI parent needs renewed curator review because the current parent
  loses both sodium-form specificity and sulfate-A specificity.

## Recommended Edits

- In
  `data/ingredients/mapped/Chondroitin_Sulfate_A_Sodium_Salt_From_Bovine_Trachea.yaml`,
  evaluate active `CHEBI:753835` and `CHEBI:18250` as narrower parent choices;
  if one is the least lossy available parent, update `ontology_mapping` and
  the parent SSSOM row while keeping the exact CAS/local registry identity
  rows.
- Rerun strict validation, term validation, aggregate/roundtrip verification,
  and `scripts/validate_sssom_invariants.py`.
