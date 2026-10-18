# `data/ingredients/mapped/4-Anisaldehyde.yaml`

## Verdict

Pass, none. The CAS-backed `CHEBI:28235` identity, synonym label, chemistry,
SSSOM row, and aggregate row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-Anisaldehyde.yaml`.
- Identifier and grounding: `identifier: CHEBI:28235` with
  `ontology_mapping.ontology_id: CHEBI:28235`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:28235` resolves to `p-methoxybenzaldehyde`,
  formula `C8H8O2`, CAS `123-11-5`, SMILES `[H]C(=O)c1ccc(OC)cc1`, and the
  stored InChI.
- The preferred term `4-Anisaldehyde` and stored synonym `4-methoxybenzaldehyde`
  are exact synonyms of the same ChEBI record.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Amino-5-hydroxymethyl-2-methylpyrimidine.yaml data/ingredients/mapped/4-Anisaldehyde.yaml data/ingredients/mapped/4-Cresol.yaml data/ingredients/mapped/4-Deoxypyridoxine.yaml data/ingredients/mapped/4-Hydroxyacetophenone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Amino-5-hydroxymethyl-2-methylpyrimidine.yaml data/ingredients/mapped/4-Anisaldehyde.yaml data/ingredients/mapped/4-Cresol.yaml data/ingredients/mapped/4-Deoxypyridoxine.yaml data/ingredients/mapped/4-Hydroxyacetophenone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-Anisaldehyde` to `CHEBI:28235` row.

## Evidence

- The CultureBotHT CAS lookup, current ChEBI CAS xref, formula, InChI, SMILES,
  and exact synonym all support the same neutral aldehyde identity.
- The August regrade correctly records `CAS_RN_LOOKUP` as the method that
  established the mapping even though the preferred term is also an exact ChEBI
  synonym of the canonical `p-methoxybenzaldehyde` label.
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
