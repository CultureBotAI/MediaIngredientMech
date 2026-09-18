# `data/ingredients/mapped/Na2s.yaml`

## Verdict

Pass. The `CHEBI:76208` anhydrous sodium sulfide identity, ChEBI-backed CAS RN,
formula, sulfide structure, source-backed `REDUCING_AGENT` role, #260 sodium
sulfide alias repair, hidden-hydrate rejection, and final exact row all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2s.yaml`.
- Identifier and grounding: `identifier: CHEBI:76208` with
  `ontology_mapping.ontology_id: CHEBI:76208`, label
  `sodium sulfide (anhydrous)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 59 CultureMech recipe occurrences across 58 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2moo42h2o` through `Na2s2o3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:76208` as active
  `sodium sulfide (anhydrous)` with `Na2S` and anhydrous sodium sulfide
  synonyms.
- The ChEBI detail page for `CHEBI:76208` carries formula `2Na.S`, the stored
  sulfide InChI, and CAS `1313-82-2`, confirming that the active CAS and
  structure are on the same anhydrous salt identity.
- The `physicochemical_roles.REDUCING_AGENT` facet is supported by imported
  CultureMech raw role text explicitly naming `Reducing Agent`.
- The final SSSOM row maps `MIM:Na2s` exactly to `CHEBI:76208`; the monohydrate
  label is rejected and no longer reaches final `other`.
- The #260 synonym addition correctly routes CultureMech's `Sodium sulfide`
  surface to this anhydrous sodium sulfide record and not to unrelated
  `CHEBI:85357`.

## Completeness

- The active ChEBI target, canonical CAS RN, formula, structure, source-backed
  reducing-agent role, 59/58 occurrence count, rejected hydrate alias, and final
  exact row agree.

## Recommended Edits

- None.
