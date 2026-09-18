# `data/ingredients/mapped/Aztreonam.yaml`

## Verdict

Pass. The CultureBotHT import exact-maps to non-obsolete `CHEBI:161680`
`aztreonam`, the CAS, formula, InChI, SMILES, and exact synonym all describe
the same zwitterionic compound, and the SSSOM row plus aggregate copy are
synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Aztreonam.yaml`.
- Identifier and grounding: `identifier: CHEBI:161680` with
  `ontology_mapping.ontology_id: CHEBI:161680`,
  `ontology_label: aztreonam`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:161680` to non-obsolete `aztreonam` with CAS
  `78110-38-0`, formula `C13H17N5O8S2`, the same InChI and SMILES stored
  locally, and the local exact synonym.
- PubChem lookup for CAS `78110-38-0` resolves to title `Aztreonam` with the
  same formula and standard InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Azithromycin.yaml data/ingredients/mapped/Azlocillin.yaml data/ingredients/mapped/Azlocillin_Sodium_Salt.yaml data/ingredients/mapped/Azomycin.yaml data/ingredients/mapped/Aztreonam.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Aztreonam.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:161680` and PubChem lookup for CAS `78110-38-0`
  confirmed the exact identity and structure.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 515 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` confirm the
  `CHEBI:161680` OAK/OLS mapping.
- The MicrobeDecoder inventory also contains `aztreonam`, but the current
  record was owned by the earlier CultureBotHT import with CAS `78110-38-0`;
  both source surfaces point to the same ChEBI identity.
- The ChEBI exact synonym is preserved as an `EXACT_SYNONYM` and appears in
  the SSSOM `other` field alongside `CAS:78110-38-0`.

## Completeness

- The exact identifier, CAS, formula, InChI, SMILES, exact synonym, provisional
  `SELECTIVE_AGENT` role, SSSOM row, and aggregate copy are populated.
- The 0/0 occurrence count is correct for a CultureBotHT-only compound not
  counted as a CultureMech recipe membership in MIM.

## Recommended Edits

- None.
