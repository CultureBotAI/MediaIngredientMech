# `data/ingredients/mapped/3-Chloro-L-tyrosine.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:53678` `3-chloro-L-tyrosine` identity,
chemistry, SSSOM row, and aggregate row pass, but `AMINO_ACID_SOURCE` is only
supported by provisional ChEBI-ancestry evidence and is contradicted by the
stale literature advisory for this record.

## Identity

- Reviewed record: `data/ingredients/mapped/3-Chloro-L-tyrosine.yaml`.
- Identifier and grounding: `identifier: CHEBI:53678` with
  `ontology_mapping.ontology_id: CHEBI:53678`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:53678`
  resolves to `3-chloro-L-tyrosine`, lists formula `C9H10ClNO3`, carries CAS
  `7423-93-0`, and matches the record formula, InChI, and SMILES.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Chloro-4-hydroxyphenylacetic_acid.yaml data/ingredients/mapped/3-Chloro-L-tyrosine.yaml data/ingredients/mapped/3-Chloroacrylic_acid.yaml data/ingredients/mapped/3-Hydroxydecanoic_Acid.yaml data/ingredients/mapped/3-Hydroxyhexanoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-Chloro-L-tyrosine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-Chloro-L-tyrosine` to `CHEBI:53678` row, with CAS `7423-93-0`
  represented in the SSSOM `other` field.

## Evidence

- The active ChEBI page and OAK/OLS review both confirm the exact L-isomer
  identity.
- `occurrence_statistics` reports `0/0`; the record came from CultureBotHT CAS
  input rather than a counted CultureMech recipe occurrence.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from ChEBI ancestry. The advisory
  literature row specifically disputes that interpretation and says the
  documented use was precursor feeding rather than routine nutritional
  complementation.
- Stale: the same `mappings/record_research_validation.tsv` section still asks
  for direct ChEBI verification; the direct ChEBI check now passes.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, and advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core chemistry is complete for the active ChEBI identity.
- The residual issue is consequential because the exported role facet asserts a
  biological media role from only broad class ancestry.

## Recommended Edits

1. Remove `AMINO_ACID_SOURCE`, or replace it with inspected
   formulation-specific evidence that directly supports this exact chlorinated
   tyrosine as an amino-acid source.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
3. Re-run the focused strict/LinkML validators, role/evidence checks,
   `just qc-sssom`, and `just qc-flat-coverage` after those edits.
