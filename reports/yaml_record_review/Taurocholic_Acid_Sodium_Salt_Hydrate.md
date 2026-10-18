# `data/ingredients/mapped/Taurocholic_Acid_Sodium_Salt_Hydrate.yaml`

## Verdict

Pass. The CultureBotHT CAS-backed record maps exactly to active
`CHEBI:181226`, the stored synonym and structure fields describe taurocholic
acid sodium salt hydrate, the hydrate grounding report confirms a
hydrate-specific term, and the final SSSOM exact row is clean.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Taurocholic_Acid_Sodium_Salt_Hydrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:181226` with
  `ontology_mapping.ontology_id: CHEBI:181226`, label
  `Taurocholic acid sodium salt hydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `345909-26-4`, formula `C26H44NO7S.H2O.Na`, and an
  InChI/SMILES for sodium taurocholate monohydrate.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Taurine` through `Tea`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:181226` as `Taurocholic acid sodium
  salt hydrate` and includes the long stored synonym on that same term.
- Fresh PubChem lookup by CAS `345909-26-4` resolves sodium taurocholate
  hydrate CIDs with formula `C26H46NNaO8S`; CID 23687511 has the same InChI as
  the YAML and lists both CAS `345909-26-4` and the CAS xref on the ChEBI term.
- `reports/hydrate_grounding.tsv` classifies `CHEBI:181226` as
  `OK_HYDRATE_TERM` for this record and formula.
- The final SSSOM has exactly one exact CHEBI row for
  `MIM:Taurocholic_Acid_Sodium_Salt_Hydrate`, points at `CHEBI:181226`, names
  `obo:chebi.owl`, and publishes only the curated same-substance long synonym
  plus `CAS:345909-26-4` in `other`.

## Completeness

- The CHEBI hydrate identity, CAS-backed structure fields, aggregate row,
  hydrate audit, and final SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT import,
  hydrate-grounding, aggregate, row-review, final SSSOM, and generated rows.

## Recommended Edits

- None.
