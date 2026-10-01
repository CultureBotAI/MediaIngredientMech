# YAML Record Review: CMC + PY + Horse Serum

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/CMC_PY_Horse_Serum.yaml`
- Started UTC: 2026-10-01T04:47:02Z
- Finished UTC: 2026-10-01T04:47:03Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/CMC_PY_Horse_Serum.yaml`
- Identifier: `UNMAPPED_0740`
- Preferred term: CMC + PY + Horse Serum
- Mapping status: `AMBIGUOUS`
- Ingredient type: `<missing>`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/unmapped data/ingredients/mapped/Na2-citrate.yaml data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml --out /tmp/mim_remaining_review_validation.tsv --workers 4 --quiet`; 275 files scanned and 0 ERROR rows.
- Not checked: this record has no `ontology_mapping.ontology_id`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `AMBIGUOUS`.
- Ontology ID: `None`.
- Ontology label: `None`.
- Mapping quality: `None`.
- Active SSSOM rows for this subject: 0.
- Identity judgement: Record is intentionally AMBIGUOUS after source review showed the flattened label should not be represented as one CMC/PY/horse-serum mixture.

## Evidence

- Current record SHA-256: `39e3ff65e31ecd99696afd0b2d3429fba96751361b019a92933e136372b74077`.
- Source occurrence traceability: 0 active occurrence(s) across 0 medium/media; source rows: microbedecoder: 1.
- Latest curation event: CORRECTED by mim-semantic-evidence-review at 2026-09-21T00:00:00+00:00: #710: original species-description evidence disproves carboxymethylcellulose expansion and a single CMC/PY/serum mixture. Withdrew all four invented component edges and fallback identity, restored UNMAPPED_0740, marked AMBIGUOUS and moved to unmapped. Kept original raw label; full withdrawn claims and prior source record are preserved in reports/semantic_review_20260921/resolution/components/before-records.json.
- Active SSSOM state: No active row for `MIM:CMC_PY_Horse_Serum`, as expected for `AMBIGUOUS`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- `reports/semantic_review_20260921/resolution/components/README.md` records the Love et al. 1979 source review that invalidated the former single CMC/PY/horse-serum component assertion.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Record is intentionally AMBIGUOUS after source review showed the flattened label should not be represented as one CMC/PY/horse-serum mixture.

## Findings

- **major**: `data/ingredients/unmapped/CMC_PY_Horse_Serum.yaml` has no exact identity mapping because the source expression remains ambiguous; keep it out of `mappings/ingredient_mappings.sssom.tsv` until the separate source preparations are represented.

## Recommended Edits

- Represent the separate source preparations for `data/ingredients/unmapped/CMC_PY_Horse_Serum.yaml` before promoting a mapping.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/CMC_PY_Horse_Serum.yaml`, `just validate-terms data/ingredients/unmapped/CMC_PY_Horse_Serum.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/CMC_PY_Horse_Serum.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/CMC_PY_Horse_Serum.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
