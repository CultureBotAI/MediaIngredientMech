# `data/ingredients/mapped/Cimicifugoside_H1.yaml`

## Verdict

Pass. The `cas:163046-73-9` fallback remains an intentional local registry
identity for Cimicifugoside H1; current OLS has no exact term, PubChem resolves
the CAS to the stored formula, InChI, and SMILES, and the zero occurrence
count, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cimicifugoside_H1.yaml`.
- Identifier and grounding: `identifier: cas:163046-73-9`,
  `ontology_mapping.ontology_id: cas:163046-73-9`,
  `ontology_label: Cimicifugoside H1`, `ontology_source: CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS search for `Cimicifugoside H1` found 0 terms, preserving the
  original fallback rationale.
- PubChem lookup of CAS `163046-73-9` resolves to CID `15241163` with formula
  `C35H52O9` and the same standard InChI stored in the record.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cimicifugoside_H1.yaml data/ingredients/mapped/Cinerubin_A.yaml data/ingredients/mapped/Cinerubin_R.yaml data/ingredients/mapped/Cinnamic_Acid.yaml data/ingredients/mapped/Cinnamycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cinerubin_R.yaml data/ingredients/mapped/Cinnamic_Acid.yaml data/ingredients/mapped/Cinnamycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all three CHEBI-scoped records in this batch. `Cimicifugoside_H1`
  and `Cinerubin_A` were intentionally skipped because their `cas` and
  `kgmicrobe.compound` CURIEs are outside Engine A's OBO prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Cimicifugoside_H1` SSSOM row, the
  expected CAS unknown-term triage row, and matching aggregate/docs rows.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no `cas:163046-73-9`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The CAS fallback identifier, formula, InChI, SMILES, zero occurrence count,
  SSSOM row, aggregate copy, and docs row are populated and agree.

## Recommended Edits

- None for this record.
