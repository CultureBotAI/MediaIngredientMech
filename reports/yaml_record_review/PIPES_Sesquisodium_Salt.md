# `data/ingredients/mapped/PIPES_Sesquisodium_Salt.yaml`

## Verdict

Needs curation; major. The CAS fallback identity for PIPES sesquisodium salt
passes, but the `BUFFER` role is only a provisional name-list prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/PIPES_Sesquisodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:100037-69-2` with
  `ontology_mapping.ontology_id: cas:100037-69-2`, label
  `PIPES sesquisodium salt`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 36 CultureMech occurrences across 36 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO term validation was skipped for this CAS-registry primary record.
- A local CAS checksum calculation confirmed that `100037-69-2` has the
  expected check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:PIPES_Sesquisodium_Salt` exactly to `cas:100037-69-2`.

## Evidence

- The YAML primary identifier, ontology fallback, and
  `chemical_properties.cas_rn` all agree on `100037-69-2`.
- The PubChem-backed formula, SMILES, InChI, and PubChem CID are mutually
  consistent with a defined PIPES sesquisodium salt record.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the final
  SSSOM row as an expected CAS registry identifier, not as a mapping needing an
  ontology repair.
- The final SSSOM row keeps only the normalized `CAS:100037-69-2` value in
  `other`.
- The `BUFFER` role is supported only by `COMPUTATIONAL_PREDICTION` evidence
  from `infer_roles_from_name_lists`.

## Completeness

- The CAS primary identifier, structured CAS-RN, formula, structure, PubChem
  CID, and final SSSOM registry row agree.
- `UNIFIED_INGREDIENT_MAPPING.tsv` still has an older `CHEBI:63055` mapping for
  this label, but the maintained MIM YAML and final MIM SSSOM now use the CAS
  fallback.

## Recommended Edits

- Major: in `data/ingredients/mapped/PIPES_Sesquisodium_Salt.yaml`, either
  replace `physicochemical_roles.BUFFER` with cited source evidence that
  supports the buffer role for this sesquisodium salt, or remove the
  provisional role facet until source-backed role evidence is curated.
