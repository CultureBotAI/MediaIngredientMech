# `data/ingredients/mapped/Acetone.yaml`

## Verdict

Pass. The exact `CHEBI:15347` identity, exact synonym, CAS, chemistry, SSSOM
row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetone.yaml`.
- Identifier and grounding: `identifier: CHEBI:15347` with
  `ontology_mapping.ontology_id: CHEBI:15347`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:15347` to `acetone` with formula
  `C3H6O`, CAS `67-64-1`, and InChIKey `CSCPPACGZOOCGX-UHFFFAOYSA-N`.
- PubChem maps CAS `67-64-1` to CID `180`; its formula and InChIKey agree with
  ChEBI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetoin.yaml data/ingredients/mapped/Acetomycin.yaml data/ingredients/mapped/Acetone.yaml data/ingredients/mapped/Acetosyringone.yaml data/ingredients/mapped/Acetovanillone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Acetone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:15688 CHEBI:209246 CHEBI:15347 CHEBI:2404 CHEBI:2781`:
  returned the expected ChEBI labels and synonyms for all five target ChEBI
  identifiers.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:15688 CHEBI:209246 CHEBI:15347 CHEBI:2404 CHEBI:2781`:
  returned formula and structure metadata for all five target ChEBI identifiers.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT import, CAS `67-64-1`, official ChEBI record, local OAK
  metadata, and PubChem CID all support the exact acetone identity.
- The stored `propan-2-one` synonym is the ChEBI exact synonym.
- The SSSOM row maps `MIM:Acetone` to `CHEBI:15347` with `skos:exactMatch` and
  exports `propan-2-one` plus `CAS:67-64-1`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the active YAML,
  aggregate copy, SSSOM row, OAK/OLS confirmation row, and ignored aggregate
  backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No role, component, environmental context, or discussion entry is needed.

## Recommended Edits

- None.
