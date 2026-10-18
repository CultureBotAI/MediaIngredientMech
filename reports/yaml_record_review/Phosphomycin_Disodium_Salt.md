# `data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml`

## Verdict

Needs curation; major. The CultureBotHT CAS fallback identity for
`cas:26016-99-9` is sound and no CHEBI primary was found, but
`SELECTIVE_AGENT` is still supported only by a provisional name-list inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:26016-99-9` with matching
  `ontology_mapping.ontology_id`, label `Phosphomycin disodium salt`, source
  `CAS`, `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh PubChem lookup for the stored CID resolves to Fosfomycin Sodium with
  formula `C3H5Na2O4P`.
- A fresh OLS4 exact search for CAS `26016-99-9` in CHEBI returned no hits.
- The final SSSOM row was inspected directly and preserves the exact
  `cas:26016-99-9` registry identity.

## Evidence

- The CAS primary identifier, mapping target, CAS `26016-99-9`, PubChem CID,
  structured formula, SMILES, and InChI all describe disodium
  fosfomycin/phosphomycin.
- The row-review and unknown-term triage tables keep this CAS primary as an
  expected local registry identifier rather than an OAK/OLS ontology term.
- The final SSSOM row exports only `CAS:26016-99-9` in `other`.
- Major: the `SELECTIVE_AGENT` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from a provisional curated name-pattern
  rule.

## Completeness

- The CAS fallback identity is complete enough while no exact CHEBI term exists
  for `26016-99-9`.
- Physicochemical-role evidence remains incomplete while the selective-agent
  role is provisional.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml`, replace
  `physicochemical_roles.SELECTIVE_AGENT` with source-backed evidence or remove
  the provisional role facet until it is curated.
