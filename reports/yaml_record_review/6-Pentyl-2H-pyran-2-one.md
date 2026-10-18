# `data/ingredients/mapped/6-Pentyl-2H-pyran-2-one.yaml`

## Verdict

Pass, none. The CAS primary identity, exact ChEBI identity row, PubChem
chemistry, SSSOM rows, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/6-Pentyl-2H-pyran-2-one.yaml`.
- Identifier and grounding: `identifier: cas:27593-23-3` with
  `ontology_mapping.ontology_id: CHEBI:66729`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- PubChem CID `33960` reports CAS `27593-23-3`, formula `C10H14O2`, the stored
  SMILES, and the stored InChI.
- The official ChEBI page resolves `CHEBI:66729` to
  `6-n-Pentyl-alpha-pyrone` with the same formula, SMILES, InChI, and
  InChIKey. That confirms the #326 regrade from parent to identity.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml data/ingredients/mapped/6-Pentyl-2H-pyran-2-one.yaml data/ingredients/mapped/6-deoxy-d-galactose.yaml data/ingredients/mapped/6-hydroxypyridine-3-carboxylic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/6-Pentyl-2H-pyran-2-one.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17901 CHEBI:26714 CHEBI:66729 CHEBI:2179 CHEBI:16168 CHEBI:28847`:
  returned the official related synonym set for `CHEBI:66729`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17901 CHEBI:26714 CHEBI:66729 CHEBI:2179 CHEBI:16168 CHEBI:28847`:
  returned the expected ChEBI formula, structure strings, and mass for
  `CHEBI:66729`.

## Evidence

- PubChem and ChEBI agree on formula, SMILES, InChI, and InChIKey for the
  6-pentyl-2H-pyran-2-one identity.
- PubChem CID `33960` lists `6-Pentyl-2H-pyran-2-one`,
  `6-n-pentyl-alpha-pyrone`, and `27593-23-3`, supporting both the local CAS
  identity and the ChEBI synonym match.
- The SSSOM export has the expected exact identity row to `CHEBI:66729` and
  registry row to `cas:27593-23-3`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  rows, row-review rows for the ChEBI/CAS/kgmicrobe surfaces, and ignored
  aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, PubChem CID, the same-formula ChEBI mapping, and
  `ingredient_type` are populated.
- No synonyms, roles, components, source occurrences, environmental context, or
  discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
