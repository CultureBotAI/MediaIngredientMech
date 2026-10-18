# `data/ingredients/mapped/L-cysteine_Zwitterion.yaml`

## Verdict

Needs curation. The hydrate-sibling-created exact CHEBI:35235 identity and
final SSSOM row pass, but the amino-acid-source role is provisional and the
occurrence count is not traceable to media occurrences.

## Identity

- Reviewed record: `data/ingredients/mapped/L-cysteine_Zwitterion.yaml`.
- Identifier and grounding: `identifier: CHEBI:35235` with
  `ontology_mapping.ontology_id: CHEBI:35235`, label
  `L-cysteine zwitterion`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C3H7NO2S`, zwitterionic InChI and
  SMILES, and no CAS RN.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-cysteine.yaml data/ingredients/mapped/L-cysteine_Hcl.yaml data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml data/ingredients/mapped/L-cysteine_Hydrochloride_Monohydrate.yaml data/ingredients/mapped/L-cysteine_Zwitterion.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 exact search for `L-cysteine zwitterion` returns active
  `CHEBI:35235`, and its exact or related synonyms include both YAML synonyms.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:35235` with
  only `(2R)-2-ammonio-3-sulfanylpropanoate` in `other`; that synonym resolves
  on the same ChEBI zwitterion identity.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern
  and says review is recommended. The name pattern can propose this role, but
  the record still lacks inspected source evidence that this zwitterion was
  used as an amino-acid source in a medium.
- Minor: `occurrence_statistics` records `total_occurrences: 3` with
  `media_count: 0` and no `source_occurrences`; the three-count came from
  hydration-routing synonyms, not traceable medium occurrences.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, the separate free L-cysteine sibling that still
  exports this label, and the OAK/OLS row-review confirmation.

## Completeness

- The exact ChEBI identity, zwitterionic structure, aggregate copy, and final
  SSSOM row are present and consistent.
- The provisional amino-acid role and occurrence count need curation.

## Recommended Edits

- Major: either replace
  `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/L-cysteine_Zwitterion.yaml` with source-backed
  evidence for this exact zwitterion, or remove the provisional role.
- Minor: reconcile `occurrence_statistics` with the hydrate-routing provenance;
  set it to real media occurrences or clear the count if no medium uses this
  exact zwitterion.
- Sync the aggregate copy and regenerate the SSSOM/docs products after the YAML
  changes; rerun strict, term, round-trip, component, and SSSOM validation.
