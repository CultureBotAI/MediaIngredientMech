# `data/ingredients/mapped/2-Mercaptopyridine_N-oxide_Sodium_Salt.yaml`

## Verdict

Pass with minor issues. The record denotes `2-Mercaptopyridine N-oxide sodium
salt` exactly through `CHEBI:201738`; only stale advisory rows still ask for
direct ChEBI verification.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-Mercaptopyridine_N-oxide_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:201738` with
  `ontology_mapping.ontology_id: CHEBI:201738`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:201738`
  resolves to `2-Mercaptopyridine N-oxide sodium salt` and lists
  `sodium;1-oxidopyridine-2-thione`, formula `C5H4NOS.Na`, SMILES
  `[Na+].[O-]n1ccccc1=S`, and InChI matching the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Hydroxypyridine.yaml data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml data/ingredients/mapped/2-Mercaptopyridine_N-oxide_Sodium_Salt.yaml data/ingredients/mapped/2-Nitrophenol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Mercaptopyridine_N-oxide_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Mercaptopyridine_N-oxide_Sodium_Salt.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Mercaptopyridine_N-oxide_Sodium_Salt` to `CHEBI:201738` row with the
  exact sodium synonym and CAS `3811-73-2`.

## Evidence

- The active ChEBI target confirms the mapped identity, exact synonym, formula,
  SMILES, and InChI.
- Stale: `mappings/record_research_validation.tsv` still has old rows that
  asked for direct ChEBI verification; the current ChEBI page now resolves the
  term.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, stale advisory rows, and no unresolved active duplicate for
  `CHEBI:201738`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI salt.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `CHEBI:201738` uncertainty no longer implies pending
   work.
2. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   `2-Mercaptopyridine N-oxide sodium salt` record.
