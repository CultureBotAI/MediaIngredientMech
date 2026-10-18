# `data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml`

## Verdict

Needs curation, major. The local CAS identity, PubChem chemistry, and registry
SSSOM rows pass, but the ChEBI parent is the generic `sodium salt` class, the
SSSOM row exports an unrelated propionate label, and the carbon-source role is
only a provisional computational assertion.

## Identity

- Reviewed record:
  `data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:157574-76-0` with
  `ontology_mapping.ontology_id: CHEBI:26714`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- PubChem CID `132285181` reports formula `C23H38NNaO19`, the stored InChI,
  and a sodium salt with `[Na+]`, agreeing with the CAS primary identity.
- Local OAK metadata resolves `CHEBI:26714` to `sodium salt` and defines it as
  any alkali metal salt having sodium(1+) as the cation. That is a generic
  class, not a specific 6'-O-sialyllactose parent.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml data/ingredients/mapped/6-Pentyl-2H-pyran-2-one.yaml data/ingredients/mapped/6-deoxy-d-galactose.yaml data/ingredients/mapped/6-hydroxypyridine-3-carboxylic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17901 CHEBI:26714 CHEBI:66729 CHEBI:2179 CHEBI:16168 CHEBI:28847`:
  returned the expected generic `sodium salt` label for `CHEBI:26714`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17901 CHEBI:26714 CHEBI:66729 CHEBI:2179 CHEBI:16168 CHEBI:28847`:
  confirmed that `CHEBI:26714` is a generic sodium-salt class with no specific
  6'-O-sialyllactose structure.

## Evidence

- PubChem CID `132285181` lists `157574-76-0`, `6'-Sialyllactose sodium salt`,
  and related sodium-salt synonyms, and reports the same formula, connectivity
  SMILES, and InChI as the YAML.
- The SSSOM registry row to `cas:157574-76-0` and companion row to
  `kgmicrobe.compound:6-o-sialyllactose_sodium_salt` correctly preserve the
  local exact identity.
- The `skos:narrowMatch` ChEBI row to `CHEBI:26714` discards the entire glycan
  and retains only "sodium salt". That parent is too broad to be useful for the
  record's ontology mapping.
- The SSSOM row to `CHEBI:26714` exports `Propionate (sodium salt)` in `other`;
  that label is absent from the YAML and is not a synonym of 6'-O-sialyllactose
  sodium salt.
- The `CARBON_SOURCE` role is asserted only from a
  `COMPUTATIONAL_PREDICTION` placeholder that says review is recommended. No
  inspected occurrence or source entry in the record supports the role.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, three
  SSSOM rows, registry-triage rows, stale advisory rows, and ignored aggregate
  backups.

## Completeness

- CAS, formula, InChI, SMILES, PubChem CID, and the local registry SSSOM rows
  are populated.
- The exact glycan salt has useful PubChem synonyms, including
  `6'-Sialyllactose sodium salt` and `6'-SL`, but the YAML has no synonyms.

## Recommended Edits

- In `data/ingredients/mapped/6-O-sialyllactose_Sodium_Salt.yaml`, replace
  `CHEBI:26714` with a chemically relevant parent if one exists, or drop the
  ChEBI parent and keep only the local CAS and kg-microbe exact registry rows.
- Remove the stale `Propionate (sodium salt)` SSSOM `other` value at its
  maintained source, and add exact source-backed synonyms such as
  `6'-Sialyllactose sodium salt` only if they come from a maintained YAML
  synonym entry.
- Remove or evidence the provisional `CARBON_SOURCE` role, then rebuild
  `mappings/ingredient_mappings.sssom.tsv` and
  `data/curated/mapped_ingredients.yaml` and rerun strict validation, SSSOM
  invariants, and the id/label correspondence gate.
