# `data/ingredients/mapped/Cholin_Acetate.yaml`

## Verdict

Needs curation, major. The existing CAS fallback is internally coherent and
still exports, but it is stale: OLS now resolves `Cholin acetate` to active
`CHEBI:15355` acetylcholine, whose synonym and CAS structure match this record.

## Identity

- Reviewed record: `data/ingredients/mapped/Cholin_Acetate.yaml`.
- Current identifier and grounding: `identifier: cas:14586-35-7`,
  `ontology_mapping.ontology_id: cas:14586-35-7`,
  `ontology_label: Cholin acetate`, `ontology_source: CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- OLS exact and non-exact searches for `cholin acetate` now return active
  `CHEBI:15355` acetylcholine, with `choline acetate` among its related
  synonyms.
- PubChem lookup of CAS `14586-35-7` returns CID `11643980` with formula
  `C7H17NO3` and the same standard InChI stored in this record, so the source
  registry identity is the same compound now covered by `CHEBI:15355`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chocolate_agar.yaml data/ingredients/mapped/Cholesterol_Lipid_Concentrate.yaml data/ingredients/mapped/Cholic_Acid.yaml data/ingredients/mapped/Cholin_Acetate.yaml data/ingredients/mapped/Choline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ... -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  `cas:14586-35-7` is outside Engine A term-validation scope. A narrowed run
  over the three CHEBI-scoped records in this batch passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active `MIM:Cholin_Acetate` SSSOM row as an exact CAS
  registry fallback and the expected unknown-term triage row for the CAS CURIE.
- That same hidden/ignored-inclusive search found no active MIM record mapped
  to `CHEBI:15355`; hits for `14586-35-7` still belong to this stale fallback
  record and its generated copies or backups.
- The record's creation evidence states that no ChEBI entry existed when the
  CAS fallback was created. That decision has aged out because current OLS now
  exposes the exact ChEBI identity.
- The record carries no role, component, or environment claims.

## Completeness

- The current CAS fallback SSSOM row, aggregate copy, and docs row are
  synchronized, but the record is missing the now-available exact ChEBI primary
  identity.

## Recommended Edits

- In `data/ingredients/mapped/Cholin_Acetate.yaml`, promote the record from the
  `cas:14586-35-7` fallback to `CHEBI:15355` acetylcholine, keep
  `14586-35-7` as `chemical_properties.cas_rn`, retain `Cholin acetate` as a
  raw source synonym if desired, and record that the earlier fallback became
  stale once ChEBI exposed the exact term.
- Rerun the maintained per-record writer, sync `data/curated/`, rebuild
  `mappings/ingredient_mappings.sssom.tsv`, and prove the repair with strict
  validation, term validation, aggregate/roundtrip verification, and
  `scripts/validate_sssom_invariants.py`.
