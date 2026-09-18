# `data/ingredients/mapped/Methyl-2-Hydroxy-Phenylproprionate.yaml`

## Verdict

Pass. The CAS-primary fallback registry identity and final SSSOM row pass; no
fresh public OLS or PubChem candidate was found.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Methyl-2-Hydroxy-Phenylproprionate.yaml`.
- Identifier and grounding: `identifier: cas:89471-28-0` with
  `ontology_mapping.ontology_id: cas:89471-28-0`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methanol` through `Methyl-B-D-galactopyranoside`: exited 0 and wrote zero
  ERROR rows.
- Direct Engine A term validation was skipped for this CAS-primary registry
  record because CAS CURIEs are intentionally outside the OBO adapter scope.

## Evidence

- The row-review triage for the `UNKNOWN_TERM` validation stamp keeps the row
  as an expected CAS registry identifier because `object_id` matches both the
  YAML `identifier` and `chemical_properties.cas_rn`.
- Fresh exact all-ontology OLS4 search for
  `Methyl-2-Hydroxy-Phenylproprionate` returned zero results.
- Fresh PubChem lookup for CAS `89471-28-0` returned no CID.
- The final SSSOM publishes one `skos:exactMatch` row to `cas:89471-28-0` with
  `CAS:89471-28-0` as the only `other` token.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
