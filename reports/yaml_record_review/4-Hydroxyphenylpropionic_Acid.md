# `data/ingredients/mapped/4-Hydroxyphenylpropionic_Acid.yaml`

## Verdict

Pass, none. The CAS-backed `CHEBI:32980` identity, exact synonym, chemistry,
SSSOM row, and aggregate row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-Hydroxyphenylpropionic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:32980` with
  `ontology_mapping.ontology_id: CHEBI:32980`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:32980` is active, resolves to
  `phloretic acid`, has formula `C9H10O3`, CAS `501-97-3`, SMILES
  `O=C(O)CCc1ccc(O)cc1`, the stored InChI, and exact synonym
  `3-(4-hydroxyphenyl)propanoic acid`.
- PubChem CAS lookup for `501-97-3` resolves to CID `10394` with formula
  `C9H10O3` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml data/ingredients/mapped/4-Hydroxymandelic_Acid_Monohydrate.yaml data/ingredients/mapped/4-Hydroxynonanoic_Acid.yaml data/ingredients/mapped/4-Hydroxynonenal.yaml data/ingredients/mapped/4-Hydroxyphenylpropionic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml data/ingredients/mapped/4-Hydroxymandelic_Acid_Monohydrate.yaml data/ingredients/mapped/4-Hydroxynonanoic_Acid.yaml data/ingredients/mapped/4-Hydroxynonenal.yaml data/ingredients/mapped/4-Hydroxyphenylpropionic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-Hydroxyphenylpropionic_Acid` to `CHEBI:32980` row.

## Evidence

- The CultureBotHT CAS lookup, current ChEBI CAS xref, PubChem CAS lookup,
  formula, InChI, SMILES, and exact synonym all support the same neutral
  hydroxyphenylpropionic acid identity.
- The August `CAS_RN_LOOKUP` grade correctly records that the CAS xref, not a
  primary-label match, established the mapping to the canonical `phloretic acid`
  label.
- The OAK/OLS row-review manifest confirmed this mapping and asked for no
  curation action.
- The SSSOM `other` field carries an exact synonym and the CAS number, not a
  rejected or broader label.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, exact synonym, and `ingredient_type` are
  populated.
- This CultureBotHT CAS import has no recipe-count occurrence; no role,
  component, environment, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
