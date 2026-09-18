# `data/ingredients/mapped/Nah2po4_X_2_H2o.yaml`

## Verdict

Needs curation - major. The record now preserves the dihydrate as a distinct
`kgmicrobe.compound:nah2po4_x_2_h2o` identity and publishes the expected exact
registry row next to a `skos:closeMatch` parent row, but it still carries
anhydrous structure strings, a stale downstream node ID, and monohydrate and
anhydrous aliases in the final SSSOM synonym surface.

## Identity

- Reviewed record: `data/ingredients/mapped/Nah2po4_X_2_H2o.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:nah2po4_x_2_h2o` with
  `ontology_mapping.ontology_id: CHEBI:37585`, label
  `sodium dihydrogenphosphate`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 53 CultureMech recipe occurrences across 53 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nah2po4_X_2_H2o` through `Nalidixic_Acid_Sodium_Salt`: exited 0 and left
  `reports/instance_validation_failures.tsv` header-only.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.

## Evidence

- Fresh OLS4 searches for `NaH2PO4 x 2 H2O` and
  `sodium dihydrogenphosphate dihydrate` returned no exact standalone CHEBI
  term for this dihydrate; the latter search returned only the anhydrous parent
  `CHEBI:37585` and monohydrate `CHEBI:114249`.
- `reports/hydrate_grounding.tsv` classifies
  `kgmicrobe.compound:nah2po4_x_2_h2o` as `OK_LOCAL_REGISTRY_ID`.
- The final SSSOM output carries both expected rows:
  `MIM:Nah2po4_X_2_H2o skos:closeMatch CHEBI:37585` and
  `MIM:Nah2po4_X_2_H2o skos:exactMatch
  kgmicrobe.compound:nah2po4_x_2_h2o`.
- Major: `chemical_properties.inchi` and `chemical_properties.smiles` still
  describe the anhydrous `CHEBI:37585` parent even though
  `chemical_properties.molecular_formula` was corrected to
  `H2O4P.Na.2H2O`.
- Major: `kg_microbe_node_id: CHEBI:37585` is a stale cross-prefix
  compatibility value after the local registry mint; an ignored- and
  hidden-inclusive search found the same mismatch in
  `reports/kg_microbe_node_id_mismatches.tsv`.
- Major: final SSSOM `other` still publishes the monohydrate labels
  `NaH2PO4 x H2O` and the middle-dot/ideographic-dot monohydrate variants, plus
  the anhydrous label `sodium phosphate monobasic anhydrous`. Those labels
  erase the dihydrate/monohydrate/anhydrous boundary.

## Completeness

- The local exact identity, close parent mapping, exact registry row, corrected
  hydrate formula, CAS removal, aggregate copy, occurrence count, and `BUFFER`
  role are present.
- The structure strings, compatibility node ID, and final `other` synonyms are
  the remaining consequential gaps.

## Recommended Edits

- Major: replace or remove the anhydrous `chemical_properties.inchi` and
  `chemical_properties.smiles` values in
  `data/ingredients/mapped/Nah2po4_X_2_H2o.yaml`.
- Major: replace or delete `kg_microbe_node_id: CHEBI:37585` so downstream
  node exports do not collapse the dihydrate onto the anhydrous ChEBI parent.
- Major: reject or delete the monohydrate and anhydrous active synonyms so the
  close-match SSSOM row only emits aliases for the dihydrate.
