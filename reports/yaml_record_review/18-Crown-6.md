# `data/ingredients/mapped/18-Crown-6.yaml`

## Verdict

Pass with minor issues. The record denotes `18-Crown-6` exactly through
`CHEBI:32397`, and the synchronized outputs agree; only stale advisory
verification rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/18-Crown-6.yaml`.
- Identifier and grounding: `identifier: CHEBI:32397` with
  `ontology_mapping.ontology_id: CHEBI:32397`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:32397`
  resolves to `18-crown-6` and lists
  `1,4,7,10,13,16-hexaoxacyclooctadecane`, CAS `17455-13-9`, formula
  `C12H24O6`, SMILES `C1COCCOCCOCCOCCOCCO1`, and InChI matching the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/14-naphthoquinone.yaml data/ingredients/mapped/15-Pentanediol.yaml data/ingredients/mapped/16-Hexanediamine.yaml data/ingredients/mapped/18-Crown-6.yaml data/ingredients/mapped/2-6-dihydroxybenzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/18-Crown-6.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/18-Crown-6.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:18-Crown-6` to `CHEBI:32397` row with
  `other_label: 1,4,7,10,13,16-hexaoxacyclooctadecane|CAS:17455-13-9`.

## Evidence

- The active ChEBI target confirms the mapped identity, synonym, CAS RN,
  formula, SMILES, and InChI.
- Stale: `mappings/record_research_validation.tsv` still contains an old row
  from before direct ChEBI verification; the current ChEBI page resolves.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, stale advisory rows, and no unresolved active duplicate for
  `CHEBI:32397`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `CHEBI:32397` uncertainty no longer implies pending
   work.
2. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   `18-Crown-6` record.
