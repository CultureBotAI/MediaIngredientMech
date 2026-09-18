# `data/ingredients/mapped/Ciprofloxacin.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder ciprofloxacin import is exactly
grounded to active `CHEBI:100241`; its formula, InChI, SMILES, 218-count
MicrobeDecoder source occurrence, zero CultureMech membership, SSSOM row, and
aggregate copy agree. The active final SSSOM row still publishes
`ciprofloxacin (if needed)` as a resolving `other` synonym even though the
parenthetical is recipe-use noise.

## Identity

- Reviewed record: `data/ingredients/mapped/Ciprofloxacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:100241`,
  `ontology_mapping.ontology_id: CHEBI:100241`,
  `ontology_label: ciprofloxacin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS lookup for `ciprofloxacin` returns active `CHEBI:100241`
  labelled `ciprofloxacin`. It also surfaces salt and metabolite sibling terms,
  but the exact parent drug is the top-level match and agrees with this record.
- PubChem lookup by `ciprofloxacin` returns CID 2764, formula `C17H18FN3O3`,
  and the same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cinoxacin.yaml data/ingredients/mapped/Ciprofloxacin.yaml data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml data/ingredients/mapped/Cis-aconitate.yaml data/ingredients/mapped/Cisplatin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cinoxacin.yaml data/ingredients/mapped/Ciprofloxacin.yaml data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml data/ingredients/mapped/Cis-aconitate.yaml data/ingredients/mapped/Cisplatin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-scoped records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Ciprofloxacin` SSSOM row, the
  MicrobeDecoder import-review approval, the residual CultureMech alias
  backfill for `ciprofloxacin (if needed)`, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:100241` only in this active record.
- Hidden/ignored-inclusive search of `data/custom/microbedecoder` found
  `kgmicrobe.trait:ciprofloxacin` in `BacDive_Antibiotic_resistance` and
  `BacDive_Antibiotic_sensitivity` with count 218, matching the explicit
  `source_occurrences` entry.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:100241`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- `mappings/ingredient_mappings.sssom.tsv` emits `ciprofloxacin (if needed)` in
  the final `other` column. That text still resolves to the correct ingredient,
  but it is not a genuine synonym for ciprofloxacin; it is a CultureMech recipe
  surface with a parenthetical use qualifier.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, source occurrence, SSSOM
  row, aggregate copy, and docs row are populated and agree.
- The only active gap is the noisy raw synonym that still reaches final SSSOM
  and search outputs.

## Recommended Edits

- Minor: in `data/ingredients/mapped/Ciprofloxacin.yaml`, either demote
  `ciprofloxacin (if needed)` to a non-resolving provenance entry or generalize
  `src/mediaingredientmech/synonym_policy.py` so CultureMech `if needed`
  parentheticals are omitted from SSSOM `other` and label-search exports.
