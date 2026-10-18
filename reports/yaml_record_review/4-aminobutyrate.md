# `data/ingredients/mapped/4-aminobutyrate.yaml`

## Verdict

Pass with minor issues, minor. The promoted `CHEBI:30566` GABA anion identity,
microbedecoder occurrence count, chemistry, SSSOM row, and aggregate row pass,
but stale pre-promotion import text remains in `notes`.

## Identity

- Reviewed record: `data/ingredients/mapped/4-aminobutyrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:30566` with
  `ontology_mapping.ontology_id: CHEBI:30566`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:30566` is active, resolves to
  `gamma-aminobutyrate`, has formula `C4H8NO2`, SMILES `NCCCC(=O)[O-]`, the
  stored InChI, and related synonym `4-aminobutyrate`.
- The #213 promotion note documents the positional and Greek locant equivalence
  between 4-aminobutyrate and gamma-aminobutyrate.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-acetoxyphenol.yaml data/ingredients/mapped/4-aminobenzoate.yaml data/ingredients/mapped/4-aminobutyrate.yaml data/ingredients/mapped/4-azido-L-phenylalanine.yaml data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-acetoxyphenol.yaml data/ingredients/mapped/4-aminobenzoate.yaml data/ingredients/mapped/4-aminobutyrate.yaml data/ingredients/mapped/4-azido-L-phenylalanine.yaml data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-aminobutyrate` to `CHEBI:30566` row.

## Evidence

- The manual #213 promotion, current ChEBI label/synonym set, formula, InChI,
  and SMILES support the GABA anion identity.
- `source_occurrences` correctly preserves the seven microbedecoder
  `BacDive_Metabolite_utilization` hits that led to this record; the
  CultureMech recipe counts are correctly zero.
- Minor: the top-level `notes` still say there was no CAS-RN or CHEBI/NCIT
  match and that curator review is needed. The record was later promoted to
  `CHEBI:30566`, so the old unmapped triage note is stale.
- Minor: `synonyms[0]` is a duplicate `RAW_TEXT` copy of the preferred term from
  the microbedecoder import. It is harmless and does not export in the SSSOM
  `other` field, but the active record no longer needs it.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, microbedecoder source rows, generated
  docs, stale advisory rows, and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, `ingredient_type`, and microbedecoder
  `source_occurrences` are populated.
- No CAS is asserted, which is fine for this ChEBI anion.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

Optionally replace the stale top-level `notes` with a post-promotion statement
or remove the note entirely, and drop the duplicate `RAW_TEXT` synonym.
