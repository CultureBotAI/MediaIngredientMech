# `data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml`

## Verdict

Needs curation, with a major supplied-form boundary issue. CAS
`108321-42-2` and PubChem CID 16218858 support G418 disulfate, but the record
denotes a `salt solution`, stores the salt CAS as an exact registry identity,
and publishes bare `G418` as a final SSSOM synonym.

## Identity

- Reviewed record:
  `data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml`.
- Identifier and grounding: `identifier: cas:108321-42-2` with matching
  `ontology_mapping.ontology_id`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `108321-42-2` returned CID 16218858 among the
  disulfate records, and CID 16218858 has formula `C20H44N4O18S2` plus the
  same InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml data/ingredients/mapped/G9_Trace_Metals_For_J_Medium.yaml data/ingredients/mapped/GYPS.yaml data/ingredients/mapped/Galactarate.yaml data/ingredients/mapped/Galactitol.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation passed for the two CHEBI-primary files in this batch
  and was intentionally skipped for this CAS-primary registry record because
  Engine A/OBO term validation does not cover CAS registry CURIEs.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  CAS identifier, CultureBotHT source, structure fields, CAS RN, `G418`
  synonym, and ingredient type as the per-record YAML.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` marks the CAS row as
  an expected registry identifier, so the CAS CURIE itself is not an OAK/OLS
  repair target.
- Major: the PubChem identity is the G418 disulfate salt, while the record's
  preferred term and ontology label both include `solution`. If the MIM subject
  is a stock solution, the exact registry ID should be a local ingredient with
  the active disulfate salt represented as a component or supplied form; if the
  intended subject is the salt, the label should drop `solution`.
- Major: final SSSOM maps `MIM:G418_Disulfate_Salt_Solution` exactly to
  `cas:108321-42-2` and publishes `G418` in `other`, but bare G418 erases the
  disulfate salt and solution boundaries.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, row-review manifest row, and expected CAS unknown-term triage row.

## Completeness

- The CAS RN, registry fallback row, PubChem structure fields, and CultureBotHT
  provenance are populated.
- The record has not resolved whether it represents the active G418 disulfate
  chemical or a purchased stock solution containing that chemical.

## Recommended Edits

- Major: choose the maintained identity for
  `data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml`; either make the
  record a local stock-solution mint with G418 disulfate as a component or
  supplied form, or rename it to the disulfate salt and keep
  `cas:108321-42-2` as the exact registry identity.
- Major: remove or retag bare `G418` unless the chosen subject is the free-base
  antibiotic rather than the disulfate salt or the stock solution; regenerate
  final SSSOM and rerun SSSOM invariants to prove `other` contains only true
  same-subject aliases.
