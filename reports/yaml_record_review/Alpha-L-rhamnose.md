# `data/ingredients/mapped/Alpha-L-rhamnose.yaml`

## Verdict

Needs curation. The manual `CHEBI:27907` alpha-L-rhamnopyranose grounding,
MicrobeDecoder occurrence, ChEBI/PubChem chemistry, SSSOM row, and aggregate
copy pass, but the active record still carries stale unmapped-import prose that
says no CHEBI/NCIT match was found and curator review is needed.

## Identity

- Reviewed record: `data/ingredients/mapped/Alpha-L-rhamnose.yaml`.
- Identifier and grounding: `identifier: CHEBI:27907` with
  `ontology_mapping.ontology_id: CHEBI:27907`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:27907` to
  `alpha-L-rhamnopyranose` with formula `C6H12O5`, SMILES
  `C[C@@H]1O[C@@H](O)[C@H](O)[C@H](O)[C@H]1O`, and InChIKey
  `SHZGCJCMOBCMKK-HGVZOGFYSA-N`.
- ChEBI lists `alpha-L-rhamnose` as a related synonym of
  `alpha-L-rhamnopyranose`, matching the manual `#213` promotion rationale.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Allura_Red_AC.yaml data/ingredients/mapped/Aloin.yaml data/ingredients/mapped/Alpha-D-glucose_6-phosphate.yaml data/ingredients/mapped/Alpha-L-rhamnose.yaml data/ingredients/mapped/Alpha-Lactose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-L-rhamnose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:172687 CHEBI:73222 CHEBI:17665 CHEBI:27907 CHEBI:189432 CHEBI:36219`:
  returned canonical `alpha-L-rhamnopyranose` plus the expected rhamnose
  synonyms for `CHEBI:27907`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:172687 CHEBI:73222 CHEBI:17665 CHEBI:27907 CHEBI:189432 CHEBI:36219`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:27907`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:alpha_l_rhamnose` in `BacDive_Metabolite_utilization` with
  count `1`, matching `source_occurrences`.
- `mappings/record_research_validation.tsv` records the cross-lane resolution
  for `Alpha-L-rhamnose`: the Claude lane confirmed `CHEBI:27907`, the Edison
  UNMAPPED recommendation was resolved, and the missing chemistry report is now
  satisfied by the populated `chemical_properties`.
- `mappings/ingredient_mappings.sssom.tsv` row 374 maps
  `MIM:Alpha-L-rhamnose` to `CHEBI:27907` with `skos:exactMatch` and the
  expected `manual:promote_resolved_unmapped|PROMOTED|2026-08-06` trailer.
- The top-level `notes` field still repeats the original unmapped import text:
  no CAS-RN or CHEBI/NCIT match and curator review needed. That no longer
  matches the promoted `mapping_status`, `ontology_mapping`, or chemistry.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, record-research validation rows,
  MicrobeDecoder raw occurrence, generated indexes, and ignored aggregate
  backups.

## Completeness

- Formula, SMILES, InChI, source occurrence, curation history, manual promotion
  evidence, and `ingredient_type` are populated.
- No CAS, role, component, environmental context, discussion, or dataset entry
  is needed.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:27907` row, which
  is consistent with `occurrence_statistics.total_occurrences: 0` because the
  record is sourced from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Remove or replace the stale top-level `notes` in
  `data/ingredients/mapped/Alpha-L-rhamnose.yaml`; the append-only
  `CREATED_AS_UNMAPPED` history already preserves the original no-match import
  state.
- Optionally convert the `Alpha-L-rhamnose` raw synonym to a reviewed exact
  synonym or remove it as redundant with `preferred_term`.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-L-rhamnose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
