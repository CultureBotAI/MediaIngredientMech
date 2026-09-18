# `data/ingredients/mapped/3-methyl-2-butenol.yaml`

## Verdict

Pass with minor issues, minor. The CAS-backed `CHEBI:16019` `prenol` identity,
exact synonym, chemistry, CAS-based mapping grade, SSSOM row, and aggregate row
pass; only stale advisory rows remain.

## Identity

- Reviewed record: `data/ingredients/mapped/3-methyl-2-butenol.yaml`.
- Identifier and grounding: `identifier: CHEBI:16019` with
  `ontology_mapping.ontology_id: CHEBI:16019`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:16019` resolves to `prenol`,
  IUPAC `3-methylbut-2-en-1-ol`, CAS `556-82-1`, formula `C5H10O`, InChI
  `InChI=1S/C5H10O/c1-5(2)3-4-6/h3,6H,4H2,1-2H3`, and SMILES `CC(C)=CCO`;
  the record matches.
- The preferred term is a valid alternate surface form for prenol, and
  `3-methylbut-2-en-1-ol` is a valid exact synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-hydroxybutyric_Acid.yaml data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml data/ingredients/mapped/3-methyl-1-butanol.yaml data/ingredients/mapped/3-methyl-2-butenol.yaml data/ingredients/mapped/3-methyl-2-oxopentanoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-hydroxybutyric_Acid.yaml data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml data/ingredients/mapped/3-methyl-1-butanol.yaml data/ingredients/mapped/3-methyl-2-butenol.yaml data/ingredients/mapped/3-methyl-2-oxopentanoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:3-methyl-2-butenol` to `CHEBI:16019` row.

## Evidence

- CultureBotHT supplied CAS `556-82-1`; ChEBI confirms that this CAS belongs to
  the same `C5H10O` prenol structure.
- The August `CAS_RN_LOOKUP` regrade is correct: the source identity was
  established by explicit CAS lookup, and Rule D still emits an own-identifier
  `skos:exactMatch`.
- The batch P2 label warning is a false positive here because `prenol` and
  `3-methyl-2-butenol` denote the same ChEBI entity.
- Stale: `mappings/record_research_validation.tsv` still requests direct
  ChEBI verification and has old `EXACT_MATCH`/`UNMAPPED` advice that predates
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
