# `data/ingredients/mapped/Tricalcium_Phosphate.yaml`

## Verdict

Pass. The CAS-to-CHEBI identity, formula alias, CAS RN, PubChem structure,
occurrence count, aggregate row, and final SSSOM row for tricalcium phosphate
are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Tricalcium_Phosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:9679` with matching
  `ontology_mapping.ontology_id`, label `tricalcium bis(phosphate)`, source
  `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `7758-87-4`.
- Synonyms: formula alias `Ca3(PO4)2`.
- Occurrences: 1 CultureMech recipe occurrence in 1 medium.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tribenuron-methyl` through `Tricine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `tricalcium bis(phosphate)` returns `CHEBI:9679`
  and lists `Ca3(PO4)2` among the related synonyms for that term.
- Fresh PubChem lookup for CAS `7758-87-4` returns formula `Ca3O8P2` and the
  same calcium/phosphate InChI as the YAML.
- The final SSSOM row has
  `MIM:Tricalcium_Phosphate skos:exactMatch CHEBI:9679` and exports only the
  formula alias plus `CAS:7758-87-4` in `other`.

## Completeness

- The CHEBI identity, CAS RN, structure fields, formula alias, occurrence
  count, aggregate copy, and final SSSOM row agree.
- No roles, components, environmental contexts, or bad final SSSOM tokens are
  asserted.

## Recommended Edits

- None.
