# `data/ingredients/mapped/Penicillin_G.yaml`

## Verdict

Needs curation; major. The CAS-to-CHEBI mapping identifies benzylpenicillin
sodium correctly, but the `SELECTIVE_AGENT` role is only a provisional
name-list prediction and final SSSOM `other` exports a vendor note.

## Identity

- Reviewed record: `data/ingredients/mapped/Penicillin_G.yaml`.
- Identifier and grounding: `identifier: CHEBI:51765` with
  `ontology_mapping.ontology_id: CHEBI:51765`, label `benzylpenicillin sodium`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3 CultureMech occurrences across 3 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:51765` resolves `CHEBI:51765`
  `benzylpenicillin sodium`.
- A local CAS checksum calculation confirmed that `69-57-8` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps `MIM:Penicillin_G`
  exactly to `CHEBI:51765`.

## Evidence

- The CAS-derived CHEBI primary identifier, mapping target, structured formula,
  InChI, SMILES, exact chemical synonym, and `CAS:69-57-8` all describe
  benzylpenicillin sodium.
- The `CAS_RN_LOOKUP` grade accurately records how the mapping was established;
  Rule D still emits the own-identifier row as `skos:exactMatch`.
- Major: the `SELECTIVE_AGENT` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists`.
- Major: `Penicillin G (Parke)` is a source/vendor-qualified recipe surface,
  not a real synonym for benzylpenicillin sodium, but final SSSOM exports it in
  `other`.

## Completeness

- The CAS-to-CHEBI mapping is complete enough.
- Role evidence and the final synonym surface remain incomplete while the
  provisional role facet and vendor-qualified `other` token are still present.

## Recommended Edits

- Major: in `data/ingredients/mapped/Penicillin_G.yaml`, either replace
  `physicochemical_roles.SELECTIVE_AGENT` with cited source evidence that
  supports the selective-agent role for benzylpenicillin sodium, or remove the
  provisional role facet until source-backed role evidence is curated.
- Major: retype or suppress `Penicillin G (Parke)` so it remains occurrence
  provenance only and no longer appears in `mappings/ingredient_mappings.sssom.tsv`;
  rebuild the final SSSOM and rerun `scripts/validate_sssom_invariants.py`.
