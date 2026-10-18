# `data/ingredients/mapped/Synanthrin.yaml`

## Verdict

Pass. The local `kgmicrobe.compound` fallback identity, MicrobeDecoder source
occurrence, aggregate row, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Synanthrin.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:synanthrin` with
  the same `ontology_mapping.ontology_id`, label `Synanthrin`, source
  `kgmicrobe.compound`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and no public-ontology parent.
- Chemical properties: absent, because the record lacks a CAS RN, CHEBI term,
  NCIT term, or PubChem CID.
- Occurrences: zero CultureMech recipe occurrences and 1 MicrobeDecoder
  metabolite-utilization row.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Supplemented_Seawater` through `Synephrine_Tartrate`: exited 0 and wrote
  zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this local
  `kgmicrobe.compound` fallback row because that prefix is intentionally
  outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `Synanthrin` returned zero results, and fresh
  PubChem name lookup found no CID.
- `data/custom/microbedecoder/unmapped_labels.tsv` preserves the single
  MicrobeDecoder import for `kgmicrobe.trait:synanthrin`.
- The local research-validation table explicitly rejected CAS `9005-80-5` as
  an unsuitable Synanthrin CAS transfer because it denotes inulin instead.
- The final SSSOM row exact-matches
  `kgmicrobe.compound:synanthrin`, uses `semapv:ManualMappingCuration`, and
  leaves `other` empty.

## Completeness

- The local fallback identity, aggregate row, MicrobeDecoder source occurrence,
  and final SSSOM row agree.
- The record has no components, roles, environmental contexts, datasets, or
  structure fields needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder,
  no-ontology fallback, research-validation, aggregate, generated index, and
  final SSSOM rows, and no second active MIM record for Synanthrin.

## Recommended Edits

- None.
