# `data/ingredients/mapped/Acetomycin.yaml`

## Verdict

Pass. The exact `CHEBI:209246` identity, microbedecoder source occurrence,
ChEBI chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:209246` with
  `ontology_mapping.ontology_id: CHEBI:209246`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- ChEBI resolves `CHEBI:209246` to `Acetomycin` with formula `C10H14O5` and
  InChIKey `OYMZTORLGBISLR-RHFNHBFPSA-N`.
- Local OAK metadata carries the same formula, stereochemical SMILES, and
  InChI for the same ChEBI compound.
- `ingredient_type: SINGLE_INGREDIENT` is present, and the
  `source_occurrences` entry preserves the microbedecoder
  `BacDive_Metabolite_production` provenance.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetoin.yaml data/ingredients/mapped/Acetomycin.yaml data/ingredients/mapped/Acetone.yaml data/ingredients/mapped/Acetosyringone.yaml data/ingredients/mapped/Acetovanillone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Acetomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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

- The microbedecoder import used an OLS label-exact ChEBI match from
  `kgmicrobe.trait:acetomycin`, and ChEBI confirms that `CHEBI:209246` denotes
  Acetomycin.
- Local OAK metadata, ChEBI, and the live `chemical_properties` agree on the
  formula, stereochemical SMILES, InChI, InChIKey, and molecular weight for
  Acetomycin.
- The SSSOM row maps `MIM:Acetomycin` to `CHEBI:209246` with
  `skos:exactMatch` and the approved microbedecoder review trailer.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the active YAML,
  aggregate copies, SSSOM row, microbedecoder import row, manual approval
  trail, and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, ChEBI grounding, microbedecoder provenance, and
  `ingredient_type` are populated.
- No CAS, role, component, environmental context, or discussion entry is needed
  for this sparse single-ingredient record.

## Recommended Edits

- None.
