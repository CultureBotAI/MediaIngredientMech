# `data/ingredients/mapped/Mannitol.yaml`

## Verdict

Needs curation. The generic ChEBI mannitol identity and CultureMech-backed
carbon-source role pass, but the record exports the stereospecific
D-mannitol CAS number on the generic `CHEBI:29864` row.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mannitol.yaml`.
- Identifier and grounding: `identifier: CHEBI:29864` with
  `ontology_mapping.ontology_id: CHEBI:29864`, label `mannitol`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 72 total occurrences in 72 CultureMech recipes.
- Chemical formula: `C6H14O6`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mandelic_Acid` through `Mannitol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:29864` as active generic `mannitol` with formula
  `C6H14O6` and no CAS cross-reference.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mannitol` to
  `CHEBI:29864` with `CAS:69-65-8` in `other`.
- The sibling `D-mannitol` record is grounded to `CHEBI:16899` and already
  owns the same `CAS:69-65-8` surface form.

## Completeness

- The CultureMech `Original role text: Carbon Source` evidence supports the
  `CARBON_SOURCE` facet.
- CAS `69-65-8` is exact to stereospecific D-mannitol, not the generic
  mannitol class. Keeping it on this record duplicates the sibling
  D-mannitol registry identity and makes the generic final SSSOM row too
  specific.

## Recommended Edits

- Remove `chemical_properties.cas_rn: 69-65-8` from `Mannitol` or remodel the
  record as a local generic mannitol identity that is not conflated with
  D-mannitol's CAS number.
