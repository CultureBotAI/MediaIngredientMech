# `data/ingredients/mapped/Toray_Silicone_SH_5535.yaml`

## Verdict

Needs curation, major. The MeSH CURIE exists, but the exact match from
`Toray silicone SH 5535` to MeSH `Toray Silicone` is a stem-substring match
that erases the specific SH 5535 product label.

## Identity

- Reviewed record: `data/ingredients/mapped/Toray_Silicone_SH_5535.yaml`.
- Identifier and grounding: `identifier: mesh:C069668` with matching
  `ontology_mapping.ontology_id`, label `Toray Silicone`, source `MESH`,
  `mapping_quality: LEXICAL_MATCH`, `mapping_status: MAPPED`.
- Synonyms: raw mim-queue source form `Toray silicone SH 5535`.
- Occurrences: 2 CultureMech recipe occurrences in 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tomato_Juice` through `Trace_Element_Solution`: exited 0 and wrote zero
  ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this MeSH row because
  `mesh:C069668` is intentionally outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Prefix-specific OLS validation resolves `mesh:C069668`, so the CURIE itself
  is live.
- Fresh exact OLS4 search for `Toray Silicone` returns `mesh:C069668` and lists
  `SH 792` / `SH-792` as synonyms.
- Fresh exact OLS4 search for the full source surface
  `Toray silicone SH 5535` returns no exact hit.
- The final SSSOM row has
  `MIM:Toray_Silicone_SH_5535 skos:exactMatch mesh:C069668`, uses
  `registry:mesh`, and leaves `other` empty.

## Issues

### Major: SH 5535 is not verified as MeSH Toray Silicone

The grounding came from `resolve_unmapped_v2 strategy=stem-match`; the live
MeSH concept resolves as `Toray Silicone` with `SH 792` synonyms, not `SH
5535`. Without product-specific evidence, the exact row can collapse a
distinct Toray silicone formulation into the wrong MeSH supplementary concept.

## Completeness

- Occurrence counts, the aggregate row, and the final SSSOM row agree.
- No roles, CAS RN, chemical properties, components, or final SSSOM synonyms
  are asserted.
- The unresolved product identity is the remaining blocker.

## Recommended Edits

- Verify whether SH 5535 and MeSH `mesh:C069668` denote the same Toray
  silicone formulation. If not, demote this record to a local registry
  fallback or a broader non-exact relation.
