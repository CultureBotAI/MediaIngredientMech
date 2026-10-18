# `data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml`

## Verdict

Needs curation; major. The CAS-to-ChEBI lookup for paromomycin sulfate passes,
but the `SELECTIVE_AGENT` role is only a provisional name-list prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:7935` with
  `ontology_mapping.ontology_id: CHEBI:7935`, label `paromomycin sulfate`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: no CultureMech media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `Paromomycin sulfate` resolves `CHEBI:7935`
  `paromomycin sulfate`.
- A local CAS checksum calculation confirmed that `1263-89-4` has the
  expected check digit.
- The final SSSOM row was inspected directly and maps
  `MIM:Paromomycin_Sulfate_Salt` exactly to `CHEBI:7935`.

## Evidence

- The CAS-derived CHEBI primary identifier, mapping target, structured formula,
  InChI, and SMILES all describe paromomycin sulfate.
- The `CAS_RN_LOOKUP` grade accurately records how the mapping was established;
  Rule D still emits the own-identifier row as `skos:exactMatch`.
- The final SSSOM exports the long curated same-salt synonym and
  `CAS:1263-89-4`, which matches the structured CAS-RN.
- The `SELECTIVE_AGENT` role is supported only by `COMPUTATIONAL_PREDICTION`
  evidence from `infer_roles_from_name_lists`.

## Completeness

- The CAS-to-ChEBI mapping and final SSSOM synonym set are complete enough.
- Role evidence remains incomplete because no source-backed selective-agent
  assertion has been curated.

## Recommended Edits

- Major: in `data/ingredients/mapped/Paromomycin_Sulfate_Salt.yaml`, either
  replace `physicochemical_roles.SELECTIVE_AGENT` with cited source evidence
  that supports the selective-agent role for paromomycin sulfate, or remove the
  provisional role facet until source-backed role evidence is curated.
