# `data/ingredients/mapped/Mycobacidin.yaml`

## Verdict

Pass. The exact `mesh:C010250` mycobacidin identity, MeSH upgrade, and final
exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mycobacidin.yaml`.
- Identifier and grounding: `identifier: mesh:C010250` with
  `ontology_mapping.ontology_id: mesh:C010250`, label `mycobacidin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no direct CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mucin_From_Porcine_Stomach_Type_III` through `Mycobactin_J`: exited 0 and
  wrote zero ERROR rows.
- Direct CHEBI-focused LinkML term validation was skipped for this MeSH record
  in the mixed batch.

## Evidence

- A fresh MeSH-scoped EBI OLS4 lookup resolves `mesh:C010250` as active
  `mycobacidin`.
- The curation history records a label-exact upgrade from the original local
  `kgmicrobe.compound` placeholder to the MeSH term.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mycobacidin`
  to `mesh:C010250` with empty `other`.

## Completeness

- The MeSH target, exact identity row, upgrade rationale, and empty final
  `other` agree.
- The record does not assert components, roles, chemical properties, or
  non-synonym final `other` text.

## Recommended Edits

- None.
