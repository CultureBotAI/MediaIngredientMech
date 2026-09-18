# `data/ingredients/mapped/Colchiceine.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record is grounded to active `CHEBI:183909`
Colchiceine, the CAS RN, formula, InChI, SMILES, exact synonym, zero occurrence
count, final SSSOM row, and aggregate copy agree, and there are no unsupported
roles or component claims.

## Identity

- Reviewed record: `data/ingredients/mapped/Colchiceine.yaml`.
- Identifier and grounding: `identifier: CHEBI:183909`,
  `ontology_mapping.ontology_id: CHEBI:183909`, `ontology_label: Colchiceine`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:183909` returns active `CHEBI:183909` labelled
  `Colchiceine` with exact synonym
  `N-[(7S)-10-hydroxy-1,2,3-trimethoxy-9-oxo-6,7-dihydro-5H-benzo[a]heptalen-7-yl]acetamide`.
- The record stores CAS RN `477-27-0`, formula `C21H23NO6`, and populated InChI
  and SMILES values for a small-molecule ChEBI identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cocl2_X_6_H2o.yaml data/ingredients/mapped/Coenzyme_A.yaml data/ingredients/mapped/Colchiceine.yaml data/ingredients/mapped/Colistin_Sulfate.yaml data/ingredients/mapped/Colistin_Sulfate_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cocl2_X_6_H2o.yaml data/ingredients/mapped/Coenzyme_A.yaml data/ingredients/mapped/Colchiceine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-identified records in this batch.
  `Colistin_Sulfate` and `Colistin_Sulfate_Salt` were intentionally skipped
  because they are grounded to NCIT, while this LinkML term-validation pass was
  limited to CHEBI records.
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
  `reports` found exactly the expected active `MIM:Colchiceine` final SSSOM
  row, the OAK/OLS row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive search under `data/ingredients` found no second
  active record using `CHEBI:183909`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:183909` rows,
  matching the explicit 0/0 `occurrence_statistics`.
- The final SSSOM `other` column contains the exact long ChEBI synonym and
  `CAS:477-27-0`, with no role-like, concentration-like, or salt-qualified
  residue.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym, SSSOM
  row, aggregate copy, docs row, and zero occurrence count are populated and
  agree.
- No recommended edits.

## Recommended Edits

- None.
