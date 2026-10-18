# `data/ingredients/mapped/Andrographolide.yaml`

## Verdict

Pass. The exact `CHEBI:65408` identity, CAS, formula, exact ChEBI synonym,
row-review confirmation, SSSOM row, aggregate copy, and zero CultureMech
memberships agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Andrographolide.yaml`.
- Identifier and grounding: `identifier: CHEBI:65408` with
  `ontology_mapping.ontology_id: CHEBI:65408`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:65408` to
  `andrographolide` with formula `C20H30O5`, the stored SMILES and InChI, and
  InChIKey `BOJKULTULYSRAS-OTESTREVSA-N`; local OAK records CAS `5508-58-7`.
- The stored long structural synonym is an exact ChEBI synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Andrographolide.yaml data/ingredients/mapped/Anethole.yaml data/ingredients/mapped/Angolamycin.yaml data/ingredients/mapped/Angustmycin.yaml data/ingredients/mapped/Anhydrotetracycline_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Andrographolide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:65408 CHEBI:2716 CHEBI:8612 CHEBI:201752`:
  returned canonical `andrographolide` and the stored exact structural synonym
  for `CHEBI:65408`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:65408 CHEBI:2716 CHEBI:8612 CHEBI:201752`:
  returned the CAS, formula, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:65408`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Andrographolide` to `CHEBI:65408` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no action was
  required in that row-review pass.
- `mappings/ingredient_mappings.sssom.tsv` row 425 maps
  `MIM:Andrographolide` to `CHEBI:65408` with `skos:exactMatch`, the exact
  structural synonym, CAS `5508-58-7`, and the `CONFIRMED` trailer.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, CultureMech memberships, and batch
  review reports found the active YAML, aggregate copy, exact SSSOM row, and no
  `culturemech_recipe_membership.tsv` rows for `CHEBI:65408`.

## Completeness

- CAS, formula, SMILES, InChI, exact structural synonym, curation history, and
  `ingredient_type` are populated.
- No component, role, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

None.
