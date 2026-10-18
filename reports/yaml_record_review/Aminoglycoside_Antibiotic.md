# `data/ingredients/mapped/Aminoglycoside_Antibiotic.yaml`

## Verdict

Pass. The generic MicrobeDecoder antibiotic-sensitivity label maps exactly to
ChEBI's `aminoglycoside antibiotic` class, with a matching source occurrence,
review-ingredients approval, SSSOM row, and aggregate copy.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Aminoglycoside_Antibiotic.yaml`.
- Identifier and grounding: `identifier: CHEBI:22507` with
  `ontology_mapping.ontology_id: CHEBI:22507`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:22507` to the class `aminoglycoside antibiotic` and
  related synonym `aminoglycoside antibiotics`.
- The record denotes a ChEBI class of antibiotics rather than a concrete
  structure, so no `chemical_properties` are expected.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Aminoacids.yaml data/ingredients/mapped/Aminoglycoside_Antibiotic.yaml data/ingredients/mapped/Aminophenazone.yaml data/ingredients/mapped/Aminovalerate.yaml data/ingredients/mapped/Ammonia.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Aminoglycoside_Antibiotic.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:22507 CHEBI:160246 CHEBI:16134 CHEBI:28938`:
  returned canonical `aminoglycoside antibiotic` for `CHEBI:22507`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:22507 CHEBI:160246 CHEBI:16134`:
  returned the `CHEBI:22507` class label without structure metadata, as expected
  for an antibiotic class.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:aminoglycoside_antibiotic` in
  `BacDive_Antibiotic_sensitivity` with count `3`, matching
  `source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved
  `Aminoglycoside_Antibiotic.yaml` after `CHEBI:22507` resolved locally with
  canonical label `aminoglycoside antibiotic`.
- `mappings/ingredient_mappings.sssom.tsv` row 394 maps
  `MIM:Aminoglycoside_Antibiotic` to `CHEBI:22507` with `skos:exactMatch` and
  the expected review-ingredients `APPROVED` trailer.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence, review row,
  and generated reports.

## Completeness

- Source occurrence, mapping evidence, and curation history are populated.
- No CAS, structure, synonym, role, component, environmental context,
  discussion, or dataset entry is needed for the generic class.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:22507` row, which
  is consistent with `occurrence_statistics.total_occurrences: 0` because the
  record is sourced from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
