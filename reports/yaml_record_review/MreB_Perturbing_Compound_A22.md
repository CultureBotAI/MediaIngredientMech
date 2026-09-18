# `data/ingredients/mapped/MreB_Perturbing_Compound_A22.yaml`

## Verdict

Pass. The CAS fallback for MreB Perturbing Compound A22, PubChem-backed
structure, fallback registry mapping, and final CAS row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/MreB_Perturbing_Compound_A22.yaml`.
- Identifier and grounding: `identifier: cas:22816-60-0` with
  `ontology_mapping.ontology_id: cas:22816-60-0`, source `CAS`,
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

- A fresh PubChem lookup for CAS `22816-60-0` resolves CID `2830968` with
  formula `C8H9Cl3N2S` and the same InChI stored on the record.
- The CAS fallback rationale is bounded: the curation note records that no
  ChEBI entry existed in the OAK ChEBI sqlite or PubChem CID synonyms at
  creation time.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:MreB_Perturbing_Compound_A22` to `cas:22816-60-0` with
  `CAS:22816-60-0` in `other`.

## Completeness

- The CAS fallback identity, PubChem structure, and final row agree.
- The record does not assert components, roles, or non-synonym final `other`
  text.

## Recommended Edits

- None.
