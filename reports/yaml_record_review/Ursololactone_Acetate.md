# `data/ingredients/mapped/Ursololactone_Acetate.yaml`

## Verdict

Pass. The CAS fallback identity, aggregate row, and final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Ursololactone_Acetate.yaml`.
- Identifier and grounding: `identifier: cas:28290-51-9` with matching
  `ontology_mapping.ontology_id`, label `Ursololactone Acetate`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `28290-51-9`.
- Occurrences: 0.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Uridine_5-monophosphate_Disodium_Salt` through `V-8_Juice`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch;
  this CAS fallback row has no OBO adapter for that focused check.

## Evidence

- PubChem name lookup for CAS `28290-51-9` resolves to CID `21669106`; that CID
  carries `28290-51-9` and ursolic-acid-lactone acetate synonyms, consistent
  with the CultureBotHT CAS fallback identity.
- Fresh OLS4 CHEBI search for CAS `28290-51-9` returned no CHEBI documents, so
  the CAS fallback remains the best available exact registry identity.
- The final SSSOM row correctly maps
  `MIM:Ursololactone_Acetate skos:exactMatch cas:28290-51-9` with the CAS
  fallback review tag.

## Issues

None.

## Completeness

- The CAS fallback identity, aggregate copy, and final SSSOM row agree.
- No structure fields are recorded locally for this CAS fallback; that is a
  completeness opportunity, not an identity defect.

## Recommended Edits

None.
