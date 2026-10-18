# `data/ingredients/mapped/2-Deoxy-D-Ribose.yaml`

## Verdict

Needs curation, major. The active `CHEBI:28816` identity is correct, but the
record asserts `CARBON_SOURCE` from only provisional ChEBI-ancestry evidence and
still reports `0/0` occurrences after folding a one-recipe CultureMech
`Deoxyribose` alias onto the record.

## Identity

- Reviewed record: `data/ingredients/mapped/2-Deoxy-D-Ribose.yaml`.
- Identifier and grounding: `identifier: CHEBI:28816` with
  `ontology_mapping.ontology_id: CHEBI:28816`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:28816`
  resolves to `2-deoxy-D-ribose` and lists `Deoxyribose`,
  `2-deoxy-D-erythro-pentose`, CAS `533-67-5`, formula `C5H10O4`, SMILES
  `O=CC[C@H](O)[C@H](O)CO`, and InChI matching the record.
- The CultureMech alias `Deoxyribose` is exact for this ChEBI target, so the
  synonym text itself is not the issue.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Acetylpyrrole.yaml data/ingredients/mapped/2-Aminoethylphosphonate.yaml data/ingredients/mapped/2-Azetidinone.yaml data/ingredients/mapped/2-Chlorobenzoic_acid.yaml data/ingredients/mapped/2-Deoxy-D-Ribose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Deoxy-D-Ribose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Deoxy-D-Ribose.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Deoxy-D-Ribose` to `CHEBI:28816` row with exact `Deoxyribose` and
  `2-deoxy-D-erythro-pentose` labels.

## Evidence

- The active ChEBI target confirms the mapped identity, CultureMech alias, CAS
  RN, formula, SMILES, and InChI.
- Major: the `CARBON_SOURCE` nutritional role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence inferred from ChEBI carbohydrate ancestry.
  That proves a class relationship, not actual use of `2-deoxy-D-ribose` as a
  medium carbon source.
- Major: `mappings/culturemech_residual_groundings.tsv` records `Deoxyribose`
  as one occurrence across one CultureMech recipe that was folded onto this
  record, but `occurrence_statistics` and generated docs still publish `0/0`.
- Stale: `mappings/record_research_validation.tsv` still has an old row that
  requested direct verification of `CHEBI:28816`; the current ChEBI page now
  resolves the term.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, the one-recipe residual alias row, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- The component slots are correctly empty for this single ChEBI chemical.

## Recommended Edits

1. In `data/ingredients/mapped/2-Deoxy-D-Ribose.yaml`, either remove the
   provisional `CARBON_SOURCE` role or replace it with inspected
   formulation-specific evidence that directly supports the exact ingredient as
   a carbon source.
2. Refresh `occurrence_statistics` from the maintained CultureMech occurrence
   table or the residual grounding table so the folded `Deoxyribose` source row
   is reflected.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, docs, and mapping review queues.
4. Re-run strict/LinkML validation and SSSOM/docs export checks after the role
   and occurrence updates.
