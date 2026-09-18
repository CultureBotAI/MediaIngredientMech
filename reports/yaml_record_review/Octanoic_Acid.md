# `data/ingredients/mapped/Octanoic_Acid.yaml`

## Verdict

Needs curation, major. The CAS-backed `CHEBI:28837` octanoic acid identity and
final SSSOM synonyms pass, but `CARBON_SOURCE` is only a provisional
name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Octanoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:28837` with
  `ontology_mapping.ontology_id: CHEBI:28837`, label `octanoic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: curated `Caprylic acid`.
- Structure: `cas_rn: 124-07-2`, formula `C8H16O2`, and matching InChI and
  SMILES populated from the CAS-backed CultureBotHT import.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:28837` as active `octanoic acid`,
  carries CAS xref `124-07-2`, lists `Caprylic acid` as a synonym, and reports
  the same formula, InChI, and SMILES stored in the YAML.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirms the final
  `CHEBI:28837` mapping.
- The final SSSOM row maps `MIM:Octanoic_Acid` exactly to `CHEBI:28837`; its
  `other` tokens are the curated synonym `Caprylic acid` and the structured
  `CAS:124-07-2` value.
- `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule with a
  provisional curator note.

## Completeness

- The active ChEBI term, CAS xref, synonym, formula, structure fields, final
  SSSOM synonyms, and SSSOM row-review result agree.
- The only consequential gap is source evidence for the carbon-source role.

## Recommended Edits

- In `data/ingredients/mapped/Octanoic_Acid.yaml`, remove
  `nutritional_roles.CARBON_SOURCE` or replace the provisional
  `COMPUTATIONAL_PREDICTION` evidence with source evidence that demonstrates
  this role for octanoic acid.
- Sync the aggregate record, regenerate the final SSSOM, and rerun strict
  validation plus `scripts/validate_sssom_invariants.py`.
