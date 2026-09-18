# `data/ingredients/mapped/D-Glucosamine_Hydrochloride.yaml`

## Verdict

Pass. The CultureBotHT CAS primary is retained for D-glucosamine hydrochloride,
`NCIT:C83732` resolves as the broader Glucosamine Hydrochloride parent, the
CAS and kg-microbe registry SSSOM rows preserve the specific local identity,
and the record exports no unsafe synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/D-Glucosamine_Hydrochloride.yaml`.
- Current identifier and grounding: `identifier: cas:66-84-2`,
  `ontology_mapping.ontology_id: NCIT:C83732`,
  `ontology_label: Glucosamine Hydrochloride`, `ontology_source: NCIT`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Live prefix-specific OLS lookup for `NCIT:C83732` returns current label
  `Glucosamine Hydrochloride`.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `cas:66-84-2` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Galacturonic_Acid_Monohydrate.yaml data/ingredients/mapped/D-Glucaric_Acid.yaml data/ingredients/mapped/D-Gluconic_acid.yaml data/ingredients/mapped/D-Glucosamine_6-phosphate.yaml data/ingredients/mapped/D-Glucosamine_Hydrochloride.yaml`:
  passed; 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Glucaric_Acid.yaml data/ingredients/mapped/D-Gluconic_acid.yaml data/ingredients/mapped/D-Glucosamine_6-phosphate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch.
  This record and `D-Galacturonic_Acid_Monohydrate` were intentionally skipped
  because their primary identifiers are CAS registry CURIEs.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- The CAS primary, PubChem-derived formula, SMILES, InChI, and CID all describe
  the D-glucosamine hydrochloride supplied form rather than the generic NCIT
  parent.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` records that
  prefix-specific EBI OLS resolves `NCIT:C83732` exactly and that the CAS and
  kg-microbe rows are expected registry identifiers.
- `mappings/culturemech_recipe_membership.tsv` contains no rows for this CAS
  primary or `NCIT:C83732`, matching the record's 0/0
  `occurrence_statistics`.
- The final SSSOM publishes the `MIM:D-Glucosamine_Hydrochloride
  skos:narrowMatch NCIT:C83732` parent row plus the required exact CAS and
  kg-microbe registry rows, and the only `other` payload is `CAS:66-84-2` on
  the registry rows.

## Completeness

- No roles, active synonyms, or mixture components are asserted, so there are
  no unsupported secondary claims to adjudicate.
- Hidden/ignored-inclusive searches over `data`, `mappings`, `scripts`,
  `tests`, and `reports` found only the expected generic-validator misses and
  prefix-specific acceptance rows; no current curated record conflicts with the
  `cas:66-84-2` identity.

## Recommended Edits

- None for this record.
