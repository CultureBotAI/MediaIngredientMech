# `data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml`

## Verdict

Pass with minor issues. The record now correctly preserves the CAS salt as the
exact identity and uses `CHEBI:16763` only as a narrow parent; only optional salt
chemistry enrichment and stale advisory rows remain.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:2013-26-5` with
  `ontology_mapping.ontology_id: CHEBI:16763`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- The primary identity remains the registry-backed sodium salt because no exact
  ChEBI term exists for `2-oxobutyric acid sodium salt`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:16763`
  resolves to the anion parent `2-oxobutanoate`, so the current
  `skos:narrowMatch` direction from the sodium salt to the anion parent is the
  intended non-exact relation.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-oxobutanoate.yaml data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml data/ingredients/mapped/2-oxopentanoate.yaml data/ingredients/mapped/2-pentyl-furan.yaml data/ingredients/mapped/2-propanolCO2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected non-exact
  `MIM:2-oxobutyric_Acid_Sodium_Salt` to `CHEBI:16763` `skos:narrowMatch` row,
  exact registry rows for `cas:2013-26-5` and
  `kgmicrobe.compound:2-oxobutyric_acid_sodium_salt`, and the
  `Sodium 2-oxobutyrate` exact synonym.

## Evidence

- The old P1 problem was the generic parent `CHEBI:26714` / `sodium salt`;
  active YAML and SSSOM now use `CHEBI:16763` / `2-oxobutanoate` instead.
- The current CAS-primary model correctly says that ChEBI contributes a parent,
  not an exact external identifier for the whole sodium salt.
- Stale: `mappings/record_research_validation.tsv` still contains P1/P2 rows
  against the old `CHEBI:26714` parent and a P3 fallback row recommending
  `UNMAPPED`; those predate the #322 regrounding and exact registry-row repair.
- Stale: the July `ingredient_mappings_oak_ols_review.tsv` row suggested
  enriching the generic `CHEBI:26714` parent with `Sodium 2-oxobutyrate`; the
  synonym is now represented on the CAS-primary salt record and the parent is no
  longer generic.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN is populated for the active sodium-salt identity.
- Formula/InChI/SMILES for the exact sodium salt remain absent. That would be
  useful enrichment but not an identity blocker now that the record no longer
  copies anion chemistry onto the salt.

## Recommended Edits

1. No identity or parent-mapping edit is required for
   `data/ingredients/mapped/2-oxobutyric_Acid_Sodium_Salt.yaml`.
2. Optionally backfill exact sodium-salt formula and structure from an
   inspected registry source.
3. When stale advisory TSVs are next regenerated, confirm the old
   `CHEBI:26714` rows drop out for this record.
