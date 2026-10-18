# `data/ingredients/mapped/Amphotericin_B.yaml`

## Verdict

Needs curation. The exact `CHEBI:2682` identity, CAS, chemistry, 4 CultureMech
memberships, row-review confirmation, and SSSOM row pass, but the record exports
a liposomal formulation as an exact synonym, keeps CultureMech role metadata in
synonyms, and carries an unsupported provisional `SELECTIVE_AGENT` role.

## Identity

- Reviewed record: `data/ingredients/mapped/Amphotericin_B.yaml`.
- Identifier and grounding: `identifier: CHEBI:2682` with
  `ontology_mapping.ontology_id: CHEBI:2682`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:2682` to
  `amphotericin B` with formula `C47H73NO17`, CAS `1397-89-3`, the stored
  SMILES and InChI, and InChIKey `APKFDSVGJQXUKY-INPOYWNPSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Amphotericin_A.yaml data/ingredients/mapped/Amphotericin_B.yaml data/ingredients/mapped/Ampicillin.yaml data/ingredients/mapped/Ampicillin_Sodium_Salt.yaml data/ingredients/mapped/Amygdalin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amphotericin_B.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:2682 CHEBI:28971 CHEBI:34535 CHEBI:27613`:
  returned canonical `amphotericin B`, the exact structural synonym, and ChEBI
  related synonyms for `CHEBI:2682`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:2682 CHEBI:28971 CHEBI:34535 CHEBI:27613`:
  returned the CAS, formula, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:2682`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Amphotericin_B` to `CHEBI:2682` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no action was
  required in that row-review pass.
- `mappings/culturemech_recipe_membership.tsv` contains exactly 4
  `CHEBI:2682` rows, matching `occurrence_statistics.total_occurrences: 4`.
- `mappings/ingredient_mappings.sssom.tsv` row 413 maps
  `MIM:Amphotericin_B` to `CHEBI:2682` with `skos:exactMatch`, CAS
  `1397-89-3`, and the `CONFIRMED` trailer.
- `Liposomal Amphotericin B` is stored and exported as `EXACT_SYNONYM`; it
  denotes a liposomal formulation rather than the unformulated ChEBI molecular
  entity.
- `Role: Antimicrobial agent` is stored as a `RAW_TEXT` synonym even though it
  is CultureMech metadata, not a label for amphotericin B.
- The `SELECTIVE_AGENT` role is a computational prediction inferred from a
  curated name-pattern rule, not source-backed role evidence.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, CultureMech membership rows, SSSOM and row-review TSVs, and
  residual-triage rows found the active YAML, aggregate copy, 4 CultureMech
  memberships, the `Amphotericin B (5 mg/ml DMSO)` residual alias, and the
  exact SSSOM row.

## Completeness

- CAS, formula, SMILES, InChI, occurrence statistics, curation history, and
  `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The over-broad liposomal exact synonym, raw role synonym, and unsupported
  selective-agent role remain active gaps.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the synonym and role defects.

## Recommended Edits

- In `data/ingredients/mapped/Amphotericin_B.yaml`, remove or reject
  `Liposomal Amphotericin B` so a formulation is not exported as an exact
  synonym of `CHEBI:2682`.
- Remove the `Role: Antimicrobial agent` raw synonym from the synonym list.
- Replace the provisional `SELECTIVE_AGENT` assignment with source-backed
  evidence, or remove it.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amphotericin_B.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
