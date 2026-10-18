# `data/ingredients/mapped/Anthranilic_Acid.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS, formula, exact synonym, SSSOM
row, and aggregate copy all pass, but the `AMINO_ACID_SOURCE` nutritional role
is only a provisional ChEBI-ancestry inference and has no direct media-use
evidence for anthranilic acid.

## Identity

- Reviewed record: `data/ingredients/mapped/Anthranilic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30754` with
  `ontology_mapping.ontology_id: CHEBI:30754`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and EBI OLS resolve `CHEBI:30754` to non-obsolete ChEBI
  `anthranilic acid` with CAS `118-92-3`, formula `C7H7NO2`, exact synonym
  `2-AMINOBENZOIC ACID`, SMILES `Nc1ccccc1C(=O)O`, and the stored InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits a concrete ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Anisodamine_Hydrobromide.yaml data/ingredients/mapped/Anthracene.yaml data/ingredients/mapped/Anthracycline_Antibiotic.yaml data/ingredients/mapped/Anthranilamide.yaml data/ingredients/mapped/Anthranilic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anthranilic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:35298 CHEBI:49322 CHEBI:193638 CHEBI:30754`:
  returned formula, SMILES, InChI, InChIKey, CAS, and KEGG metadata for
  `CHEBI:30754`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:35298 CHEBI:49322 CHEBI:193638 CHEBI:30754`:
  returned the canonical `anthranilic acid` label, exact
  `2-AMINOBENZOIC ACID` synonym, and related synonyms for `CHEBI:30754`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The ChEBI xref for `CHEBI:30754` includes the stored CAS `118-92-3`, and
  ChEBI's exact synonyms include the stored exact synonym
  `2-AMINOBENZOIC ACID`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Anthranilic_Acid` to `CHEBI:30754` row, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no mapping
  repair was needed.
- `mappings/ingredient_mappings.sssom.tsv` row 436 maps
  `MIM:Anthranilic_Acid` to `CHEBI:30754` with `skos:exactMatch`, CAS
  `118-92-3`, synonym `2-AMINOBENZOIC ACID`, and a `CONFIRMED` trailer.
- The `nutritional_roles` entry cites only `Inferred from CHEBI ancestry:
  subclass/has_role of CHEBI:33709 (amino acid)` and explicitly says the
  role is provisional; that does not establish anthranilic acid as an amino
  acid source in a medium.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, and `scripts` found the active YAML, aggregate copy, SSSOM row,
  row-review entries, and the sibling `2-aminobenzoate` record but no direct
  source occurrence or recipe evidence for an anthranilic-acid
  `AMINO_ACID_SOURCE` role.

## Completeness

- CAS, formula, SMILES, InChI, exact synonym, ChEBI identity, curation history,
  `ingredient_type`, SSSOM, and the aggregate copy are populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS import rather than a media recipe ingredient.
- No component, environmental context, discussion, or dataset entry is needed.
- The only consequential gap is the unsupported nutritional role.

## Recommended Edits

- In `data/ingredients/mapped/Anthranilic_Acid.yaml`, remove
  `nutritional_roles.AMINO_ACID_SOURCE` unless a direct medium source shows that
  anthranilic acid is being used as an amino acid source in this corpus.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anthranilic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
