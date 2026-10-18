# `data/ingredients/mapped/Malonic_Acid.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS number, structure, exact synonym,
and final SSSOM row pass, but the `CARBON_SOURCE` role is still supported only
by provisional computational name-pattern evidence.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Malonic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:30794` with
  `ontology_mapping.ontology_id: CHEBI:30794`, label `malonic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 141-82-2`, formula `C3H4O4`, InChI and SMILES
  copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Malonic_Acid` through `Malt_Extract_Agar_Oxoid`: exited 0 and wrote zero
  ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:30794` as active `malonic acid` with CAS
  `141-82-2`, formula `C3H4O4`, and the same InChI and SMILES carried in the
  YAML.
- ChEBI carries `Propanedioic acid` as an exact synonym.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Malonic_Acid` to `CHEBI:30794` with `Propanedioic acid` and
  `CAS:141-82-2` in `other`.

## Completeness

- The identity, chemistry, exact synonym, and final SSSOM predicate are
  consistent.
- `CARBON_SOURCE` is backed only by `COMPUTATIONAL_PREDICTION` evidence from a
  curated media-role name-pattern rule with a provisional curator note.

## Recommended Edits

- Remove `CARBON_SOURCE` unless source-backed evidence for malonic acid as a
  media carbon source can be attached.
