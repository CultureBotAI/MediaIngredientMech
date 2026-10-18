# `data/ingredients/mapped/Acetate_Carbon_Source.yaml`

## Verdict

Pass with minor issues. This record is intentionally a rejected tombstone after
`Acetate (carbon source)` was merged into the active `CHEBI:30089` acetate
record; the live pointer, aggregate copy, and absent SSSOM export pass, but
stale notes and advisory TSV rows still describe earlier pre-merge states.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetate_Carbon_Source.yaml`.
- Tombstone status: `mapping_status: REJECTED`.
- Current pointer: `identifier: CHEBI:30089` with
  `ontology_mapping.ontology_id: CHEBI:30089`, source `CHEBI`, and
  `mapping_quality: EXACT_MATCH`.
- The retained record, `data/ingredients/mapped/Acetate.yaml`, carries the
  active `CHEBI:30089` identity and owns the `Acetate (carbon source)` raw
  surface after the August 2026 merge.
- Local OAK and the official ChEBI page resolve `CHEBI:30089` to the acetate
  anion with formula `C2H3O2` and InChIKey
  `QTBSBXVTEAMEQO-UHFFFAOYSA-M`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetamide.yaml data/ingredients/mapped/Acetate.yaml data/ingredients/mapped/Acetate_Carbon_Source.yaml data/ingredients/mapped/Acetic_Acid.yaml data/ingredients/mapped/Acetoacetate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Acetate_Carbon_Source.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:27856 CHEBI:30089 CHEBI:15366 CHEBI:13705`:
  returned the expected ChEBI labels and synonyms for all four target ChEBI
  identifiers.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27856 CHEBI:30089 CHEBI:15366 CHEBI:13705`:
  returned formula and structure metadata for all four target ChEBI identifiers.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The `MERGED_INTO` curation event explains that the duplicate was merged into
  `CHEBI:30089` `Acetate`, occurrences were transferred, and SSSOM rows were
  dropped.
- The retained `Acetate` record has a matching `MERGED_FROM_MAPPED_RECORD`
  event and stores `Acetate (carbon source)` as a raw merged surface.
- Hidden/ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`
  found no active `MIM:Acetate_~28carbon_Source~29` row.
- The tombstone's top-level `notes` still say no CAS-RN or CHEBI/NCIT match was
  available and that curator review was needed; later history supersedes that
  statement with the normalized `CHEBI:30089` upgrade and rejection.
- Two advisory mapping-review TSVs still retain the old
  `MIM:Acetate_~28carbon_Source~29` rows; those rows are stale after the merge
  but do not currently re-export the tombstone.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the tombstone YAML,
  active retained YAML, alias row, stale row-review rows, stale cross-record
  baseline row, aggregate copies, and ignored aggregate backups.

## Completeness

- The tombstone is complete enough for a rejected duplicate: the active
  `Acetate` record owns the identity and the duplicate no longer exports an
  SSSOM row.
- The only non-live gaps are stale provenance notes and advisory review rows
  that predate the August 2026 merge.

## Recommended Edits

- Optionally refresh the stale top-level `notes` in
  `data/ingredients/mapped/Acetate_Carbon_Source.yaml` and derived
  row-review/cross-record tables so they no longer describe this tombstone as
  still pending mapping review. No tombstone, SSSOM, or ChEBI pointer edit is
  required.
