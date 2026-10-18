# `data/ingredients/mapped/Furaltadone_Hydrochloride.yaml`

## Verdict

Needs curation, with a major predicate/grade issue. The NCIT term resolves as
an exact label match for furaltadone hydrochloride, but the record still grades
that exact target as `NARROW_MATCH`, so final SSSOM publishes a
`skos:narrowMatch` row plus companion registry rows that should not be needed
for this exact external identifier.

## Identity

- Reviewed record: `data/ingredients/mapped/Furaltadone_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: cas:3759-92-1` with
  `ontology_mapping.ontology_id: NCIT:C217928`, label
  `Furaltadone Hydrochloride`, source `NCIT`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `NCIT:C217928` as an exact NCIT CURIE with label
  `Furaltadone Hydrochloride`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fumaric_Acid.yaml data/ingredients/mapped/Fumarprotocetraric_Acid.yaml data/ingredients/mapped/Fungichromin.yaml data/ingredients/mapped/Furaltadone_Hydrochloride.yaml data/ingredients/mapped/Furaxone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation passed for the three CHEBI-primary records in this
  batch and was intentionally skipped for this CAS-primary NCIT record because
  the Engine A/OBO primary-ID check does not cover CAS registry CURIEs.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same CAS
  identifier, NCIT exact label, narrow grade, CAS RN, ingredient type, and
  absence of structure fields as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` output has three rows for
  this subject: `skos:narrowMatch` to `NCIT:C217928`, an exact CAS registry
  row, and a local exact `kgmicrobe.compound:furaltadone_hydrochloride`
  registry row.
- Major: `NCIT:C217928` is an exact label match for this record's preferred
  term, so `mapping_quality: NARROW_MATCH` overstates specificity loss and
  causes the final SSSOM to publish the wrong predicate and companion registry
  shape.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` confirms that the
  NCIT `UNKNOWN_TERM` row was a prefix-dispatch coverage issue rather than a
  broken external CURIE.
- PubChem lookup by CAS RN `3759-92-1` found no CID, so the CAS alias still
  needs registry-source verification if this row is reworked.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports`, excluding prior per-record review reports and
  historical aggregate backups, found the active YAML, aggregate copy, final
  SSSOM rows, NCIT external-prefix validation, row-review entries, and
  expected unknown-term triage rows.

## Completeness

- The exact NCIT target, CAS registry identity, and final SSSOM registry rows
  are populated.
- CAS and chemical structure evidence are incomplete until the CAS RN is
  verified against a source that resolves this hydrochloride.

## Recommended Edits

- Major: regrade `data/ingredients/mapped/Furaltadone_Hydrochloride.yaml` from
  `NARROW_MATCH` to an exact NCIT mapping or promote `NCIT:C217928` as the
  primary identifier, sync `data/curated/mapped_ingredients.yaml`, regenerate
  final SSSOM so it no longer emits `skos:narrowMatch` or unnecessary local
  registry rows, and rerun SSSOM invariants.
- Minor: verify CAS RN `3759-92-1` from the original CultureBotHT input or
  another registry source before keeping it as an exact registry identity.
