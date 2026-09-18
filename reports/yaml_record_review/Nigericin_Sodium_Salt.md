# `data/ingredients/mapped/Nigericin_Sodium_Salt.yaml`

## Verdict

Needs curation - major. The CAS-backed sodium salt identity and structure are
sound, but the record still uses a CAS fallback primary plus a local registry
identity even though the current `CHEBI:201444` term exactly represents
nigericin sodium.

## Identity

- Reviewed record: `data/ingredients/mapped/Nigericin_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:28643-80-3` with
  `ontology_mapping.ontology_id: CHEBI:201444`, label `Nigericin sodium`,
  source `CHEBI`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nicotine_Fluka` through `Nisin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:201444` as active `Nigericin sodium`
  with formula `C40H67O11.Na` and the same InChI and SMILES as the record.
- A fresh PubChem CAS lookup for `28643-80-3` resolves to CID 16760591 with
  formula `C40H67NaO11` and the same InChI as both the record and
  `CHEBI:201444`.
- The long final SSSOM `other` token is the exact IUPAC synonym currently
  carried by `CHEBI:201444`.
- Major: the record's 2026-04-29 note says no CHEBI entry existed, but the
  exact sodium salt now resolves. The final SSSOM still publishes a
  `skos:narrowMatch` row to that exact CHEBI term plus exact CAS and
  kg-microbe registry rows that should not be needed after promotion.

## Completeness

- The CAS RN, formula, structure, active ChEBI term, and zero occurrence count
  agree.
- The remaining consequential gap is stale fallback modeling after an exact
  CHEBI term became available.

## Recommended Edits

- Major: promote `data/ingredients/mapped/Nigericin_Sodium_Salt.yaml` from
  `cas:28643-80-3` to `CHEBI:201444`, change
  `ontology_mapping.mapping_quality` to `EXACT_MATCH`, keep
  `CAS:28643-80-3` as structured chemistry metadata, and rebuild final SSSOM so
  it emits one exact CHEBI row rather than parent plus registry fallback rows.
