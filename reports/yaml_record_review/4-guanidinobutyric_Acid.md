# `data/ingredients/mapped/4-guanidinobutyric_Acid.yaml`

## Verdict

Pass, none. The `CHEBI:15728` identity, CAS-backed grounding, exact synonyms,
chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-guanidinobutyric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:15728` with
  `ontology_mapping.ontology_id: CHEBI:15728`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:15728` is active, resolves to
  `4-guanidinobutanoic acid`, defines the 4-guanidino derivative of butanoic
  acid, and has formula `C5H11N3O2`, CAS `463-00-3`, SMILES
  `N=C(N)NCCCC(=O)O`, and the stored InChI.
- PubChem lookup for `4-guanidinobutanoic acid` resolves to CID `500` with
  formula `C5H11N3O2` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-coumarate.yaml data/ingredients/mapped/4-dihydroxy-biphenyl.yaml data/ingredients/mapped/4-guanidinobutyric_Acid.yaml data/ingredients/mapped/4-hydroxy-L-proline.yaml data/ingredients/mapped/4-hydroxybenzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-guanidinobutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2,951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, K; Rule B4 was skipped because the
  sibling `kg-microbe` ontology transforms are absent.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed;
  `docs/data/` is fresh and every curated label is published.

## Evidence

- ChEBI now carries the same CAS, formula, SMILES, and InChI that the record
  imported through PubChem-backed FEBA enrichment.
- Every active `kg_microbe` synonym is present on the current ChEBI term:
  `4-(carbamimidamido)butanoic acid`, `4-carbamimidamidobutanoic acid`,
  `4-guanidinobutanoic acid`, `gamma-Guanidinobutyrate`, and
  `gamma-Guanidinobutyric acid`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:4_Guanidinobutyric_acid` alias to `CHEBI:15728` mapping and asked for
  no curation action.
- The SSSOM row maps `MIM:4-guanidinobutyric_Acid` to `CHEBI:15728` with
  `skos:exactMatch` and carries only ChEBI-backed synonyms plus `CAS:463-00-3`
  in `other`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, `tests`, `scripts`, `conf`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, FEBA occurrence rows, and ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, synonyms, FEBA occurrence counts, and
  `ingredient_type` are populated.
- No roles, components, environment, or discussion entries need review.
- The Edison advisory row that asked for independent CURIE verification is
  stale relative to the current ChEBI and PubChem checks.

## Recommended Edits

No YAML edit is required for this record.
