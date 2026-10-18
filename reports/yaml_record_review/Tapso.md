# `data/ingredients/mapped/Tapso.yaml`

## Verdict

Pass. The local CAS fallback avoids known OLS acronym false positives, PubChem
resolves the current CAS RN to TAPSO, the aggregate row is synchronized, and the
final SSSOM exact registry row publishes only real TAPSO synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Tapso.yaml`.
- Identifier and grounding: `identifier: cas:68399-81-5` with the same
  `ontology_mapping.ontology_id`, label `TAPSO`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `68399-81-5`.
- Occurrences: 12 CultureMech recipe occurrences across 12 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tangeritin` through `Tartrate`: exited 0 and wrote zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this CAS fallback row
  because registry CURIEs are intentionally outside the CHEBI-focused OBO term
  subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `TAPSO` found geographic `Tapso` municipality
  rows and the known MeSH dermorphin fragment, not a TAPSO buffer term.
- Fresh PubChem lookup by CAS `68399-81-5` resolves CID 109334, lists
  `68399-81-5`, and returns a `C7H17NO7S` formula with a TAPSO InChI.
- The final SSSOM has exactly one exact CAS registry row for `MIM:Tapso`,
  points at `cas:68399-81-5`, names `registry:cas`, and publishes only the two
  curated same-substance names plus `CAS:68399-81-5` in `other`.

## Completeness

- The CAS fallback identity, occurrence count, aggregate row, cleaned synonym
  set, and final SSSOM row agree.
- No OBO parent, components, roles, or environmental contexts are asserted.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected false-candidate reviews,
  CAS promotion, occurrence refresh, aggregate, row-review, final SSSOM, and
  generated rows.

## Recommended Edits

- None.
