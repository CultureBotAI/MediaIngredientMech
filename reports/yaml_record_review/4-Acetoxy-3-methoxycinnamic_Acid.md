# `data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml`

## Verdict

Pass, none. The CAS-backed `CHEBI:86582` identity, synonym label, chemistry,
SSSOM row, and aggregate row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:86582` with
  `ontology_mapping.ontology_id: CHEBI:86582`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:86582` resolves to `O-acetylferulic acid`,
  formula `C12H12O5`, CAS `2596-47-6`, SMILES
  `COc1cc(/C=C/C(=O)O)ccc1OC(C)=O`, and the stored InChI.
- The preferred term `4-Acetoxy-3-methoxycinnamic acid` is an exact synonym of
  the same CHEBI record; `synonyms` also preserves the exact systematic name
  `(2E)-3-[4-(acetyloxy)-3-methoxyphenyl]prop-2-enoic acid`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml data/ingredients/mapped/36-Dihydroxyflavone.yaml data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml data/ingredients/mapped/36-Dihydroxyflavone.yaml data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-Acetoxy-3-methoxycinnamic_Acid` to `CHEBI:86582` row.

## Evidence

- The CultureBotHT CAS lookup, current ChEBI CAS xref, formula, InChI, SMILES,
  and exact synonyms all support the same neutral-acid identity.
- The August regrade correctly records `CAS_RN_LOOKUP` as the method that
  established the mapping even though the preferred term is also an exact ChEBI
  synonym of the canonical `O-acetylferulic acid` label.
- The OAK/OLS row-review manifest confirmed this mapping and asked for no
  curation action.
- The SSSOM `other` field carries an exact synonym and the CAS number, not a
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
