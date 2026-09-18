# `data/ingredients/mapped/Tertiomycin_B.yaml`

## Verdict

Needs curation - major. The kg-microbe placeholder identity is still the best
available local fallback for `Tertiomycin B`, but its `SELECTIVE_AGENT` role is
only a provisional computational name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Tertiomycin_B.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:tertiomycin_b` with the same
  `ontology_mapping.ontology_id`, label `Tertiomycin B`, source
  `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`, `mapping_status:
  MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tertiomycin_B` through `Tetrachloroethene`: exited 0 and wrote zero ERROR
  rows.
- Direct old Engine A/OBO term validation was skipped for this local
  `kgmicrobe.compound` placeholder row because that prefix is intentionally
  outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `Tertiomycin B` returned zero results, and fresh
  PubChem lookup found no CID.
- `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`
  records that the reviewed OLS candidates were not label or synonym identity
  matches for Tertiomycin B.
- The final SSSOM has exactly one exact local registry row for
  `MIM:Tertiomycin_B`, points at `kgmicrobe.compound:tertiomycin_b`, names
  `kgm:compound`, and publishes no unsafe `other` synonyms.
- Major: `physicochemical_roles.SELECTIVE_AGENT` cites only
  `reference_type: COMPUTATIONAL_PREDICTION` from a curated name pattern and
  explicitly notes that review is recommended.

## Completeness

- The local placeholder identity, manual no-promotion decision, aggregate row,
  and final SSSOM row agree.
- The asserted selective-agent role is incomplete until it is replaced with
  source-backed evidence for this exact antibiotic or removed.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected placeholder import,
  candidate-review, aggregate, unknown-term triage, final SSSOM, and generated
  rows.

## Recommended Edits

- Major: replace the provisional name-pattern `SELECTIVE_AGENT` role in
  `data/ingredients/mapped/Tertiomycin_B.yaml` with source-backed evidence for
  Tertiomycin B as a selective agent, or remove the role if no maintained
  source supports it.
- Major: after any role edit, synchronize `data/curated/mapped_ingredients.yaml`
  and regenerate generated products so the role facets match the per-record
  YAML.
