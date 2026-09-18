# `data/ingredients/mapped/Strychnine_Sulfate.yaml`

## Verdict

Pass. The exact `CHEBI:233239` strychnine sulfate identity, CAS-backed formula,
curated IUPAC synonym, and final SSSOM row all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Strychnine_Sulfate.yaml`.
- Identifier and grounding: `identifier: CHEBI:233239` with
  `ontology_mapping.ontology_id: CHEBI:233239`, label `strychnine sulfate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `60-41-3`, formula `2C21H22N2O2.H2O4S`, and
  matching ChEBI/PubChem InChI values.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Streptomycin_Sulfate_Salt` through `Suberic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:233239` with label
  `strychnine sulfate`, CAS xref `60-41-3`, formula
  `2C21H22N2O2.H2O4S`, and the stored IUPAC string as an exact synonym.
- PubChem resolves CAS `60-41-3` to `Strychnine sulfate` with the same InChI.
- The final SSSOM row exact-matches `CHEBI:233239`; its `other` tokens are the
  ChEBI IUPAC synonym and `CAS:60-41-3`, both true synonyms for this subject.

## Completeness

- The exact sulfate identity, synonym, CAS, chemical properties, aggregate row,
  and final SSSOM row agree.
- An ignored/hidden search of local curated, mapping, generated, report, source,
  and documentation paths found the expected rows for this record and no
  unsupported active role, component, or final SSSOM payload.

## Recommended Edits

- None.
