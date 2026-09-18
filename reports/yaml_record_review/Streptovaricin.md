# `data/ingredients/mapped/Streptovaricin.yaml`

## Verdict

Pass. The MicrobeDecoder source label exact-matches active `CHEBI:26790`, the
non-media occurrence is kept in `source_occurrences`, and the final SSSOM row
has no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Streptovaricin.yaml`.
- Identifier and grounding: `identifier: CHEBI:26790` with
  `ontology_mapping.ontology_id: CHEBI:26790`, label `streptovaricin`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: 0 CultureMech media occurrences plus 1 MicrobeDecoder source
  occurrence from `BacDive_Metabolite_production`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Streptomycin_Sulfate_Salt` through `Suberic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:26790` with label `streptovaricin`,
  matching the MicrobeDecoder `kgmicrobe.trait:streptovaricin` import label.
- `mappings/microbedecoder_auto_mapped_review.tsv` shows the local
  `review-ingredients` promotion that approved the OAK label check and moved
  the record from `PENDING_REVIEW` back to `MAPPED`.
- The final SSSOM row exact-matches `CHEBI:26790` and leaves `other` empty.

## Completeness

- The exact identity, aggregate row, MicrobeDecoder source occurrence, and
  final SSSOM row agree.
- An ignored/hidden search of local curated, mapping, generated, report, source,
  and documentation paths found the expected rows for this record and no
  unsupported active synonym, role, component, or final SSSOM payload.

## Recommended Edits

- None.
