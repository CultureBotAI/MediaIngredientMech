# `data/ingredients/mapped/Netilmycin.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:7528` netilmycin identity, structure,
reviewed MicrobeDecoder promotion, and final exact row pass, but the merged
`Netilmicin` synonym now conflicts with active stereochemical sibling
`CHEBI:748901`.

## Identity

- Reviewed record: `data/ingredients/mapped/Netilmycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:7528` with
  `ontology_mapping.ontology_id: CHEBI:7528`, label `netilmycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences and 18 MicrobeDecoder source
  occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Neomycin_F` through `Netilmycin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:7528` as active `netilmycin` with
  formula `C21H41N5O7`, the same InChI and SMILES as the record, and
  `Netilmicin` as a related synonym.
- Major: a fresh OLS4 lookup also resolves active `CHEBI:748901` with label
  `netilmicin`, the same formula, and a different InChI. A fresh PubChem CAS
  lookup for the `CHEBI:7528` cross-reference CAS `56391-56-1` likewise
  resolves to the `CHEBI:748901`-like stereochemistry rather than to the
  current `CHEBI:7528` structure. `Netilmicin` therefore should not publish as
  an exact alias for `MIM:Netilmycin` without a new curation decision.
- The final SSSOM row otherwise maps `MIM:Netilmycin` exactly to
  `CHEBI:7528` with the expected MicrobeDecoder review provenance.

## Completeness

- The active `CHEBI:7528` term, structure, MicrobeDecoder occurrences, empty
  CultureMech occurrence count, and exact final row agree.
- The remaining consequential gap is the stale absorbed `Netilmicin` raw
  synonym, which now leaks into final SSSOM `other`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Netilmycin.yaml`, reject or delete the
  `Netilmicin` raw synonym, then rebuild final SSSOM so `MIM:Netilmycin` does
  not export the active `CHEBI:748901` label as an exact alias for
  `CHEBI:7528`.
