# `data/ingredients/mapped/3-nitropropanoate.yaml`

## Verdict

Needs curation, major. The exact anion mapping to `CHEBI:59899`, chemistry,
microbedecoder occurrence count, SSSOM row, and aggregate row pass, but the
record publishes neutral `3-nitropropanoic acid` as a `RAW_TEXT` synonym and
therefore as SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/3-nitropropanoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:59899` with
  `ontology_mapping.ontology_id: CHEBI:59899`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The direct microbedecoder `BacDive_Metabolite_utilization` count of 1 is
  preserved under `source_occurrences`.
- Formula `C3H4NO4`, InChI
  `InChI=1S/C3H5NO4/c5-3(6)1-2-4(7)8/h1-2H2,(H,5,6)/p-1`, and SMILES
  `O=C([O-])CC[N+](=O)[O-]` describe the same monoanion.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-methyl-3-butenol.yaml data/ingredients/mapped/3-nitropropanoate.yaml data/ingredients/mapped/3-octanone.yaml data/ingredients/mapped/3-phenylpropionate.yaml data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-methyl-3-butenol.yaml data/ingredients/mapped/3-nitropropanoate.yaml data/ingredients/mapped/3-octanone.yaml data/ingredients/mapped/3-phenylpropionate.yaml data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:3-nitropropanoate` to `CHEBI:59899` row.

## Evidence

- The ChEBI identity denotes the 3-nitropropanoate conjugate base, and the
  record's anion formula and structure agree.
- The older `microbedecoder_auto_mapped_review.tsv` row explicitly warned that
  its approval did not check for homonyms or wrong-sense matches. The anion
  structure review performed here closes the core identity gap for this record.
- Major: `3-nitropropanoic acid` is a neutral conjugate acid, not the
  `CHEBI:59899` anion. Keeping it as `RAW_TEXT` publishes that acid label
  through the SSSOM `other` field.
- Stale: `mappings/record_research_validation.tsv` still reports
  `ingredient_type` and `chemical_properties` as missing; both are now
  populated. Its occurrence-count concern is also stale because
  microbedecoder non-media source counts are intentionally stored in
  `source_occurrences` while `total_occurrences` and `media_count` remain 0.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, microbedecoder review row, generated
  docs, source import rows, stale advisory rows, and ignored aggregate backups.

## Completeness

- Formula, molecular weight, InChI, and SMILES are populated from ChEBI/PubChem.
- The direct microbedecoder occurrence is traceable.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

1. In `data/ingredients/mapped/3-nitropropanoate.yaml`, remove or reject the
   neutral-acid `3-nitropropanoic acid` `RAW_TEXT` synonym so it no longer ships
   as `other` for the anion.
2. Run `just sync-curated`, rebuild SSSOM and docs, then verify with
   `just validate-all`, `just qc-sssom`, `just qc-roundtrip`, and
   `just validate-terms data/ingredients/mapped/3-nitropropanoate.yaml`.
