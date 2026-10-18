# `data/ingredients/mapped/5-Aminolevulinic_Acid.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:17549` identity, CAS, ChEBI synonyms,
chemistry, and SSSOM row pass, but the `AMINO_ACID_SOURCE` role is only an
ancestry-inferred provisional assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/5-Aminolevulinic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:17549` with
  `ontology_mapping.ontology_id: CHEBI:17549`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:17549` is active and resolves to
  `5-aminolevulinic acid`.
- The current ChEBI page reports CAS `106-60-5`, formula `C5H9NO3`, the stored
  SMILES, and the stored InChI for `CHEBI:17549`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-vinylphenol.yaml data/ingredients/mapped/4_Carbon_Mix.yaml data/ingredients/mapped/4h-pyran-4-one.yaml data/ingredients/mapped/5-Aminolevulinic_Acid.yaml data/ingredients/mapped/5-Azacytidine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/5-Aminolevulinic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- The active ChEBI term, CAS, formula, SMILES, InChI, and two exact ChEBI
  synonyms support the 5-aminolevulinic acid identity.
- The SSSOM row maps `MIM:5-Aminolevulinic_Acid` to `CHEBI:17549` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and the expected two ChEBI
  synonyms plus `CAS:106-60-5` in `other`.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is a
  `COMPUTATIONAL_PREDICTION` inferred from ChEBI ancestry with confidence 0.70,
  and the evidence explicitly says review is recommended. The record has no
  medium-specific source showing this compound was supplied as an amino acid
  source.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy, SSSOM
  row, generated docs, source review outputs, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, exact ChEBI synonyms, and `ingredient_type` are
  populated.
- No components, environment, or discussion entries need review.

## Recommended Edits

1. Remove `nutritional_roles.AMINO_ACID_SOURCE`, or replace its evidence with a
   source that specifically supports 5-aminolevulinic acid as an amino acid
   source in a curated medium context.
