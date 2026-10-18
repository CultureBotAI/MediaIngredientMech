# `data/ingredients/mapped/13-Butandiol.yaml`

## Verdict

Pass with minor issues. The active record denotes `1,3-Butanediol` exactly via
`CHEBI:52683`, and the aggregate, SSSOM, and docs rows agree; only stale
advisory TSV rows still describe the old German preferred label state.

## Identity

- Reviewed record: `data/ingredients/mapped/13-Butandiol.yaml`.
- Identifier and grounding: `identifier: CHEBI:52683` with
  `ontology_mapping.ontology_id: CHEBI:52683`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Preferred label: `1,3-Butanediol`. The slug and raw synonym preserve the old
  `1,3-Butandiol` source spelling, but the preferred term was corrected on
  2026-08-18.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:52683`
  resolves to `butane-1,3-diol` and lists `1,3-Butanediol`,
  `1,3-Butandiol`, CAS `107-88-0`, formula `C4H10O2`, SMILES, and InChI that
  match the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/13-Butandiol.yaml data/ingredients/mapped/13-Hexanediol.yaml data/ingredients/mapped/13-Propanediol.yaml data/ingredients/mapped/14-B-D-Galactobiose.yaml data/ingredients/mapped/14-Butanediol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- LinkML term validation passed for
  `data/ingredients/mapped/13-Butandiol.yaml`.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:13-Butandiol` to `CHEBI:52683` row with
  `other_label: 1,3-Butandiol|CAS:107-88-0`.

## Evidence

- The active ChEBI target confirms the mapped identity, exact retained spelling,
  CAS RN, formula, SMILES, and InChI.
- The curation history records the 2026-08-18 label correction and the
  2026-08-24 regrade to `CAS_RN_LOOKUP`, matching the current mapping state.
- Minor: `mappings/record_research_validation.tsv` still has stale rows that
  describe the pre-correction German preferred label and slug rather than the
  active `1,3-Butanediol` preferred label.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows and stale advisory rows, with no unresolved active duplicate for
  `CHEBI:52683`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale `1,3-Butandiol` preferred-label findings no longer
   imply pending work.
2. No YAML, aggregate, SSSOM, or docs identity edit is needed for the active
   `CHEBI:52683` mapping.
