# `data/ingredients/mapped/Heparin_Sodium_Salt_From_Porcine_Intestinal_Mucosa.yaml`

## Verdict

Pass. The local source-qualified heparin sodium identity, active broader
`CHEBI:230519` parent, CAS RN, narrow-match grade, Rule B1 registry rows, and
final SSSOM rows are internally consistent.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Heparin_Sodium_Salt_From_Porcine_Intestinal_Mucosa.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:heparin_sodium_salt_from_porcine_intestinal_mucosa`
  with `ontology_mapping.ontology_id: CHEBI:230519`, label `heparin sodium`,
  source `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `9041-08-1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Helenine.yaml data/ingredients/mapped/Hemin_solution_see_below.yaml data/ingredients/mapped/Hemoglobin.yaml data/ingredients/mapped/Henicosane.yaml data/ingredients/mapped/Heparin_Sodium_Salt_From_Porcine_Intestinal_Mucosa.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:230519`.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1418`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1418`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:230519` as active `heparin sodium`, with exact synonyms
  including `heparin sodium salt` and `sodium heparin`.
- A fresh OLS4 text search for the full preferred term did not return an exact
  source-qualified heparin sodium candidate; its sole hit was NCIT
  `Tinzaparin Sodium`, a different low-molecular-weight heparin salt obtained
  by heparin depolymerization.
- The record correctly preserves `Heparin sodium salt from porcine intestinal
  mucosa` as a local identity that is narrower than generic ChEBI
  `heparin sodium`.
- The final SSSOM publishes the parent as `skos:narrowMatch` and publishes
  exact registry rows to both the local `kgmicrobe.ingredient` identifier and
  the KG-Microbe compound projection. Both exact rows keep the local
  preferred term and `CAS:9041-08-1` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate record, docs projections, and row-review decisions that keep this
  as a local source-qualified record.

## Completeness

- The active parent, local identifier, CAS RN, final registry rows, and
  synchronized aggregate entry are present and consistent.
- No unsupported roles or exact synonyms are asserted.

## Recommended Edits

- None.
