# `data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml`

## Verdict

Needs curation. The source-qualified kgmicrobe.ingredient identity, narrower
CHEBI:6452 parent mapping, CAS payload, registry sibling rows, and final SSSOM
predicates pass, but `nutritional_roles.CARBON_SOURCE` is still a provisional
CHEBI-ancestry inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:lichenan_icelandic_moss`
  with `ontology_mapping.ontology_id: CHEBI:6452`, label `lichenin`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `1402-10-4`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Levorin` through `Lignin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for
  `Levulinic_Acid.yaml`, `Lichenan_Icelandic_Moss.yaml`, `Licl.yaml`, and
  `Lignin.yaml`.

## Evidence

- EBI OLS4 resolves `CHEBI:6452` as active `lichenin`, lists `Lichenan` as a
  synonym, and lists CAS `1402-10-4`.
- PubChem lookup by CAS RN `1402-10-4` resolves to a small monomer-like
  structure, so it is not used as structure support for this source-qualified
  lichenan polymer record.
- The final SSSOM publishes the expected `skos:narrowMatch` row to
  `CHEBI:6452` plus exact registry rows to
  `kgmicrobe.ingredient:lichenan_icelandic_moss` and
  `kgmicrobe.compound:lichenan_icelandic_moss`, preserving the local subject
  identity required for a parent mapping.
- The registry-row `other` fields contain only `CAS:1402-10-4`; the CHEBI
  parent row has an empty `other` field.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from CHEBI ancestry through
  `CHEBI:16646` and says review is recommended. The carbohydrate ancestry is
  enough to propose the role, but the record still lacks inspected
  medium-level evidence that exact lichenan from Icelandic moss was supplied as
  a carbon source.

## Completeness

- The local identifier, active CHEBI parent, CAS RN, aggregate copy, and final
  SSSOM registry rows are present and consistent.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Lichenan_Icelandic_Moss.yaml` with inspected source
  evidence for exact lichenan from Icelandic moss use, or remove the provisional
  role.
- Sync the aggregate copy and regenerate final SSSOM after the YAML change;
  rerun strict, term, round-trip, component, and SSSOM validation.
