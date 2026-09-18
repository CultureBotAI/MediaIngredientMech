# `data/ingredients/mapped/Palatinose_Hydrate.yaml`

## Verdict

Needs curation; major. The `cas:343336-76-5` hydrate identity and close match
to parent `CHEBI:18394` pass, but the final SSSOM is missing the intended
KG-Microbe compound registry sibling and the `CARBON_SOURCE` role is only a
provisional name-list prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Palatinose_Hydrate.yaml`.
- Identifier and grounding: `identifier: cas:343336-76-5` with
  `ontology_mapping.ontology_id: CHEBI:18394`, label
  `6-O-alpha-D-glucopyranosyl-D-fructofuranose`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh exact OLS4 search for `palatinose hydrate` returned zero class
  documents.
- A local CAS checksum calculation confirmed that `343336-76-5` has the
  expected check digit.
- The final SSSOM rows were inspected directly: the record publishes the
  expected close match to `CHEBI:18394` and a CAS exact row to
  `cas:343336-76-5`.

## Evidence

- The hydrate-specific formula, SMILES, InChI, PubChem CID, and structured
  CAS-RN agree on the monohydrate form rather than the anhydrous Palatinose
  CHEBI term.
- The `CLOSE_MATCH` predicate to parent `CHEBI:18394` correctly avoids a
  false subsumption claim between a hydrate and its anhydrous parent.
- Major: `reports/hydrate_grounding.tsv` still classifies this record as
  `CAS_MISSING_ANCHOR_ROWS`; the final SSSOM has a CAS exact row, but lacks the
  `kgmicrobe.compound:palatinose_hydrate` exact registry row described by the
  hydrate anchoring curation history.
- The `CARBON_SOURCE` role is supported only by `COMPUTATIONAL_PREDICTION`
  evidence from `infer_roles_from_name_lists`.

## Completeness

- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies the CAS
  registry row as expected, not as an ontology repair.
- The close parent and CAS identity are present, but the hydrate-specific
  KG-Microbe registry sibling and source-backed carbon-source role evidence are
  missing.

## Recommended Edits

- Major: restore the exact `kgmicrobe.compound:palatinose_hydrate` registry row
  for `MIM:Palatinose_Hydrate` in the maintained SSSOM build path, rebuild
  `mappings/ingredient_mappings.sssom.tsv`, and rerun
  `scripts/validate_sssom_invariants.py`.
- Major: in `data/ingredients/mapped/Palatinose_Hydrate.yaml`, either replace
  `nutritional_roles.CARBON_SOURCE` with cited experimental or recipe evidence,
  or remove the provisional role facet until source-backed role evidence is
  curated.
