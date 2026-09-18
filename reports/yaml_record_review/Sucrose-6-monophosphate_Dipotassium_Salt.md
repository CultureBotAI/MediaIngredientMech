# `data/ingredients/mapped/Sucrose-6-monophosphate_Dipotassium_Salt.yaml`

## Verdict

Needs curation - major. The CAS registry row is the expected fallback shape, but
the stored PubChem structure has only one potassium under a dipotassium label
and the `CARBON_SOURCE` role is still provisional.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Sucrose-6-monophosphate_Dipotassium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:36064-19-4` with
  `ontology_mapping.ontology_id: cas:36064-19-4`, label
  `Sucrose-6-monophosphate dipotassium salt`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `36064-19-4`, PubChem CID `16219958`, formula
  `C12H23KO14P`, and PubChem-derived InChI/SMILES fields.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Substrate` through `Sucrose-6-monophosphate_Dipotassium_Salt`: exited 0 and
  wrote zero ERROR rows.
- Engine A term validation was skipped for this CAS-primary record because
  `cas:` is a registry prefix, not an OBO prefix.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- `mappings/ingredient_mappings_unknown_term_triage.tsv` intentionally keeps
  `cas:36064-19-4` as an expected registry identifier outside OAK/OLS.
- PubChem still resolves CAS `36064-19-4` to CID `16219958`, the stored
  `pubchem_cid`, but that CID has formula `C12H23KO14P` and an InChI with one
  disconnected potassium component. A current second PubChem CID for the same
  CAS has the same one-potassium formula. Neither structure reproduces the
  stated dipotassium salt.
- The final SSSOM row exact-matches `cas:36064-19-4` and publishes only
  `CAS:36064-19-4` in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by
  `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists`, with the
  provisional name-pattern curator note.

## Completeness

- The CAS fallback identifier, aggregate row, zero occurrence count, and final
  SSSOM row agree.
- An ignored/hidden search of local curated, mapping, generated, report, source,
  and documentation paths found the expected CAS fallback and no CHEBI exact
  replacement row, but the PubChem-backed structure remains internally
  inconsistent with the preferred dipotassium label.

## Recommended Edits

- Major: inspect CAS `36064-19-4` and the PubChem entries for the exact salt;
  then either correct the preferred salt label, move the one-potassium PubChem
  fields into a separately named identity, or replace the chemistry with a
  source that reproduces sucrose-6-monophosphate dipotassium salt.
- Major: either replace `nutritional_roles.CARBON_SOURCE` with inspected
  source-backed evidence, or remove the provisional role facet.
