# `data/ingredients/mapped/Apigenin.yaml`

## Verdict

Pass. The record exactly denotes ChEBI `apigenin`, and the CAS, formula, exact
synonym, structure, SSSOM row, and aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Apigenin.yaml`.
- Identifier and grounding: `identifier: CHEBI:18388` with
  `ontology_mapping.ontology_id: CHEBI:18388`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and EBI OLS resolve `CHEBI:18388` to non-obsolete ChEBI `apigenin`
  with CAS `520-36-5`, formula `C15H10O5`, exact synonym
  `5,7-dihydroxy-2-(4-hydroxyphenyl)-4H-chromen-4-one`, SMILES, and the stored
  InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits a concrete ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Apidaecin_IB.yaml data/ingredients/mapped/Apigenin.yaml data/ingredients/mapped/Apigenin_Dimethyl_Ether.yaml data/ingredients/mapped/Apiole.yaml data/ingredients/mapped/Apple_Juice.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Apigenin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18388 CHEBI:28887 CHEBI:70353`:
  returned formula, SMILES, InChI, InChIKey, CAS, KEGG, and HMDB metadata for
  `CHEBI:18388`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:18388 CHEBI:28887 CHEBI:70353`:
  returned the canonical `apigenin` label and the stored exact ChEBI synonym.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The ChEBI xref for `CHEBI:18388` includes the stored CAS `520-36-5`, and the
  exact structural synonym is also an exact ChEBI synonym.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Apigenin` to `CHEBI:18388` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no mapping
  repair was needed.
- `mappings/ingredient_mappings.sssom.tsv` row 443 maps `MIM:Apigenin` to
  `CHEBI:18388` with `skos:exactMatch`, CAS `520-36-5`, the exact structural
  synonym, and a `CONFIRMED` trailer.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, `scripts`, and non-review `reports` found the active YAML,
  aggregate copy, SSSOM row, and row-review rows, with no active duplicate for
  `CHEBI:18388` or CAS `520-36-5`.

## Completeness

- CAS, formula, SMILES, InChI, exact synonym, ChEBI identity, curation history,
  `ingredient_type`, SSSOM, and the aggregate copy are populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS import rather than a media recipe ingredient.
- No component, role, environmental context, discussion, or dataset entry is
  needed.

## Recommended Edits

- None.
