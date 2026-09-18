# `data/ingredients/mapped/14-Butanediol.yaml`

## Verdict

Needs curation, major. The active `1,4-Butanediol` identity to `CHEBI:41189` is
correct, but raw fragments from a duplicate parse, `Butane-1` and `4-diol`, are
still exported as labels for the active chemical.

## Identity

- Reviewed record: `data/ingredients/mapped/14-Butanediol.yaml`.
- Identifier and grounding: `identifier: CHEBI:41189` with
  `ontology_mapping.ontology_id: CHEBI:41189`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:41189`
  resolves to `butane-1,4-diol` and lists `1,4-BUTANEDIOL`, CAS `110-63-4`,
  formula `C4H10O2`, SMILES, and InChI consistent with the record.
- Duplicate/tombstone boundary: `data/ingredients/mapped/Butane-14-diol.yaml`
  and `data/ingredients/unmapped/4-diol.yaml` are rejected tombstones, while
  `data/ingredients/mapped/14-Butanediol.yaml` is the active record for the
  chemical identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/13-Butandiol.yaml data/ingredients/mapped/13-Hexanediol.yaml data/ingredients/mapped/13-Propanediol.yaml data/ingredients/mapped/14-B-D-Galactobiose.yaml data/ingredients/mapped/14-Butanediol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- LinkML term validation passed for
  `data/ingredients/mapped/14-Butanediol.yaml`.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:14-Butanediol` to `CHEBI:41189` row, but its `other_label` value includes
  `Butane-1|4-diol|CAS:110-63-4`.

## Evidence

- The active ChEBI target confirms the mapped identity, CAS RN, formula, SMILES,
  and InChI for `1,4-Butanediol`.
- Major: `Butane-1` and `4-diol` are parse fragments from the merged duplicate
  and do not exactly name `1,4-Butanediol`. Keeping them as exact synonyms leaks
  invalid aliases into SSSOM, docs, and the label index.
- The rejected duplicate records are traceable in YAML and docs, so their mere
  existence is not the curation defect. The active record's synonym carryover is
  the live defect.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, rejected tombstone rows for `Butane-1,4-diol` and `4-diol`, and the live
  raw-fragment synonyms on the active `1,4-Butanediol` record.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical.

## Recommended Edits

1. In `data/ingredients/mapped/14-Butanediol.yaml`, remove exact synonym entries
   for `Butane-1` and `4-diol`; keep only labels that exactly denote
   `1,4-Butanediol`.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs so invalid fragments no
   longer appear as labels for the active ingredient.
3. Re-run strict/LinkML validation, `scripts/audit_duplicate_identifiers.py
   --check`, and the SSSOM/docs export checks after the synonym cleanup.
