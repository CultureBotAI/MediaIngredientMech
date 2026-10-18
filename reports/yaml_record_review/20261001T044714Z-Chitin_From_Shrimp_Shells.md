# YAML Record Review: Chitin from shrimp shells

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/unmapped/Chitin_From_Shrimp_Shells.yaml`
- Started UTC: 2026-10-01T04:47:14Z
- Finished UTC: 2026-10-01T04:47:15Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/unmapped/Chitin_From_Shrimp_Shells.yaml`
- Identifier: `UNMAPPED_0248`
- Preferred term: Chitin from shrimp shells
- Mapping status: `UNMAPPED`
- Ingredient type: `UNDEFINED_MIXTURE`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/unmapped data/ingredients/mapped/Na2-citrate.yaml data/ingredients/mapped/Nitrilotriacetic_Acid_Trisodium_Salt.yaml --out /tmp/mim_remaining_review_validation.tsv --workers 4 --quiet`; 275 files scanned and 0 ERROR rows.
- Passed: `just validate-terms data/ingredients/unmapped/Chitin_From_Shrimp_Shells.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `UNMAPPED`.
- Ontology ID: `CHEBI:17029`.
- Ontology label: `chitin`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 0.
- Identity judgement: Mixture/extract/preparation is intentionally left unmapped until the source supports a component decomposition or exact preparation identity.

## Evidence

- Current record SHA-256: `06104c43c1f5d9f74b2bc6bceca4158cd6916316a2736044795c9b71eb4fdb83`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: ADDED_PARENT_CONTEXT by edison_contextual_parent at 2026-08-07T00:00:00+00:00: Recorded CHEBI:17029 (chitin) as the nearest ontology parent with mapping_quality=NARROW_MATCH: the report calls it "a source-qualified polymer preparation, not a uniquely defined small molecule"; chitin is that source-free polymer. Status stays UNMAPPED and NO SSSOM row is published — this follows the existing contextual pattern on Inorganic salts-starch agar (CHEBI:24839, "retained ... only as contextual curation") and five sibling records. exactMatch/closeMatch are withheld deliberately: they license node substitution, and a source- or grade-qualified preparation is not interchangeable with the substance it is prepared from. Whether this pattern should instead publish a skos:narrowMatch row is the open question in #294.
- Active SSSOM state: No active row for `MIM:Chitin_From_Shrimp_Shells`, as expected for `UNMAPPED`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- The 2026-09-01 unmapped review explains the residual unmapped policy: named media, undefined mixtures, and exact single-ingredient residuals must stay unmapped until exact same-form evidence is available.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/unmapped_ingredients.yaml`.
- Consequential unresolved item: Mixture/extract/preparation is intentionally left unmapped until the source supports a component decomposition or exact preparation identity.

## Findings

- **major**: `data/ingredients/unmapped/Chitin_From_Shrimp_Shells.yaml` remains `UNMAPPED`; the label denotes a mixture, extract, or incompletely specified preparation. Do not exact-match it to a broader parent, component, hydrate, salt, or lookalike label.

## Recommended Edits

- Curate an exact same-form identity or decomposition for `data/ingredients/unmapped/Chitin_From_Shrimp_Shells.yaml` before mapping it.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/unmapped/Chitin_From_Shrimp_Shells.yaml`, `just validate-terms data/ingredients/unmapped/Chitin_From_Shrimp_Shells.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/unmapped/Chitin_From_Shrimp_Shells.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/unmapped/Chitin_From_Shrimp_Shells.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
