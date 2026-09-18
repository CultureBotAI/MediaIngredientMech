# `data/ingredients/mapped/2-Hydroxy-34-Dimethoxybenzoic_Acid.yaml`

## Verdict

Pass. The comma-restored `2-Hydroxy-3,4-Dimethoxybenzoic Acid` record denotes
`CHEBI:184501` exactly, and the chemistry, SSSOM, aggregate, and docs rows
agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-Hydroxy-34-Dimethoxybenzoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:184501` with
  `ontology_mapping.ontology_id: CHEBI:184501`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:184501`
  resolves to `2-HYDROXY-3,4-DIMETHOXYBENZOIC ACID` and lists CAS `5653-46-3`,
  formula `C9H10O5`, SMILES `COc1ccc(C(=O)O)c(O)c1OC`, and InChI matching the
  record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Deoxycytidine_5-monophosphate.yaml data/ingredients/mapped/2-Ethylhexanol.yaml data/ingredients/mapped/2-Furfuraldehyde.yaml data/ingredients/mapped/2-Hydroxy-34-Dimethoxybenzoic_Acid.yaml data/ingredients/mapped/2-Hydroxybutyric_Acid_Sodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Hydroxy-34-Dimethoxybenzoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Hydroxy-34-Dimethoxybenzoic_Acid.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Hydroxy-34-Dimethoxybenzoic_Acid` to `CHEBI:184501` row with
  `CAS:5653-46-3`.

## Evidence

- The active ChEBI target confirms the mapped identity, CAS RN, formula, SMILES,
  and InChI.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the active YAML/aggregate/SSSOM rows and no
  unresolved active duplicate for `CHEBI:184501`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

No curated YAML, aggregate, SSSOM, or docs edit is needed for the active
`2-Hydroxy-3,4-Dimethoxybenzoic Acid` record.
