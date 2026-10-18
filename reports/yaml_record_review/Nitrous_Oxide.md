# `data/ingredients/mapped/Nitrous_Oxide.yaml`

## Verdict

Needs curation - major. The CAS-backed `CHEBI:17045` dinitrogen oxide
identity, `#N2O` surface-form curation, occurrence count, structure block, and
final SSSOM row pass, but `ELECTRON_ACCEPTOR` is still backed only by a
provisional in-session LLM role assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Nitrous_Oxide.yaml`.
- Identifier and grounding: `identifier: CHEBI:17045` with
  `ontology_mapping.ontology_id: CHEBI:17045`, label `dinitrogen oxide`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 3 CultureMech recipe occurrences across 3 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:17045` as active
  `dinitrogen oxide` with formula `N2O`, CAS `10024-97-2`, InChI
  `InChI=1S/N2O/c1-2-3`, and SMILES `N#[N+][O-]`, matching the record.
- A fresh PubChem lookup for CAS `10024-97-2` resolves to formula `N2O` and the
  same InChI.
- The final SSSOM row maps `MIM:Nitrous_Oxide` exactly to `CHEBI:17045`; its
  `other` tokens are the duplicate-reviewed `N2O` and `#N2O` surfaces, the
  reviewed ChEBI synonym `oxidodinitrogen(N--N)`, and `CAS:10024-97-2`.
- Major: `cellular_metabolic_roles.ELECTRON_ACCEPTOR` cites a
  `COMPUTATIONAL_PREDICTION` with the note `Assigned by in-session Claude
  reasoning (no external API)`. The evidence is explicitly provisional and
  should be replaced with source-backed role evidence or removed.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, 3/3 occurrence count, and
  final exact row otherwise agree.
- The remaining consequential gap is the unsupported electron-acceptor role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nitrous_Oxide.yaml`, replace the
  `ELECTRON_ACCEPTOR` role evidence with inspected source-backed evidence for
  nitrous oxide acting as a media electron acceptor, or remove the role until
  that evidence exists.
