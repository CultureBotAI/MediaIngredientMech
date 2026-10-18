# `data/ingredients/mapped/20AA_mix.yaml`

## Verdict

Pass with minor issues. The `kgmicrobe.ingredient:20aa_mix` local stock-solution
identity, single CultureBotHT occurrence, SSSOM row, aggregate row, and docs
pass; only stale local-CURIE advisory rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/20AA_mix.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:20aa_mix` with the
  same `ontology_mapping.ontology_id`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The fallback identity is scoped to the named `20AA_mix` preparation used by
  the source CultureBotHT medium. It is intentionally not mapped to a single
  amino-acid class or external chemical ontology term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-undecanol.yaml data/ingredients/mapped/20AA_mix.yaml data/ingredients/mapped/22-Dipyridyl.yaml data/ingredients/mapped/22-dibromo-2-cyanoacetamide.yaml data/ingredients/mapped/2244688-heptamethylnonane.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/20AA_mix.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  skipped as expected because `kgmicrobe.ingredient` is not an OBO-backed prefix
  for Engine A.
- Whole-corpus checks run earlier in this review pass passed, including the
  Engine B id/label product gate; only the shared evidence validator was
  unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:20AA_mix` to `kgmicrobe.ingredient:20aa_mix` row.

## Evidence

- The maintained curation note explains why this record remains local: the
  source label denotes a named recurring multi-component preparation, not a
  single compound with a CHEBI, NCIT, MeSH, FOODON, or ENVO term.
- `occurrence_statistics` preserves the single CultureBotHT media occurrence
  from the import.
- Stale: batch-review rows and `record_research_validation.tsv` still flag the
  local `kgmicrobe.ingredient` identifier as though it should be an external
  OBO term; the `FALLBACK_REGISTRY` mapping is the intended local identity for
  this stock solution.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, old unmapped audit, and stale advisory rows.

## Completeness

- `ingredient_type: STOCK_SOLUTION` and `solution_type: AMINO_ACID_MIX` are
  present.
- Empty chemical-property and component slots are acceptable: the label names a
  stock solution but not its exact amino-acid identities or concentrations.

## Recommended Edits

1. No curation edit is required for `data/ingredients/mapped/20AA_mix.yaml`.
2. When stale advisory artifacts are next regenerated, confirm the obsolete
   local-CURIE findings drop out for this record.
