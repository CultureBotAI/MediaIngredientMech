# `data/ingredients/mapped/TYGVS_Glucose.yaml`

## Verdict

Pass. `TYGVS + Glucose` is a MicrobeDecoder-specific undefined mixture with a
local ingredient fallback, partial component partonomy, synchronized aggregate
data, and one clean exact registry row in the final SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/TYGVS_Glucose.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:tygvs_glucose` with the same
  `ontology_mapping.ontology_id`, label `TYGVS + Glucose`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- Ingredient type: `UNDEFINED_MIXTURE`.
- Occurrences: zero CultureMech recipe occurrences and 1 MicrobeDecoder
  substrate row.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `TYGVS_Glucose` through `Takara_DO_Supp_MinusHisLeuTrp`: exited 0 and wrote
  zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this local
  `kgmicrobe.ingredient` fallback row because that prefix is intentionally
  outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `TYGVS + Glucose` returned zero results, and
  fresh PubChem name lookup found no CID.
- `data/custom/microbedecoder/unmapped_labels.tsv` preserves the imported
  `kgmicrobe.trait:tygvs_glucose` source label.
- `mappings/microbedecoder_residual_research_decomposition.tsv` records the
  maintained decomposition into trypticase peptone, yeast extract, glucose, and
  a volatile-fatty-acid mixture.
- The final SSSOM has exactly one exact registry row for
  `MIM:TYGVS_Glucose`, points at `kgmicrobe.ingredient:tygvs_glucose`, names
  `kgm:ingredient`, and publishes no unsafe `other` synonyms.

## Completeness

- The local identity, undefined-mixture type, aggregate row, source occurrence,
  and final SSSOM row agree mechanically.
- Four components are curated. Three resolve to existing cataloged MIM
  components, and the volatile-fatty-acid mixture intentionally remains an
  unmapped component in a partial decomposition with unknown completeness.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder source,
  residual decomposition, component-migration, aggregate, generated-docs, and
  final SSSOM rows.

## Recommended Edits

- None.
