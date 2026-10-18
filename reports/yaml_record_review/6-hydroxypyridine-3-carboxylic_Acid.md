# `data/ingredients/mapped/6-hydroxypyridine-3-carboxylic_Acid.yaml`

## Verdict

Pass with minor issues. The CAS-backed exact `CHEBI:16168` identity, exact
synonym, chemistry, SSSOM row, and aggregate copy pass; one historic
auto-backfill `changes` string contains a truncated InChI.

## Identity

- Reviewed record:
  `data/ingredients/mapped/6-hydroxypyridine-3-carboxylic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16168` with
  `ontology_mapping.ontology_id: CHEBI:16168`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:16168` to
  `6-hydroxynicotinic acid` with formula `C6H5NO3`, the stored SMILES, and the
  stored InChI.
- Local OAK metadata carries `cas:5006-66-6` and exact synonym
  `6-hydroxypyridine-3-carboxylic acid`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml data/ingredients/mapped/6-Pentyl-2H-pyran-2-one.yaml data/ingredients/mapped/6-deoxy-d-galactose.yaml data/ingredients/mapped/6-hydroxypyridine-3-carboxylic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/6-hydroxypyridine-3-carboxylic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17901 CHEBI:26714 CHEBI:66729 CHEBI:2179 CHEBI:16168 CHEBI:28847`:
  returned the official exact and related synonym set for `CHEBI:16168`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17901 CHEBI:26714 CHEBI:66729 CHEBI:2179 CHEBI:16168 CHEBI:28847`:
  returned the expected ChEBI formula, structure strings, CAS xref, and mass
  for `CHEBI:16168`.

## Evidence

- The active ChEBI term, OAK `cas:5006-66-6` xref, PubChem CAS resolution to a
  6-hydroxynicotinic-acid CID, formula, SMILES, InChI, and exact ChEBI synonym
  support the 6-hydroxynicotinic-acid identity.
- The SSSOM row maps `MIM:6-hydroxypyridine-3-carboxylic_Acid` to
  `CHEBI:16168` with `skos:exactMatch`, `CAS:5006-66-6` in `other`, and the
  expected `CAS_RN_LOOKUP` manual provenance.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI after `.../c8-5-2-1-4(3-7-5)6(9)10/h1-3H,(H,`, but the live
  `chemical_properties.inchi` value is complete and matches ChEBI.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, source review confirmation, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes` string in
  `data/ingredients/mapped/6-hydroxypyridine-3-carboxylic_Acid.yaml` so it no
  longer shows a truncated InChI. No identity, chemistry, or SSSOM edit is
  required.
