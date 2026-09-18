# `data/ingredients/mapped/Palmatine_Chloride.yaml`

## Verdict

Pass. The CAS fallback identity for Palmatine chloride is form-specific and the
final SSSOM keeps only the matching normalized CAS value.

## Identity

- Reviewed record: `data/ingredients/mapped/Palmatine_Chloride.yaml`.
- Identifier and grounding: `identifier: cas:10605-02-4` with
  `ontology_mapping.ontology_id: cas:10605-02-4`, label
  `Palmatine chloride`, source `CAS`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this CAS-registry primary record.
- A fresh exact OLS4 search for `Palmatine chloride` found no form-specific
  chloride class.
- A local CAS checksum calculation confirmed that `10605-02-4` has the
  expected check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:Palmatine_Chloride` exactly to `cas:10605-02-4`.

## Evidence

- The YAML primary identifier, ontology fallback, and
  `chemical_properties.cas_rn` all agree on `10605-02-4`.
- The PubChem-backed formula, SMILES, InChI, and PubChem CID are mutually
  consistent with the palmatine chloride salt.
- The fresh OLS4 search found parent `mesh:C005413` palmatine but no exact
  chloride term, so the CAS fallback correctly preserves the salt boundary.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the final
  SSSOM row as an expected CAS registry identifier, not as a mapping needing an
  ontology repair.
- The final SSSOM row keeps only the normalized `CAS:10605-02-4` value in
  `other`.

## Completeness

- The CAS primary identifier, structured CAS-RN, formula, structure, PubChem
  CID, and final SSSOM registry row agree.

## Recommended Edits

- None.
