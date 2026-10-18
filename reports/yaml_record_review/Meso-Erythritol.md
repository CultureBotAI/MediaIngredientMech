# `data/ingredients/mapped/Meso-Erythritol.yaml`

## Verdict

Needs curation. The CAS-grounded ChEBI identity, structure, exact synonym, and
final SSSOM row pass, but `CARBON_SOURCE` is only a provisional ChEBI-ancestry
inference.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Meso-Erythritol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17113` with
  `ontology_mapping.ontology_id: CHEBI:17113`, label `erythritol`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.
- Chemical identity: `cas_rn: 149-32-6`, formula `C4H10O4`, and InChI and
  SMILES copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Meso-Erythritol` through `Methane`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:17113` as active `erythritol` with CAS `149-32-6`,
  formula `C4H10O4`, the same InChI and SMILES carried in the YAML, and the
  curated `MESO-ERYTHRITOL` synonym.
- PubChem resolves CAS `149-32-6` to CID 222285 with formula `C4H10O4` and the
  same InChI carried in the YAML.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Meso-Erythritol` to `CHEBI:17113`, with `CAS:149-32-6` as the only
  `other` token.

## Completeness

- `CARBON_SOURCE` is only backed by a `COMPUTATIONAL_PREDICTION` inferred from
  ChEBI carbohydrate ancestry. No source attached to the role verifies that
  this meso-erythritol record was supplied as a carbon source.

## Recommended Edits

- Curate recipe or literature evidence for `CARBON_SOURCE`, or remove the
  provisional nutritional role.
