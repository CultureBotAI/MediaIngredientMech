# `data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml`

## Verdict

Pass, none. The `CHEBI:44718` identity, CAS, chemistry, SSSOM row, and
aggregate row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml`.
- Identifier and grounding: `identifier: CHEBI:44718` with
  `ontology_mapping.ontology_id: CHEBI:44718`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:44718` is active, resolves to
  `4-benzoyl-L-phenylalanine`, has formula `C16H15NO3`, CAS `104504-45-2`,
  SMILES `N[C@@H](Cc1ccc(C(=O)c2ccccc2)cc1)C(=O)O`, and the stored InChI.
- PubChem CAS lookup for `104504-45-2` resolves to CID `7020128` with formula
  `C16H15NO3` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-acetoxyphenol.yaml data/ingredients/mapped/4-aminobenzoate.yaml data/ingredients/mapped/4-aminobutyrate.yaml data/ingredients/mapped/4-azido-L-phenylalanine.yaml data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-acetoxyphenol.yaml data/ingredients/mapped/4-aminobenzoate.yaml data/ingredients/mapped/4-aminobutyrate.yaml data/ingredients/mapped/4-azido-L-phenylalanine.yaml data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-benzoyl-L-phenylalanine` to `CHEBI:44718` row.

## Evidence

- The CultureBotHT import, current ChEBI CAS xref, PubChem CAS lookup, formula,
  InChI, and SMILES all support the exact L-stereochemistry and benzoyl
  substitution.
- The OAK/OLS row-review manifest confirmed this mapping and asked for no
  curation action.
- The SSSOM `other` field carries only `CAS:104504-45-2`; no rejected or
  broader synonym is exported for this record.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, the name-list role inference exclusion, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, and `ingredient_type` are populated.
- This CultureBotHT import has no recipe-count occurrence; no role, component,
  environment, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
