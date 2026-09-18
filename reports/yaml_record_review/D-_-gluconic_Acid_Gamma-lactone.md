# `data/ingredients/mapped/D-_-gluconic_Acid_Gamma-lactone.yaml`

## Verdict

Needs curation, with major role-evidence issues. The CAS-resolved active
`CHEBI:16217` identity, structure fields, 0/0 occurrence count, and final SSSOM
synonym payload pass, but `CARBON_SOURCE` and `ENERGY_SOURCE` are asserted only
from provisional computational evidence.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-_-gluconic_Acid_Gamma-lactone.yaml`.
- Current identifier and grounding: `identifier: CHEBI:16217`,
  `ontology_mapping.ontology_id: CHEBI:16217`,
  `ontology_label: D-glucono-1,5-lactone`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:16217` returns active `CHEBI:16217` labelled
  `D-glucono-1,5-lactone`, CAS xref `90-80-2`, formula `C6H10O6`, and matching
  InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:`/`ontology_id:` search under
  `data/ingredients` found only this record using `CHEBI:16217`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Sucrose.yaml data/ingredients/mapped/D-_-galactosamine_Hydrochloride.yaml data/ingredients/mapped/D-_-gluconic_Acid_Gamma-lactone.yaml data/ingredients/mapped/D-_-lyxose.yaml data/ingredients/mapped/D-_-melezitose_Hydrate.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-_-galactosamine_Hydrochloride.yaml data/ingredients/mapped/D-_-gluconic_Acid_Gamma-lactone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the two live CHEBI-primary exact records in this batch.
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

- The record's formula, InChI, SMILES, and CAS RN agree with active
  `CHEBI:16217`; the explicit 2026-08-24 regrade preserves the
  CAS-to-CHEBI lookup method behind the mapping.
- The hidden/ignored-inclusive membership search found no `CHEBI:16217` rows in
  `mappings/culturemech_recipe_membership.tsv`, matching the record's 0/0
  `occurrence_statistics`.
- The final SSSOM row publishes
  `MIM:D-_-gluconic_Acid_Gamma-lactone skos:exactMatch CHEBI:16217`. Its
  `other` column contains two exact `CHEBI:16217` synonyms and `CAS:90-80-2`.
- `CARBON_SOURCE` is supported only by `COMPUTATIONAL_PREDICTION` from a
  curated name-pattern rule; `ENERGY_SOURCE` is supported only by a provisional
  canonical-substrate `COMPUTATIONAL_PREDICTION`.

## Completeness

- No parent mappings, supplied-form assertions, components, or source
  occurrences are asserted, so there are no unsupported secondary claims beyond
  the two provisional nutritional roles.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry.

## Recommended Edits

- In `data/ingredients/mapped/D-_-gluconic_Acid_Gamma-lactone.yaml`, either
  replace the computational `CARBON_SOURCE` and `ENERGY_SOURCE` evidence with
  direct CultureBotHT or source-backed media-role evidence for this ingredient,
  or remove the role facets; then rerun strict validation and the final SSSOM
  build.
