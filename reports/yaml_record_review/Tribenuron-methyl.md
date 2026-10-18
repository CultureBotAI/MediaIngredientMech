# `data/ingredients/mapped/Tribenuron-methyl.yaml`

## Verdict

Pass. The CAS-to-CHEBI identity, exact synonym, CAS RN, PubChem structure,
aggregate row, and final SSSOM row for tribenuron methyl are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Tribenuron-methyl.yaml`.
- Identifier and grounding: `identifier: CHEBI:9678` with matching
  `ontology_mapping.ontology_id`, label `tribenuron methyl`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `101200-48-0`.
- Synonyms: exact ChEBI systematic name for the methyl ester.
- Occurrences: no MediaDive/media occurrence count.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tribenuron-methyl` through `Tricine`: exited 0 and wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `tribenuron methyl` returns `CHEBI:9678` with
  label `tribenuron methyl`.
- Fresh PubChem lookup for CAS `101200-48-0` returns formula `C15H17N5O6S` and
  the same InChI as the YAML.
- The final SSSOM row has
  `MIM:Tribenuron-methyl skos:exactMatch CHEBI:9678` and exports only the
  exact ChEBI synonym plus `CAS:101200-48-0` in `other`.

## Completeness

- The CHEBI identity, CAS RN, structure fields, exact synonym, aggregate copy,
  and final SSSOM row agree.
- No roles, components, environmental contexts, or bad final SSSOM tokens are
  asserted.

## Recommended Edits

- None.
