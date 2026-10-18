# `data/ingredients/mapped/4-Pyridoxic_Acid.yaml`

## Verdict

Needs curation, major. The `CHEBI:17405` identity, exact synonym, CAS, and
chemistry pass, but the provisional `VITAMIN_SOURCE` role is only inferred from
ChEBI ancestry and remains unreviewed on a vitamin B6 catabolite.

## Identity

- Reviewed record: `data/ingredients/mapped/4-Pyridoxic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17405` with
  `ontology_mapping.ontology_id: CHEBI:17405`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:17405` is active, resolves to
  `4-pyridoxic acid`, has formula `C8H9NO4`, CAS `82-82-6`, SMILES
  `Cc1ncc(CO)c(C(=O)O)c1O`, the stored InChI, and exact synonym
  `3-hydroxy-5-(hydroxymethyl)-2-methylpyridine-4-carboxylic acid`.
- PubChem CAS lookup for `82-82-6` resolves to CID `6723` with formula
  `C8H9NO4` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Methoxyflavone.yaml data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml data/ingredients/mapped/4-Methylimidazole.yaml data/ingredients/mapped/4-Pyridoxic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Methoxyflavone.yaml data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml data/ingredients/mapped/4-Methylimidazole.yaml data/ingredients/mapped/4-Pyridoxic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-Pyridoxic_Acid` to `CHEBI:17405` row.

## Evidence

- The CultureBotHT import, current ChEBI CAS xref, PubChem CAS lookup, formula,
  InChI, SMILES, and exact synonym all support the same 4-pyridoxic acid
  identity.
- The OAK/OLS row-review manifest confirmed this mapping and asked for no
  curation action.
- The SSSOM `other` field carries an exact synonym and the CAS number, not a
  rejected or broader label.
- Major: the `nutritional_roles.VITAMIN_SOURCE` entry is only a
  `COMPUTATIONAL_PREDICTION` inferred from `CHEBI:33229` ancestry and explicitly
  says review is recommended. The live ChEBI description identifies
  4-pyridoxic acid as a vitamin B6 catabolic product excreted in urine, which is
  not evidence that the compound serves as a vitamin source in media.
- Stale: `mappings/record_research_validation.tsv` still treats the ChEBI
  grounding as unresolved before the OAK/OLS confirmation.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, provisional role inference surfaces, stale advisory rows, and ignored
  aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, exact synonym, and `ingredient_type` are
  populated.
- The record has no recipe-count occurrence; no component, environment, or
  discussion entries need review.
- The only role should remain absent unless a medium or physiology source
  specifically supports 4-pyridoxic acid as a supplied vitamin source.

## Recommended Edits

Remove `nutritional_roles.VITAMIN_SOURCE`, or replace its evidence with a
specific source showing 4-pyridoxic acid itself functions as a vitamin source in
the curated medium context. Then resync the aggregate and rebuild docs.
