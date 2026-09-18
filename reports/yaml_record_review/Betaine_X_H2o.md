# `data/ingredients/mapped/Betaine_X_H2o.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:91242` glycine betaine hydrate
identity, CAS, hydrate formula, InChI, SMILES, SSSOM row, occurrence count, and
aggregate copy pass, but the active `ontology_mapping.evidence` list still
carries superseded parent/narrow/close-match decisions as if they were evidence
for the current exact ChEBI row.

## Identity

- Reviewed record: `data/ingredients/mapped/Betaine_X_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:91242` with
  `ontology_mapping.ontology_id: CHEBI:91242`,
  `ontology_label: glycine betaine hydrate`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS search by numeric ChEBI ID returns current `CHEBI:91242` as
  `glycine betaine hydrate` and lists the record's two exact synonyms.
- PubChem resolves CAS `590-47-6` to multiple hydrate entries; CID 24884197 has
  the same monohydrate InChI and dot-water SMILES stored in the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Betaine_X_H2o.yaml data/ingredients/mapped/Betanin.yaml data/ingredients/mapped/Bg-11_Medium.yaml data/ingredients/mapped/Bg-11_Trace_Metals_Solution.yaml data/ingredients/mapped/Bicarbonate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Betaine_X_H2o.yaml data/ingredients/mapped/Betanin.yaml data/ingredients/mapped/Bicarbonate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three ChEBI-backed records in this batch.
- Engine A term validation is intentionally skipped for the two non-ChEBI
  records here: `MICRO` is omitted by the local justfile's OBO-safe adapter list
  and `kgmicrobe.ingredient` is a local registry prefix.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 586 and the aggregate copy in
  `data/curated/mapped_ingredients.yaml`.
- `reports/hydrate_grounding.tsv` reports the `CHEBI:91242` mapping as
  `OK_HYDRATE_TERM`.
- `mappings/culturemech_recipe_membership.tsv` contains 40 rows for
  `CHEBI:91242`, matching the record's refreshed 40/40 medium and total
  occurrence counts.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact hydrate-specific CHEBI identifier, CAS RN, single-ingredient
  classification, formula, InChI, SMILES, SSSOM row, occurrence statistics, and
  aggregate copy are populated.
- Minor gap: `ontology_mapping.evidence` still includes superseded entries for
  the historical registry mint, the temporary `NARROW_MATCH`, and the temporary
  `CLOSE_MATCH` to `CHEBI:17750`. That provenance belongs in
  `curation_history`, but it no longer supports the active exact mapping.

## Recommended Edits

- Minor: prune the superseded #321/#334/#342 parent evidence from
  `data/ingredients/mapped/Betaine_X_H2o.yaml` and keep only evidence that
  supports the current exact `CHEBI:91242` identity. Then run
  `just sync-curated` and focused strict/term validation.
