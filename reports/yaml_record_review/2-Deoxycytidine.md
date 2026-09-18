# `data/ingredients/mapped/2-Deoxycytidine.yaml`

## Verdict

Pass. The record denotes `2'-Deoxycytidine` exactly through `CHEBI:15698`, and
the synchronized outputs agree.

## Identity

- Reviewed record: `data/ingredients/mapped/2-Deoxycytidine.yaml`.
- Identifier and grounding: `identifier: CHEBI:15698` with
  `ontology_mapping.ontology_id: CHEBI:15698`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:15698`
  resolves to `2'-deoxycytidine` and lists CAS `951-77-9`, formula
  `C9H13N3O4`, and InChI matching the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Deoxy-D-glucose.yaml data/ingredients/mapped/2-Deoxy-D-ribonic_Acid_Lithium_Salt.yaml data/ingredients/mapped/2-Deoxyadenosine_5-monophosphate.yaml data/ingredients/mapped/2-Deoxyadenosine_Monohydrate.yaml data/ingredients/mapped/2-Deoxycytidine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Deoxycytidine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Deoxycytidine.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Deoxycytidine` to `CHEBI:15698` row with `CAS:951-77-9`.

## Evidence

- The active ChEBI target confirms the mapped identity, CAS RN, formula, and
  InChI.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the active YAML/aggregate/SSSOM rows and no
  unresolved active duplicate for `CHEBI:15698`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

No curated YAML, aggregate, SSSOM, or docs edit is needed for the active
`2'-Deoxycytidine` record.
