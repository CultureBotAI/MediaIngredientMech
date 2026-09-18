# `data/ingredients/mapped/Stallimycin.yaml`

## Verdict

Needs curation - major. The Stallimycin-to-DISTAMYCIN A identity is supported,
but the record publishes process-qualified `produces: stallimycin` as a synonym
and still has a provisional selective-agent role.

## Identity

- Reviewed record: `data/ingredients/mapped/Stallimycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:41958` with
  `ontology_mapping.ontology_id: CHEBI:41958`, label `DISTAMYCIN A`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `C22H27N9O4` with ChEBI/OAK structure values.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Stallimycin` through `Stearic_Acid`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:41958` with canonical label
  `DISTAMYCIN A`, matching the stored CHEBI target.
- PubChem resolves `stallimycin` to CID `3115`, with formula `C22H27N9O4`,
  IUPAC name for distamycin A, and synonyms including `Stallimycin` and
  `DISTAMYCIN A`.
- Major: `produces: stallimycin` is a process-qualified predicate phrase, not
  an ingredient synonym, but the backfilled YAML synonym is exported unchanged
  in final SSSOM `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by
  `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists`, with the
  provisional name-pattern curator note.

## Completeness

- The CHEBI identity, structure fields, aggregate row, and final SSSOM
  identifier agree.
- No unsupported component or CAS payload was found; the active problems are
  the process-qualified synonym and provisional role.

## Recommended Edits

- Major: remove `produces: stallimycin` from
  `data/ingredients/mapped/Stallimycin.yaml` or retype it as non-exported
  provenance so SSSOM `other` carries only true synonym surfaces.
- Major: either remove `physicochemical_roles.SELECTIVE_AGENT` or replace the
  provisional name-pattern evidence with a source that explicitly uses
  stallimycin/distamycin A as a selective agent in a culture context.
