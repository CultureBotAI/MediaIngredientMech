# `data/ingredients/mapped/Congo_Red.yaml`

## Verdict

Pass. The CultureMech record is grounded to active `CHEBI:34653` Congo Red, the
CAS RN, formula, InChI, SMILES, exact synonyms, 3/3 CultureMech occurrence
count, pH-indicator role evidence, final SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Congo_Red.yaml`.
- Identifier and grounding: `identifier: CHEBI:34653`,
  `ontology_mapping.ontology_id: CHEBI:34653`, `ontology_label: Congo Red`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:34653` returns active `CHEBI:34653` labelled
  `Congo Red` and includes the record's exact synonyms: `Direct red 28`,
  `Kongorot`, `Sodium diphenyldiazo-bis-alpha-naphthylaminesulfonate`, and the
  two disodium chemical names.
- The record stores CAS RN `573-58-0`, formula `C32H22N6O6S2.2Na`, and
  populated InChI and SMILES values for the exact ChEBI identity.

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
  `reports` found the active `MIM:Congo_Red` final SSSOM row, the OAK/OLS
  row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact identity search under `data/ingredients` found
  no second active record using `CHEBI:34653`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 3 rows for `CHEBI:34653`
  whose occurrence weights sum to 3, matching the explicit 3/3
  `occurrence_statistics`.
- The final SSSOM `other` column contains exact Congo Red synonyms and
  `CAS:573-58-0`; the raw `Role: pH indicator` text is filtered and does not
  reach final SSSOM.
- `PH_INDICATOR` is backed by the original CultureMech `Role: pH indicator`
  database text.

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms,
  pH-indicator role evidence, SSSOM row, aggregate copy, docs row, and
  occurrence count are populated and agree.
- No recommended edits.

## Recommended Edits

- None.
