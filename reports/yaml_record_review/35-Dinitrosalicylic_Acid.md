# `data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml`

## Verdict

Pass, none. The exact `CHEBI:53648` identity, CAS-backed CultureBotHT evidence,
ChEBI chemistry, exact synonym, SSSOM row, and aggregate row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:53648` with
  `ontology_mapping.ontology_id: CHEBI:53648`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:53648` resolves to
  `3,5-dinitrosalicylic acid`, formula `C7H4N2O7`, CAS `609-99-4`, SMILES
  `O=C(O)c1cc([N+](=O)[O-])cc([N+](=O)[O-])c1O`, and the stored InChI.
- The exact synonym `2-hydroxy-3,5-dinitrobenzoic acid` is present and
  publishes through SSSOM `other`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml data/ingredients/mapped/36-Dihydroxyflavone.yaml data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml data/ingredients/mapped/36-Dihydroxyflavone.yaml data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:35-Dinitrosalicylic_Acid` to `CHEBI:53648` row.

## Evidence

- The CultureBotHT CAS lookup, current ChEBI CAS xref, formula, InChI, and
  SMILES all support the exact neutral-acid identity.
- The OAK/OLS row-review manifest confirmed this mapping and asked for no
  curation action.
- The SSSOM `other` field carries the exact synonym plus CAS number, not a
  rejected or broader label.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation rows, generated
  docs, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, exact synonym, and `ingredient_type` are populated.
- This was a CultureBotHT CAS import with no recipe-count occurrence, so
  `total_occurrences: 0` and `media_count: 0` are expected.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
