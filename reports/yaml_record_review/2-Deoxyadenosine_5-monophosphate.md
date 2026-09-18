# `data/ingredients/mapped/2-Deoxyadenosine_5-monophosphate.yaml`

## Verdict

Pass. The record denotes `2-Deoxyadenosine 5-monophosphate` exactly through a
CAS-backed `CHEBI:17713` mapping, with matching chemistry, SSSOM, aggregate, and
docs rows.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-Deoxyadenosine_5-monophosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17713` with
  `ontology_mapping.ontology_id: CHEBI:17713`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:17713`
  resolves to `2'-deoxyadenosine 5'-monophosphate` and lists
  `2'-deoxy-5'-adenylic acid`, CAS `653-63-4`, formula `C10H14N5O6P`, and
  InChI matching the record.
- The 2026-08-24 regrade correctly records the CAS-derived mapping method and
  leaves the SSSOM predicate as `skos:exactMatch`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Deoxy-D-glucose.yaml data/ingredients/mapped/2-Deoxy-D-ribonic_Acid_Lithium_Salt.yaml data/ingredients/mapped/2-Deoxyadenosine_5-monophosphate.yaml data/ingredients/mapped/2-Deoxyadenosine_Monohydrate.yaml data/ingredients/mapped/2-Deoxycytidine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Deoxyadenosine_5-monophosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Deoxyadenosine_5-monophosphate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Deoxyadenosine_5-monophosphate` to `CHEBI:17713` row with the exact
  adenylic-acid synonym and CAS `653-63-4`.

## Evidence

- The active ChEBI target confirms the mapped identity, exact synonym, CAS RN,
  formula, and InChI.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` says the proposed
  surface text is already represented, so no live synonym edit is pending.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows and no unresolved active duplicate for `CHEBI:17713`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

No curated YAML, aggregate, SSSOM, or docs edit is needed for the active
`2-Deoxyadenosine 5-monophosphate` record.
