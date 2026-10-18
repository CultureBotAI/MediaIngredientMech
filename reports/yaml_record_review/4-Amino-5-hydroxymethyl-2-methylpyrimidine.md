# `data/ingredients/mapped/4-Amino-5-hydroxymethyl-2-methylpyrimidine.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:16892` grounding and restored
CultureMech occurrence evidence pass, but the residual record still lacks
`ingredient_type` and `chemical_properties`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-Amino-5-hydroxymethyl-2-methylpyrimidine.yaml`.
- Identifier and grounding: `identifier: CHEBI:16892` with
  `ontology_mapping.ontology_id: CHEBI:16892`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `match_level: EXACT`, and
  `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:16892` resolves to
  `4-amino-5-hydroxymethyl-2-methylpyrimidine`, formula `C6H9N3O`, SMILES
  `Cc1ncc(CO)c(N)n1`, and InChI
  `InChI=1S/C6H9N3O/c1-4-8-2-5(3-10)6(7)9-4/h2,10H,3H2,1H3,(H2,7,8,9)`.
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
  same exact `MIM:4-Amino-5-hydroxymethyl-2-methylpyrimidine` to `CHEBI:16892`
  row with `MIM:culturemech:output/ingredient_occurrences.tsv` in `source`.

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

- The record is traceable to two CultureMech residual occurrences.
- Mapping evidence exists on the structured field consumed by SSSOM generation.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

1. Add `ingredient_type: SINGLE_INGREDIENT`.
2. Populate `chemical_properties` from `CHEBI:16892`.
3. Run `just sync-curated`, rebuild docs as needed, then verify with
   `just validate-all` and
   `just validate-terms data/ingredients/mapped/4-Amino-5-hydroxymethyl-2-methylpyrimidine.yaml`.
