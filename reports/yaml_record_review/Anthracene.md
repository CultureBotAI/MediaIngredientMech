# `data/ingredients/mapped/Anthracene.yaml`

## Verdict

Pass. The record exactly denotes ChEBI `anthracene`, preserves the
MicrobeDecoder source occurrence that introduced it, and the ChEBI formula,
structure, SSSOM row, and aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Anthracene.yaml`.
- Identifier and grounding: `identifier: CHEBI:35298` with
  `ontology_mapping.ontology_id: CHEBI:35298`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and EBI OLS resolve `CHEBI:35298` to non-obsolete ChEBI
  `anthracene`, formula `C14H10`, CAS `120-12-7`, KEGG Compound `C14315`,
  SMILES `c1ccc2cc3ccccc3cc2c1`, and the stored InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits a concrete ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Anisodamine_Hydrobromide.yaml data/ingredients/mapped/Anthracene.yaml data/ingredients/mapped/Anthracycline_Antibiotic.yaml data/ingredients/mapped/Anthranilamide.yaml data/ingredients/mapped/Anthranilic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anthracene.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:35298 CHEBI:49322 CHEBI:193638 CHEBI:30754`:
  returned formula, SMILES, InChI, InChIKey, CAS, and KEGG metadata for
  `CHEBI:35298`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:35298 CHEBI:49322 CHEBI:193638 CHEBI:30754`:
  returned the canonical `anthracene` label and exact ChEBI synonyms for
  `CHEBI:35298`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:anthracene` with raw label `anthracene`, source column
  `BacDive_Metabolite_utilization`, and count 1, matching the record
  `source_occurrences` entry.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the
  `Anthracene.yaml` import against `CHEBI:35298`; the record history preserves
  the PENDING_REVIEW hold and later `review-ingredients` promotion.
- `mappings/ingredient_mappings.sssom.tsv` row 433 maps `MIM:Anthracene` to
  `CHEBI:35298` with `skos:exactMatch`, `manual:review-ingredients`, and
  `APPROVED`.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, and `scripts` found the active YAML, aggregate copy, SSSOM row,
  MicrobeDecoder review row, and the raw ignored MicrobeDecoder source row.

## Completeness

- Formula, SMILES, InChI, ChEBI identity, non-media source occurrence, curation
  history, `ingredient_type`, SSSOM, and the aggregate copy are populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed for this ChEBI single-ingredient import.

## Recommended Edits

- None.
