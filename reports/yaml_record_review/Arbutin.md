# `data/ingredients/mapped/Arbutin.yaml`

## Verdict

Pass. The record exactly denotes NCIT `Arbutin`, preserves the raw
MicrobeDecoder occurrence that introduced it, and the NCIT mapping, SSSOM row,
and aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Arbutin.yaml`.
- Identifier and grounding: `identifier: NCIT:C87429` with
  `ontology_mapping.ontology_id: NCIT:C87429`, `ontology_source: NCIT`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `NCIT:C87429` to non-obsolete NCIT `Arbutin`, CAS
  `497-76-7`, formula `C12H16O7`, a ChEBI xref, UNII `C5INA23HXF`, and exact
  NCIT synonyms including `4-Hydroxyphenyl-beta-D-Glucopyranoside`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arbutin.yaml data/ingredients/mapped/Ardacin_A.yaml data/ingredients/mapped/Ardacin_B.yaml data/ingredients/mapped/Ardacin_C.yaml data/ingredients/mapped/Arecoline_Hydrobromide.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arbutin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:ncit term-metadata NCIT:C87429 NCIT:C169786`:
  returned CAS, formula, ChEBI xref, and UNII metadata for `NCIT:C87429`.
- `uv run --frozen runoak -i sqlite:obo:ncit aliases NCIT:C87429 NCIT:C169786`:
  returned the canonical `Arbutin` label and exact NCIT synonyms for
  `NCIT:C87429`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:arbutin` with raw label `arbutin`, source column
  `BacDive_Metabolite_utilization`, and count 792, matching the record
  `source_occurrences` entry.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the `Arbutin.yaml`
  import against `NCIT:C87429`; the record history preserves the PENDING_REVIEW
  hold and later `review-ingredients` promotion.
- `mappings/ingredient_mappings.sssom.tsv` row 466 maps `MIM:Arbutin` to
  `NCIT:C87429` with `skos:exactMatch`, `manual:review-ingredients`, and
  `APPROVED`.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, generated docs, SSSOM row,
  MicrobeDecoder review row, and raw ignored MicrobeDecoder source row.

## Completeness

- NCIT identity, non-media source occurrence, curation history, SSSOM, and the
  aggregate copy are populated.
- Chemical properties are correctly absent because the record is NCIT-grounded
  and its NCIT target, not the local YAML, carries the CAS/formula metadata.
- No role, component, environmental context, discussion, or dataset entry is
  needed for this MicrobeDecoder import.

## Recommended Edits

- None.
