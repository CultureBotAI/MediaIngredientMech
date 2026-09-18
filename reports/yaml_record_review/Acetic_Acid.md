# `data/ingredients/mapped/Acetic_Acid.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The exact `CHEBI:15366`
acetic acid identity, CAS, exact synonyms, chemistry, SSSOM row, and aggregate
copy pass, but the `ENERGY_SOURCE` role is still only a provisional
computational assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:15366` with
  `ontology_mapping.ontology_id: CHEBI:15366`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:15366` to `acetic acid` with formula
  `C2H4O2`, CAS `64-19-7`, and InChIKey
  `QTBSBXVTEAMEQO-UHFFFAOYSA-N`.
- PubChem maps CAS `64-19-7` to CID `176`; its formula and InChIKey agree with
  ChEBI.
- `kg_microbe_node_id: CHEBI:15366` agrees with the same-prefix primary
  identifier.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetamide.yaml data/ingredients/mapped/Acetate.yaml data/ingredients/mapped/Acetate_Carbon_Source.yaml data/ingredients/mapped/Acetic_Acid.yaml data/ingredients/mapped/Acetoacetate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Acetic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:27856 CHEBI:30089 CHEBI:15366 CHEBI:13705`:
  returned the expected ChEBI labels and synonyms for all four target ChEBI
  identifiers.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:27856 CHEBI:30089 CHEBI:15366 CHEBI:13705`:
  returned formula and structure metadata for all four target ChEBI identifiers.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureMech direct match, CAS `64-19-7`, official ChEBI record, local
  OAK metadata, and PubChem CID all support the exact acetic acid identity.
- The stored abbreviation, formula, food-additive, and common-name synonyms
  are ChEBI related synonyms and exact lexical names for acetic acid.
- The SSSOM row maps `MIM:Acetic_Acid` to `CHEBI:15366` with
  `skos:exactMatch` and exports the expected synonyms plus `CAS:64-19-7`.
- The `CARBON_SOURCE` role is supported by the imported CultureMech role text.
- The `ENERGY_SOURCE` role is still sourced only to a computational
  `Canonical energy substrate` assertion with its own `curator_note` saying
  review is recommended.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the active YAML,
  aggregate copy, SSSOM row, OAK/OLS confirmation row, CultureMech occurrence
  rows, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, ChEBI grounding, kg-microbe node ID,
  `ingredient_type`, occurrence counts, and exact synonyms are populated.
- The only consequential gap is evidence for the provisional
  `ENERGY_SOURCE` role.

## Recommended Edits

- Replace or remove
  `data/ingredients/mapped/Acetic_Acid.yaml`'s
  `nutritional_roles.ENERGY_SOURCE` entry after inspecting evidence that
  specifically supports acetic acid as an energy source. Re-run
  `scripts/validate_strict.py` and `scripts/validate_sssom_invariants.py`.
