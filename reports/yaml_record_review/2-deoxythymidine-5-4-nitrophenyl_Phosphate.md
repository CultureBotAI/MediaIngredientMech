# `data/ingredients/mapped/2-deoxythymidine-5-4-nitrophenyl_Phosphate.yaml`

## Verdict

Needs curation, minor. The local fallback identity is internally synchronized
and valid, but the top-level `notes` field still describes the obsolete
pre-promotion unmapped state.

## Identity

- Reviewed record:
  `data/ingredients/mapped/2-deoxythymidine-5-4-nitrophenyl_Phosphate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:2-deoxythymidine-5-4-nitrophenyl_phosphate`
  with the same `ontology_mapping.ontology_id`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The record intentionally uses a local `kgmicrobe.compound` mint because the
  #213 curation searched CHEBI, NCIT, FOODON, ENVO, BTO, UBERON, and live OLS4
  without finding a term for this exact substance.
- The four non-media `microbedecoder` occurrences are represented under
  `occurrence_statistics.source_occurrences`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-deoxyinosine.yaml data/ingredients/mapped/2-deoxythymidine-5-4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/2-deoxyuridine.yaml data/ingredients/mapped/2-dichloroethane.yaml data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/2-deoxythymidine-5-4-nitrophenyl_Phosphate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  skipped as expected because `kgmicrobe.compound` is not an OBO-backed prefix
  for Engine A.
- Whole-corpus checks run earlier in this review pass passed, including the
  Engine B id/label product gate; only the shared evidence validator was
  unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-deoxythymidine-5-4-nitrophenyl_Phosphate` to
  `kgmicrobe.compound:2-deoxythymidine-5-4-nitrophenyl_phosphate` row.

## Evidence

- The #213 fallback rationale is placed directly on `ontology_mapping.evidence`
  and explains why the exact local mint was used instead of a class-level
  overclaim.
- `mappings/record_research_validation.tsv` classifies the old Edison UNMAPPED
  recommendation as `REGISTRY_FALLBACK_AGREES`, so that row is not an active
  identity dispute.
- Stale: top-level `notes` still say no CAS-RN or CHEBI/NCIT match existed and
  curator review was needed, even though the record was promoted to a
  fallback-registry mapped record on 2026-08-06.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the active YAML/aggregate/SSSOM rows, sibling 4-nitrophenyl records, and
  only stale local-CURIE findings from generated batch validators.

## Completeness

- The local identifier, source raw text, and source occurrence count are present.
- Empty component, role, and ChEBI chemistry slots are acceptable for this exact
  local compound fallback.

## Recommended Edits

1. In
   `data/ingredients/mapped/2-deoxythymidine-5-4-nitrophenyl_Phosphate.yaml`,
   replace the stale `notes` text with a concise statement that no external
   ontology term was found and the record was intentionally minted as a local
   `kgmicrobe.compound` fallback.
2. Run `just sync-curated`, `just validate-strict
   data/ingredients/mapped/2-deoxythymidine-5-4-nitrophenyl_Phosphate.yaml`,
   `just qc-sssom`, and `just qc-flat-coverage` after that curation edit.
