# `data/ingredients/mapped/Conessine.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived record is grounded to active `CHEBI:27965`
conessine, the CAS RN, formula, InChI, SMILES, exact synonym, zero occurrence
count, final SSSOM row, and aggregate copy agree, and there are no unsupported
roles or component claims.

## Identity

- Reviewed record: `data/ingredients/mapped/Conessine.yaml`.
- Identifier and grounding: `identifier: CHEBI:27965`,
  `ontology_mapping.ontology_id: CHEBI:27965`, `ontology_label: conessine`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:27965` returns active `CHEBI:27965` labelled
  `conessine` with exact synonym `N,N-dimethylcon-5-enin-3beta-amine`.
- The record stores CAS RN `546-06-5`, formula `C24H40N2`, and populated InChI
  and SMILES values for the exact ChEBI identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Collagen.yaml data/ingredients/mapped/Collinomycin.yaml data/ingredients/mapped/Columbia_Agar_Base.yaml data/ingredients/mapped/Conessine.yaml data/ingredients/mapped/Congo_Red.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Collagen.yaml data/ingredients/mapped/Conessine.yaml data/ingredients/mapped/Congo_Red.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-identified records in this batch.
  `Collinomycin` and `Columbia_Agar_Base` were intentionally skipped because
  their local `kgmicrobe.compound` and MICRO identifiers are outside this
  CHEBI-focused LinkML term-validation pass.
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
  `reports` found the active `MIM:Conessine` final SSSOM row, the OAK/OLS
  row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `CHEBI:27965`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:27965` rows,
  matching the explicit 0/0 `occurrence_statistics`.
- The final SSSOM `other` column contains the exact ChEBI synonym and
  `CAS:546-06-5`, with no role-like, concentration-like, or salt-qualified
  residue.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym, SSSOM
  row, aggregate copy, docs row, and zero occurrence count are populated and
  agree.
- No recommended edits.

## Recommended Edits

- None.
