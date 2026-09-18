# `data/ingredients/mapped/2-Deoxy-D-glucose.yaml`

## Verdict

Needs curation, major. The active `CHEBI:15866` identity is correct, but the
record asserts `CARBON_SOURCE` from only provisional ChEBI-ancestry evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/2-Deoxy-D-glucose.yaml`.
- Identifier and grounding: `identifier: CHEBI:15866` with
  `ontology_mapping.ontology_id: CHEBI:15866`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:15866`
  resolves to `2-deoxy-D-glucose` and lists the exact synonym
  `2-Deoxy-D-arabino-hexose`, CAS `154-17-6`, and formula `C6H12O5`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Deoxy-D-glucose.yaml data/ingredients/mapped/2-Deoxy-D-ribonic_Acid_Lithium_Salt.yaml data/ingredients/mapped/2-Deoxyadenosine_5-monophosphate.yaml data/ingredients/mapped/2-Deoxyadenosine_Monohydrate.yaml data/ingredients/mapped/2-Deoxycytidine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Deoxy-D-glucose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Deoxy-D-glucose.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Deoxy-D-glucose` to `CHEBI:15866` row with
  `2-Deoxy-D-arabino-hexose` and CAS `154-17-6`.

## Evidence

- The active ChEBI target confirms the mapped identity, exact synonym, CAS RN,
  and formula.
- Major: the `CARBON_SOURCE` nutritional role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence inferred from ChEBI carbohydrate ancestry.
  That proves a class relationship, not actual use of `2-deoxy-D-glucose` as a
  medium carbon source.
- Stale: `mappings/record_research_validation.tsv` still has old rows that
  requested direct verification of `CHEBI:15866`; the current ChEBI page now
  resolves the term.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN and formula are populated for the active ChEBI form.
- Empty component slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. In `data/ingredients/mapped/2-Deoxy-D-glucose.yaml`, either remove the
   provisional `CARBON_SOURCE` role or replace it with inspected
   formulation-specific evidence that directly supports the exact ingredient as
   a carbon source.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, docs, and mapping review queues.
3. Re-run strict/LinkML validation and SSSOM/docs export checks after the role
   update.
