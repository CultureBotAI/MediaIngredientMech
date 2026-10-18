# `data/ingredients/mapped/Antimycin_A3.yaml`

## Verdict

Pass. The record exactly denotes ChEBI `Antimycin A3`, preserves the
MicrobeDecoder source occurrence that introduced it, and the formula,
structure, SSSOM row, and aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Antimycin_A3.yaml`.
- Identifier and grounding: `identifier: CHEBI:197950` with
  `ontology_mapping.ontology_id: CHEBI:197950`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and EBI OLS resolve `CHEBI:197950` to non-obsolete ChEBI
  `Antimycin A3` with formula `C26H36N2O9`, SMILES matching the record, and
  the stored InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits a concrete ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Antimonate.yaml data/ingredients/mapped/Antimycin_A.yaml data/ingredients/mapped/Antimycin_A3.yaml data/ingredients/mapped/Antipyrine.yaml data/ingredients/mapped/Aphidicolin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Antimycin_A3.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30295 CHEBI:2762 CHEBI:197950 CHEBI:31225 CHEBI:2766`:
  returned formula, SMILES, InChI, InChIKey, and ChemSpider metadata for
  `CHEBI:197950`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:30295 CHEBI:2762 CHEBI:197950 CHEBI:31225 CHEBI:2766`:
  returned the canonical `Antimycin A3` label for `CHEBI:197950`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:antimycin_a3` with raw label `antimycin A3`, source column
  `BacDive_Metabolite_production`, and count 1, matching the record
  `source_occurrences` entry.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the
  `Antimycin_A3.yaml` import against `CHEBI:197950`; the record history
  preserves the PENDING_REVIEW hold and later `review-ingredients` promotion.
- `mappings/ingredient_mappings.sssom.tsv` row 439 maps
  `MIM:Antimycin_A3` to `CHEBI:197950` with `skos:exactMatch`,
  `manual:review-ingredients`, and `APPROVED`.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, `scripts`, and non-review `reports` found the active YAML,
  aggregate copy, SSSOM row, MicrobeDecoder review row, and raw ignored
  MicrobeDecoder source row.

## Completeness

- Formula, SMILES, InChI, ChEBI identity, non-media source occurrence, curation
  history, `ingredient_type`, SSSOM, and the aggregate copy are populated.
- No synonym, component, role, environmental context, discussion, or dataset
  entry is needed.

## Recommended Edits

- None.
