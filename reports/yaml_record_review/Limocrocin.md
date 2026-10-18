# `data/ingredients/mapped/Limocrocin.yaml`

## Verdict

Pass. The promoted MeSH `C079132` identity is active, label-exact for
`limocrocin`, and the final SSSOM row has no unsafe synonym payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Limocrocin.yaml`.
- Identifier and grounding: `identifier: mesh:C079132` with
  `ontology_mapping.ontology_id: mesh:C079132`, label `limocrocin`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The record has no curated formula, structure, CAS RN, or role facets.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lignin_Alkali` through `Lincomycin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for
  `Limonin.yaml`, `Linalool.yaml`, and `Lincomycin.yaml`. `Lignin_Alkali.yaml`
  and `Limocrocin.yaml` were skipped from that CHEBI/OBO subset because their
  ontology IDs are local CAS and MeSH registry CURIEs.

## Evidence

- EBI OLS4 search for `Limocrocin` in MeSH resolves active `mesh:C079132` with
  label `limocrocin`.
- The final SSSOM publishes one `skos:exactMatch` row to `mesh:C079132` and has
  an empty `other` field.
- The aggregate `data/curated/mapped_ingredients.yaml` copy matches the
  per-record identity, status, and mapping.

## Completeness

- The active MeSH identity, aggregate copy, and final SSSOM row are present and
  consistent.
- No nutritional, physicochemical, cellular, environmental, structure, or CAS
  assertion is present.

## Recommended Edits

- None.
