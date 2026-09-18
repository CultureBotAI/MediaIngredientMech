# `data/ingredients/mapped/Mucin_From_Porcine_Stomach_Type_III.yaml`

## Verdict

Needs curation. The CAS fallback for the porcine stomach type III mucin
preparation and 1/1 occurrence count pass, but bound-sialic-acid text still
publishes in final SSSOM `other`.

Severity: major.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Mucin_From_Porcine_Stomach_Type_III.yaml`.
- Identifier and grounding: `identifier: cas:84082-64-4` with
  `ontology_mapping.ontology_id: cas:84082-64-4`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: one CultureBotHT media occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mucin_From_Porcine_Stomach_Type_III` through `Mycobactin_J`: exited 0 and
  wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this CAS-primary record
  because `cas:` is outside the OBO subset used for the batch.

## Evidence

- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mucin_From_Porcine_Stomach_Type_III` to `cas:84082-64-4`.
- The final SSSOM `other` field includes `CAS:84082-64-4`, which is a valid
  CAS alias for the record.
- The final SSSOM `other` field also exports `Mucin from porcine stomach type
  III, bound sialic acid 0.5-1.5 %, Mucin from porcine stomach type III`, which
  is a comma-joined, concentration-qualified source label rather than a clean
  identity synonym.

## Completeness

- The CAS fallback identity, CultureBotHT provenance, and 1/1 occurrence count
  agree.
- Fresh PubChem and EBI OLS4 lookups for the sibling type II CAS fallback found
  no CID or same-label ontology term for this CAS family, so no active external
  replacement was visible during the adjacent bounded search.

## Recommended Edits

- Major: reclassify the bound-sialic-acid source label as raw provenance or a
  rejected export label, and filter it from final SSSOM `other`.
