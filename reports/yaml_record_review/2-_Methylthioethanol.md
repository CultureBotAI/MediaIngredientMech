# `data/ingredients/mapped/2-_Methylthioethanol.yaml`

## Verdict

Pass with minor issues. The active CAS-backed ChEBI identity is exact; only stale
advisory rows and the historical escaped SSSOM alias surface remain.

## Identity

- Reviewed record: `data/ingredients/mapped/2-_Methylthioethanol.yaml`.
- Identifier and grounding: `identifier: CHEBI:63861` with
  `ontology_mapping.ontology_id: CHEBI:63861`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:63861`
  resolves to `2-methylthioethanol` and lists `2-(methylsulfanyl)ethanol`, CAS
  `5271-38-5`, formula `C3H8OS`, and SMILES `CSCCO`.
- The escaped `MIM:2-~28Methylthio~29ethanol` row in
  `mappings/mim_curie_aliases.tsv` is an expected alias to
  `MIM:2-_Methylthioethanol`, not a second record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Piperidinone.yaml data/ingredients/mapped/2-Sulfobenzoic_Acid.yaml data/ingredients/mapped/2-_Methylthioethanol.yaml data/ingredients/mapped/2-aminobenzoate.yaml data/ingredients/mapped/2-aminopentanoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-_Methylthioethanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-_Methylthioethanol` to `CHEBI:63861` row with CAS `5271-38-5` and the
  stored exact synonym.

## Evidence

- The active ChEBI target confirms the mapped identity, exact synonym, CAS RN,
  formula, and SMILES for the stored neutral compound.
- Stale: `mappings/record_research_validation.tsv` still contains old rows that
  asked for direct ChEBI verification before trusting `CHEBI:63861`; the
  current ChEBI page resolves the term and confirms the CAS-grounded structure.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the expected alias, active YAML/aggregate/SSSOM rows, and stale advisory
  rows, with no live contradiction of the active `CHEBI:63861` identity.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, InChI, SMILES, and an exact ChEBI synonym are populated for
  the active chemical form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `CHEBI:63861` uncertainty no longer implies pending
   work.
2. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   `2-_Methylthioethanol` record.
