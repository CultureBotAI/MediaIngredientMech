# `data/ingredients/mapped/Minerals.yaml`

## Verdict

Needs curation. `CHEBI:46662` is active and validates, but the record treats
the bare CultureMech `Minerals` surface as an exact synonym of ChEBI's
geologic `mineral` class even though OLS exposes `minerals` only as a related
synonym, not an exact one.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Minerals.yaml`.
- Identifier and grounding: `identifier: CHEBI:46662` with
  `ontology_mapping.ontology_id: CHEBI:46662`, label `mineral`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Occurrences: one CultureMech recipe occurrence.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mineral_3B_Solution_Minus_Phosphorus` through `Minerals`: exited 0 and
  wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- EBI OLS4 resolves `CHEBI:46662` as active `mineral`, but its OLS synonym
  scope for `minerals` is `related_synonyms`.
- `mappings/culturemech_residual_groundings.tsv` grounded the single residual
  `Minerals` surface to `CHEBI:46662` as a new record.
- The only originating CultureMech recipe also contains many explicit mineral
  salt rows and a `Vitamins` stock row, so the bare `Minerals` row needs
  human review before it is safe to equate it to the geologic ChEBI class.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Minerals` to
  `CHEBI:46662`.

## Completeness

- The CHEBI target is active, the structured CultureMech provenance is present,
  and the final row has empty `other`.
- The current evidence note says `minerals` exactly matched an exact ontology
  synonym, but the fresh OLS4 result places that token under related synonyms.

## Recommended Edits

- Major: re-review the CultureMech `Minerals` row and either ground it to a
  stock-solution record for the source recipe or record stronger evidence that
  its intended referent is `CHEBI:46662`.
- Major: if `CHEBI:46662` is retained, revise the evidence and
  `mapping_quality` so they no longer claim an exact ontology synonym.
