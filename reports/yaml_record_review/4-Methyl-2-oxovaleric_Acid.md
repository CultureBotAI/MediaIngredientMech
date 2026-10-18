# `data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml`

## Verdict

Needs curation, major. The neutral `CHEBI:48430` identity, CAS, chemistry,
SSSOM row, and aggregate row pass, but the conjugate-base anion remains an exact
synonym and publishes through SSSOM.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:48430` with
  `ontology_mapping.ontology_id: CHEBI:48430`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:48430` is active, resolves to
  `4-methyl-2-oxopentanoic acid`, has formula `C6H10O3`, CAS `816-66-0`,
  SMILES `CC(C)CC(=O)C(=O)O`, and the stored InChI.
- PubChem CAS lookup for `816-66-0` resolves to CID `70` with formula `C6H10O3`
  and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Methoxyflavone.yaml data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml data/ingredients/mapped/4-Methylimidazole.yaml data/ingredients/mapped/4-Pyridoxic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Methoxyflavone.yaml data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml data/ingredients/mapped/4-Methylimidazole.yaml data/ingredients/mapped/4-Pyridoxic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-Methyl-2-oxovaleric_Acid` to `CHEBI:48430` row.

## Evidence

- The CultureBotHT CAS lookup, current ChEBI CAS xref, PubChem CAS lookup,
  formula, InChI, and SMILES all support the same neutral acid identity.
- The August `CAS_RN_LOOKUP` grade correctly records that the CAS xref, not a
  primary-label match to `4-Methyl-2-oxovaleric acid`, established the mapping.
- The OAK/OLS row-review manifest confirmed this mapping and asked for no
  curation action.
- Major: `4-Methyl-2-oxopentanoate` is the anion label without the acidic
  proton, but it is stored as an `EXACT_SYNONYM` and exported in the SSSOM
  `other` field for the neutral acid.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, same-name conflict baseline, stale advisory rows, and ignored aggregate
  backups.

## Completeness

- CAS, formula, InChI, SMILES, and `ingredient_type` are populated.
- This CultureBotHT CAS import has no recipe-count occurrence; no role,
  component, environment, or discussion entries need review.

## Recommended Edits

Remove or demote `4-Methyl-2-oxopentanoate` so the anion no longer publishes as
an exact neutral-acid synonym, then resync the aggregate and rebuild SSSOM/docs.
