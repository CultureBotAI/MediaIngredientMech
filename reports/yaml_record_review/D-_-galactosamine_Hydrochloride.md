# `data/ingredients/mapped/D-_-galactosamine_Hydrochloride.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The exact active
`CHEBI:181432` hydrochloride identity, structure fields, 0/0 occurrence count,
and final SSSOM synonym payload pass, but `CARBON_SOURCE` is asserted only from
provisional CHEBI-ancestry evidence and needs direct media-use support or
removal.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-_-galactosamine_Hydrochloride.yaml`.
- Current identifier and grounding: `identifier: CHEBI:181432`,
  `ontology_mapping.ontology_id: CHEBI:181432`,
  `ontology_label: D-(+)-Galactosamine hydrochloride`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:181432` returns active `CHEBI:181432` labelled
  `D-(+)-Galactosamine hydrochloride` with formula `C6H13NO5.HCl` and
  matching InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:`/`ontology_id:` search under
  `data/ingredients` found only this record using `CHEBI:181432`.

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
  `CHEBI:181432`.
- The hidden/ignored-inclusive membership search found no `CHEBI:181432` rows
  in `mappings/culturemech_recipe_membership.tsv`, matching the record's 0/0
  `occurrence_statistics`.
- The final SSSOM row publishes
  `MIM:D-_-galactosamine_Hydrochloride skos:exactMatch CHEBI:181432`.
  Its `other` tokens are the live exact IUPAC synonym and `CAS:1772-03-8`,
  both safe for this hydrochloride subject.
- The `CARBON_SOURCE` facet is supported only by
  `COMPUTATIONAL_PREDICTION` from CHEBI ancestry and its own `curator_note`
  calls it provisional.

## Completeness

- No parent mappings, supplied-form assertions, components, or source
  occurrences are asserted, so there are no unsupported secondary claims beyond
  the provisional nutritional role.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry.

## Recommended Edits

- In `data/ingredients/mapped/D-_-galactosamine_Hydrochloride.yaml`, either
  replace the computational `CARBON_SOURCE` evidence with direct CultureBotHT
  or source-backed media-role evidence for this ingredient, or remove the role
  facet; then rerun strict validation and the final SSSOM build.
