# `data/ingredients/mapped/Mgco3.yaml`

## Verdict

Needs curation. The exact synonym mapping to `CHEBI:31793` magnesium carbonate,
PubChem structure, occurrence count, and `kg_microbe_node_id` pass, but malformed
raw CultureMech labels still publish in the final SSSOM `other` field.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mgco3.yaml`.
- Identifier and grounding: `identifier: CHEBI:31793` with
  `ontology_mapping.ontology_id: CHEBI:31793`, label
  `magnesium carbonate`, source `CHEBI`, `mapping_quality: SYNONYM_MATCH`,
  `mapping_status: MAPPED`, `kg_microbe_node_id: CHEBI:31793`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 11 CultureMech recipe occurrences.
- Chemical identity: magnesium carbonate InChI and molecular weight `84.313`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgcl2x_6_H2o` through `Mgso4_X_6_H2o`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the other CHEBI-identified records in the same batch.

## Evidence

- EBI OLS4 resolves exact query `MgCO3` to active `CHEBI:31793`,
  `magnesium carbonate`, with `MgCO3` as a synonym.
- PubChem resolves `MgCO3` to CID 11029 with formula `CMgO3`, molecular weight
  `84.31`, SMILES, and the same InChI carried in the YAML.
- The row was curated from a raw `MgCO3` surface and correctly regraded to
  `SYNONYM_MATCH` because the record's label matches a ChEBI synonym rather
  than the primary ChEBI label.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mgco3` to
  `CHEBI:31793`.

## Completeness

- The active magnesium carbonate target, structure, occurrence count, and
  same-prefix compatibility identifier agree.
- The final SSSOM `other` field still exports raw labels `MgCO` and
  `MgCO3(MCIB CB486)`. `MgCO` is missing carbonate oxygen, and
  `MgCO3(MCIB CB486)` includes the source strain text that the curation audit
  only used to recover the exact `MgCO3` formula.

## Recommended Edits

- Major: mark `MgCO` and `MgCO3(MCIB CB486)` as `REJECTED_LABEL` or otherwise
  filter raw non-synonym CultureMech labels from final SSSOM `other`.
- Minor: backfill the missing local `molecular_formula` and `smiles` fields
  from the active `CHEBI:31793` or PubChem CID 11029 structure.
