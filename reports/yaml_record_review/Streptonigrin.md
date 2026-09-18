# `data/ingredients/mapped/Streptonigrin.yaml`

## Verdict

Pass. The exact `CHEBI:9287` identity, CAS-backed structure fields, curated
IUPAC synonym, and final SSSOM row all denote streptonigrin.

## Identity

- Reviewed record: `data/ingredients/mapped/Streptonigrin.yaml`.
- Identifier and grounding: `identifier: CHEBI:9287` with
  `ontology_mapping.ontology_id: CHEBI:9287`, label `streptonigrin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `3930-19-6`, formula `C25H22N4O8`, and matching
  ChEBI/PubChem InChI values.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Streptomycin_Sulfate_Salt` through `Suberic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:9287` with label `streptonigrin`,
  CAS xref `3930-19-6`, formula `C25H22N4O8`, and the stored IUPAC name as an
  exact synonym.
- PubChem resolves CAS `3930-19-6` to `Streptonigrin` with the same molecular
  formula and InChI.
- The final SSSOM row exact-matches `CHEBI:9287`; its `other` tokens are the
  ChEBI IUPAC synonym and `CAS:3930-19-6`, both true synonyms for this subject.

## Completeness

- The exact identity, synonym, CAS, chemical properties, aggregate row, and
  final SSSOM row agree.
- An ignored/hidden search of local curated, mapping, generated, report, source,
  and documentation paths found the expected rows for this record and no
  unsupported active role, component, or final SSSOM payload.

## Recommended Edits

- None.
