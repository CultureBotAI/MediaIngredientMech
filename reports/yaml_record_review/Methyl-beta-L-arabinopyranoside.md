# `data/ingredients/mapped/Methyl-beta-L-arabinopyranoside.yaml`

## Verdict

Pass. The CAS-primary fallback registry identity, PubChem structure, and final
SSSOM row pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Methyl-beta-L-arabinopyranoside.yaml`.
- Identifier and grounding: `identifier: cas:1825-00-9` with
  `ontology_mapping.ontology_id: cas:1825-00-9`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 1825-00-9`, PubChem CID 102169, formula
  `C6H12O5`, and the PubChem InChI for methyl-beta-L-arabinopyranoside.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl-alpha-D-xylopyranoside` through `Methyl-trans-p-coumarate`: exited 0
  and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this CAS-primary registry
  record because CAS CURIEs are intentionally outside the OBO adapter scope.

## Evidence

- PubChem resolves CAS `1825-00-9` to CID 102169 with formula `C6H12O5` and the
  same InChI carried in the YAML.
- The row-review triage for the `UNKNOWN_TERM` validation stamp keeps the row
  as an expected CAS registry identifier because `object_id` matches both the
  YAML `identifier` and `chemical_properties.cas_rn`.
- The final SSSOM publishes one `skos:exactMatch` row to `cas:1825-00-9` with
  `CAS:1825-00-9` as the only `other` token.

## Completeness

- The record does not publish unsupported roles or non-exact synonyms.

## Recommended Edits

- None.
