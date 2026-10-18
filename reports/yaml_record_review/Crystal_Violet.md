# `data/ingredients/mapped/Crystal_Violet.yaml`

## Verdict

Needs curation; major. The `CHEBI:41688` crystal violet identity, structure,
4/4 count, and final SSSOM row pass, but `physicochemical_roles.SELECTIVE_AGENT`
is still backed only by a provisional in-session computational assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Crystal_Violet.yaml`.
- Identifier and grounding: `identifier: CHEBI:41688`,
  `ontology_mapping.ontology_id: CHEBI:41688`,
  `ontology_label: crystal violet`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `match_level: EXACT` by equality of the record and ontology identifiers.
- Live OLS lookup by `CHEBI:41688` returns active `CHEBI:41688` labelled
  `crystal violet` with the curated chemical synonym as an exact synonym.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this active record using `CHEBI:41688` as a
  primary identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Crystal_Violet.yaml data/ingredients/mapped/Crystalline_Cellulose.yaml data/ingredients/mapped/Cu_No32_X_3_H2o.yaml data/ingredients/mapped/Cucl.yaml data/ingredients/mapped/Cucl2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Crystal_Violet.yaml data/ingredients/mapped/Crystalline_Cellulose.yaml data/ingredients/mapped/Cucl.yaml data/ingredients/mapped/Cucl2.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-exact records in this batch.
  `Cu_No32_X_3_H2o` was intentionally skipped because its local
  `kgmicrobe.compound` primary identifier and close ChEBI parent are outside
  this CHEBI-focused exact-label validation pass.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive searches over `data`, `mappings`, `docs/data`,
  `scripts`, `tests`, and `reports` found the active `MIM:Crystal_Violet`
  final SSSOM row, generated docs rows, and the OAK/OLS row-review
  confirmation for `CHEBI:41688`.
- `mappings/culturemech_recipe_membership.tsv` contains four `CHEBI:41688`
  rows and a total occurrence sum of 4, matching `occurrence_statistics` `4/4`.
- The final SSSOM `other` tokens are the ChEBI exact synonym on `CHEBI:41688`
  and the structured `CAS:548-62-9` value from `chemical_properties.cas_rn`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` uses
  `reference_type: COMPUTATIONAL_PREDICTION` with `reference_text: Assigned by
  in-session Claude reasoning (no external API)`. No inspected source is
  attached to the role-level claim.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, final SSSOM row,
  aggregate copy, occurrence count, and generated docs rows are populated and
  agree.
- The remaining gap is only role evidence: the curated identity is complete
  enough, but the selective-agent facet needs a database or recipe-level source.

## Recommended Edits

- Major: either replace the provisional `SELECTIVE_AGENT` evidence in
  `data/ingredients/mapped/Crystal_Violet.yaml` with a source-backed
  `DATABASE_ENTRY`, or drop the role if the CultureBotHT/CultureMech rows do
  not actually support using crystal violet as a selective agent.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
