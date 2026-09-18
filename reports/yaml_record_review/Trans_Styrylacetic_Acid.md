# `data/ingredients/mapped/Trans_Styrylacetic_Acid.yaml`

## Verdict

Pass. The reviewed local `kgmicrobe.compound` placeholder identity, retained
exact synonym, aggregate row, and final SSSOM row for trans-styrylacetic acid
are synchronized pending a future exact external ontology term.

## Identity

- Reviewed record: `data/ingredients/mapped/Trans_Styrylacetic_Acid.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.compound:trans_styrylacetic_acid` with matching
  `ontology_mapping.ontology_id`, label `Trans Styrylacetic Acid`, source
  `kgmicrobe.compound`, `mapping_quality: PLACEHOLDER`, `mapping_status:
  MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: exact hyphenated lowercase surface `trans-styrylacetic acid`.
- Occurrences: no MediaDive/media occurrence count.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trans-cinnamic_Acid` through `Trehalose`: exited 0 and wrote zero ERROR
  rows.
- Direct old Engine A/OBO term validation was skipped for this row because
  `kgmicrobe.compound` is a non-OBO local registry prefix.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- The May manual candidate review rejected the CHEBI candidates as unrelated
  trans-acid lexical hits and retained the local compound placeholder.
- Fresh exact OLS4 search for `Trans Styrylacetic Acid` returns no exact
  external ontology hit, so the reviewed local placeholder still represents
  the best available exact identity.
- The final SSSOM row has
  `MIM:Trans_Styrylacetic_Acid skos:exactMatch
  kgmicrobe.compound:trans_styrylacetic_acid` and exports only the hyphenated
  exact synonym in `other`.

## Completeness

- The local identity, exact synonym, aggregate copy, and final SSSOM row agree.
- No roles, components, chemical properties, or environmental contexts are
  asserted.

## Recommended Edits

- None until an exact external ontology term is curated.
