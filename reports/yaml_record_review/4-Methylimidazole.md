# `data/ingredients/mapped/4-Methylimidazole.yaml`

## Verdict

Pass, none. The `CHEBI:40035` identity, exact synonym, CAS, chemistry, SSSOM
row, and aggregate row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-Methylimidazole.yaml`.
- Identifier and grounding: `identifier: CHEBI:40035` with
  `ontology_mapping.ontology_id: CHEBI:40035`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:40035` is active, resolves to
  `4-methylimidazole`, has formula `C4H6N2`, CAS `822-36-6`, SMILES
  `Cc1cncn1`, the stored InChI, and exact synonym `4-methyl-1H-imidazole`.
- PubChem CAS lookup for `822-36-6` resolves to CID `13195` with formula
  `C4H6N2` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Methoxyflavone.yaml data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml data/ingredients/mapped/4-Methylimidazole.yaml data/ingredients/mapped/4-Pyridoxic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Methoxyflavone.yaml data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml data/ingredients/mapped/4-Methylimidazole.yaml data/ingredients/mapped/4-Pyridoxic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-Methylimidazole` to `CHEBI:40035` row.

## Evidence

- The CultureBotHT import, current ChEBI CAS xref, PubChem CAS lookup, formula,
  InChI, SMILES, and exact synonym all support the same imidazole identity.
- The OAK/OLS row-review manifest confirmed this mapping and asked for no
  curation action.
- The SSSOM `other` field carries an exact synonym and the CAS number, not a
  rejected or broader label.
- Stale: `mappings/record_research_validation.tsv` still says this CURIE needed
  direct verification; the current OLS/ChEBI and OAK/OLS row-review checks have
  resolved that.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, stale advisory rows, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, exact synonym, and `ingredient_type` are
  populated.
- This CultureBotHT import has no recipe-count occurrence; no role, component,
  environment, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
