# `data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:566519` grounding and restored
CultureMech occurrence evidence pass, but the residual record still lacks
`ingredient_type` and `chemical_properties`.

## Identity

- Reviewed record: `data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:566519` with
  `ontology_mapping.ontology_id: CHEBI:566519`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:566519` resolves to
  `3,4,5-trimethoxycinnamic acid`, formula `C12H14O5`, SMILES
  `[H]C(=Cc1cc(OC)c(OC)c(OC)c1)C(=O)O`, and InChI
  `InChI=1S/C12H14O5/c1-15-9-6-8(4-5-11(13)14)7-10(16-2)12(9)17-3/h4-7H,1-3H3,(H,13,14)`.
- The record preserves 4 total occurrences in 4 CultureMech media and
  structured `ontology_mapping.evidence` restored from the creation history.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml data/ingredients/mapped/36-Dihydroxyflavone.yaml data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml data/ingredients/mapped/36-Dihydroxyflavone.yaml data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:345-Trimethoxycinnamic_acid` to `CHEBI:566519` row with
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

- The record is traceable to four CultureMech residual occurrences.
- Mapping evidence exists on the structured field consumed by SSSOM generation.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

1. Add `ingredient_type: SINGLE_INGREDIENT`.
2. Populate `chemical_properties` from `CHEBI:566519`.
3. Run `just sync-curated`, rebuild docs as needed, then verify with
   `just validate-all` and
   `just validate-terms data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml`.
