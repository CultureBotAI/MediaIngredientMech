# `data/ingredients/mapped/6-Hydroxyflavone.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:34472` identity, CAS, chemistry,
SSSOM row, and aggregate copy pass; one historic auto-backfill `changes` string
contains a truncated InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/6-Hydroxyflavone.yaml`.
- Identifier and grounding: `identifier: CHEBI:34472` with
  `ontology_mapping.ontology_id: CHEBI:34472`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:34472` to `6-Hydroxyflavone` with
  formula `C15H10O3`, CAS `6665-83-4`, the stored SMILES, and the stored
  InChI.
- Local OAK metadata carries the same formula, structure strings, CAS xref, and
  related synonym `6-Hydroxy-2-phenyl-4-benzopyrone`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-trimethoxybenzoate.yaml data/ingredients/mapped/56-dihydro-5-azathymidine.yaml data/ingredients/mapped/574-Trimethoxyisoflavone.yaml data/ingredients/mapped/5z-4-bromo-5-_Bromomethylene-2_5h-furanone.yaml data/ingredients/mapped/6-Hydroxyflavone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/6-Hydroxyflavone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:58989 CHEBI:34472`:
  returned the official ChEBI label and related synonyms for `CHEBI:34472`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:58989 CHEBI:34472`:
  returned the expected ChEBI formula, structure strings, CAS xref, and mass
  for `CHEBI:34472`.

## Evidence

- The active ChEBI term, CAS, formula, SMILES, and InChI all support the exact
  6-Hydroxyflavone identity.
- The SSSOM row maps `MIM:6-Hydroxyflavone` to `CHEBI:34472` with
  `skos:exactMatch` and `CAS:6665-83-4` in `other`.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI after `.../c16-11-6-7-14-12(8-11)13(17)9-15`, but the live
  `chemical_properties.inchi` value is complete and matches ChEBI.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, source review confirmation, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, and `ingredient_type` are populated.
- No synonyms, roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes` string in
  `data/ingredients/mapped/6-Hydroxyflavone.yaml` so it no longer shows a
  truncated InChI. No identity, chemistry, or SSSOM edit is required.
