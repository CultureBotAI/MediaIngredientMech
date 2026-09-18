# `data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml`

## Verdict

Needs curation; major. The CAS fallback identity for
`p-lacto-N-neo-hexaose` passes, but the `CARBON_SOURCE` role is only a
provisional name-list prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml`.
- Identifier and grounding: `identifier: cas:64309-00-8` with
  `ontology_mapping.ontology_id: cas:64309-00-8`, label
  `p-lacto-N-neo-hexaose`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences; the record was imported from
  CultureBotHT CAS-RN `64309-00-8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- CHEBI/OBO label validation was skipped for this CAS-registry primary record.
- The final SSSOM row was inspected directly and maps
  `MIM:P-lacto-N-neo-hexaose` exactly to `cas:64309-00-8`.

## Evidence

- The YAML primary identifier and `chemical_properties.cas_rn` agree on
  `64309-00-8`, and a local CAS checksum calculation confirmed that the check
  digit is valid.
- The PubChem-backed formula, InChI, SMILES, and PubChem CID are consistent
  with this defined oligosaccharide record.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the final
  SSSOM row as an expected CAS registry identifier, not as a mapping needing an
  ontology repair.
- The final SSSOM row keeps only the normalized `CAS:64309-00-8` value in
  `other`.
- The `CARBON_SOURCE` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists`.

## Completeness

- The CAS primary identifier, structured CAS-RN, formula, structure, PubChem
  CID, and final SSSOM registry row agree.
- The missing CHEBI target is explicitly represented by the CAS fallback and
  by the expected `UNKNOWN_TERM` triage row.

## Recommended Edits

- Major: in `data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml`, either
  replace `nutritional_roles.CARBON_SOURCE` with cited experimental or recipe
  evidence, or remove the provisional role facet until source-backed role
  evidence is curated.
