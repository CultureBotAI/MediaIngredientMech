# `data/ingredients/mapped/Chlororaphin.yaml`

## Verdict

Pass. `Chlororaphin` is intentionally retained as the local
`kgmicrobe.compound:chlororaphin` placeholder while no exact CHEBI, NCIT, or
MeSH compound identity is available, and the placeholder record, manual
candidate rejection, SSSOM row, zero occurrence count, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Chlororaphin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:chlororaphin`,
  `ontology_mapping.ontology_id: kgmicrobe.compound:chlororaphin`,
  `ontology_label: Chlororaphin`, `ontology_source: kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Current exact OLS search for `Chlororaphin` across CHEBI, NCIT, and MeSH
  returns only `NCIT:C86699` `Pseudomonas chlororaphis` via its description;
  `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`
  already rejected that organism/taxon-like candidate as not the compound
  `Chlororaphin`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chloridazon.yaml data/ingredients/mapped/Chlorogenic_Acid.yaml data/ingredients/mapped/Chlororaphin.yaml data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml data/ingredients/mapped/Chlortetracycline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chloridazon.yaml data/ingredients/mapped/Chlorogenic_Acid.yaml data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml data/ingredients/mapped/Chlortetracycline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 4 CHEBI-grounded records in this batch. `Chlororaphin` was
  intentionally skipped because its `kgmicrobe.compound` placeholder CURIE is a
  local registry ID outside Engine A's OBO prefix scope.
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
  `reports` found the active local `MIM:Chlororaphin` SSSOM row, the
  `expected_registry_identifier` row-review disposition, the
  `NO_EXACT_CANDIDATE` placeholder OLS review, the manual rejection of
  `NCIT:C86699`, and matching aggregate and docs rows for
  `kgmicrobe.compound:chlororaphin`.
- Hidden/ignored-inclusive search of `data/custom/microbedecoder` found a
  lowercase `chlororaphin` raw MicrobeDecoder label in
  `BacDive_Metabolite_production`, but the active record is older provenance
  from `kg-microbe metatraits unmapped_compounds.tsv` and makes no
  MicrobeDecoder `source_occurrences` claim.
- `reports/yaml_record_review_batch/validation_report.md` still says
  `kgmicrobe.compound:chlororaphin` is invalid and does not exist. That is the
  batch validator's known local-prefix limitation; the active row review keeps
  this local registry identifier pending promotion to an exact external term.
- Hidden/ignored-inclusive search of `mappings/culturemech_recipe_membership.tsv`
  plus `data` found no CultureMech membership rows for
  `kgmicrobe.compound:chlororaphin`, matching the explicit 0/0
  `occurrence_statistics`.
- The record carries no synonym, role, chemical property, component, or
  environment claims.

## Completeness

- The local kg-microbe placeholder identifier, manual no-promotion decision,
  local SSSOM row, aggregate copy, docs row, and zero occurrence count are
  populated and agree.
- No local alternate label, rejected label, or additional lookup key is
  currently required for this local identity.

## Recommended Edits

- None for this record.
