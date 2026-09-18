# `data/ingredients/mapped/12-dichloropropane.yaml`

## Verdict

Pass with minor issues. The record has already moved from generic
`CHEBI:142468` to the CAS-specific racemate `CHEBI:82163`, and synchronized
outputs agree; only stale advisory review rows still refer to the old target.

## Identity

- Reviewed record: `data/ingredients/mapped/12-dichloropropane.yaml`.
- Identifier and grounding: `identifier: CHEBI:82163` with
  `ontology_mapping.ontology_id: CHEBI:82163`, label
  `rac-1,2-dichloropropane`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:82163`
  resolves to `rac-1,2-dichloropropane` and lists the record's CAS RN
  `78-87-5`.
- CAS-specific boundary: the #320 repair correctly treats CAS `78-87-5` as the
  specific commercial form and keeps the record on the racemate rather than the
  less specific `CHEBI:142468` parent.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/12-dichloropropane.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/12-dichloropropane.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/11-Biphenyl-2-ol.yaml data/ingredients/mapped/112-trichloroethane.yaml data/ingredients/mapped/1122-Tetrachloroethane.yaml data/ingredients/mapped/12-Propanediol.yaml data/ingredients/mapped/12-dichloropropane.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `CHEBI:82163` row with CAS `78-87-5`, the dropped-locant raw label, and the
  CultureMech stock-surface raw label in `other_label`.

## Evidence

- Current ChEBI confirms that the active target is `CHEBI:82163`
  `rac-1,2-dichloropropane` and carries CAS `78-87-5`, matching the #320
  rationale.
- `2-dichloropropane` and `1,2--Dichloropropane (10 mg/ml in methanol)` are
  stored as raw source text only, not as exact synonyms.
- Minor: `mappings/ingredient_mappings_oak_ols_review.tsv`,
  `mappings/ingredient_mappings_row_review_manifest.tsv`, and
  `mappings/record_research_validation.tsv` still contain pre-#320 rows for the
  old `CHEBI:142468` target.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the active YAML/aggregate/SSSOM/docs rows,
  stale advisory rows that still mention `CHEBI:142468`, and no duplicate
  active YAML for `CHEBI:82163`.

## Completeness

- Empty component and role slots are acceptable for this single ChEBI chemical.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical form.

## Recommended Edits

1. If the mapping review TSVs are intended to be live queues, regenerate them so
   stale `CHEBI:142468` rows no longer imply pending work for this repaired
   record.
2. No identifier, CAS-specific ChEBI grounding, raw source label, SSSOM,
   aggregate, or docs edit is needed for the active identity.
