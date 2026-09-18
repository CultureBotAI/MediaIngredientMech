# `data/ingredients/mapped/Apramycin.yaml`

## Verdict

Pass. The record exactly denotes ChEBI `apramycin`, preserves the raw
MicrobeDecoder occurrence that introduced it, and the ChEBI formula, structure,
SSSOM row, and aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Apramycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:2790` with
  `ontology_mapping.ontology_id: CHEBI:2790`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:2790` to non-obsolete ChEBI `apramycin`, formula
  `C21H41N5O11`, CAS `37321-09-8`, KEGG Compound `C01555`, the stored SMILES,
  and the stored InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits a concrete ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Apramycin.yaml data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml data/ingredients/mapped/Arabinitol.yaml data/ingredients/mapped/Arabinobiose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Apramycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:2790 CHEBI:190734 CHEBI:22605`:
  returned formula, SMILES, InChI, InChIKey, CAS, and KEGG metadata for
  `CHEBI:2790`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:2790 CHEBI:190734 CHEBI:22605`:
  returned the canonical `apramycin` label and exact/related ChEBI synonyms for
  `CHEBI:2790`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:apramycin` with raw label `apramycin`, source columns
  `BacDive_Antibiotic_resistance|BacDive_Antibiotic_sensitivity|BacDive_Metabolite_production`,
  and count 19, matching the record `source_occurrences` entry.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the
  `Apramycin.yaml` import against `CHEBI:2790`; the record history preserves
  the PENDING_REVIEW hold and later `review-ingredients` promotion.
- `mappings/ingredient_mappings.sssom.tsv` row 449 maps `MIM:Apramycin` to
  `CHEBI:2790` with `skos:exactMatch`, `manual:review-ingredients`, and
  `APPROVED`.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, SSSOM row, MicrobeDecoder review row,
  and raw ignored MicrobeDecoder source row.

## Completeness

- Formula, SMILES, InChI, ChEBI identity, non-media source occurrence, curation
  history, `ingredient_type`, SSSOM, and the aggregate copy are populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed for this ChEBI single-ingredient import.

## Recommended Edits

- None.
