# `data/ingredients/mapped/DAMPA.yaml`

## Verdict

Pass. `DAMPA` is a CAS-backed local identity, PubChem confirms the CAS points at
deoxyaminopteroic acid with the recorded formula and InChI, current OLS did not
find an exact ChEBI replacement, and the final SSSOM row publishes only the
structured CAS token.

## Identity

- Reviewed record: `data/ingredients/mapped/DAMPA.yaml`.
- Identifier and grounding: `identifier: cas:19741-14-1` with
  `ontology_mapping.ontology_id: cas:19741-14-1`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem resolves `19741-14-1` to CID 72441,
  `Deoxyaminopteroic Acid`, formula `C15H15N7O2`, and InChIKey
  `LWCXZSDKANNOAR-UHFFFAOYSA-N`, matching the structure stored in
  `chemical_properties`.
- Live OLS exact search found no exact `DAMPA` ChEBI class, and the CAS lookup
  for `19741-14-1` found only lexical false positives in unrelated CHEBI
  identifiers.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DAMPA.yaml data/ingredients/mapped/DCMU.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DAMPA.yaml data/ingredients/mapped/DCMU.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed through `D` and then failed on `DAMPA` because its `cas:` fallback
  hit the known OAK SQL label-lookup error:
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-xylose.yaml data/ingredients/mapped/D-xylose_5-phosphate_Lithium_Salt.yaml data/ingredients/mapped/D.yaml data/ingredients/mapped/DCMU.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-file CHEBI subset after skipping `DAMPA`.
- `curl -L ... q=DAMPA&ontology=chebi&exact=true`: live OLS returned no exact
  ChEBI hit.
- `curl -L ... q=19741-14-1&ontology=chebi&exact=true`: live OLS returned
  only unrelated CHEBI false positives whose identifiers contain `19741`.
- `curl -L ... /compound/name/19741-14-1/property/.../JSON`: PubChem resolved
  the CAS value to CID 72441, `Deoxyaminopteroic Acid`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `cas:19741-14-1`, matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the CAS
  object as `expected_registry_identifier`, matching the current local
  fallback identity.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:DAMPA` to
  `cas:19741-14-1` with `skos:exactMatch`, object source `registry:cas`, and
  only `CAS:19741-14-1` in `other`.
- The record does not assert synonyms, nutritional roles, environmental
  contexts, or mixture components, so there are no unsupported claim-specific
  evidence objects to resolve.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over `data`, `mappings`,
  `docs`, `reports`, `.claude`, `.github`, `scripts`, `src`, and `tests` found
  no second primary record for `cas:19741-14-1`; the CAS appears in this
  record, synchronized/generated projections, and registry review surfaces.
- The CAS value, PubChem CID, molecular formula, SMILES, and InChI are
  populated.
- No parent term is currently required because live OLS did not expose an exact
  or narrower ChEBI target for DAMPA.

## Recommended Edits

- None.
