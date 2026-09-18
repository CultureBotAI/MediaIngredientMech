# `data/ingredients/mapped/4-Cresol.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:17847` synonym grounding and restored
CultureMech occurrence evidence pass, but the residual record still lacks
`ingredient_type` and `chemical_properties`.

## Identity

- Reviewed record: `data/ingredients/mapped/4-Cresol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17847` with
  `ontology_mapping.ontology_id: CHEBI:17847`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:17847` resolves to `p-cresol`, formula `C7H8O`,
  SMILES `Cc1ccc(O)cc1`, and InChI `InChI=1S/C7H8O/c1-6-2-4-7(8)5-3-6/h2-5,8H,1H3`.
- The `4-Cresol` source string is an exact synonym of the `p-cresol` ChEBI
  record.
- The record preserves 2 total occurrences in 2 CultureMech media and
  structured `ontology_mapping.evidence` restored from the creation history.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Amino-5-hydroxymethyl-2-methylpyrimidine.yaml data/ingredients/mapped/4-Anisaldehyde.yaml data/ingredients/mapped/4-Cresol.yaml data/ingredients/mapped/4-Deoxypyridoxine.yaml data/ingredients/mapped/4-Hydroxyacetophenone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Amino-5-hydroxymethyl-2-methylpyrimidine.yaml data/ingredients/mapped/4-Anisaldehyde.yaml data/ingredients/mapped/4-Cresol.yaml data/ingredients/mapped/4-Deoxypyridoxine.yaml data/ingredients/mapped/4-Hydroxyacetophenone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-Cresol` to `CHEBI:17847` row with
  `MIM:culturemech:output/ingredient_occurrences.tsv` in `source`.

## Evidence

- The CHEBI exact-synonym grounding is valid for the CultureMech source string.
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

- The record is traceable to two CultureMech residual occurrences.
- Mapping evidence exists on the structured field consumed by SSSOM generation.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

1. Add `ingredient_type: SINGLE_INGREDIENT`.
2. Populate `chemical_properties` from `CHEBI:17847`.
3. Consider adding `4-Cresol` as an exact synonym if the project wants the
   CultureMech surface form retained separately from `preferred_term`.
4. Run `just sync-curated`, rebuild docs as needed, then verify with
   `just validate-all` and `just validate-terms data/ingredients/mapped/4-Cresol.yaml`.
