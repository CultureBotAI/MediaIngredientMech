# `data/ingredients/mapped/13-Propanediol.yaml`

## Verdict

Pass. The record denotes `1,3-Propanediol` exactly through a CAS-backed
`CHEBI:16109` mapping, and the formula, structure, raw synonym handling,
aggregate record, SSSOM row, and docs row agree.

## Identity

- Reviewed record: `data/ingredients/mapped/13-Propanediol.yaml`.
- Identifier and grounding: `identifier: CHEBI:16109` with
  `ontology_mapping.ontology_id: CHEBI:16109`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:16109`
  resolves to `propane-1,3-diol` and lists formula `C3H8O2`, SMILES `OCCCO`,
  and InChI consistent with the record.
- Raw source wording: the microbedecoder synonym `Trimethyleneglycol` is
  retained as an exact synonym of the same compound and is exported in
  `other_label`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/13-Butandiol.yaml data/ingredients/mapped/13-Hexanediol.yaml data/ingredients/mapped/13-Propanediol.yaml data/ingredients/mapped/14-B-D-Galactobiose.yaml data/ingredients/mapped/14-Butanediol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- LinkML term validation passed for
  `data/ingredients/mapped/13-Propanediol.yaml`.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:13-Propanediol` to `CHEBI:16109` row with
  `other_label: Trimethyleneglycol|CAS:504-63-2`.

## Evidence

- The active ChEBI target confirms the mapped identity and structure-derived
  values for the same `1,3-Propanediol` form.
- CAS `504-63-2` is the RN for the active target rather than a sibling
  stereochemical, salt, or hydrate form.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows and no unresolved active duplicate for `CHEBI:16109`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

No curated YAML, aggregate, SSSOM, or docs edit is needed for the active
`CHEBI:16109` mapping.
