# `data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:39912` grounding, corrected occurrence
statistics, and restored CultureMech occurrence evidence pass, but the residual
record still lacks `ingredient_type` and `chemical_properties`.

## Identity

- Reviewed record: `data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:39912` with
  `ontology_mapping.ontology_id: CHEBI:39912`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:39912` resolves to
  `3,5-dihydroxybenzoic acid`, formula `C7H6O4`, SMILES
  `O=C(O)c1cc(O)cc(O)c1`, and InChI
  `InChI=1S/C7H6O4/c8-5-1-4(7(10)11)2-6(9)3-5/h1-3,8-9H,(H,10,11)`.
- The current record preserves 1 total occurrence in 1 CultureMech medium; the
  `refresh_occurrence_statistics` history explains the change from the older
  residual-import count.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml data/ingredients/mapped/36-Dihydroxyflavone.yaml data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml data/ingredients/mapped/36-Dihydroxyflavone.yaml data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:35-Dihydroxybenzoic_acid` to `CHEBI:39912` row with
  `MIM:culturemech:output/ingredient_occurrences.tsv` in `source`.

## Evidence

- The CHEBI canonical-label grounding is valid for the CultureMech source
  string.
- The September restore fixed the important provenance loss by putting the
  CultureMech residual occurrence table into `ontology_mapping.evidence`, where
  the SSSOM builder can read it.
- Minor: this residual record still lacks `ingredient_type: SINGLE_INGREDIENT`.
- Minor: the ChEBI formula, SMILES, InChI, and molecular mass are available but
  have not been copied into `chemical_properties`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, CultureMech residual grounding rows,
  generated docs, and ignored aggregate backups.

## Completeness

- The corrected current occurrence count is traceable in history.
- Mapping evidence exists on the structured field consumed by SSSOM generation.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

1. Add `ingredient_type: SINGLE_INGREDIENT`.
2. Populate `chemical_properties` from `CHEBI:39912`.
3. Run `just sync-curated`, rebuild docs as needed, then verify with
   `just validate-all` and
   `just validate-terms data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml`.
