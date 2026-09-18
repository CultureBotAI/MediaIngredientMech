# `data/ingredients/mapped/4-hydroxybenzoic_Acid.yaml`

## Verdict

Pass, none. The `CHEBI:30763` identity, CAS, exact synonyms, carbon-source role,
chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-hydroxybenzoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30763` with
  `ontology_mapping.ontology_id: CHEBI:30763`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:30763` is active, resolves to
  `4-hydroxybenzoic acid`, defines the para monohydroxybenzoic acid, and has
  formula `C7H6O3`, CAS `99-96-7`, SMILES `O=C(O)c1ccc(O)cc1`, and the stored
  InChI.
- PubChem CAS lookup for `99-96-7` resolves to CID `135` with formula
  `C7H6O3` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-coumarate.yaml data/ingredients/mapped/4-dihydroxy-biphenyl.yaml data/ingredients/mapped/4-guanidinobutyric_Acid.yaml data/ingredients/mapped/4-hydroxy-L-proline.yaml data/ingredients/mapped/4-hydroxybenzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-hydroxybenzoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2,951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, K; Rule B4 was skipped because the
  sibling `kg-microbe` ontology transforms are absent.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed;
  `docs/data/` is fresh and every curated label is published.

## Evidence

- The current ChEBI term carries the same CAS, formula, SMILES, and InChI that
  the record populated through PubChem.
- ChEBI lists the active `kg_microbe` synonyms `4-carboxyphenol`,
  `P-HYDROXYBENZOIC ACID`, and `p-salicylic acid` on the same term.
- `nutritional_roles.CARBON_SOURCE` is supported by the imported CultureMech
  role text and kept narrowly as `Original role text: Carbon Source`.
- The `RAW_TEXT` CultureMech source string that included role and property
  descriptors is retained in YAML for traceability but is correctly suppressed
  from SSSOM `other`; only ChEBI-backed synonyms and `CAS:99-96-7` publish.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the mapping and
  asked for no curation action.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, `tests`, `scripts`, `conf`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, CultureMech occurrence rows, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, exact synonyms, the carbon-source role,
  CultureMech occurrence counts, and `ingredient_type` are populated.
- No components, environment, datasets, or discussion entries need review.

## Recommended Edits

No YAML edit is required for this record.
