# `data/ingredients/mapped/Indolicidin.yaml`

## Verdict

Pass. The CultureBotHT CAS-derived exact ChEBI identity, CAS alias, lack of
ChEBI structural fields, and final SSSOM row are consistent for indolicidin.

## Identity

- Reviewed record: `data/ingredients/mapped/Indolicidin.yaml`.
- Identifier and grounding: `identifier: CHEBI:80180` with
  `ontology_mapping.ontology_id: CHEBI:80180`, label `Indolicidin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `140896-21-5`; ChEBI does not expose formula,
  InChI, or SMILES annotations for this term in OLS.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Indole-3-propionic_Acid.yaml data/ingredients/mapped/Indole-3-pyruvic_Acid.yaml data/ingredients/mapped/Indole.yaml data/ingredients/mapped/Indole_3-acetic_Acid_Sodium_Salt.yaml data/ingredients/mapped/Indolicidin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for the 4 CHEBI/OBO-compatible
  records; `Indole-3-pyruvic_Acid` was outside adapter scope because its
  primary identifier is a CAS registry CURIE.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_1555`
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_1555`
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- OLS4 resolves `CHEBI:80180` as the active ChEBI class `Indolicidin` and lists
  the KEGG compound xref already used in the final SSSOM object source set.
- PubChem resolves CAS RN `140896-21-5` to an indolicidin structure, so the
  record's CAS alias is externally resolvable even though ChEBI does not carry
  formula or structure annotations for `CHEBI:80180`.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Indolicidin`
  to `CHEBI:80180` and exports only `CAS:140896-21-5` in `other`.
- The hidden and ignored-inclusive search over `data`, `src`, `tests`,
  `mappings`, `scripts`, `conf`, `docs`, and `.claude` found the current
  aggregate row, final SSSOM row, docs projections, and OAK/OLS review row
  marking the mapping `CONFIRMED`.

## Completeness

- The active ChEBI identifier, CAS RN, aggregate copy, and final SSSOM row are
  present and consistent.
- No unsupported roles or non-synonym final `other` tokens are asserted.

## Recommended Edits

- None.
