# `data/ingredients/mapped/25-Dihydroxy-4-Methoxychalcone.yaml`

## Verdict

Needs curation, minor. The `cas:6342-92-3` registry fallback is the expected
primary identity while no ChEBI term exists, and the SSSOM registry row exports,
but PubChem now resolves the CAS RN and the record only stores the CAS number,
not formula, InChI, or SMILES.

## Identity

- Reviewed record:
  `data/ingredients/mapped/25-Dihydroxy-4-Methoxychalcone.yaml`.
- Identifier and grounding: `identifier: cas:6342-92-3` with
  `ontology_mapping.ontology_id: cas:6342-92-3`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem CAS check: CAS `6342-92-3` resolves to formula `C16H14O4`, SMILES
  `COC1=CC=C(C=C1)/C=C/C(=O)C2=C(C=CC(=C2)O)O`, and IUPAC
  `(E)-1-(2,5-dihydroxyphenyl)-3-(4-methoxyphenyl)prop-2-en-1-one`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` marks the
  `cas:6342-92-3` unknown-term row as `expected_registry_identifier` and says
  to keep it because the CAS object ID matches the YAML identifier and CAS
  registry CURIEs are not OAK/OLS ontology terms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/24-Dinitrophenol.yaml data/ingredients/mapped/24-diamino-67-di-iso-propylpteridine_phosphate.yaml data/ingredients/mapped/25-Dihydroxy-4-Methoxychalcone.yaml data/ingredients/mapped/3-Aminophenol.yaml data/ingredients/mapped/3-Aminopropionitrile_Fumarate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Focused `linkml-term-validator` could not complete for this CAS-registry
  record because OAK tried to download `cas.db.gz` for the `cas:` prefix and
  received an HTML response instead of gzip content.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected
  `MIM:25-Dihydroxy-4-Methoxychalcone` to `cas:6342-92-3` registry row.

## Evidence

- OAK/OLS review cannot resolve `cas:6342-92-3`; the later unknown-term triage
  row records this as an expected registry identifier, not a mapping repair.
- PubChem now verifies that the CAS RN names the chalcone structure represented
  by the record label.
- `occurrence_statistics` reports `0/0`; the record came from a CultureBotHT
  CAS source rather than a counted CultureMech recipe occurrence.
- Stale: `mappings/record_research_validation.tsv` still contains old P1/P3
  rows arguing against the registry fallback, while the row-review manifest now
  records `expected_registry_identifier` for the CAS fallback.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, unknown-term triage, OAK/OLS review, and advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Minor: the PubChem formula, InChI, and SMILES are not backfilled.
- There is no active ChEBI target to promote to.

## Recommended Edits

1. Backfill formula `C16H14O4`, InChI, and SMILES from inspected PubChem CAS
   evidence.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
3. Re-run the focused strict validator, CAS-fallback review, `just qc-sssom`,
   and `just qc-flat-coverage` after those edits.
