# `data/ingredients/mapped/2-Acetylpyrrole.yaml`

## Verdict

Pass with minor issues. The record denotes `2-Acetylpyrrole` exactly through
`CHEBI:59981`, and the synchronized outputs agree; only stale advisory rows
still describe pre-verification uncertainty.

## Identity

- Reviewed record: `data/ingredients/mapped/2-Acetylpyrrole.yaml`.
- Identifier and grounding: `identifier: CHEBI:59981` with
  `ontology_mapping.ontology_id: CHEBI:59981`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:59981`
  resolves to `2-acetylpyrrole` and lists CAS `1072-83-9`, formula `C6H7NO`,
  SMILES `CC(=O)c1cccn1`, and InChI matching the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Acetylpyrrole.yaml data/ingredients/mapped/2-Aminoethylphosphonate.yaml data/ingredients/mapped/2-Azetidinone.yaml data/ingredients/mapped/2-Chlorobenzoic_acid.yaml data/ingredients/mapped/2-Deoxy-D-Ribose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Acetylpyrrole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Acetylpyrrole.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Acetylpyrrole` to `CHEBI:59981` row with `CAS:1072-83-9`.

## Evidence

- The active ChEBI target confirms the mapped identity, CAS RN, formula, SMILES,
  and InChI.
- Stale: `mappings/record_research_validation.tsv` still has old rows that
  asked for direct ChEBI verification or recommended suppressing the mapping;
  the current ChEBI page now resolves the term.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, stale advisory rows, and no unresolved active duplicate for
  `CHEBI:59981`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `CHEBI:59981` uncertainty no longer implies pending
   work.
2. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   `2-Acetylpyrrole` record.
