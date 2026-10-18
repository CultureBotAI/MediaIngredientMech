# `data/ingredients/mapped/Suberic_Acid.yaml`

## Verdict

Pass. The exact `CHEBI:9300` suberic-acid identity, CAS-backed structure,
curated `octanedioic acid` synonym, and final SSSOM row all agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Suberic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:9300` with
  `ontology_mapping.ontology_id: CHEBI:9300`, label `suberic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `505-48-6`, formula `C8H14O4`, and matching
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

- Fresh OLS4 lookup resolves active `CHEBI:9300` with label `suberic acid`, CAS
  xref `505-48-6`, formula `C8H14O4`, and `octanedioic acid` as an exact IUPAC
  synonym.
- PubChem resolves CAS `505-48-6` to `Suberic acid` with the same molecular
  formula and InChI.
- The final SSSOM row exact-matches `CHEBI:9300`; its `other` tokens are
  `octanedioic acid` and `CAS:505-48-6`, both true synonyms for this subject.

## Completeness

- The exact identity, synonym, CAS, chemical properties, aggregate row, and
  final SSSOM row agree.
- An ignored/hidden search of local curated, mapping, generated, report, source,
  and documentation paths found the expected rows for this record and no
  unsupported active role, component, or final SSSOM payload.

## Recommended Edits

- None.
