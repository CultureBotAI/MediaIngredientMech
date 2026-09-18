# `data/ingredients/mapped/Levulinic_Acid.yaml`

## Verdict

Needs curation. The CAS-backed CHEBI:45630 identity, CAS RN, PubChem structure,
occurrence count, and final SSSOM row pass, but `nutritional_roles.CARBON_SOURCE`
is still a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Levulinic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:45630` with
  `ontology_mapping.ontology_id: CHEBI:45630`, label `4-oxopentanoic acid`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `123-76-2`, molecular formula `C5H8O3`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Levorin` through `Lignin`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for
  `Levulinic_Acid.yaml`, `Lichenan_Icelandic_Moss.yaml`, `Licl.yaml`, and
  `Lignin.yaml`.

## Evidence

- EBI OLS4 resolves `CHEBI:45630` as active `4-oxopentanoic acid`, lists
  `levulinic acid` as a synonym, lists CAS `123-76-2`, and records the same
  formula, InChI, and SMILES as the YAML record.
- PubChem resolves CAS RN `123-76-2` to CID `11579` with formula `C5H8O3` and
  the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:45630`; its
  `other` field contains only `CAS:123-76-2`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated media-role name pattern and
  says review is recommended. The record needs inspected medium-level evidence
  that exact levulinic acid was supplied as a carbon source before retaining
  that role.

## Completeness

- The active CHEBI identity, CAS RN, formula, structure block, aggregate copy,
  one-recipe occurrence count, and final SSSOM row are present and consistent.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Levulinic_Acid.yaml` with inspected source evidence
  for exact levulinic acid use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  change; rerun strict, term, round-trip, component, and SSSOM validation.
