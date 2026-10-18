# YAML Record Review: sn-Glycerol 3-phosphate bis(cyclohexylammonium) salt

- Repository: CultureBotAI/MediaIngredientMech
- Record: `data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml`
- Started UTC: 2026-10-01T05:03:23Z
- Finished UTC: 2026-10-01T05:03:24Z
- Verdict: needs_curation

## Target

- Class: `IngredientRecord`
- Path: `data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml`
- Identifier: `cas:29849-82-9`
- Preferred term: sn-Glycerol 3-phosphate bis(cyclohexylammonium) salt
- Mapping status: `MAPPED`
- Ingredient type: `SINGLE_INGREDIENT`
- Maintained status: per-record YAML synchronized from `data/curated`

## Validation

- Passed: `just validate-strict data/ingredients/mapped --out /tmp/mim_mapped_review_validation.tsv --workers 4 --quiet`.
- Passed: `just validate-terms data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml`.
- Passed: aggregate comparison for this target found exactly one current aggregate row.
- Passed: parsed `mappings/ingredient_mappings.sssom.tsv` to inspect active rows for this exact `MIM:` subject.

## Identity and Grounding

- Mapping status: `MAPPED`.
- Ontology ID: `CHEBI:15978`.
- Ontology label: `sn-glycerol 3-phosphate`.
- Mapping quality: `NARROW_MATCH`.
- Active SSSOM rows for this subject: 3.
- Identity judgement: Refreshed `reports/yaml_record_review/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.md` after the record changed from b1f78b81519a0ba3363001a8f98ff3f4ee76b3643178be76af5d0ce83984b007 to 185d299a1d5a117e5ce42e2826e3f9fb83cba57459c5fc7e09f2dcf263a660f1; preserved the previous major finding floor pending targeted retirement.

## Evidence

- Current record SHA-256: `185d299a1d5a117e5ce42e2826e3f9fb83cba57459c5fc7e09f2dcf263a660f1`.
- Previous review: `reports/yaml_record_review/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.md`.
- Previous record SHA-256: `b1f78b81519a0ba3363001a8f98ff3f4ee76b3643178be76af5d0ce83984b007`.
- Source occurrence traceability: 0 occurrence(s) across 0 medium/media.
- Latest curation event: REJECTED_PARENT_NAME_SYNONYMS by claude at 2026-09-22T20:41:14.285965+00:00: Retyped names of the parent compound or of a different hydrate as provenance-only REJECTED_LABEL, because this record is a distinct salt, hydrate or tombstone form and the label index resolved the parent's name here (#232): '(2R)-2,3-dihydroxypropyl dihydrogen phosphate'; 'sn-glycerol 3-(dihydrogen phosphate)'. Preserved original text and source metadata. No identity, mapping, role, or remaining-synonym claim was adjudicated.
- Active SSSOM state: 3 active row(s) for `MIM:Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt`.
- Aggregate state: Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.

## Completeness

- The record has raw-label/source provenance through its synonyms or history.
- Per-record YAML is identical to its keyed row in `data/curated/mapped_ingredients.yaml`.
- Consequential unresolved item: Refreshed `reports/yaml_record_review/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.md` after the record changed from b1f78b81519a0ba3363001a8f98ff3f4ee76b3643178be76af5d0ce83984b007 to 185d299a1d5a117e5ce42e2826e3f9fb83cba57459c5fc7e09f2dcf263a660f1; preserved the previous major finding floor pending targeted retirement.

## Findings

- **major**: The previous finding set in `reports/yaml_record_review/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.md` was tied to the prior record content; carry it forward as an unresolved curation floor until a targeted current review retires it. Previous summary: The narrow parent and exact registry rows pass, but final SSSOM exports free-acid parent synonyms and CARBON_SOURCE is provisional.

## Recommended Edits

- Resolve or explicitly retire the findings provisionally carried forward from `reports/yaml_record_review/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.md`.
- After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml`, `just validate-terms data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml` where applicable, and `just qc-sssom`.

## Follow-up Checks

- Re-run strict schema validation on `data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml` after any future curation edit.
- Re-run `just validate-terms data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml` if an OBO-backed `ontology_mapping` is added or changed.
- Re-run `just qc-sssom` and `just qc-roundtrip` if `mapping_status`, `identifier`, `ontology_mapping`, synonyms, or the record path changes.

## Additional Notes

- This read-only review did not append a curation event or promote a mapping.
- iModulonDB was not applicable: this ingredient record does not name a gene, regulator, transcriptomics dataset, or iModulon component.
