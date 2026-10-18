# `data/ingredients/mapped/Isovitalex.yaml`

## Verdict

Pass. `Isovitalex` is represented as a local stock-solution registry term after
manual `#288` review found no public ontology class that denotes the named
multi-component enrichment supplement, and the final SSSOM row preserves its
CultureMech catalog aliases.

## Identity

- Reviewed record: `data/ingredients/mapped/Isovitalex.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:isovitalex` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:isovitalex`, label
  `Isovitalex`, source `kgmicrobe.ingredient`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- The record has 4 current CultureMech occurrences and two source-backed
  catalog variants: `IsoVitaleX (BD 211876)` and
  `isovitalex (BD Biosciences)`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Isovitalex.yaml data/ingredients/mapped/Isovitexin.yaml data/ingredients/mapped/Itaconate.yaml data/ingredients/mapped/Itaconic_Acid.yaml data/ingredients/mapped/Izalpinin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 3 CHEBI records.
  `Isovitalex` and `Izalpinin` were outside adapter scope because their primary
  identifiers are local `kgmicrobe.ingredient` and CAS registry CURIEs.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2120`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2120`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- The `#288` curator evidence records a search across ChEBI, NCIT, MeSH,
  FOODON, and ENVO, and classifies `Isovitalex` as a named multi-component
  preparation rather than a single substance.
- A fresh exact live OLS4 search for `Isovitalex` returned zero hits,
  supporting continued use of the local fallback registry term.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Isovitalex` to
  `kgmicrobe.ingredient:isovitalex` and exports the two CultureMech
  source-form catalog variants in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, `UNMAPPED_0407` promotion,
  current recipe memberships for all 4 occurrences, and the older unmapped OLS
  exact audit with no exact OLS hit.

## Completeness

- The local fallback identifier, stock-solution type, catalog variants,
  aggregate copy, and final SSSOM row are present and consistent.
- The record intentionally has no CAS RN, structure fields, or single-compound
  ChEBI parent.

## Recommended Edits

- None.
