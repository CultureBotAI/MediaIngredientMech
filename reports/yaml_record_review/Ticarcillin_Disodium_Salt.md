# `data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml`

## Verdict

Needs curation, major. The CAS-to-CHEBI identity and final SSSOM synonym are
correct, but `SELECTIVE_AGENT` is still supported only by provisional
name-pattern evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Ticarcillin_Disodium_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:35017` with matching
  `ontology_mapping.ontology_id`, label `ticarcillin disodium`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `4697-14-7`.
- Synonyms: exact ChEBI chemical name for disodium ticarcillin.
- Occurrences: no MediaDive/media occurrence count; the import evidence cites
  the CultureBotHT Hans80Anti panel.
- Roles: one `physicochemical_roles.SELECTIVE_AGENT` facet at confidence
  `0.8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Ticarcillin` through `TitaniumIII_Chloride`: exited 0 and wrote zero ERROR
  rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 search for `ticarcillin` returns `CHEBI:35017` with label
  `ticarcillin disodium` and the same exact disodium chemical synonym that the
  YAML exports.
- The stored formula and structure encode two sodium ions and ticarcillin
  dianion, matching the disodium salt rather than the neutral acid.
- The final SSSOM row has
  `MIM:Ticarcillin_Disodium_Salt skos:exactMatch CHEBI:35017`, keeps the CAS
  RN and ChEBI exact synonym in `other`, and does not leak broader,
  process-qualified, or vendor-specific text.

## Issues

### Major: `SELECTIVE_AGENT` is provisional name-pattern evidence

The only role assertion is:

```yaml
physicochemical_roles:
- role: SELECTIVE_AGENT
  confidence: 0.8
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Inferred from curated media-role name pattern
    curator_note: Provisional role from a curated name-pattern rule; review recommended.
```

That is the same provisional `infer_roles_from_name_lists` path flagged for
other antibiotic salts. The CAS-RN lookup establishes the molecule, but it does
not independently curate the media role.

## Completeness

- The CAS RN, CHEBI identity, salt structure, exact synonym, aggregate copy,
  and final SSSOM row agree.
- No component, occurrence, or final SSSOM synonym repair is needed.
- The only residual problem is the provisional `SELECTIVE_AGENT` facet.

## Recommended Edits

- Replace the `COMPUTATIONAL_PREDICTION` role evidence with curated
  database/literature evidence for the CultureBotHT use, or remove
  `physicochemical_roles` until such support is added.
