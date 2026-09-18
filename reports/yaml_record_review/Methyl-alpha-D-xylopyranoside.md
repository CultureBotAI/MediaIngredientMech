# `data/ingredients/mapped/Methyl-alpha-D-xylopyranoside.yaml`

## Verdict

Pass. The CAS-primary fallback registry identity, PubChem structure, and final
SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl-alpha-D-xylopyranoside.yaml`.
- Identifier and grounding: `identifier: cas:91-09-8` with
  `ontology_mapping.ontology_id: cas:91-09-8`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 91-09-8`, PubChem CID 101554, formula `C6H12O5`,
  and the PubChem InChI for methyl-alpha-D-xylopyranoside.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl-alpha-D-xylopyranoside` through `Methyl-trans-p-coumarate`: exited 0
  and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this CAS-primary registry
  record because CAS CURIEs are intentionally outside the OBO adapter scope.

## Evidence

- PubChem resolves CAS `91-09-8` to CID 101554 with formula `C6H12O5` and the
  same InChI carried in the YAML.
- The row-review triage for the `UNKNOWN_TERM` validation stamp keeps the row
  as an expected CAS registry identifier because `object_id` matches both the
  YAML `identifier` and `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row to `cas:91-09-8` with
  `CAS:91-09-8` as the only `other` token.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
