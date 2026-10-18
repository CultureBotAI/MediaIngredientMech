# `data/ingredients/mapped/Bis-4-nitrophenyl-phosphorylcholine.yaml`

## Verdict

Needs curation, minor. The `kgmicrobe.compound` fallback identity,
MicrobeDecoder source occurrence, registry SSSOM row, and aggregate copy agree,
but top-level `notes` still say curator review is needed.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Bis-4-nitrophenyl-phosphorylcholine.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:bis-4-nitrophenyl-phosphorylcholine` with the
  same `ontology_mapping.ontology_id`,
  `ontology_label: Bis-4-nitrophenyl-phosphorylcholine`,
  `ontology_source: kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- Live OLS exact search for `Bis-4-nitrophenyl-phosphorylcholine` returned 0
  results across OLS, so no obvious exact external ontology term has superseded
  the local registry identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py 'data/ingredients/mapped/Bis(2-ethylhexyl)phthalate.yaml' data/ingredients/mapped/Bis-4-nitrophenyl-phenyl_Phosphonate.yaml data/ingredients/mapped/Bis-4-nitrophenyl-phosphorylcholine.yaml data/ingredients/mapped/Bis-4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/Bis-tris.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Engine A term validation is intentionally skipped for this record because
  `kgmicrobe.compound` has no OBO adapter; the registry identity is covered by
  strict schema validation and the SSSOM invariant check.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the MicrobeDecoder raw label in
  `data/custom/microbedecoder/unmapped_labels.tsv`, the fallback-registry SSSOM
  row at `mappings/ingredient_mappings.sssom.tsv` row 603, the Edison
  validation row recording that the registry fallback agrees, and the aggregate
  copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Bis-4-nitrophenyl-phosphorylcholine` to
  `kgmicrobe.compound:bis-4-nitrophenyl-phosphorylcholine` with
  `skos:exactMatch`, which is the registry/identity shape required for a
  locally minted primary ID.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The local registry identifier, raw MicrobeDecoder synonym, source occurrence
  count, fallback SSSOM row, and aggregate copy are populated.
- Minor gap: top-level `notes` still say curator review was needed even though
  the record now has a reviewed `FALLBACK_REGISTRY` mapping.

## Recommended Edits

- Minor: replace the stale import note in
  `data/ingredients/mapped/Bis-4-nitrophenyl-phosphorylcholine.yaml` with a
  current note that records the reviewed fallback-registry decision, then run
  `just sync-curated` and focused strict validation.
