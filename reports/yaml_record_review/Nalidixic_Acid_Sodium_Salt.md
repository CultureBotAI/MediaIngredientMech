# `data/ingredients/mapped/Nalidixic_Acid_Sodium_Salt.yaml`

## Verdict

Needs curation - major. The `cas:3374-05-8` nalidixate sodium anhydrous
identity, parent `CHEBI:100147` mapping, exact registry rows, and
CAS-backed structure pass, but final SSSOM exports a parent-acid synonym and
the `SELECTIVE_AGENT` role is still provisional.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Nalidixic_Acid_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:3374-05-8` with
  `ontology_mapping.ontology_id: CHEBI:100147`, label `nalidixic acid`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media; the creation
  event traces the CAS fallback to the CultureBotHT Hans80 antibiotic and FEBA
  stress panels.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nah2po4_X_2_H2o` through `Nalidixic_Acid_Sodium_Salt`: exited 0 and left
  `reports/instance_validation_failures.tsv` header-only.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.

## Evidence

- A fresh PubChem CAS lookup for `3374-05-8` resolves to nalidixate sodium
  anhydrous with the same formula, PubChem CID, InChI, and SMILES as the
  record.
- A fresh exact OLS4 search for `Nalidixic acid sodium salt` and a fresh OLS4
  search for `3374-05-8` returned zero CHEBI hits; keeping `cas:3374-05-8` as
  the exact identity with an acid parent mapping is still appropriate.
- The final SSSOM output carries both expected exact registry rows:
  `cas:3374-05-8` and
  `kgmicrobe.compound:nalidixic_acid_sodium_salt`. Their `UNKNOWN_TERM`
  validation stamps are expected for CAS and kg-microbe registry identifiers
  and are already triaged in `mappings/ingredient_mappings_unknown_term_triage.tsv`.
- Major: the parent `skos:narrowMatch CHEBI:100147` row publishes
  `1-ethyl-7-methyl-4-oxo-1,4-dihydro-1,8-naphthyridine-3-carboxylic acid` in
  final SSSOM `other`. That is an OLS synonym for neutral nalidixic acid, not
  for the sodium salt identity.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from `infer_roles_from_name_lists`, and
  the curator note explicitly marks it provisional.

## Completeness

- The CAS identity, PubChem structure, local exact registry rows, ChEBI parent
  mapping, empty CultureMech occurrence count, and unknown-term triage rows are
  present.
- The active final SSSOM parent-row synonym and unsupported selective-agent
  role are the remaining consequential gaps.

## Recommended Edits

- Major: remove or suppress the parent-acid IUPAC synonym from
  `data/ingredients/mapped/Nalidixic_Acid_Sodium_Salt.yaml` so the parent
  `skos:narrowMatch` row keeps only nalidixate sodium salt synonyms.
- Major: either remove `physicochemical_roles.SELECTIVE_AGENT` or replace its
  name-pattern placeholder with source-backed evidence from maintained
  CultureBotHT role input or literature. Rerun strict validation and final
  SSSOM validation after these changes.
