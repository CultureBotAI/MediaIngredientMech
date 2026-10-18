# `data/ingredients/mapped/2-Hydroxypyridine.yaml`

## Verdict

Pass with minor issues. The record denotes `2-Hydroxypyridine` exactly through a
CAS-backed `CHEBI:16540` mapping, and only stale advisory rows still describe
pre-verification uncertainty.

## Identity

- Reviewed record: `data/ingredients/mapped/2-Hydroxypyridine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16540` with
  `ontology_mapping.ontology_id: CHEBI:16540`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:16540`
  resolves to `pyridin-2-ol` and lists `2-hydroxypyridine`, CAS `142-08-5`,
  and formula `C5H5NO`.
- The 2026-08-24 regrade correctly records the CAS-derived mapping method and
  leaves the SSSOM predicate as `skos:exactMatch`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Hydroxypyridine.yaml data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Monohydrate.yaml data/ingredients/mapped/2-Mercaptopyridine_N-oxide_Sodium_Salt.yaml data/ingredients/mapped/2-Nitrophenol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Hydroxypyridine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Hydroxypyridine.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Hydroxypyridine` to `CHEBI:16540` row with `CAS:142-08-5`.

## Evidence

- The active ChEBI target confirms the mapped identity, CAS RN, and formula.
- Stale: `mappings/record_research_validation.tsv` still has old rows that
  asked for direct ChEBI verification; the current ChEBI page now resolves the
  term.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, stale advisory rows, and no unresolved active duplicate for
  `CHEBI:16540`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `CHEBI:16540` uncertainty no longer implies pending
   work.
2. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   `2-Hydroxypyridine` record.
