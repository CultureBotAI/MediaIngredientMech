# `data/ingredients/mapped/Abyssomicin_D.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The exact MeSH grounding for
`Abyssomicin D` passes, but the first ontology evidence row still describes a
pre-promotion placeholder, the SSSOM trailer still says `UNKNOWN_TERM`, and the
selective-agent role is only a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Abyssomicin_D.yaml`.
- Identifier and grounding: `identifier: mesh:C512805` with
  `ontology_mapping.ontology_id: mesh:C512805`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- EBI OLS resolves `mesh:C512805` to `abyssomicin D`, agreeing with the record's
  preferred term and ontology label.
- The second ontology evidence row records the automatic label-exact upgrade
  from `kgmicrobe.compound:abyssomicin_d` to the MeSH term.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Abikoviromycin.yaml data/ingredients/mapped/Abscisic_Acid.yaml data/ingredients/mapped/Aburamycin_A.yaml data/ingredients/mapped/Abyssomicin_B.yaml data/ingredients/mapped/Abyssomicin_D.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Abyssomicin_D.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Prefix-specific OLS lookup resolves `mesh:C512805` exactly to
  `abyssomicin D`, matching the row-review triage result for this record.
- The first `ontology_mapping.evidence` entry is stale: it still says the
  `kgmicrobe.compound` placeholder is pending curator promotion, even though the
  live identifier and second evidence row record the promotion to MeSH.
- The SSSOM row maps `MIM:Abyssomicin_D` to `mesh:C512805` with
  `skos:exactMatch`, but its review trailer is still
  `none|UNKNOWN_TERM|2026-07-07` even though the triage row resolved the CURIE
  as an exact MeSH term.
- The `physicochemical_roles.SELECTIVE_AGENT` assertion is still sourced only
  to `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with no
  inspected Abyssomicin D support.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copy, SSSOM row, unknown-term
  triage row, and ignored aggregate backups.

## Completeness

- The exact MeSH mapping and the original kg-microbe provenance are populated.
- ChEBI, CAS, formula, and structure slots are acceptably empty because this
  record is grounded to MeSH rather than a structure-bearing ChEBI term.
- The consequential gaps are role evidence and stale evidence/export
  annotations left from the `UNKNOWN_TERM` promotion path.

## Recommended Edits

- Replace or remove
  `data/ingredients/mapped/Abyssomicin_D.yaml`'s
  `physicochemical_roles.SELECTIVE_AGENT` entry after inspecting evidence that
  specifically supports Abyssomicin D as a selective agent.
- Update `data/ingredients/mapped/Abyssomicin_D.yaml` so the first
  `ontology_mapping.evidence` row no longer describes the placeholder as
  pending promotion after the MeSH upgrade.
- Update the maintained SSSOM row-review/export input so
  `mappings/ingredient_mappings.sssom.tsv` no longer publishes
  `none|UNKNOWN_TERM|2026-07-07` for `mesh:C512805`.
- Re-run `scripts/validate_strict.py` and
  `scripts/validate_sssom_invariants.py`.
