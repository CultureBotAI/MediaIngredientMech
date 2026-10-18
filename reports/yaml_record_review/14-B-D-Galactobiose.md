# `data/ingredients/mapped/14-B-D-Galactobiose.yaml`

## Verdict

Needs curation, major. The repaired chemical identity now correctly maps
`1,4-B-D-Galactobiose` to `CHEBI:36226`, but the record still asserts
`CARBON_SOURCE` from only a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/14-B-D-Galactobiose.yaml`.
- Identifier and grounding: `identifier: cas:2152-98-9` with
  `ontology_mapping.ontology_id: CHEBI:36226`,
  `ontology_mapping.ontology_label: beta-D-galactopyranosyl-(1->4)-D-galactopyranose`,
  source `CHEBI`, and `mapping_quality: SYNONYM_MATCH`.
- The #326 repair intentionally regraded the PubChem-cross-referenced ChEBI
  target from `NARROW_MATCH` to `SYNONYM_MATCH` because the CAS PubChem InChIKey
  matches the ChEBI identity and the formulas agree.
- Official ChEBI and PubChem checks: ChEBI `CHEBI:36226` and PubChem CID
  `9548802` agree on formula `C12H22O11` and the InChIKey prefix
  `GUBGYTABKSRVRQ` for the active registry-backed identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/13-Butandiol.yaml data/ingredients/mapped/13-Hexanediol.yaml data/ingredients/mapped/13-Propanediol.yaml data/ingredients/mapped/14-B-D-Galactobiose.yaml data/ingredients/mapped/14-Butanediol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- LinkML term validation passed for
  `data/ingredients/mapped/14-B-D-Galactobiose.yaml`.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:14-B-D-Galactobiose` to `CHEBI:36226` mapping and an exact registry row
  for `cas:2152-98-9`.

## Evidence

- The official ChEBI and PubChem records support the current exact identity
  repair.
- Major: the `nutritional_roles` slot asserts `CARBON_SOURCE` at confidence
  `0.8` from only `COMPUTATIONAL_PREDICTION` evidence with
  `Inferred from curated media-role name pattern`. A name-pattern rule is a lead,
  not evidence that this exact galactobiose is used as a carbon source in a
  medium formulation.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found stale old P1/P2 rows about missing
  identity and the pre-#326 narrow ChEBI mapping; those are stale. Edison row
  510 still points to the live provisional role evidence issue.

## Completeness

- CAS RN, formula, InChI, and the registry mapping are populated for the active
  chemical form.
- Empty component slots are acceptable for this single chemical.
- The nutritional role is consequential because generated users could read the
  record as evidence-backed support for carbon-source use.

## Recommended Edits

1. In `data/ingredients/mapped/14-B-D-Galactobiose.yaml`, either remove the
   provisional `CARBON_SOURCE` role or replace it with inspected
   formulation-specific evidence that directly supports this exact ingredient
   as a carbon source.
2. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
3. Re-run the focused strict/LinkML validators and the full role/evidence
   checks after the role edit.
