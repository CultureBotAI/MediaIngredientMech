# `data/ingredients/mapped/Hydroxystreptomycin.yaml`

## Verdict

Needs curation. The record says the relationship to
`CHEBI:24750` `5'-hydroxystreptomycin` is only close, but it also uses that
same CHEBI CURIE as its primary identifier, so the final SSSOM is forced to
publish an exact own-identifier row.

## Identity

- Reviewed record: `data/ingredients/mapped/Hydroxystreptomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:24750` with
  `ontology_mapping.ontology_id: CHEBI:24750`, label
  `5'-hydroxystreptomycin`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Source occurrences: one MicrobeDecoder occurrence from
  `BacDive_Metabolite_production`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Hydroxyacetophenone.yaml data/ingredients/mapped/Hydroxyethylcellulose.yaml data/ingredients/mapped/Hydroxylamine_Hydrochloride.yaml data/ingredients/mapped/Hydroxystreptomycin.yaml data/ingredients/mapped/Hydroxyurea.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Hydroxystreptomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1510`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1510`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:24750` as the active ChEBI class
  `5'-hydroxystreptomycin` and lists `Hydroxystreptomycin` as a related
  synonym.
- Major: the YAML stores `mapping_quality: CLOSE_MATCH`, but the record primary
  identifier and ontology target are both `CHEBI:24750`. A close ChEBI target
  should be paired with a distinct local subject, or the record should be
  regraded to an exact/synonym match if curator review decides the unqualified
  MicrobeDecoder label denotes `5'-hydroxystreptomycin`.
- Major: because the record uses its close-match target as its own identifier,
  the final SSSOM publishes a `skos:exactMatch` row from
  `MIM:Hydroxystreptomycin` to `CHEBI:24750` despite the close-match YAML
  grade.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and open
  `mappings/record_research_validation.tsv` rows that still dispute the older
  close-match state and missing chemistry.

## Completeness

- The promoted ChEBI target is active and the aggregate copy is synchronized.
- The record is incomplete until the exact-vs-close decision, primary
  identifier, mapping quality, and generated SSSOM predicate all agree.

## Recommended Edits

- Major: either regrade the record to an exact or synonym match to
  `CHEBI:24750` with source-backed chemistry fields, or keep the unqualified
  hydroxystreptomycin label under a distinct local primary identifier with a
  `skos:closeMatch` to `CHEBI:24750`; then regenerate the SSSOM and rerun
  strict, term, round-trip, id-label, component, and SSSOM validation.
