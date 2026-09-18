# `data/ingredients/mapped/Sulfur_Compounds.yaml`

## Verdict

Needs curation - major. The `CHEBI:26835` sulfur-molecular-entity grounding
and aggregate row pass, but the final SSSOM publishes
`oxidation in darkness: sulfur compounds` in `other`; that is a
process-qualified metatrait surface, not a synonym for this ingredient class.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfur_Compounds.yaml`.
- Identifier and grounding: `identifier: CHEBI:26835` with
  `ontology_mapping.ontology_id: CHEBI:26835`, label
  `sulfur molecular entity`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: absent, as expected for this ChEBI class record.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfur_Compounds` through `Sunflower_Oil`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:26835` with label
  `sulfur molecular entity`, no structural definition, related
  sulfur-molecular-entity synonyms, and children.
- The #322 regrade correctly changed the match from `EXACT_MATCH` to
  `SYNONYM_MATCH` because `Sulfur compounds` is a plural class-like surface
  for the ChEBI sulfur-molecular-entity class, not the ontology label itself.
- Major: `claude_sssom_surface_form_backfill` added
  `oxidation in darkness: sulfur compounds` as an active raw synonym even
  though that label describes a metatrait under a condition, not a same-subject
  synonym for sulfur compounds. The final SSSOM exports the same text in
  `other`.

## Completeness

- The CHEBI class grounding, aggregate row, zero occurrence count, and expected
  `skos:exactMatch` predicate for `SYNONYM_MATCH` agree.
- The record has no components, roles, environmental contexts, datasets, or
  structure fields needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected KGM metatraits, aggregate,
  generated index, SSSOM, row-review, and docs rows. The only consequential
  extra surface for this record is the process-qualified `other` token already
  called out above.

## Recommended Edits

- Major: remove `oxidation in darkness: sulfur compounds` from the active
  synonyms in `data/ingredients/mapped/Sulfur_Compounds.yaml`; if the raw
  source text is worth preserving, keep it only as provenance that the final
  SSSOM builder will not publish in `other`.
- Major: regenerate `mappings/ingredient_mappings.sssom.tsv` and generated docs
  so the process-qualified metatrait text is no longer exported as a synonym.
