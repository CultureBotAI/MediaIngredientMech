# `data/ingredients/mapped/Bafilomycin_B1.yaml`

## Verdict

Pass. The exact `CHEBI:199416` identity, CultureBotHT CAS value,
ChEBI-backed exact synonym, structure fields, SSSOM row, and aggregate copy all
describe `Bafilomycin B1`.

## Identity

- Reviewed record: `data/ingredients/mapped/Bafilomycin_B1.yaml`.
- Identifier and grounding: `identifier: CHEBI:199416` with
  `ontology_mapping.ontology_id: CHEBI:199416`,
  `ontology_label: Bafilomycin B1`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS exact search in `chebi` resolves `CHEBI:199416` to `Bafilomycin B1` and
  returns the long IUPAC-like synonym stored on the record as an exact synonym.
- PubChem resolves CAS `88899-56-3` to CID 13375090 with synonym
  `Bafilomycin B1`, synonym `CHEBI:199416`, molecular formula `C44H65NO13`,
  and the same standard InChI string stored under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bacto_Tryptic_Soy_Agar_Difco.yaml data/ingredients/mapped/Bacto_Tryptic_Soy_Broth.yaml data/ingredients/mapped/Bacto_Tryptic_Soy_Broth_Difco.yaml data/ingredients/mapped/Bafilomycin.yaml data/ingredients/mapped/Bafilomycin_B1.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Bafilomycin_B1.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports/kg_microbe_node_id_mismatches.tsv`, excluding
  `data/curated/backups`, found the authoritative SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 532 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` row 365 already marked the
  `CHEBI:199416` mapping `CONFIRMED`; the fresh Engine A and OLS checks still
  agree with that verdict.
- The `chemical_properties.cas_rn` value `88899-56-3`, formula `C44H65NO13`,
  and InChI describe the same PubChem compound as the `Bafilomycin B1`/CHEBI
  synonym set.
- The provisional `SELECTIVE_AGENT` role is explicitly marked as a
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with review
  recommended; it is not presented as literature-backed evidence.

## Completeness

- The exact CHEBI identifier, CAS registry number, formula, InChI, SMILES,
  ChEBI exact synonym, SSSOM row, and aggregate copy are populated.
- No source occurrence, component list, or supplied-form split is required for
  this single-compound record with zero recorded medium occurrences.

## Recommended Edits

- None.
