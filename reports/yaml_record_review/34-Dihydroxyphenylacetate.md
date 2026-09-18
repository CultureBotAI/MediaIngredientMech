# `data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml`

## Verdict

Needs curation, minor. The `CHEBI:17612` synonym grounding and restored
CultureMech occurrence evidence pass, but the record is still a sparse residual
import without `ingredient_type`, `chemical_properties`, or exact synonym
metadata.

## Identity

- Reviewed record: `data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17612` with
  `ontology_mapping.ontology_id: CHEBI:17612`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:17612` resolves to
  `(3,4-dihydroxyphenyl)acetate`, formula `C8H7O4`, net charge `-1`, SMILES
  `O=C([O-])Cc1ccc(O)c(O)c1`, and the stored anion InChI.
- ChEBI also lists `3,4-dihydroxyphenylacetate` as a UniProt name, supporting
  the CultureMech surface form as an exact synonym of this anion.
- The record preserves 1 CultureMech occurrence in 1 medium and structured
  `ontology_mapping.evidence` restored from the creation history.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-trehalosamine.yaml data/ingredients/mapped/3-trichloropropane.yaml data/ingredients/mapped/34-Dihydroxyflavone.yaml data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml data/ingredients/mapped/34-Dimethoxyflavone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-trehalosamine.yaml data/ingredients/mapped/3-trichloropropane.yaml data/ingredients/mapped/34-Dihydroxyflavone.yaml data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml data/ingredients/mapped/34-Dimethoxyflavone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:34-Dihydroxyphenylacetate` to `CHEBI:17612` row with
  `MIM:culturemech:output/ingredient_occurrences.tsv` in `source`.

## Evidence

- The CHEBI exact-synonym grounding is valid for the CultureMech source string.
- The September restore fixed the important provenance loss by putting the
  CultureMech residual occurrence table into `ontology_mapping.evidence`, where
  the SSSOM builder can read it.
- Minor: unlike neighboring chemically enriched CHEBI anions, this residual
  record still lacks `ingredient_type: SINGLE_INGREDIENT`.
- Minor: the ChEBI formula, net charge, SMILES, InChI, and molecular mass are
  available but have not been copied into `chemical_properties`.
- Minor: `3,4-dihydroxyphenylacetate` is the exact imported synonym, but
  `synonyms: []` means the alias is represented only by `preferred_term`, not as
  claim-level synonym metadata.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, CultureMech residual grounding rows,
  generated docs, and ignored aggregate backups.

## Completeness

- The record is traceable to one CultureMech residual occurrence.
- Mapping evidence exists on the structured field consumed by SSSOM generation.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

1. Add `ingredient_type: SINGLE_INGREDIENT`.
2. Populate `chemical_properties` from `CHEBI:17612` for the anion form already
   used by the exact mapping.
3. Consider adding `3,4-dihydroxyphenylacetate` as an exact synonym if the
   project wants the CultureMech surface form retained separately from
   `preferred_term`.
4. Run `just sync-curated`, rebuild docs as needed, then verify with
   `just validate-all` and
   `just validate-terms data/ingredients/mapped/34-Dihydroxyphenylacetate.yaml`.
