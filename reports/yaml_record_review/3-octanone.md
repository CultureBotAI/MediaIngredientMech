# `data/ingredients/mapped/3-octanone.yaml`

## Verdict

Pass with minor issues, minor. The exact `CHEBI:80946` `3-octanone` identity,
CAS, chemistry, SSSOM row, and aggregate row pass; only stale advisory rows
remain.

## Identity

- Reviewed record: `data/ingredients/mapped/3-octanone.yaml`.
- Identifier and grounding: `identifier: CHEBI:80946` with
  `ontology_mapping.ontology_id: CHEBI:80946`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:80946` resolves to `3-octanone`, lists CAS
  `106-68-3`, IUPAC `octan-3-one`, formula `C8H16O`, InChI
  `InChI=1S/C8H16O/c1-3-5-6-7-8(9)4-2/h3-7H2,1-2H3`, and SMILES
  `CCCCCC(=O)CC`; the record matches.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-methyl-3-butenol.yaml data/ingredients/mapped/3-nitropropanoate.yaml data/ingredients/mapped/3-octanone.yaml data/ingredients/mapped/3-phenylpropionate.yaml data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-methyl-3-butenol.yaml data/ingredients/mapped/3-nitropropanoate.yaml data/ingredients/mapped/3-octanone.yaml data/ingredients/mapped/3-phenylpropionate.yaml data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:3-octanone` to `CHEBI:80946` row.

## Evidence

- CultureBotHT supplied CAS `106-68-3`; ChEBI confirms that CAS, the canonical
  label, formula, InChI, and SMILES for the same neutral ketone.
- The OAK/OLS row review had already confirmed this row and required no action.
- Stale: `mappings/record_research_validation.tsv` still requests direct ChEBI
  verification and still recommends withholding the SSSOM row. The identifier
  and structure now resolve exactly.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, generated docs, stale advisory rows,
  and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, and SMILES are populated.
- The single exact synonym `octan-3-one` is valid.
- There are no role, component, environment, or discussion entries requiring
  record-local review.

## Recommended Edits

No YAML edit is required for this record. The stale advisory rows can be ignored
or refreshed when `mappings/record_research_validation.tsv` is rebuilt.
