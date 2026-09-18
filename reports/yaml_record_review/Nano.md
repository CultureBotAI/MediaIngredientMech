# `data/ingredients/mapped/Nano.yaml`

## Verdict

Needs curation - blocker. The source labels all denote sodium nitrate
`NaNO3`, but the record normalized them to `NaNO` and exact-mapped them to
`NCIT:C54713`, the NCIT unit prefix `nano-`; the active YAML and final SSSOM
therefore denote the wrong entity.

## Identity

- Reviewed record: `data/ingredients/mapped/Nano.yaml`.
- Identifier and grounding: `identifier: NCIT:C54713` with
  `ontology_mapping.ontology_id: NCIT:C54713`, label `Nano`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 8 CultureMech source occurrences across 8 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nano` through `Naphthalene`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this NCIT-primary
  record.

## Evidence

- A fresh OLS4 lookup resolves `NCIT:C54713` as active NCIT `Nano`, a unit
  prefix meaning one-billionth, not sodium nitrate.
- The record's three retained source labels are all `NaNO3` sodium nitrate
  forms: one CAS-decorated label with sodium nitrate CAS `7631-99-4`, one
  Fisher catalog label, and one autoclave/catalog label.
- The sorted companion record `data/ingredients/mapped/Nano3.yaml` is the
  sodium nitrate record and maps to active `CHEBI:63005`.
- Blocker: final SSSOM publishes `MIM:Nano skos:exactMatch NCIT:C54713` and
  exposes the sodium nitrate `NaNO3(...)` labels as synonyms of the NCIT
  nano-prefix term.

## Completeness

- The aggregate copy, per-record copy, and final SSSOM row are synchronized,
  but they agree on the wrong ontology identity.
- The source sodium nitrate labels are represented by `Nano3`; this record is
  an erroneous residue of the `UNMAPPED_0004` auto-upgrade.

## Recommended Edits

- Blocker: merge the eight `NaNO3` occurrences and any useful provenance from
  `data/ingredients/mapped/Nano.yaml` into
  `data/ingredients/mapped/Nano3.yaml`, then retire this erroneous
  `NCIT:C54713` exact mapping so final SSSOM no longer maps sodium nitrate
  forms to the NCIT nano-prefix term.
