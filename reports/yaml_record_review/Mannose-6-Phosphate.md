# `data/ingredients/mapped/Mannose-6-Phosphate.yaml`

## Verdict

Needs curation. The synonym-grade ChEBI identity, CAS number, exact IUPAC
synonym, and final SSSOM row pass, but `CARBON_SOURCE` is only a provisional
name-pattern inference.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mannose-6-Phosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17369` with
  `ontology_mapping.ontology_id: CHEBI:17369`, label
  `D-mannose 6-phosphate`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 3672-15-9` and formula `C6H13O9P`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mannobiose` through `Marine_Broth_2216`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:17369` as active `D-mannose 6-phosphate` with CAS
  `3672-15-9`, formula `C6H13O9P`, and exact IUPAC synonym
  `D-mannose 6-(dihydrogen phosphate)`.
- OLS4 also lists `Mannose 6-phosphate` as a ChEBI synonym, so the
  `SYNONYM_MATCH` grade accurately represents the local label's relationship to
  the canonical ChEBI label without changing the `skos:exactMatch` predicate.
- PubChem resolves `3672-15-9` to CID 6101690 with formula `C6H13O9P`.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mannose-6-Phosphate` to `CHEBI:17369` with the exact IUPAC synonym and
  `CAS:3672-15-9` in `other`.

## Completeness

- The record does not publish unsupported exact synonyms or raw non-synonym
  payload in final SSSOM.
- `CARBON_SOURCE` is only backed by a `COMPUTATIONAL_PREDICTION` inferred from a
  media-role name pattern. No source attached to the role verifies that
  D-mannose 6-phosphate was supplied as a carbon source.

## Recommended Edits

- Curate recipe or literature evidence for `CARBON_SOURCE`, or remove the
  provisional nutritional role.
