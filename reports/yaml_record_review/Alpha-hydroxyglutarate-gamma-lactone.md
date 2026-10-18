# `data/ingredients/mapped/Alpha-hydroxyglutarate-gamma-lactone.yaml`

## Verdict

Pass with minor issues. The local `kgmicrobe.compound` fallback identity is
intentional because the gamma-lactone is distinct from 2-hydroxyglutarate and
had no external ontology term in the checked namespaces; only the top-level
unmapped-import note still says curator review is needed.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Alpha-hydroxyglutarate-gamma-lactone.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:alpha-hydroxyglutarate-gamma-lactone` with
  the same `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The `#213` curation note deliberately kept this label off
  `CHEBI:132941`: a gamma-lactone is not a synonym of its parent acid.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alpha-Tocopherol.yaml data/ingredients/mapped/Alpha-aminobutyrate.yaml data/ingredients/mapped/Alpha-bisabolol.yaml data/ingredients/mapped/Alpha-d-glucose.yaml data/ingredients/mapped/Alpha-hydroxyglutarate-gamma-lactone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Alpha-hydroxyglutarate-gamma-lactone.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1, so `just validate-terms` would skip Engine A for this unsupported
  local `kgmicrobe.compound` prefix.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:alpha_hydroxyglutarate_gamma_lactone` in
  `BacDive_Metabolite_utilization` with count `1`, matching
  `source_occurrences`.
- `mappings/record_research_validation.tsv` classifies this record as
  `REGISTRY_FALLBACK_AGREES`: an Edison recommendation to keep the record
  unmapped was already represented by the local `kgmicrobe.compound` fallback.
- `mappings/ingredient_mappings.sssom.tsv` row 380 maps
  `MIM:Alpha-hydroxyglutarate-gamma-lactone` to the local
  `kgmicrobe.compound` ID with the expected
  `manual:promote_resolved_unmapped|PROMOTED|2026-08-06` trailer.
- The batch validator's P1 invalid-CURIE rows for this record are advisory for
  this review: local `kgmicrobe.compound` IDs intentionally do not resolve
  through the OBO Engine A adapter.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence,
  record-research validation row, generated indexes, and ignored aggregate
  backups.

## Completeness

- Mapping evidence, source occurrence, curation history, and local fallback
  identity are populated.
- CAS, formula, SMILES, and InChI are correctly absent because no external
  structure-bearing term or registry was curated.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The top-level `notes` field still repeats the original unmapped import text
  and ends with `Curator review needed`, even though the record has since been
  curated into a local fallback mapping.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Remove or replace the stale top-level `notes` in
  `data/ingredients/mapped/Alpha-hydroxyglutarate-gamma-lactone.yaml`; the
  append-only `CREATED_AS_UNMAPPED` history already preserves the original
  no-match import state.
- Optionally convert the `Alpha-hydroxyglutarate-gamma-lactone` raw synonym to
  a reviewed exact synonym or remove it as redundant with `preferred_term`.
