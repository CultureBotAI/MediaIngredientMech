# `data/ingredients/mapped/3-Hydroxypropionate.yaml`

## Verdict

Needs curation, major. The active `CHEBI:16510` anion identity is current, but
the record carries neutral-acid CAS `503-66-2` and `CARBON_SOURCE` is only
supported by provisional name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/3-Hydroxypropionate.yaml`.
- Identifier and grounding: `identifier: CHEBI:16510` with
  `ontology_mapping.ontology_id: CHEBI:16510`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:16510`
  resolves to `3-hydroxypropionate` and lists the anion formula `C3H5O3`.
- PubChem resolves the imported CAS `503-66-2` to neutral
  `3-hydroxypropanoic acid`, formula `C3H6O3`, SMILES `C(CO)C(=O)O`, and a
  neutral InChI, not to the deprotonated anion represented by `CHEBI:16510`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Hydroxypropanal.yaml data/ingredients/mapped/3-Hydroxypropionate.yaml data/ingredients/mapped/3-Methyl-2-Oxobutanoic_Acid.yaml data/ingredients/mapped/3-Methyl-2-oxobutanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/3-Methylcatechol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-Hydroxypropionate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-Hydroxypropionate` to `CHEBI:16510` row, but also exports the
  neutral-acid `CAS:503-66-2` value in the row's `other` field.

## Evidence

- The active ChEBI page and OAK/OLS review both confirm the exact anion
  identity.
- Major: `cas_rn: 503-66-2` and the generated CAS synonym point to the neutral
  acid, which has a different formula and protonation state from the current
  anion record.
- Major: `nutritional_roles.CARBON_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule.
- Stale: `mappings/record_research_validation.tsv` still contains a P2 row
  asking for direct confirmation that `CHEBI:16510` is the -1 anion; that direct
  ChEBI check now passes, while also confirming that the CAS is the wrong scope.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, and advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Formula, InChI, and SMILES are populated for the active anion identity.
- The residual issues are consequential because the SSSOM export publishes a
  neutral-acid CAS as a synonym of an anion and because the role assertion is
  still provisional.

## Recommended Edits

1. Remove `cas_rn: 503-66-2` from the anion record, or reground the record to
   the neutral acid if the source CAS is more authoritative than the anion
   source label.
2. Either remove `CARBON_SOURCE` or replace it with inspected
   formulation-specific evidence that directly supports this exact anion as a
   carbon source.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
4. Re-run the focused strict/LinkML validators, CAS/identity plausibility
   checks, role/evidence checks, `just qc-sssom`, and
   `just qc-flat-coverage` after those edits.
