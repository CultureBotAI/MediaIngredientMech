# `data/ingredients/mapped/Sodium_Persulfate.yaml`

## Verdict

Pass. The `cas:7775-27-1` sodium persulfate identity, MeSH parent row, exact CAS
and kg-microbe registry rows, and final SSSOM payload pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sodium_Persulfate.yaml`.
- Identifier and grounding: `identifier: cas:7775-27-1` with
  `ontology_mapping.ontology_id: mesh:C024625`, label `sodium persulfate`,
  source `MESH`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 current CultureMech occurrences; the record is retained from
  the CultureBotHT compounds input.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sodium_Perchlorate` through `Sodium_Phosphate_Buffer`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this MeSH-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 search by label and accession both resolve `mesh:C024625` as
  `sodium persulfate`, agreeing with the stored parent target.
- Fresh PubChem lookup for CAS `7775-27-1` resolves to sodium persulfate with
  formula `Na2O8S2`.
- Final SSSOM preserves the MeSH parent row plus exact registry rows for
  `cas:7775-27-1` and `kgmicrobe.compound:sodium_persulfate`; the CAS rows use
  only the same-substance `CAS:7775-27-1` in `other`.
- The hidden/ignored-inclusive mapping review search found the old
  `UNKNOWN_TERM` row already triaged as a missing-prefix validator coverage
  issue, with no mapping repair requested.

## Completeness

- The CAS RN, MeSH parent, Rule B1 registry row, and final SSSOM rows agree.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
