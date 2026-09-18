# `data/ingredients/mapped/2-Furfuraldehyde.yaml`

## Verdict

Pass. The record denotes `2-Furfuraldehyde` exactly through a CAS-backed
`CHEBI:34768` mapping, and the exact furan-2-carbaldehyde synonym, chemistry,
SSSOM, aggregate, and docs rows agree.

## Identity

- Reviewed record: `data/ingredients/mapped/2-Furfuraldehyde.yaml`.
- Identifier and grounding: `identifier: CHEBI:34768` with
  `ontology_mapping.ontology_id: CHEBI:34768`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:34768`
  resolves to `furfural` and lists furan synonyms, CAS `98-01-1`, formula
  `C5H4O2`, and InChI matching the record.
- The 2026-08-24 regrade correctly records the CAS-derived mapping method and
  leaves the SSSOM predicate as `skos:exactMatch`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Deoxycytidine_5-monophosphate.yaml data/ingredients/mapped/2-Ethylhexanol.yaml data/ingredients/mapped/2-Furfuraldehyde.yaml data/ingredients/mapped/2-Hydroxy-34-Dimethoxybenzoic_Acid.yaml data/ingredients/mapped/2-Hydroxybutyric_Acid_Sodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Furfuraldehyde.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Furfuraldehyde.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Furfuraldehyde` to `CHEBI:34768` row with `furan-2-carbaldehyde` and
  CAS `98-01-1`.

## Evidence

- The active ChEBI target confirms the mapped identity, exact synonym, CAS RN,
  formula, and InChI.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` says the proposed
  `2-Furfuraldehyde` synonym is already represented by the preferred term, so no
  live synonym edit is pending.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows and no unresolved active duplicate for `CHEBI:34768`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

No curated YAML, aggregate, SSSOM, or docs edit is needed for the active
`2-Furfuraldehyde` record.
