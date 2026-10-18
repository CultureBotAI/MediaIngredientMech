# `data/ingredients/mapped/3-methyl-2-oxopentanoic_Acid.yaml`

## Verdict

Pass with minor issues, minor. The CAS-backed `CHEBI:35932`
`3-methyl-2-oxovaleric acid` identity, chemistry, exact predicate, SSSOM row,
and aggregate row pass; only stale advisory rows remain.

## Identity

- Reviewed record:
  `data/ingredients/mapped/3-methyl-2-oxopentanoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:35932` with
  `ontology_mapping.ontology_id: CHEBI:35932`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:35932` resolves to
  `3-methyl-2-oxovaleric acid`, IUPAC `3-methyl-2-oxopentanoic acid`, CAS
  `1460-34-0`, formula `C6H10O3`, InChI
  `InChI=1S/C6H10O3/c1-3-4(2)5(7)6(8)9/h4H,3H2,1-2H3,(H,8,9)`, and SMILES
  `CCC(C)C(=O)C(=O)O`; the record matches.
- The record and mapping correctly model the neutral, stereochemically
  unspecified acid, not the `3-methyl-2-oxovalerate` anion or a stereoisomer.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-hydroxybutyric_Acid.yaml data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml data/ingredients/mapped/3-methyl-1-butanol.yaml data/ingredients/mapped/3-methyl-2-butenol.yaml data/ingredients/mapped/3-methyl-2-oxopentanoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-hydroxybutyric_Acid.yaml data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml data/ingredients/mapped/3-methyl-1-butanol.yaml data/ingredients/mapped/3-methyl-2-butenol.yaml data/ingredients/mapped/3-methyl-2-oxopentanoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:3-methyl-2-oxopentanoic_Acid` to `CHEBI:35932` row.

## Evidence

- CultureBotHT supplied CAS `1460-34-0`; ChEBI confirms that this CAS belongs to
  the same `C6H10O3` neutral acid structure.
- The August `CAS_RN_LOOKUP` regrade is correct: the source identity was
  established by explicit CAS lookup, and Rule D still emits an own-identifier
  `skos:exactMatch`.
- The batch P2 label warning is a false positive here because the preferred term
  is the ChEBI IUPAC name for `CHEBI:35932`.
- Stale: `mappings/record_research_validation.tsv` still requests direct ChEBI
  verification that has now been performed.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, generated docs, stale advisory rows,
  and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, and SMILES are populated and describe the same neutral
  acid.
- The duplicate exact synonym equal to the preferred term is redundant but
  harmless.
- There are no role, component, environment, or discussion entries requiring
  record-local review.

## Recommended Edits

No YAML edit is required for this record. The stale advisory rows can be ignored
or refreshed when `mappings/record_research_validation.tsv` is rebuilt.
