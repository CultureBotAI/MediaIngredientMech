# `data/ingredients/mapped/15-Pentanediol.yaml`

## Verdict

Pass with minor issues. The record denotes `1,5-Pentanediol` exactly through
`CHEBI:185431`, and the synchronized outputs agree; only stale advisory rows
still describe the old unverified state.

## Identity

- Reviewed record: `data/ingredients/mapped/15-Pentanediol.yaml`.
- Identifier and grounding: `identifier: CHEBI:185431` with
  `ontology_mapping.ontology_id: CHEBI:185431`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:185431`
  resolves to `Pentane-1,5-diol` and lists CAS `111-29-5`, formula `C5H12O2`,
  SMILES `OCCCCCO`, and InChI matching the record.
- The 2026-08-24 regrade correctly preserves the CAS-derived mapping method
  instead of flattening this to a purely lexical grade.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/14-naphthoquinone.yaml data/ingredients/mapped/15-Pentanediol.yaml data/ingredients/mapped/16-Hexanediamine.yaml data/ingredients/mapped/18-Crown-6.yaml data/ingredients/mapped/2-6-dihydroxybenzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/15-Pentanediol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/15-Pentanediol.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:15-Pentanediol` to `CHEBI:185431` row with `CAS:111-29-5`.

## Evidence

- The active ChEBI target confirms the mapped identity, CAS RN, formula, SMILES,
  and InChI.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` says the proposed
  `1,5-Pentanediol` synonym is already represented by the preferred term, so no
  live synonym edit is pending.
- Stale: `mappings/record_research_validation.tsv` still has old rows that
  question `CHEBI:185431` and assume `mapping_quality: EXACT_MATCH`; the active
  YAML is CAS-regraded and the current ChEBI page resolves.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, stale advisory rows, and no unresolved active duplicate for
  `CHEBI:185431`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `CHEBI:185431` uncertainty no longer implies pending
   work.
2. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   `1,5-Pentanediol` record.
