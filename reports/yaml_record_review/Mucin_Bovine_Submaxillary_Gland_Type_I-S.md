# `data/ingredients/mapped/Mucin_Bovine_Submaxillary_Gland_Type_I-S.yaml`

## Verdict

Pass. The CAS fallback for the bovine submaxillary gland type I-S mucin
preparation, absent exact ontology replacement, and final CAS row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Mucin_Bovine_Submaxillary_Gland_Type_I-S.yaml`.
- Identifier and grounding: `identifier: cas:84195-52-8` with
  `ontology_mapping.ontology_id: cas:84195-52-8`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `MreB_Perturbing_Compound_A22` through
  `Mucin_From_Porcine_StomachType_II`: exited 0 and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this CAS-primary record
  because `cas:` is outside the OBO subset used for the batch.

## Evidence

- Fresh PubChem and EBI OLS4 lookups found no replacement CID or same-label
  ontology term for this CAS fallback.
- The record already records the bounded fallback decision: CAS `84195-52-8`
  was present in CultureBotHT and no ChEBI entry existed.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mucin_Bovine_Submaxillary_Gland_Type_I-S` to `cas:84195-52-8` with
  `CAS:84195-52-8` in `other`.

## Completeness

- The CAS fallback identity, absence of an exact OBO/PubChem replacement, and
  final row agree.
- The record does not assert unsupported roles, components, chemical structures,
  or non-synonym final `other` text.

## Recommended Edits

- None.
