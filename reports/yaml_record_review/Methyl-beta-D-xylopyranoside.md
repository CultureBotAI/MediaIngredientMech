# `data/ingredients/mapped/Methyl-beta-D-xylopyranoside.yaml`

## Verdict

Needs curation. The normalized CAS is correct, but this CAS-only record now
duplicates an active exact `CHEBI:74863` MIM record for the same beta-D
xylopyranoside.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Methyl-beta-D-xylopyranoside.yaml`.
- Identifier and grounding: `identifier: cas:612-05-5` with
  `ontology_mapping.ontology_id: cas:612-05-5`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Methyl-alpha-D-xylopyranoside` through `Methyl-trans-p-coumarate`: exited 0
  and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this CAS-primary registry
  record because CAS CURIEs are intentionally outside the OBO adapter scope.

## Evidence

- PubChem resolves normalized CAS `612-05-5` to CID 11768891 with formula
  `C6H12O5` and the methyl beta-D-xylopyranoside stereochemistry.
- EBI OLS4 now resolves `CHEBI:74863` as active
  `methyl beta-D-xylopyranoside` with CAS `612-05-5`, formula `C6H12O5`, and
  the same InChI as PubChem.
- `rg --no-ignore --hidden` over `data`, `mappings`, `reports`, `scripts`,
  `src`, and `tests` found the active exact sibling
  `data/ingredients/mapped/Methyl_Beta-D-xylopyranoside.yaml` on
  `CHEBI:74863`.
- The final SSSOM still publishes only a CAS registry row for
  `MIM:Methyl-beta-D-xylopyranoside`.

## Completeness

- The #310 leading-zero repair correctly normalized `cas:0612-05-5` to
  `cas:612-05-5`, but the later exact ChEBI/MicrobeDecoder record made this
  CAS-only row a duplicate identity.

## Recommended Edits

- Merge `Methyl-beta-D-xylopyranoside.yaml` into
  `Methyl_Beta-D-xylopyranoside.yaml` or promote this record to the active
  `CHEBI:74863` identity and reconcile the duplicate final SSSOM subjects.
