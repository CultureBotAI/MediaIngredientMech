# `data/ingredients/mapped/Ammonium_Sulfamate.yaml`

## Verdict

Pass. The exact `CHEBI:81950` identity, CAS cross-reference, ChEBI chemistry,
row-review confirmation, SSSOM row, aggregate copy, and zero CultureMech
memberships agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Ammonium_Sulfamate.yaml`.
- Identifier and grounding: `identifier: CHEBI:81950` with
  `ontology_mapping.ontology_id: CHEBI:81950`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:81950` to
  `Ammonium sulfamate` with formula `H2NO3S.H4N`, CAS `7773-06-0`, SMILES
  `NS(=O)(=O)[O-].[NH4+]`, and InChIKey `GEHMBYLTCISYNY-UHFFFAOYSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ammonium_Sulfamate.yaml data/ingredients/mapped/Ammonium_Sulfide_Solution.yaml data/ingredients/mapped/Ammonium_Sulfite_Monohydrate.yaml data/ingredients/mapped/Amoxicillin.yaml data/ingredients/mapped/Amphomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ammonium_Sulfamate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:81950 CHEBI:2676 CHEBI:201652`:
  returned canonical `Ammonium sulfamate` for `CHEBI:81950`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:81950 CHEBI:2676 CHEBI:201652`:
  returned the CAS, formula, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:81950`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Ammonium_Sulfamate` to `CHEBI:81950` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no action was
  required in that row-review pass.
- `mappings/ingredient_mappings.sssom.tsv` row 403 maps
  `MIM:Ammonium_Sulfamate` to `CHEBI:81950` with `skos:exactMatch`, CAS
  `7773-06-0`, and the `CONFIRMED` trailer.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, MicrobeDecoder imports, and hydrate
  review files found the active record, aggregate copy, exact SSSOM row, and
  no `culturemech_recipe_membership.tsv` rows for `CHEBI:81950`.

## Completeness

- CAS, formula, SMILES, InChI, curation history, and `ingredient_type` are
  populated.
- No synonym, component, role, environmental context, discussion, or dataset
  entry is needed.
- `occurrence_statistics.total_occurrences: 0` is consistent with a
  CultureBotHT-only FEBA/Hans80 import with no CultureMech recipe memberships.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

None.
