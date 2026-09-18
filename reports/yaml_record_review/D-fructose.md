# `data/ingredients/mapped/D-fructose.yaml`

## Verdict

Needs curation, with major synonym and role-evidence issues. The exact active
`CHEBI:15824` D-fructose identity, CAS/formula fields, 53/53 occurrence count,
and CultureMech-backed `CARBON_SOURCE` role pass, but final SSSOM still exports
the recipe annotation `Optional ingredient` as a synonym and `ENERGY_SOURCE` is
asserted only from provisional computational evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/D-fructose.yaml`.
- Current identifier and grounding: `identifier: CHEBI:15824`,
  `ontology_mapping.ontology_id: CHEBI:15824`,
  `ontology_label: D-fructose`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:15824` returns active `CHEBI:15824` labelled
  `D-fructose`, neutral formula `C6H12O6`, CAS xref `57-48-7`, and exact
  synonyms including `D-Fru`, `D-arabino-hex-2-ulose`, `D-laevulose`, and
  `Laevulose`.
- A hidden/ignored-inclusive exact `^identifier:` search under `data` found
  only this current record using `CHEBI:15824`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-arabinose.yaml data/ingredients/mapped/D-arabitol.yaml data/ingredients/mapped/D-aspartate.yaml data/ingredients/mapped/D-erythrose.yaml data/ingredients/mapped/D-fructose.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- Five `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`
  invocations, one per reviewed CHEBI-primary file in this batch: all exited 0.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with 104 non-blocking plausibility
  warnings across the full corpus.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe transformed ontology files were absent.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1334`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1334`:
  passed; 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.
- `uv run --frozen python scripts/run_shared_evidence_validator.py`: failed
  because the sibling `culturebotai-claw` evidence validator checkout is absent.

## Evidence

- The record's CAS RN and molecular formula agree with active `CHEBI:15824`.
- `mappings/culturemech_recipe_membership.tsv` contains 53 rows for
  `CHEBI:15824`, matching the record's 53/53 `occurrence_statistics`.
- The final SSSOM row publishes `MIM:D-fructose skos:exactMatch CHEBI:15824`.
  Its `other` field includes exact or kg-microbe synonyms plus `CAS:57-48-7`,
  but it also includes `Optional ingredient`.
- The hidden/ignored-inclusive `Optional ingredient` search found this same
  token in the current D-fructose, Caco3, Cellulose, and Na-acetate records,
  in the final SSSOM product, and in the synonym-enrichment review TSV. The
  term is CultureMech recipe metadata, not a D-fructose name.
- The raw `Cross-references: KEGG:fru` and `Role: Carbon source; Properties:`
  strings are retained as YAML provenance but are filtered from final SSSOM
  `other`; they do not create a current published synonym defect.
- The `CARBON_SOURCE` role has `DATABASE_ENTRY` evidence tied to the
  CultureMech `Original role text: Carbon Source` import and is supportable.
  `ENERGY_SOURCE` is supported only by a `COMPUTATIONAL_PREDICTION` that adds
  energy-source status alongside carbon-source status and calls itself
  provisional.

## Completeness

- No parent mappings, supplied-form assertions, components, environmental
  contexts, or source occurrences are asserted.
- The aggregate record in `data/curated/mapped_ingredients.yaml` round-trips
  with the per-record YAML.

## Recommended Edits

- Major: in `data/ingredients/mapped/D-fructose.yaml`, demote or reject the
  `Optional ingredient` `RAW_TEXT` synonym so the final SSSOM `other` field no
  longer exports it for `MIM:D-fructose`; rebuild the final SSSOM and rerun the
  SSSOM/product validators.
- Major: either replace the computational `ENERGY_SOURCE` evidence with direct,
  source-backed evidence for D-fructose as an energy source or remove that role
  facet; then rerun strict validation and the final SSSOM gates.
