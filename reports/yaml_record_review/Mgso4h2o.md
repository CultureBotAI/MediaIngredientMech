# `data/ingredients/mapped/Mgso4h2o.yaml`

## Verdict

Needs curation. The record label names a 1-water magnesium sulfate hydrate, but
the active YAML and final SSSOM map it exactly to `CHEBI:31795` magnesium
sulfate heptahydrate and export 7-water aliases.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mgso4h2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:31795` with
  `ontology_mapping.ontology_id: CHEBI:31795`, label
  `magnesium sulfate heptahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 5,673 total occurrences across 5,619 CultureMech recipes.
- Chemical identity: CAS `10034-99-8`, formula `7H2O.Mg.O4S`, SMILES, and
  InChI, all for the heptahydrate rather than the 1-water label.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgso4_X_7_H2o` through `Middlebrook_7H10_Agar`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the two other CHEBI-primary records in the same batch.

## Evidence

- EBI OLS4 resolves `CHEBI:31795` as active
  `magnesium sulfate heptahydrate`.
- EBI OLS4 exact search found no ChEBI class named
  `magnesium sulfate monohydrate`.
- `mappings/hydrate_review.tsv` records this source label as a 1-water hydrate,
  notes that the current CAS denotes a different hydration state, and reports
  that the exact external ontology hydrate term is unavailable or unconfirmed.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mgso4h2o` to
  `CHEBI:31795`, making the false heptahydrate identity graph-facing.

## Completeness

- The record should not share the heptahydrate exact ChEBI identity while its
  label says 1-water magnesium sulfate.
- The final `other` field repeats malformed and 7-water labels already present
  on the canonical `MgSO4 x 7 H2O` row.
- `SULFUR_SOURCE` carries CultureMech `DATABASE_ENTRY` evidence for a
  mineral-source use, while `MINERAL_SOURCE` has no evidence.

## Recommended Edits

- Major: localize the 1-water source identity or reject it into the correct
  magnesium sulfate hydrate representative so it no longer publishes an exact
  `CHEBI:31795` heptahydrate row.
- Major: clear the heptahydrate CAS and structure from
  `data/ingredients/mapped/Mgso4h2o.yaml` unless the source label is corrected
  to the heptahydrate.
- Major: remove the non-1-water final SSSOM `other` labels and repair the
  mineral-source role evidence.
