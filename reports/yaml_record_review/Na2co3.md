# `data/ingredients/mapped/Na2co3.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:29377` sodium carbonate identity,
CAS-backed structure, source-backed `BUFFER` role, duplicate merge, occurrence
count, and final exact row pass, but final SSSOM still publishes solution,
buffer, catalog, and malformed formula tokens as synonyms of the anhydrous
carbonate record.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2co3.yaml`.
- Identifier and grounding: `identifier: CHEBI:29377` with
  `ontology_mapping.ontology_id: CHEBI:29377`, label `sodium carbonate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 1751 CultureMech recipe occurrences across 1751 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2_Alpha-ketoglutarate` through `Na2co3`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:29377` as active
  `sodium carbonate`, with `cas:497-19-8`, formula `CO3.2Na`, and the stored
  structure.
- The `physicochemical_roles.BUFFER` facet is supported by a
  `DATABASE_ENTRY` imported from CultureMech raw role text explicitly naming
  `Buffer`; unlike provisional name-pattern roles, this role evidence is placed
  on the narrow role claim.
- Major: the final SSSOM `other` column for `MIM:Na2co3` still publishes
  `Sodium carbonate solution`, `Na2CO3-CO2 buffer`, `Na CO`, `NaCO3`, `Na2CO`,
  and `Na2CO3(Baker 3604)` as exact synonyms. Those are a solution sibling, a
  buffer label, malformed formulas, and a catalog label rather than clean
  same-subject sodium carbonate synonyms.
- The raw `(adjust if required)` and `Role: Buffer` CultureMech strings are
  correctly filtered from final SSSOM.

## Completeness

- The active ChEBI target, canonical CAS RN, formula, structure, source-backed
  buffer role, 1751/1751 occurrence count, duplicate merge, and final exact row
  agree.
- The remaining consequential gap is the final `other` cleanup for
  non-synonymous sodium carbonate labels.

## Recommended Edits

- Major: remove or demote the solution, buffer, catalog, and malformed formula
  tokens so they no longer publish as exact `Na2CO3` synonyms. The fix belongs
  in `data/ingredients/mapped/Na2co3.yaml` for active synonym rows and in the
  final SSSOM enrichment path for the extra `Sodium carbonate solution` token;
  rebuild final SSSOM and re-run final SSSOM validation plus product label
  validation.
