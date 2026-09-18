# `data/ingredients/mapped/Acetaldehyde.yaml`

## Verdict

Pass. The exact `CHEBI:15343` identity, CAS, chemistry, SSSOM row, and
aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetaldehyde.yaml`.
- Identifier and grounding: `identifier: CHEBI:15343` with
  `ontology_mapping.ontology_id: CHEBI:15343`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:15343` to `acetaldehyde` with
  formula `C2H4O`, CAS `75-07-0`, and InChIKey
  `IKHGUXGNUITLKF-UHFFFAOYSA-N`.
- PubChem maps CAS `75-07-0` to CID `177`; its formula and InChIKey agree with
  ChEBI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Abyssomicin_G.yaml data/ingredients/mapped/Abyssomicin_H.yaml data/ingredients/mapped/Acacetin.yaml data/ingredients/mapped/Aces.yaml data/ingredients/mapped/Acetaldehyde.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Acetaldehyde.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:15335 CHEBI:15343 CHEBI:39060 CHEBI:39061`:
  returned the expected labels, exact synonyms, and related synonyms for
  `CHEBI:15335`, `CHEBI:15343`, `CHEBI:39060`, and `CHEBI:39061`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:15335 CHEBI:15343 CHEBI:39060 CHEBI:39061`:
  returned formula and structure metadata for `CHEBI:15335`, `CHEBI:15343`,
  and `CHEBI:39060`; `CHEBI:39061` resolved only as the structureless `ACES`
  class.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT import, official ChEBI record, local OAK metadata, and
  PubChem CID all support the exact acetaldehyde identity.
- The live formula, SMILES, and InChI match ChEBI for `CHEBI:15343`.
- The SSSOM row maps `MIM:Acetaldehyde` to `CHEBI:15343` with
  `skos:exactMatch` and exports `CAS:75-07-0`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the active YAML,
  aggregate copy, SSSOM row, OAK/OLS confirmation row, and ignored aggregate
  backups.

## Completeness

- CAS, formula, InChI, SMILES, and `ingredient_type` are populated.
- No exact synonym, role, component, source occurrence, environmental context,
  or discussion entry is needed.

## Recommended Edits

- None.
