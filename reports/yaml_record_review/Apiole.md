# `data/ingredients/mapped/Apiole.yaml`

## Verdict

Pass. The record exactly denotes ChEBI `Apiole`, and the CAS, formula,
structure, SSSOM row, and aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Apiole.yaml`.
- Identifier and grounding: `identifier: CHEBI:70353` with
  `ontology_mapping.ontology_id: CHEBI:70353`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and EBI OLS resolve `CHEBI:70353` to non-obsolete ChEBI `Apiole`
  with CAS `523-80-8`, KEGG Compound `C10429`, formula `C12H14O4`, SMILES, and
  the stored InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits a concrete ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Apidaecin_IB.yaml data/ingredients/mapped/Apigenin.yaml data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml data/ingredients/mapped/Apiole.yaml data/ingredients/mapped/Apple_Juice.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Apiole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18388 CHEBI:28887 CHEBI:70353`:
  returned formula, SMILES, InChI, InChIKey, CAS, and KEGG metadata for
  `CHEBI:70353`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:18388 CHEBI:28887 CHEBI:70353`:
  returned the canonical `Apiole` label for `CHEBI:70353`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The ChEBI xref for `CHEBI:70353` includes the stored CAS `523-80-8`; the
  active formula, SMILES, and InChI also match the ChEBI values.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Apiole` to `CHEBI:70353` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no mapping
  repair was needed.
- `mappings/ingredient_mappings.sssom.tsv` row 447 maps `MIM:Apiole` to
  `CHEBI:70353` with `skos:exactMatch`, CAS `523-80-8`, and a `CONFIRMED`
  trailer.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, `scripts`, and non-review `reports` found the active YAML,
  aggregate copy, SSSOM row, and row-review rows, with no active duplicate for
  `CHEBI:70353` or CAS `523-80-8`.

## Completeness

- CAS, formula, SMILES, InChI, ChEBI identity, curation history,
  `ingredient_type`, SSSOM, and the aggregate copy are populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS import rather than a media recipe ingredient.
- No synonym, component, role, environmental context, discussion, or dataset
  entry is needed.

## Recommended Edits

- None.
