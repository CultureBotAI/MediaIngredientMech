# `data/ingredients/mapped/Tetrandrine.yaml`

## Verdict

Pass. The CAS-derived CHEBI identity, ChEBI xref, PubChem structure, aggregate
row, and final SSSOM row for tetrandrine are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Tetrandrine.yaml`.
- Identifier and grounding: `identifier: CHEBI:49` with the same
  `ontology_mapping.ontology_id`, label `(+)-Tetrandrine`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `518-34-3`, formula `C38H42N2O6`, and matching
  PubChem/ChEBI InChI and SMILES for tetrandrine.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetrandrine` through `Tetrazolium_Violet`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:49` with label `(+)-Tetrandrine`, related synonym
  `Tetrandrine`, formula `C38H42N2O6`, the stored InChI/SMILES strings, KEGG
  compound cross-reference `C09654`, and CAS xref `518-34-3`.
- Fresh PubChem lookup by CAS `518-34-3` resolves CID 73078, formula
  `C38H42N2O6`, and the same InChI as the curated record.
- The final SSSOM has exactly one exact row for `MIM:Tetrandrine`, points at
  `CHEBI:49`, keeps the reviewed `OAK+OLS:chebi|CONFIRMED|2026-07-07`
  validation token, and publishes only `CAS:518-34-3` in `other`.

## Completeness

- The CAS lookup provenance, ChEBI xref, structure fields, aggregate copy, and
  final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureBotHT CAS lookup,
  OAK/OLS row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- None.
