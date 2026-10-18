# `data/ingredients/mapped/Tween.yaml`

## Verdict

Pass. The generic Tween surface maps to the MeSH Polysorbates class, keeps
specific Tween variants separate, and agrees with the aggregate and final SSSOM
rows.

## Identity

- Reviewed record: `data/ingredients/mapped/Tween.yaml`.
- Identifier and grounding: `identifier: mesh:D011136` with matching
  `ontology_mapping.ontology_id`, label `Polysorbates`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Synonyms: raw `Tween` mim-queue label.
- Occurrences: 3 CultureMech recipe occurrences.
- KG-Microbe node: `mesh:D011136`, matching the identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tuberactinomycin` through `Tween`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Engine A label validation was limited to the CHEBI records in this batch.
  The lower-case `mesh:D011136` CURIE was checked through the exact OLS search
  below.

## Evidence

- Fresh exact OLS4 search for `Tween` returns active `mesh:D011136`
  `Polysorbates` with `Tween` as a related synonym, which matches the generic
  surface form.
- The hidden/ignored-inclusive search across `mappings`, `data/curated`, and
  `reports` found distinct mapped records for `Tween_20`, `Tween_40`,
  `Tween_60`, and `Tween_80`; the generic record is not absorbing those
  specific CHEBI identities.
- The final SSSOM row correctly has
  `MIM:Tween skos:exactMatch mesh:D011136` and no `other` synonyms.

## Issues

None.

## Completeness

- The generic MeSH mapping, occurrence count, aggregate copy, KG-Microbe node,
  and final SSSOM row agree.

## Recommended Edits

None.
