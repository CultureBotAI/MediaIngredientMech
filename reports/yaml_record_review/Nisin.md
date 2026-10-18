# `data/ingredients/mapped/Nisin.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:71629` nisin identity, CAS-backed
structure, CultureBotHT provenance, and final SSSOM row pass, but the
`SELECTIVE_AGENT` role is still only a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Nisin.yaml`.
- Identifier and grounding: `identifier: CHEBI:71629` with
  `ontology_mapping.ontology_id: CHEBI:71629`, label `nisin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nicotine_Fluka` through `Nisin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:71629` as active `nisin` with
  formula `C143H230N42O37S7`, CAS `1414-45-5`, and the same InChI and SMILES
  as the record.
- A fresh PubChem CAS lookup for `1414-45-5` resolves to nisin with the same
  InChI, confirming the chemical block and CultureBotHT CAS.
- The final SSSOM row maps `MIM:Nisin` exactly to `CHEBI:71629`; its `other`
  field carries the ChEBI exact IUPAC synonym plus `CAS:1414-45-5`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern,
  not inspected source text for nisin as a selective agent in media.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, CultureBotHT provenance,
  ingredient type, and final exact row otherwise agree.
- The remaining consequential gap is the unsupported provisional selective role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Nisin.yaml`, replace the provisional
  `SELECTIVE_AGENT` role with inspected claim-level evidence or remove it.
