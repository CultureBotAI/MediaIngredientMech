# `data/ingredients/mapped/Lemon.yaml`

## Verdict

Pass. The NCIT:C72005 exact identity, occurrence count, empty synonym payload,
and final SSSOM row are internally consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/Lemon.yaml`.
- Identifier and grounding: `identifier: NCIT:C72005` with
  `ontology_mapping.ontology_id: NCIT:C72005`, label `Lemon`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Source provenance: imported from the `mim-queue` row for
  `mediadive.ingredient:2091` by OLS label-exact NCIT matching.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lecithin` through `Leucodin`: exited 0 and wrote zero ERROR rows.
- LinkML term validation was skipped for this NCIT-primary record because the
  successful batch check covered only the CHEBI-primary records.

## Evidence

- Current OLS exact search resolves `NCIT:C72005` as `Lemon`.
- The same exact search also finds `FOODON:03315104` as exact `lemon`, a FoodOn
  fruit class that would be a domain-specific exact target if a curator chooses
  to move this food ingredient out of NCIT.
- The final SSSOM publishes one `skos:exactMatch` row to `NCIT:C72005`; its
  `other` field is empty.
- The 2/2 occurrence count agrees with the refreshed CultureMech occurrence
  table.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  row and no sibling MIM record that would split the same lemon identity.

## Completeness

- The active NCIT identity, occurrence count, aggregate copy, and final SSSOM row
  are present and consistent.

## Recommended Edits

- None.
