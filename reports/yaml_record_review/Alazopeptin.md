# `data/ingredients/mapped/Alazopeptin.yaml`

## Verdict

Pass. The exact `CHEBI:222816` identity, MicrobeDecoder production occurrence,
ChEBI/PubChem chemistry, review-ingredients approval, SSSOM row, and aggregate
copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Alazopeptin.yaml`.
- Identifier and grounding: `identifier: CHEBI:222816` with
  `ontology_mapping.ontology_id: CHEBI:222816`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:222816` to
  `Alazopeptin` with formula `C15H20N6O5`, SMILES, InChI, and InChIKey
  `LYUGICBKRYXVHJ-UHFFFAOYSA-N`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alazopeptin.yaml data/ingredients/mapped/Alboverticillin.yaml data/ingredients/mapped/Alcl3.yaml data/ingredients/mapped/Alcl3_X_6_H2o.yaml data/ingredients/mapped/Algal_Trace_Elements_Solution.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alazopeptin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:222816 CHEBI:30114 CHEBI:30115`:
  returned the expected labels and aliases for all three ChEBI terms checked in
  this batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:222816 CHEBI:30114 CHEBI:30115`:
  returned formula, charge, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:222816`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:alazopeptin` in `BacDive_Metabolite_production` with count
  `1`, matching `source_occurrences`.
- `mappings/ingredient_mappings.sssom.tsv` row 361 maps `MIM:Alazopeptin` to
  `CHEBI:222816` with `skos:exactMatch` and the expected
  review-ingredients `APPROVED` trailer.
- The ChEBI page and local ChEBI metadata support the stored formula, SMILES,
  InChI, and molecular weight.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the
  active YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence,
  generated indexes, and ignored aggregate backups.

## Completeness

- Formula, SMILES, InChI, source occurrence, curation history, and
  `ingredient_type` are populated.
- No CAS, role, component, environmental context, discussion, or dataset entry
  is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
