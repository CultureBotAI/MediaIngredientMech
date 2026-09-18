# `data/ingredients/mapped/D-Saccharic_Acid_Potassium_Salt.yaml`

## Verdict

Pass. The CAS-primary potassium-salt identity, PubChem chemistry,
`CHEBI:16002` D-glucaric-acid parent, 0/0 occurrence count, registry rows, and
empty SSSOM synonym payload are internally consistent and keep the salt
distinct from the acid parent.

## Identity

- Reviewed record:
  `data/ingredients/mapped/D-Saccharic_Acid_Potassium_Salt.yaml`.
- Current identifier and grounding: `identifier: cas:576-42-1`,
  `ontology_mapping.ontology_id: CHEBI:16002`,
  `ontology_label: D-glucaric acid`, `ontology_source: CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:16002` returns active `CHEBI:16002` labelled
  `D-glucaric acid`, formula `C6H10O8`, and exact/related
  `D-Saccharic acid` synonyms, confirming it is the acid parent rather than the
  potassium salt.
- PubChem CID `23674495` returns formula `C6H9KO8` and a canonical SMILES
  string matching the YAML potassium-salt structure.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `cas:576-42-1`; the only
  `CHEBI:16002` primary identifier in `data/ingredients` is the separate exact
  `D-Glucaric_Acid` record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Proline.yaml data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml data/ingredients/mapped/D-Ribose.yaml data/ingredients/mapped/D-Saccharic_Acid_Potassium_Salt.yaml data/ingredients/mapped/D-Serine.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Proline.yaml data/ingredients/mapped/D-Ribose.yaml data/ingredients/mapped/D-Serine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch. This record
  was skipped because its primary `cas:` identifier is outside the CHEBI/OBO
  term-validator scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- The record's formula, SMILES, InChI, PubChem CID, and CAS RN agree for
  potassium D-glucarate.
- `scripts/reground_compositional_classes.py` and the `MIM curation (#322)`
  evidence document the maintained repair from the previous generic
  `potassium salt` parent to the current `D-glucaric acid` parent.
- The hidden/ignored-inclusive membership search found no `cas:576-42-1` rows
  in `mappings/culturemech_recipe_membership.tsv`, matching the record's 0/0
  `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` keeps the current
  registry rows as expected `cas:` and `kgmicrobe.compound` identifiers.
- The final SSSOM rows publish
  `MIM:D-Saccharic_Acid_Potassium_Salt skos:narrowMatch CHEBI:16002`, an exact
  `cas:576-42-1` row, and an exact
  `kgmicrobe.compound:d-saccharic_acid_potassium_salt` row. Only the CAS value
  appears in `other`.

## Completeness

- No nutritional roles, components, source occurrences, or extra synonyms are
  asserted, so there are no unsupported secondary claims.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry.

## Recommended Edits

- No curation edits are needed.
