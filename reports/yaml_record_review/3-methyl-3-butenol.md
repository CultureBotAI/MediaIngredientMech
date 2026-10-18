# `data/ingredients/mapped/3-methyl-3-butenol.yaml`

## Verdict

Pass with minor issues, minor. The CAS-backed `CHEBI:62898`
`isopentenyl alcohol` identity, synonym boundary, chemistry, CAS-based mapping
grade, SSSOM row, and aggregate row pass; only stale advisory rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/3-methyl-3-butenol.yaml`.
- Identifier and grounding: `identifier: CHEBI:62898` with
  `ontology_mapping.ontology_id: CHEBI:62898`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- The OAK/OLS row review and the CAS xref both route CAS `763-32-6` to
  `CHEBI:62898` `isopentenyl alcohol`.
- Formula `C5H10O`, InChI `InChI=1S/C5H10O/c1-5(2)3-4-6/h6H,1,3-4H2,2H3`,
  and SMILES `C=C(C)CCO` describe the same neutral alcohol.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-methyl-3-butenol.yaml data/ingredients/mapped/3-nitropropanoate.yaml data/ingredients/mapped/3-octanone.yaml data/ingredients/mapped/3-phenylpropionate.yaml data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-methyl-3-butenol.yaml data/ingredients/mapped/3-nitropropanoate.yaml data/ingredients/mapped/3-octanone.yaml data/ingredients/mapped/3-phenylpropionate.yaml data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:3-methyl-3-butenol` to `CHEBI:62898` row.

## Evidence

- CultureBotHT supplied CAS `763-32-6`; local ChEBI xrefs and the OAK/OLS row
  review confirm `CHEBI:62898`.
- The August `CAS_RN_LOOKUP` regrade is correct: the source identity was
  established by explicit CAS lookup, and Rule D still emits an own-identifier
  `skos:exactMatch`.
- The batch P2 label warning is a false positive because `isopentenyl alcohol`
  and `3-methyl-3-butenol` denote the same term.
- Stale: `mappings/record_research_validation.tsv` still requests direct ChEBI
  verification and still has old `EXACT_MATCH`/`UNMAPPED` advice that predates
  the CAS-grade repair.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, generated docs, stale advisory rows,
  and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, and SMILES are populated and describe the same neutral
  alcohol.
- There are no role, component, environment, or discussion entries requiring
  record-local review.
- The empty occurrence count is expected for this CultureBotHT CAS import.

## Recommended Edits

No YAML edit is required for this record. The stale advisory rows can be ignored
or refreshed when `mappings/record_research_validation.tsv` is rebuilt.
