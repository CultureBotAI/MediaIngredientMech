# `data/ingredients/mapped/Levodopa.yaml`

## Verdict

Needs curation. The CAS-backed CHEBI:15765 identity, CAS RN, PubChem structure,
exact synonym, and final SSSOM row pass, but `nutritional_roles.AMINO_ACID_SOURCE`
is still a provisional CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Levodopa.yaml`.
- Identifier and grounding: `identifier: CHEBI:15765` with
  `ontology_mapping.ontology_id: CHEBI:15765`, label `L-dopa`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `59-92-7`, molecular formula `C9H11NO4`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Leupeptin` through `Levomenthol`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`
  exited 0 for all five CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:15765` as active `L-dopa`, lists `levodopa` and
  `(2S)-2-amino-3-(3,4-dihydroxyphenyl)propanoic acid` as synonyms, lists CAS
  `59-92-7`, and records the same formula, InChI, and SMILES as the YAML record.
- PubChem resolves CAS RN `59-92-7` to CID `6047` with formula `C9H11NO4` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:15765`; its
  `other` field contains only the curated ChEBI synonym and `CAS:59-92-7`.
  The `semapv:ManualMappingCuration` justification is compatible with
  `mapping_quality: CAS_RN_LOOKUP` because the object row targets the record's
  own identifier.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:33709` and says review is recommended. That class ancestry is enough
  to propose the role, but the record lacks inspected medium-level evidence
  that levodopa was supplied as an amino acid source.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  and final SSSOM row are present and consistent.
- The provisional amino-acid-source role needs curation before it can be
  treated as a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE` in
  `data/ingredients/mapped/Levodopa.yaml` with inspected source evidence for
  exact levodopa use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  change; rerun strict, term, round-trip, component, and SSSOM validation.
