# `data/ingredients/mapped/2-Azetidinone.yaml`

## Verdict

Pass with minor issues. The record denotes `2-Azetidinone` exactly through a
CAS-backed `CHEBI:327119` mapping, and only stale advisory synonym rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/2-Azetidinone.yaml`.
- Identifier and grounding: `identifier: CHEBI:327119` with
  `ontology_mapping.ontology_id: CHEBI:327119`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:327119`
  resolves to `azetidin-2-one` and lists `2-Azetidinone`, CAS `930-21-2`,
  formula `C3H5NO`, SMILES `O=C1CCN1`, and InChI matching the record.
- The 2026-08-24 regrade correctly records the CAS-derived mapping method and
  leaves the SSSOM predicate as `skos:exactMatch`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-Acetylpyrrole.yaml data/ingredients/mapped/2-Aminoethylphosphonate.yaml data/ingredients/mapped/2-Azetidinone.yaml data/ingredients/mapped/2-Chlorobenzoic_acid.yaml data/ingredients/mapped/2-Deoxy-D-Ribose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/2-Azetidinone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-Azetidinone.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-Azetidinone` to `CHEBI:327119` row with `CAS:930-21-2`.

## Evidence

- The active ChEBI target confirms the mapped identity, synonym, CAS RN,
  formula, SMILES, and InChI.
- Stale: `mappings/record_research_validation.tsv` still contains old rows that
  predate ChEBI confirmation and ask for `azetidin-2-one` as a synonym; that
  text is already represented as the ontology label in the label index.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, stale advisory rows, and no unresolved active duplicate for
  `CHEBI:327119`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `CHEBI:327119` uncertainty no longer implies pending
   work.
2. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   `2-Azetidinone` record.
