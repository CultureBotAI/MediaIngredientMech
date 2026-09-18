# `data/ingredients/mapped/2-Deoxycytidine_5-monophosphate.yaml`

## Verdict

Pass. The record denotes `2-Deoxycytidine 5-monophosphate` exactly through a
CAS-backed `CHEBI:15918` mapping, and the chemistry, SSSOM, aggregate, and docs
rows agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-Deoxycytidine_5-monophosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15918` with
  `ontology_mapping.ontology_id: CHEBI:15918`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:15918`
  resolves to `2'-deoxycytosine 5'-monophosphate`, lists CAS `1032-65-1`, and
  reports formula `C9H14N3O7P`.
- The 2026-08-24 regrade correctly records the CAS-derived mapping method and
  leaves the SSSOM predicate as `skos:exactMatch`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Deoxycytidine_5-monophosphate.yaml data/ingredients/mapped/2-Ethylhexanol.yaml data/ingredients/mapped/2-Furfuraldehyde.yaml data/ingredients/mapped/2-Hydroxy-34-Dimethoxybenzoic_Acid.yaml data/ingredients/mapped/2-Hydroxybutyric_Acid_Sodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Deoxycytidine_5-monophosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Deoxycytidine_5-monophosphate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Deoxycytidine_5-monophosphate` to `CHEBI:15918` row with
  `2'-deoxy-5'-cytidylic acid` and CAS `1032-65-1`.

## Evidence

- The active ChEBI target confirms the mapped identity, CAS RN, and formula.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` says the proposed
  surface text is already represented, so no live synonym edit is pending.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows and no unresolved active duplicate for `CHEBI:15918`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

No curated YAML, aggregate, SSSOM, or docs edit is needed for the active
`2-Deoxycytidine 5-monophosphate` record.
