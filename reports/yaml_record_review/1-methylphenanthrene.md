# `data/ingredients/mapped/1-methylphenanthrene.yaml`

## Verdict

Pass with minor issues. The active exact mapping to `CHEBI:35860` is supported
by current ChEBI and all synchronized products agree; the remaining issues are
non-blocking stale advisory rows, an optional missing CAS RN enrichment, and a
historical promotion event whose timestamp sorts before the review flag it
resolved.

## Identity

- Reviewed record:
  `data/ingredients/mapped/1-methylphenanthrene.yaml`.
- Identifier and grounding: `identifier: CHEBI:35860` with
  `ontology_mapping.ontology_id: CHEBI:35860`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:35860`
  resolves to `1-methylphenanthrene`, formula `C15H12`, SMILES
  `Cc1cccc2c1ccc1ccccc12`, and the same InChI stored in
  `chemical_properties`. ChEBI also lists CAS RN `832-69-9`.
- Source boundary: this record originated from the microbedecoder
  `BacDive_Metabolite_utilization` column and stores that single upstream
  occurrence under `occurrence_statistics.source_occurrences`.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-methylphenanthrene.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-methylphenanthrene.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-ethyl-3-methylimidazolium_Chloride.yaml data/ingredients/mapped/1-ethyl-3-methylimidazolium_Lysine.yaml data/ingredients/mapped/1-methylphenanthrene.yaml`:
  passed; 3 files scanned, 0 ERROR rows.
- Whole-corpus checks run earlier in this review pass passed:
  `scripts/validate_strict.py`, `scripts/validate_all.py --mode both`,
  `scripts/validate_sssom_invariants.py`,
  `scripts/check_flat_export_coverage.py`,
  `scripts/audit_duplicate_identifiers.py --check`,
  `scripts/audit_kg_microbe_node_ids.py --check`,
  `scripts/validate_component_partonomy.py`, and
  `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`.
- Evidence-reference validation:
  `uv run --frozen python scripts/run_shared_evidence_validator.py` could not
  run because the sibling `culturebotai-claw` checkout was absent at
  `../culturebotai-claw/scripts/validate_evidence_references.py`.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed after ignoring empty default fields that
  are materialized only in the aggregate export.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact row:
  `MIM:1-methylphenanthrene skos:exactMatch CHEBI:35860`.
- `docs/data/mapped_ingredients.*`, `docs/data/all_ingredients.*`,
  `docs/data/ingredients.json`, and graph/UMAP data contain the same
  `CHEBI:35860` identity and ChEBI label.

## Evidence

- The exact ChEBI grounding is supported: the official ChEBI name for
  `CHEBI:35860` is `1-methylphenanthrene`, and the ChEBI formula, SMILES, and
  InChI agree with the populated `chemical_properties`.
- The microbedecoder provenance is traceable. A hidden/ignored-inclusive search
  found the originating
  `data/custom/microbedecoder/unmapped_labels.tsv` and
  `data/custom/microbedecoder/ingredient_candidates.tsv` rows with count `1`
  from `BacDive_Metabolite_utilization`.
- The `mappings/microbedecoder_auto_mapped_review.tsv` row records why
  `CHEBI:35860` was promoted: the ID resolved in the local OAK adapter and its
  canonical label exact-matched the record's ontology label. The official
  ChEBI page now supplies the additional current check that the term denotes
  the same 1-positional isomer and neutral formula.
- The old `mappings/record_research_validation.tsv` P1/P3 rows for this slug
  are stale. They predate the populated ChEBI/PubChem formula, SMILES, InChI,
  molecular weight, and `ingredient_type`; the active ChEBI page verifies the
  exact identity.
- Minor: the `REVIEWED_AND_PROMOTED` history event has timestamp
  `2026-08-04T00:00:00+00:00` even though it appears after the
  `FLAGGED_FOR_REVIEW` event at `2026-08-04T03:08:34.142678+00:00`. The event
  content is still understandable, but the chronological ordering is odd.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden -n "record_research_validation|1-ethyl-3-methylimidazolium_Lysine|CHEBI:61326|1-methylphenanthrene|CHEBI:35860" . -g '*record_research_validation*' -g '*review*' -g '*.tsv' -g '*.yaml'`
  covered ignored and hidden YAML/TSV/review files. It found the current
  methylphenanthrene YAML/aggregate/SSSOM/source rows, ignored backups, and
  stale advisory `record_research_validation.tsv` rows, with no duplicate active
  YAML for `CHEBI:35860`.

## Completeness

- Empty component and role slots are acceptable. This record models a defined
  neutral polycyclic aromatic hydrocarbon, not a mixture, and no retained source
  supports a narrower ingredient role assertion.
- `total_occurrences: 0` and `media_count: 0` are acceptable for the
  microbedecoder import convention; the source-specific count is preserved
  under `source_occurrences`.
- The only optional chemistry gap is `chemical_properties.cas_rn`. Current
  ChEBI lists `832-69-9`, so a future enrichment can add that CAS RN if the
  maintainer wants CAS coverage here.

## Recommended Edits

1. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the stale
   methylphenanthrene rows resolved.
2. Optionally add ChEBI-backed `chemical_properties.cas_rn: 832-69-9` through a
   normal enrichment pass.
3. Optionally correct the `REVIEWED_AND_PROMOTED` timestamp so curation history
   sorts in true event order.
