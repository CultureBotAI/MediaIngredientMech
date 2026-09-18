# `data/ingredients/mapped/Voso4_X_N_H2o.yaml`

## Verdict

Pass. The variable-hydrate `CHEBI:87020` vanadyl sulfate hydrate identity,
structure fields, source-backed trace-element role, aggregate row, and final
SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Voso4_X_N_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:87020` with matching
  `ontology_mapping.ontology_id`, label `vanadyl sulfate hydrate`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `123334-20-3`.
- Chemical fields: variable formula `(H2O)n.O5SV` with populated InChI and
  SMILES strings.
- Synonyms: raw CultureMech role/property strings, ChEBI variable-hydrate
  formula strings, merged duplicate hydrate spellings, and raw CultureMech
  middle-dot and kana-middle-dot variable-hydrate spellings.
- Occurrences: 65 CultureMech recipe occurrences across 65 media.
- Role: `TRACE_ELEMENT` imported from CultureMech original role text.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Voso4_X_N_H2o` through `Washed_agar`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the three
  CHEBI-primary records in this batch exited 0.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup for `CHEBI:87020` returns active label
  `vanadyl sulfate hydrate`, defines it as a vanadyl sulfate hydrate with an
  unspecified water count, and exposes formula `(H2O)n.O5SV`.
- The same OLS4 term carries the variable-hydrate synonyms `VOSO4(H2O)n`,
  `VOSO4(H2O)x`, `VOSO4.nH2O`, and `VOSO4.xH2O`.
- The `TRACE_ELEMENT` role is backed by `DATABASE_ENTRY` evidence carrying the
  original CultureMech role text `Mineral`.
- The final SSSOM row correctly has
  `MIM:Voso4_X_N_H2o skos:exactMatch CHEBI:87020` and exports only
  variable-hydrate formula spellings in `other`.

## Issues

None.

## Completeness

- The exact variable-hydrate CHEBI mapping, structure fields, occurrence count,
  source-backed trace-element role, aggregate copy, and final SSSOM row agree.

## Recommended Edits

None.
