# `data/ingredients/mapped/Anthracycline_Antibiotic.yaml`

## Verdict

Pass. The record intentionally represents the ChEBI class
`anthracycline antibiotic`, the MicrobeDecoder raw class label matches that
scope exactly, and the class-level SSSOM row and aggregate copy are
synchronized.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Anthracycline_Antibiotic.yaml`.
- Identifier and grounding: `identifier: CHEBI:49322` with
  `ontology_mapping.ontology_id: CHEBI:49322`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and EBI OLS resolve `CHEBI:49322` to non-obsolete ChEBI
  `anthracycline antibiotic`, a class with definition, alternative IDs, and
  related synonyms `anthracycline antibiotics` and `anthracyclines`.
- The missing formula and structure fields are correct for this class-level
  import; the record does not assert a member anthracycline as the whole.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Anisodamine_Hydrobromide.yaml data/ingredients/mapped/Anthracene.yaml data/ingredients/mapped/Anthracycline_Antibiotic.yaml data/ingredients/mapped/Anthranilamide.yaml data/ingredients/mapped/Anthranilic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anthracycline_Antibiotic.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:35298 CHEBI:49322 CHEBI:193638 CHEBI:30754`:
  returned the `CHEBI:49322` label, definition, alternative IDs, and ChEBI
  namespace.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:35298 CHEBI:49322 CHEBI:193638 CHEBI:30754`:
  returned the canonical `anthracycline antibiotic` label and related ChEBI
  synonyms.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:anthracycline_antibiotic` with raw label
  `anthracycline antibiotic`, source column `BacDive_Metabolite_production`,
  and count 1, matching the record `source_occurrences` entry.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the
  `Anthracycline_Antibiotic.yaml` import against `CHEBI:49322`; the record
  history preserves the PENDING_REVIEW hold and later `review-ingredients`
  promotion.
- `mappings/ingredient_mappings.sssom.tsv` row 434 maps
  `MIM:Anthracycline_Antibiotic` to `CHEBI:49322` with `skos:exactMatch`,
  `manual:review-ingredients`, and `APPROVED`.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, and `scripts` found the active YAML, aggregate copy, SSSOM row,
  MicrobeDecoder review row, and the raw ignored MicrobeDecoder source row.

## Completeness

- The source occurrence, ChEBI class grounding, SSSOM row, aggregate copy, and
  review history are populated.
- Chemical properties and components are correctly absent because
  `CHEBI:49322` is a chemical class, not a single fixed formula or stock
  mixture.
- No role, environmental context, discussion, or dataset entry is needed.

## Recommended Edits

- None.
