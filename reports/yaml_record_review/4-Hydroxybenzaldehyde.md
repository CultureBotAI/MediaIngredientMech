# `data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml`

## Verdict

Pass with minor issues, minor. The active `CHEBI:17597` identity, CAS,
formula, InChI, SMILES, SSSOM row, and aggregate row pass; only stale advisory
research rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml`.
- Identifier and grounding: `identifier: CHEBI:17597` with
  `ontology_mapping.ontology_id: CHEBI:17597`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:17597` is active, resolves to
  `4-hydroxybenzaldehyde`, has formula `C7H6O2`, CAS `123-08-0`, SMILES
  `[H]C(=O)c1ccc(O)cc1`, and the stored InChI.
- PubChem CAS lookup for `123-08-0` resolves to CID `126` with formula
  `C7H6O2` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml data/ingredients/mapped/4-Hydroxymandelic_Acid_Monohydrate.yaml data/ingredients/mapped/4-Hydroxynonanoic_Acid.yaml data/ingredients/mapped/4-Hydroxynonenal.yaml data/ingredients/mapped/4-Hydroxyphenylpropionic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml data/ingredients/mapped/4-Hydroxymandelic_Acid_Monohydrate.yaml data/ingredients/mapped/4-Hydroxynonanoic_Acid.yaml data/ingredients/mapped/4-Hydroxynonenal.yaml data/ingredients/mapped/4-Hydroxyphenylpropionic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-Hydroxybenzaldehyde` to `CHEBI:17597` row.

## Evidence

- The CultureBotHT CAS import, current ChEBI CAS xref, PubChem CAS lookup,
  formula, InChI, and SMILES all support the same neutral aldehyde identity.
- The OAK/OLS row-review manifest confirmed this mapping and asked for no
  curation action.
- The SSSOM `other` field carries only `CAS:123-08-0`; no rejected or broader
  synonym is exported for this record.
- Stale: `mappings/record_research_validation.tsv` still contains advisory
  rows from an earlier research pass that treated the live ChEBI identity as
  unresolved. The current OLS/ChEBI and PubChem checks resolve that concern.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, stale advisory rows, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, and `ingredient_type` are populated.
- This record has two occurrence counts from CultureMech recipe membership; no
  role, component, environment, or discussion entries need review.
- Optional synonym enrichment is not required because the preferred term is
  already an exact ChEBI synonym for `CHEBI:17597`.

## Recommended Edits

No YAML edit is required for this record. If the stale advisory TSVs are ever
regenerated, their `4-Hydroxybenzaldehyde` warnings should disappear.
