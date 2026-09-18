# `data/ingredients/mapped/Tetracycline_Hydrochloride.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:35006` hydrochloride identity, CAS RN,
aggregate row, and final SSSOM row pass, but `SELECTIVE_AGENT` is still only a
provisional name-pattern role.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Tetracycline_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:35006` with
  `ontology_mapping.ontology_id: CHEBI:35006`, label
  `Tetracycline hydrochloride`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `64-75-5` and formula `C22H24N2O8.HCl`.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetracycline` through `Tetramethyl_Ammonium_Chloride`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:35006` as `Tetracycline
  hydrochloride` and lists `cas:64-75-5` as a database cross-reference.
- Fresh PubChem lookup by CAS `64-75-5` resolves CID 54704426, confirms a
  tetracycline hydrochloride InChI and the `C22H25ClN2O8` formula equivalent to
  `C22H24N2O8.HCl`, and lists CAS `64-75-5`.
- The final SSSOM has exactly one exact CHEBI row for
  `MIM:Tetracycline_Hydrochloride`, points at `CHEBI:35006`, names
  `obo:chebi.owl`, and publishes only `CAS:64-75-5` in `other`.
- Major: `physicochemical_roles.SELECTIVE_AGENT` cites only
  `reference_type: COMPUTATIONAL_PREDICTION` from a curated name pattern and
  explicitly notes that review is recommended.

## Completeness

- The CHEBI hydrochloride identity, CAS, aggregate row, and final SSSOM row
  agree.
- The selective-agent role is incomplete until it is replaced with
  source-backed evidence for tetracycline hydrochloride as a selective agent or
  removed.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT import,
  aggregate, row-review, final SSSOM, and generated rows.

## Recommended Edits

- Major: replace the provisional name-pattern `SELECTIVE_AGENT` role in
  `data/ingredients/mapped/Tetracycline_Hydrochloride.yaml` with source-backed
  evidence for tetracycline hydrochloride as a selective agent, or remove the
  role if no maintained source supports it.
- Major: after any role edit, synchronize `data/curated/mapped_ingredients.yaml`
  and regenerate generated products so the role facets match the per-record
  YAML.
