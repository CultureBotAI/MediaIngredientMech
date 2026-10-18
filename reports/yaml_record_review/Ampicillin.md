# `data/ingredients/mapped/Ampicillin.yaml`

## Verdict

Needs curation. The exact `CHEBI:28971` identity, CAS conflict resolution,
chemistry, 23 CultureMech memberships, source-backed selective-agent role,
row-review confirmation, and SSSOM row pass, but the record still stores
CultureMech role/property metadata strings as synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Ampicillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:28971` with
  `ontology_mapping.ontology_id: CHEBI:28971`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:28971` to `ampicillin`
  with formula `C16H19N3O4S`, the stored SMILES and InChI, and InChIKey
  `AVKUERGKIZMTKX-NJBDSQKTSA-N`.
- The stored CAS `69-53-4` is ChEBI's CAS xref for ampicillin; curation history
  records that a conflicting sodium-salt CAS `69-52-3` was resolved via the OAK
  canonical xref.
- `kg_microbe_node_id: CHEBI:28971` and `ingredient_type: SINGLE_INGREDIENT`
  are present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Amphotericin_A.yaml data/ingredients/mapped/Amphotericin_B.yaml data/ingredients/mapped/Ampicillin.yaml data/ingredients/mapped/Ampicillin_Sodium_Salt.yaml data/ingredients/mapped/Amygdalin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ampicillin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:2682 CHEBI:28971 CHEBI:34535 CHEBI:27613`:
  returned canonical `ampicillin`, the exact structural synonym, and ChEBI
  related synonyms for `CHEBI:28971`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:2682 CHEBI:28971 CHEBI:34535 CHEBI:27613`:
  returned the CAS, formula, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:28971`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Ampicillin` to `CHEBI:28971` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no action was
  required in that row-review pass.
- `mappings/culturemech_recipe_membership.tsv` contains exactly 23
  `CHEBI:28971` rows, matching `occurrence_statistics.total_occurrences: 23`.
- `mappings/ingredient_mappings.sssom.tsv` row 414 maps `MIM:Ampicillin` to
  `CHEBI:28971` with `skos:exactMatch`, CAS `69-53-4`, exact and related ChEBI
  aliases, and the `CONFIRMED` trailer.
- The `SELECTIVE_AGENT` role is backed by a CultureMech database entry and
  cites the original source role text instead of a name-pattern rule.
- Four `RAW_TEXT` synonyms are `Role: Antimicrobial agent; Properties: ...`
  strings that encode CultureMech role/property metadata rather than labels for
  ampicillin.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, CultureMech membership rows, SSSOM and row-review TSVs, and
  residual-triage rows found the active YAML, aggregate copy, 23 CultureMech
  memberships, the `Ampicillin (50 mg/ml)` residual alias, and the exact SSSOM
  row.

## Completeness

- CAS, formula, SMILES, InChI, occurrence statistics, source-backed role
  evidence, curation history, `kg_microbe_node_id`, and `ingredient_type` are
  populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The CultureMech role/property strings in `synonyms` remain the consequential
  active gap.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the raw metadata synonyms.

## Recommended Edits

- In `data/ingredients/mapped/Ampicillin.yaml`, remove the four
  `Role: Antimicrobial agent; Properties: ...` strings from `synonyms`.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Ampicillin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
