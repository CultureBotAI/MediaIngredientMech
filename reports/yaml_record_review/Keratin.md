# `data/ingredients/mapped/Keratin.yaml`

## Verdict

Needs curation. The singular Keratin record is intentionally a close match to
the broader MeSH plural `Keratins` class, but the final SSSOM row publishes that
close parent mapping as `skos:exactMatch`.

## Identity

- Reviewed record: `data/ingredients/mapped/Keratin.yaml`.
- Identifier and grounding: `identifier: mesh:D007633` with
  `ontology_mapping.ontology_id: mesh:D007633`, label `Keratins`, source
  `MESH`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `media_count: 1`.
- Chemical properties: intentionally absent; the record is grounded to MeSH
  rather than a structure-bearing ChEBI or CAS term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Kcl.yaml data/ingredients/mapped/Keratin.yaml data/ingredients/mapped/Ketomycin.yaml data/ingredients/mapped/Kf.yaml data/ingredients/mapped/Kh2po4.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2245`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2245`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `mesh:D007633` as active MeSH term `Keratins` and lists
  `Keratin` as a synonym, matching the #213 decision to keep this as a
  `CLOSE_MATCH` because the ontology term is a plural class.
- Major: `mappings/ingredient_mappings.sssom.tsv` publishes `MIM:Keratin` to
  `mesh:D007633` as `skos:exactMatch`, contradicting the curated
  `mapping_quality: CLOSE_MATCH`. The row should be `skos:closeMatch`.
- Minor: `notes` still carries the original "Curator review needed" text even
  though #213 and `promote_resolved_unmapped` supplied the MeSH parent mapping.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM row, docs projections, and no current SSSOM invariant reject; it
  found no hits in `reports/kg_microbe_node_id_mismatches.tsv`,
  `reports/hydrate_grounding.tsv`, or `mappings/needs_curator_review.tsv`.

## Completeness

- The MeSH parent mapping, aggregate copy, and occurrence count are present.
- The final SSSOM is incomplete until the published predicate matches the
  curated `CLOSE_MATCH` semantics.

## Recommended Edits

- Major: regenerate or repair `mappings/ingredient_mappings.sssom.tsv` so
  `MIM:Keratin` maps to `mesh:D007633` with `skos:closeMatch`, then rerun
  SSSOM invariants and id-label validation.
- Minor: refresh `notes` in `data/ingredients/mapped/Keratin.yaml` so it no
  longer says curator review is pending after the MeSH repair.
