# `data/ingredients/mapped/Antimycin_A.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS, formula, exact synonym, SSSOM
row, and aggregate copy pass, but the `SELECTIVE_AGENT` role is still only a
provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Antimycin_A.yaml`.
- Identifier and grounding: `identifier: CHEBI:2762` with
  `ontology_mapping.ontology_id: CHEBI:2762`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and EBI OLS resolve `CHEBI:2762` to non-obsolete ChEBI
  `antimycin A` with CAS `1397-94-0`, formula `C28H40N2O9`, the stored exact
  structural synonym, SMILES, and InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits a concrete ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Antimonate.yaml data/ingredients/mapped/Antimycin_A.yaml data/ingredients/mapped/Antimycin_A3.yaml data/ingredients/mapped/Antipyrine.yaml data/ingredients/mapped/Aphidicolin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Antimycin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30295 CHEBI:2762 CHEBI:197950 CHEBI:31225 CHEBI:2766`:
  returned formula, SMILES, InChI, InChIKey, CAS, and KEGG metadata for
  `CHEBI:2762`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:30295 CHEBI:2762 CHEBI:197950 CHEBI:31225 CHEBI:2766`:
  returned the canonical `antimycin A` label and the stored exact structural
  synonym for `CHEBI:2762`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The ChEBI xref for `CHEBI:2762` includes the stored CAS `1397-94-0`, and the
  exact structural synonym is also an exact ChEBI synonym.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Antimycin_A` to `CHEBI:2762` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no mapping
  repair was needed.
- `mappings/ingredient_mappings.sssom.tsv` row 438 maps `MIM:Antimycin_A` to
  `CHEBI:2762` with `skos:exactMatch`, CAS `1397-94-0`, the exact structural
  synonym, and a `CONFIRMED` trailer.
- The only `physicochemical_roles` evidence cites `Inferred from curated
  media-role name pattern` and explicitly marks the selective-agent role as
  provisional, so the current role is not supported by claim-level source
  evidence.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, `scripts`, and non-review `reports` found the active YAML,
  aggregate copy, SSSOM row, and row-review rows; it found no active duplicate
  for `CHEBI:2762` or CAS `1397-94-0`.

## Completeness

- CAS, formula, SMILES, InChI, exact synonym, ChEBI identity, curation history,
  `ingredient_type`, SSSOM, and the aggregate copy are populated.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS import rather than a media recipe ingredient.
- No component, environmental context, discussion, or dataset entry is needed.
- The unsupported selective-agent role is the only consequential gap.

## Recommended Edits

- In `data/ingredients/mapped/Antimycin_A.yaml`, remove
  `physicochemical_roles.SELECTIVE_AGENT` unless direct source evidence for
  Antimycin A as a selective agent is attached to that role.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Antimycin_A.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
