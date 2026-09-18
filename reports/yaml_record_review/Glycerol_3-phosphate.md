# `data/ingredients/mapped/Glycerol_3-phosphate.yaml`

## Verdict

Needs curation. The MicrobeDecoder close match to biological
`CHEBI:15978` sn-glycerol 3-phosphate was explicitly documented, but the final
SSSOM row exports plain glycerol labels as `other` synonyms on the phosphate
record.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycerol_3-phosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:15978` with matching
  `ontology_mapping.ontology_id`, canonical label `sn-glycerol 3-phosphate`,
  source `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gly-Glu.yaml data/ingredients/mapped/Glycerate.yaml data/ingredients/mapped/Glycerol.yaml data/ingredients/mapped/Glycerol_2.yaml data/ingredients/mapped/Glycerol_3-phosphate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Gly-Glu.yaml data/ingredients/mapped/Glycerate.yaml data/ingredients/mapped/Glycerol.yaml data/ingredients/mapped/Glycerol_2.yaml data/ingredients/mapped/Glycerol_3-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI close match, stale top-level note, raw restored glycerol
  synonyms, one CultureMech occurrence, and singleton type as the per-record
  YAML.
- OLS4 resolves `CHEBI:15978` as `sn-glycerol 3-phosphate`, matching the YAML
  `ontology_mapping`.
- The #213 promotion evidence explicitly records the intended close match: the
  source label says `Glycerol 3-phosphate`, while the ChEBI term fixes the
  biological stereoisomer.
- Major: the final `mappings/ingredient_mappings.sssom.tsv` row exports `Gro`,
  `glycerolum`, and `glycyl alcohol` in `other`. Those are plain glycerol
  labels restored by `claude_sssom_surface_form_backfill`, not synonyms for
  glycerol 3-phosphate.
- Minor: top-level `notes` still carry the original MicrobeDecoder import text
  and say curator review is needed even though the record has been promoted,
  classified, had occurrences refreshed, and exported.
- Minor: `chemical_properties` is absent even though the close-matched ChEBI
  phosphate term has a structure.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, final SSSOM
  row, hydrate/salt sibling records grounded to glycerol-phosphate parents,
  generated indexes, old batch validation reports, and ignored aggregate
  backups.

## Completeness

- The close ChEBI identity, MicrobeDecoder source occurrence, CultureMech
  occurrence count, ingredient type, and final SSSOM row are populated.
- Plain glycerol surface forms need to be removed, and structure properties
  need backfill.

## Recommended Edits

- Major: change `Gro`, `glycerolum`, and `glycyl alcohol` in
  `data/ingredients/mapped/Glycerol_3-phosphate.yaml` to provenance-only text
  or make `src/mediaingredientmech/synonym_policy.py` filter plain glycerol
  labels for this phosphate record before rebuilding final SSSOM.
- Minor: refresh the stale top-level `notes`.
- Minor: backfill `chemical_properties` from `CHEBI:15978`.
