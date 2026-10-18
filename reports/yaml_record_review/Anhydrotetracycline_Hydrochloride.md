# `data/ingredients/mapped/Anhydrotetracycline_Hydrochloride.yaml`

## Verdict

Needs curation. The exact `CHEBI:201752` identity, chemistry, exact structural
synonym, row-review confirmation, SSSOM row, and aggregate copy pass, but the
active record has an unsupported provisional `SELECTIVE_AGENT` role inferred
from the name pattern.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Anhydrotetracycline_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:201752` with
  `ontology_mapping.ontology_id: CHEBI:201752`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:201752` to
  `Anhydrotetracycline hydrochloride` with formula `C22H22N2O7.HCl`, the stored
  SMILES and InChI, and InChIKey `SPFAOPCHYIJPHJ-UHFFFAOYSA-N`.
- The stored long structural synonym is an exact ChEBI synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Andrographolide.yaml data/ingredients/mapped/Anethole.yaml data/ingredients/mapped/Angolamycin.yaml data/ingredients/mapped/Angustmycin.yaml data/ingredients/mapped/Anhydrotetracycline_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anhydrotetracycline_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:65408 CHEBI:2716 CHEBI:8612 CHEBI:201752`:
  returned canonical `Anhydrotetracycline hydrochloride` and the stored exact
  structural synonym for `CHEBI:201752`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:65408 CHEBI:2716 CHEBI:8612 CHEBI:201752`:
  returned the formula, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:201752`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Anhydrotetracycline_Hydrochloride` to `CHEBI:201752` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no action was
  required in that row-review pass.
- `mappings/ingredient_mappings.sssom.tsv` row 429 maps
  `MIM:Anhydrotetracycline_Hydrochloride` to `CHEBI:201752` with
  `skos:exactMatch`, the exact structural synonym, CAS `13803-65-1`, and the
  `CONFIRMED` trailer.
- The only role is a `SELECTIVE_AGENT` computational prediction inferred from a
  curated name-pattern rule; no medium or source claim demonstrates that
  anhydrotetracycline hydrochloride was curated as a selective agent in this
  record.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, CultureMech memberships, and batch
  review reports found the active YAML, aggregate copy, exact SSSOM row,
  row-review confirmation, and no `culturemech_recipe_membership.tsv` rows for
  `CHEBI:201752`.

## Completeness

- CAS, formula, SMILES, InChI, exact structural synonym, curation history, and
  `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The unsupported selective-agent role is the only active gap.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the provisional role.

## Recommended Edits

- In `data/ingredients/mapped/Anhydrotetracycline_Hydrochloride.yaml`, replace
  the `SELECTIVE_AGENT` computational prediction with source-backed evidence,
  or remove it.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anhydrotetracycline_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
