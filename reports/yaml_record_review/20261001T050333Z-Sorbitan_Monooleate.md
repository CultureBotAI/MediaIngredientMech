# YAML Record Review: Sorbitan Monooleate

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sorbitan_Monooleate.yaml`
- Started UTC: 2026-10-01T05:03:33Z
- Finished UTC: 2026-10-01T05:03:34Z
- Verdict: pass

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sorbitan_Monooleate.yaml`
- Identifier: `kgmicrobe.ingredient:sorbitan_monooleate`
- Preferred term: Sorbitan Monooleate
- Mapping status: `MAPPED`
- Ingredient type: `<missing>`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sorbitan_Monooleate.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `kgmicrobe.ingredient:sorbitan_monooleate`.
- Ontology label: `Sorbitan Monooleate`.
- Mapping quality: `EXACT_MATCH`.
- Active SSSOM rows for this subject: 1.
- Identity judgement: Refreshed `reports/yaml_record_review/Sorbitan_Monooleate.md` after the record changed from a5bb2cfc0cb31d0d026dc7292f159f68c45c55bc55fb31eb1e2326eabc90bf66 to 09a88638de346c0f2cb44d3c09fd751b03f6266c9abdf7b6b927dec56c17d083; no prior finding is carried forward.

## Evidence

- Current record SHA-256: `09a88638de346c0f2cb44d3c09fd751b03f6266c9abdf7b6b927dec56c17d083`.
- Previous review: `reports/yaml_record_review/Sorbitan_Monooleate.md`.
- Previous record SHA-256: `a5bb2cfc0cb31d0d026dc7292f159f68c45c55bc55fb31eb1e2326eabc90bf66`.
- Source occurrence traceability: 2 occurrence(s) across 2 medium/media.
- Latest curation event: CORRECTED by kgmicrobe_scope_review at 2026-09-23T19:20:33.161389+00:00: Use a local unresolved material identity for the two CultureMech ATCC 416 recipe occurrences. Withdraw the label-only exact NCIT:C75654 grounding; exact molecular mapping to it or CHEBI:183688 is withheld pending material/product evidence. ATCC supplies only the generic name (1 g/L); JECFA describes a commercial mixture. Do not infer Tween 80/CHEBI:53426 from the conflicting FoodOn alias. Neither CAS 1338-43-8 nor CAS 9005-65-6 is assigned without product confirmation.
- Active SSSOM state: 1 active row(s) for `MIM:Sorbitan_Monooleate`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: None found.

## Findings

None found.

## Recommended Edits

- None.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sorbitan_Monooleate.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sorbitan_Monooleate.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
