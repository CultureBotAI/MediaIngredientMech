# `data/ingredients/mapped/34-Dihydroxyflavone.yaml`

## Verdict

Pass with minor issues, minor. The CAS-backed local identity for
`3,4'-Dihydroxyflavone`, PubChem chemistry, MeSH parent, CAS and kg-microbe
registry rows, SSSOM, and aggregate row pass; only stale prefix-validator
advisory rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/34-Dihydroxyflavone.yaml`.
- Identifier and grounding: `identifier: cas:14919-49-4` with
  `ontology_mapping.ontology_id: mesh:C559991`, source `MESH`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- PubChem CID `688715` resolves to `3,4'-Dihydroxyflavone`, CAS `14919-49-4`,
  formula `C15H10O4`, and the stored InChI
  `InChI=1S/C15H10O4/c16-10-7-5-9(6-8-10)15-14(18)13(17)11-3-1-2-4-12(11)19-15/h1-8,16,18H`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` confirms
  that prefix-specific EBI OLS lookup resolves `mesh:C559991` to
  `3,4'-dihydroxyflavone`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-trehalosamine.yaml data/ingredients/mapped/3-trichloropropane.yaml data/ingredients/mapped/34-Dihydroxyflavone.yaml data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml data/ingredients/mapped/34-Dimethoxyflavone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-trehalosamine.yaml data/ingredients/mapped/3-trichloropropane.yaml data/ingredients/mapped/34-Dihydroxyflavone.yaml data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml data/ingredients/mapped/34-Dimethoxyflavone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  expected `MIM:34-Dihydroxyflavone` narrow MeSH row plus exact CAS and
  kg-microbe registry rows.

## Evidence

- The local CAS/PubChem identity is self-consistent for the exact flavone
  isomer named by `preferred_term`.
- The active SSSOM rows preserve the exact CAS identity alongside the broader
  MeSH parent; this matches the non-exact parent plus registry-row contract in
  `MAPPING_SEMANTICS.md`.
- Stale: `reports/yaml_record_review_batch/validation_report.md` reports
  `mesh:C559991` as invalid, and `mappings/ingredient_mappings_oak_ols_review.tsv`
  reports the MeSH, CAS, and kg-microbe registry rows as `UNKNOWN_TERM`. The
  curated unknown-term triage and prefix-specific OLS validation rows supersede
  those false positives.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM rows, generated docs, unknown-term triage
  rows, stale advisory rows, and ignored aggregate backups.

## Completeness

- CAS, PubChem CID, formula, InChI, and SMILES are populated for the exact
  CAS-named molecule.
- Exact ChEBI grounding is absent; the current MeSH parent plus CAS and
  kg-microbe registry identity rows preserve the exact CAS-backed local identity.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record. The stale OAK/OLS and batch advisory
rows can be ignored or refreshed when those generated reports are rebuilt.
