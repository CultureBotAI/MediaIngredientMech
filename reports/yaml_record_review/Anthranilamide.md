# `data/ingredients/mapped/Anthranilamide.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup resolves to ChEBI `2-Aminobenzamide`, the
preferred term is the same anthranilamide molecule, and CAS, formula,
structure, SSSOM, and the aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Anthranilamide.yaml`.
- Identifier and grounding: `identifier: CHEBI:193638` with
  `ontology_mapping.ontology_id: CHEBI:193638`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Local OAK and EBI OLS resolve `CHEBI:193638` to non-obsolete ChEBI
  `2-Aminobenzamide` with CAS `88-68-6`, formula `C7H8N2O`, SMILES
  `NC(=O)c1ccccc1N`, and the stored InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits a concrete ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Anisodamine_Hydrobromide.yaml data/ingredients/mapped/Anthracene.yaml data/ingredients/mapped/Anthracycline_Antibiotic.yaml data/ingredients/mapped/Anthranilamide.yaml data/ingredients/mapped/Anthranilic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anthranilamide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:35298 CHEBI:49322 CHEBI:193638 CHEBI:30754`:
  returned formula, SMILES, InChI, InChIKey, CAS, and KEGG metadata for
  `CHEBI:193638`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:35298 CHEBI:49322 CHEBI:193638 CHEBI:30754`:
  returned the canonical `2-Aminobenzamide` label and exact `2-aminobenzamide`
  synonym for `CHEBI:193638`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The ChEBI xref for `CHEBI:193638` includes the record CAS `88-68-6`, matching
  the CultureBotHT lookup evidence and stored `chemical_properties.cas_rn`.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` already reviewed
  the apparent `anthranilamide` to `2-Aminobenzamide` label mismatch as
  represented, and `mappings/ingredient_mappings_row_review_manifest.tsv`
  carries that `ALREADY_REPRESENTED` disposition.
- `mappings/ingredient_mappings.sssom.tsv` row 435 maps `MIM:Anthranilamide` to
  `CHEBI:193638` with `skos:exactMatch`, CAS `88-68-6`, and
  `OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07`.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, and `scripts` found the active YAML, aggregate copy, SSSOM row,
  and row-review entries, with no active duplicate for CAS `88-68-6`.

## Completeness

- CAS, formula, SMILES, InChI, ChEBI identity, curation history,
  `ingredient_type`, SSSOM, and the aggregate copy are populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS lookup rather than a media recipe ingredient.
- No synonym, component, role, environmental context, discussion, or dataset
  entry is needed.

## Recommended Edits

- None.
