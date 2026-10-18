# `data/ingredients/mapped/Azlocillin_Sodium_Salt.yaml`

## Verdict

Pass. The CultureBotHT CAS lookup exact-maps to non-obsolete `CHEBI:51864`
`azlocillin sodium`, the CAS, formula, InChI, SMILES, and exact synonym all
describe the sodium salt, and the SSSOM row plus aggregate copy are
synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Azlocillin_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:51864` with
  `ontology_mapping.ontology_id: CHEBI:51864`,
  `ontology_label: azlocillin sodium`, `ontology_source: CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:51864` to non-obsolete `azlocillin sodium` with CAS
  `37091-65-9`, formula `C20H22N5O6S.Na`, the same InChI and SMILES stored
  locally, and the local exact synonym.
- PubChem lookup for CAS `37091-65-9` resolves to title `Azlocillin Sodium`
  with the same standard InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azithromycin.yaml data/ingredients/mapped/Azlocillin.yaml data/ingredients/mapped/Azlocillin_Sodium_Salt.yaml data/ingredients/mapped/Azomycin.yaml data/ingredients/mapped/Aztreonam.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Azlocillin_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:51864` and PubChem lookup for CAS `37091-65-9`
  confirmed the exact sodium-salt identity and structure.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 513 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm the
  `CHEBI:51864` OAK/OLS mapping.
- The ChEBI exact synonym
  `sodium 2,2-dimethyl-6beta-[(2R)-2-{[(2-oxoimidazolidin-1-yl)carbonyl]amino}-2-phenylacetamido]penam-3alpha-carboxylate`
  is preserved as an `EXACT_SYNONYM` and appears in the SSSOM `other` field
  alongside `CAS:37091-65-9`.
- The CAS lookup provenance, later `CAS_RN_LOOKUP` regrade, local structure
  fields, and SSSOM row all point to the sodium salt rather than the parent
  azlocillin acid.

## Completeness

- The exact identifier, CAS, formula, InChI, SMILES, exact synonym, provisional
  `SELECTIVE_AGENT` role, SSSOM row, and aggregate copy are populated.
- The 0/0 occurrence count is correct for a CultureBotHT-only compound not
  present in CultureMech recipe memberships.

## Recommended Edits

- None.
