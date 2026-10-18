# `data/ingredients/mapped/Nano3.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:63005` sodium nitrate identity,
CAS-backed structure, `NITROGEN_SOURCE` role, occurrence count, and core ChEBI
aliases pass, but final SSSOM still publishes a role-qualified label as an
exact synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Nano3.yaml`.
- Identifier and grounding: `identifier: CHEBI:63005` with
  `ontology_mapping.ontology_id: CHEBI:63005`, label `sodium nitrate`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 644 source occurrences across 643 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nano` through `Naphthalene`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 search by `CHEBI:63005` and by `sodium nitrate` resolves
  active `CHEBI:63005` with formula `NO3.Na` and the expected sodium nitrate
  synonyms.
- A fresh PubChem CAS lookup for `7631-99-4` resolves to sodium nitrate with
  the same InChI as the record.
- The #226 merge correctly absorbed the same sodium nitrate duplicate, and
  `NITROGEN_SOURCE` is supported by imported CultureMech `Nitrogen Source`
  role text.
- Major: `Sodium nitrate (nitrogen source)` remains an active synonym and
  publishes in final SSSOM `other`; it is a role-qualified label, not a clean
  synonym for `CHEBI:63005`.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 643/644 occurrence count,
  role evidence, and final exact row otherwise agree.
- The remaining consequential gap is the role-qualified merged synonym in
  final `other`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nano3.yaml`, reject or delete
  `Sodium nitrate (nitrogen source)`, then rebuild final SSSOM so `other`
  keeps only true sodium nitrate synonyms plus `CAS:7631-99-4`.
