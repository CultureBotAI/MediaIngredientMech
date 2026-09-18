# `data/ingredients/mapped/Acetamide.yaml`

## Verdict

Pass. The exact `CHEBI:27856` identity, microbedecoder source occurrence,
ChEBI/PubChem chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetamide.yaml`.
- Identifier and grounding: `identifier: CHEBI:27856` with
  `ontology_mapping.ontology_id: CHEBI:27856`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:27856` to `acetamide` with formula
  `C2H5NO`, CAS `60-35-5`, and InChIKey `DLFVBJFMPXGRIB-UHFFFAOYSA-N`.
- PubChem maps CAS `60-35-5` to CID `178`; its formula and InChIKey agree with
  ChEBI.
- `ingredient_type: SINGLE_INGREDIENT` is present, and the
  `source_occurrences` entry preserves the microbedecoder
  `BacDive_Metabolite_utilization` provenance.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetamide.yaml data/ingredients/mapped/Acetate.yaml data/ingredients/mapped/Acetate_Carbon_Source.yaml data/ingredients/mapped/Acetic_Acid.yaml data/ingredients/mapped/Acetoacetate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Acetamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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

- The microbedecoder import used an OLS label-exact ChEBI match from
  `kgmicrobe.trait:acetamide`, and ChEBI confirms that `CHEBI:27856` denotes
  acetamide.
- The live `chemical_properties` formula, SMILES, InChI, and molecular weight
  match the OAK, ChEBI, and PubChem structures for `CHEBI:27856`.
- The SSSOM row maps `MIM:Acetamide` to `CHEBI:27856` with
  `skos:exactMatch` and the approved microbedecoder review trailer.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the active YAML,
  aggregate copies, SSSOM row, microbedecoder import row, manual approval
  trail, and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, ChEBI grounding, microbedecoder provenance, and
  `ingredient_type` are populated.
- No role, component, environmental context, or discussion entry is needed for
  this sparse single-ingredient record.

## Recommended Edits

- None.
