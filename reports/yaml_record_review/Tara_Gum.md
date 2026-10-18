# `data/ingredients/mapped/Tara_Gum.yaml`

## Verdict

Pass. The CAS-primary tara gum record has an active FOODON parent, expected
exact CAS and KG-Microbe registry sibling rows, a synchronized aggregate row,
and no unsafe synonyms in the final SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/Tara_Gum.yaml`.
- Identifier and grounding: `identifier: cas:39300-88-4` with
  `ontology_mapping.ontology_id: FOODON:03413299`, label `tara gum`, source
  `FOODON`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `39300-88-4`.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tangeritin` through `Tartrate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this FOODON-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `FOODON:03413299` as `tara gum`.
- Fresh PubChem lookup by CAS `39300-88-4` found no CID, consistent with using
  a CAS/local exact registry identity plus a FOODON parent instead of a
  PubChem-backed CHEBI structure.
- The final SSSOM publishes the expected `skos:narrowMatch` row to
  `FOODON:03413299`, an exact CAS registry row to `cas:39300-88-4`, and an
  exact local registry sibling row to `kgmicrobe.ingredient:tara_gum`.
- The FOODON parent row has empty `other`, and the two exact registry rows
  publish only `CAS:39300-88-4`.

## Completeness

- The FOODON parent identity, CAS RN, aggregate row, and final SSSOM registry
  rows are present and consistent.
- No components, roles, environmental contexts, or CultureMech occurrence rows
  are asserted.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT import,
  FOODON parent backfill, aggregate, unknown-term triage, row-review, final
  SSSOM, and generated rows.

## Recommended Edits

- None.
