# `data/ingredients/mapped/Phleomycin.yaml`

## Verdict

Needs curation; major. The CultureBotHT CAS import maps exactly to active
`CHEBI:75044` phleomycin and final SSSOM CAS output is safe, but
`SELECTIVE_AGENT` is still supported only by a provisional name-list inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Phleomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:75044` with
  `ontology_mapping.ontology_id: CHEBI:75044`, label `phleomycin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 0 MediaRecipe occurrences; this row was created from the
  CultureBotHT CAS table.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:75044` resolves `CHEBI:75044`
  `phleomycin`.
- A fresh PubChem lookup for CAS `11006-33-0` resolves to Phleomycin.
- The final SSSOM row was inspected directly and maps `MIM:Phleomycin`
  exactly to `CHEBI:75044`.

## Evidence

- The CHEBI primary identifier and CultureBotHT CAS both describe phleomycin.
  CHEBI models phleomycin as a glycopeptide-antibiotic mixture, and the record
  correctly avoids formula, InChI, or SMILES assertions for a single pure
  structure.
- The final SSSOM row exports only `CAS:11006-33-0` in `other`, with no stale
  or broader synonyms.
- Major: the `SELECTIVE_AGENT` role is supported only by
  `COMPUTATIONAL_PREDICTION` evidence from a provisional curated name-pattern
  rule.

## Completeness

- The identity and final synonym surface are complete enough for this
  CultureBotHT exact CHEBI mapping.
- Physicochemical-role evidence remains incomplete while the selective-agent
  role is provisional.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phleomycin.yaml`, replace
  `physicochemical_roles.SELECTIVE_AGENT` with source-backed evidence or remove
  the provisional role facet until it is curated.
