# `data/ingredients/mapped/Chrysanthemic_Acid_Ethyl_Ester.yaml`

## Verdict

Pass. The CAS-backed record has been correctly regraded to exact identity with
active `CHEBI:228794` `Ethyl chrysanthemumate`; its CAS, formula, InChI,
SMILES, exact synonym, SSSOM rows, zero occurrence count, and aggregate copy
agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Chrysanthemic_Acid_Ethyl_Ester.yaml`.
- Identifier and grounding: `identifier: cas:97-41-6`,
  `ontology_mapping.ontology_id: CHEBI:228794`,
  `ontology_label: Ethyl chrysanthemumate`, `ontology_source: CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS lookup for `Ethyl chrysanthemumate` returns one active
  `CHEBI:228794` term with the same label and with
  `ethyl 2,2-dimethyl-3-(2-methylprop-1-enyl)cyclopropane-1-carboxylate` as an
  exact synonym.
- PubChem lookup of CAS `97-41-6` resolves to CID `7334` with formula
  `C12H20O2` and the same standard InChI and SMILES stored in the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chrysanthemic_Acid_Ethyl_Ester.yaml data/ingredients/mapped/Chrysarobin.yaml data/ingredients/mapped/Chrysin.yaml data/ingredients/mapped/Chrysophanol.yaml data/ingredients/mapped/Chu_Stock_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chrysanthemic_Acid_Ethyl_Ester.yaml data/ingredients/mapped/Chrysarobin.yaml data/ingredients/mapped/Chrysin.yaml data/ingredients/mapped/Chrysophanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all four CHEBI-scoped records in this batch. `Chu_Stock_Solution`
  was intentionally skipped because its `kgmicrobe.ingredient` placeholder
  CURIE is a local registry ID outside Engine A's OBO prefix scope.
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
  `reports` found the active exact `MIM:Chrysanthemic_Acid_Ethyl_Ester` row to
  `CHEBI:228794`, the exact CAS registry row, the expected unknown-term rows
  for the CAS/local registry surfaces, the synonym-enrichment no-op row, and
  matching aggregate/docs rows.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` plus active per-record YAML and
  review reports found no membership rows for either `cas:97-41-6` or
  `CHEBI:228794`, matching the explicit 0/0 media-recipe occurrence
  statistics.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI target, exact CAS registry row, CAS, formula, InChI, SMILES,
  exact synonym, zero occurrence count, SSSOM rows, aggregate copy, and docs row
  are populated and agree.

## Recommended Edits

- None for this record.
