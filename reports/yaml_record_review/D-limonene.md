# `data/ingredients/mapped/D-limonene.yaml`

## Verdict

Needs curation. The CAS fallback is internally consistent and still produces a
registry SSSOM row, but it is stale: a live OLS search now finds exact ChEBI
d-limonene candidates, and the stored CAS `138-86-7` no longer resolves through
PubChem as a compound name.

## Identity

- Reviewed record: `data/ingredients/mapped/D-limonene.yaml`.
- Identifier and grounding: `identifier: cas:138-86-7` with
  `ontology_mapping.ontology_id: cas:138-86-7`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- The record's preferred term and object label are both `d-limonene`; its
  `chemical_properties.cas_rn` matches the primary identifier.
- The original CultureBotHT evidence says the fallback was kept because no
  ChEBI entry existed. A live OLS search for `d-limonene` now returns active
  `CHEBI:748872` labelled `d-limonene` and active `CHEBI:15382`
  `(4R)-limonene`, which carries `d-limonene` as an exact synonym.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-histidine.yaml data/ingredients/mapped/D-limonene.yaml data/ingredients/mapped/D-malate.yaml data/ingredients/mapped/D-mannitol.yaml data/ingredients/mapped/D-mannose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-histidine.yaml data/ingredients/mapped/D-malate.yaml data/ingredients/mapped/D-mannitol.yaml data/ingredients/mapped/D-mannose.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 4-file CHEBI subset. `D-limonene` was skipped because its `cas:`
  fallback crashes the OAK SQL label lookup with
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `curl -L ... q=d-limonene&ontology=chebi`: found exact live ChEBI candidates
  at `CHEBI:748872` and `CHEBI:15382`.
- `curl -L ... q=138-86-7&ontology=chebi`: found no ChEBI hit for the stored
  CAS value.
- `curl -L ... /compound/name/138-86-7/cids/JSON`: PubChem reported
  `No CID found`.
- `curl -L ... /compound/name/d-limonene/property/.../JSON`: PubChem resolved
  the source label to CID `440917`, formula `C10H16`, and InChIKey
  `XMGQYMWWDOXHJM-JTQLQIEISA-N`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_unknown_term_triage.tsv` classifies
  `MIM:D-limonene` as an expected CAS registry identifier rather than a
  malformed ontology term, which was appropriate for the old fallback state.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:D-limonene` to `cas:138-86-7` with `skos:exactMatch`,
  `object_source: registry:cas`, and `CAS:138-86-7` in `other`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `cas:138-86-7`, matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- Live OLS metadata for `CHEBI:15382` gives formula `C10H16`, InChIKey
  `XMGQYMWWDOXHJM-JTQLQIEISA-N`, and CAS `5989-27-5`. PubChem resolves the
  `d-limonene` name to the same formula and InChIKey, while PubChem does not
  resolve the stored CAS `138-86-7` at all.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, and `docs` found no second MIM record for `cas:138-86-7`.
- The record has no roles, environmental contexts, synonyms, or mixture
  components.
- The CAS fallback lacks formula, InChI, and SMILES. That was tolerable for a
  local registry stub, but should be filled if the record is promoted to a
  ChEBI-backed chemical mapping.

## Recommended Edits

- In `data/ingredients/mapped/D-limonene.yaml`, recheck the CultureBotHT source
  CAS and remap the record to the best live ChEBI target, likely
  `CHEBI:15382` or `CHEBI:748872`, rather than leaving the stale
  `cas:138-86-7` fallback untouched.
- Update `chemical_properties` from the chosen registry/ChEBI identity and
  drop `CAS:138-86-7` from the final SSSOM `other` payload if it is not a CAS
  for the exact d-limonene subject.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data ...` on the repaired
  CHEBI record, and `uv run --frozen python scripts/validate_sssom_invariants.py`.
