# `data/ingredients/mapped/Mucin_From_Porcine_StomachType_II.yaml`

## Verdict

Needs curation. The CAS fallback for the porcine stomach type II mucin
preparation and the refreshed 1/1 occurrence count pass, but autoclaving
process text still publishes in final SSSOM `other`.

Severity: major.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Mucin_From_Porcine_StomachType_II.yaml`.
- Identifier and grounding: `identifier: cas:84082-64-4` with
  `ontology_mapping.ontology_id: cas:84082-64-4`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `MreB_Perturbing_Compound_A22` through
  `Mucin_From_Porcine_StomachType_II`: exited 0 and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this CAS-primary record
  because `cas:` is outside the OBO subset used for the batch.

## Evidence

- Fresh PubChem and EBI OLS4 lookups found no replacement CID or same-label
  ontology term for this CAS fallback.
- The 2026-05-11 curation event explicitly says `autoclaved, Mucin from porcine
  stomach type II` was reclassified as raw source text because preparation
  method text is not an identity synonym.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mucin_From_Porcine_StomachType_II` to `cas:84082-64-4`.

## Completeness

- The CAS fallback identity, absence of an exact OBO/PubChem replacement, and
  1/1 occurrence count agree.
- The final SSSOM `other` field still exports `autoclaved, Mucin from porcine
  stomach type II`, contradicting the record's own process-synonym cleanup
  history.

## Recommended Edits

- Major: filter `autoclaved, Mucin from porcine stomach type II` from final
  SSSOM `other` while retaining it as raw source provenance in
  `data/ingredients/mapped/Mucin_From_Porcine_StomachType_II.yaml`.
