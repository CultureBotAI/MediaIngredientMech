# `data/ingredients/mapped/Phytone.yaml`

## Verdict

Needs curation; major. `Phytone` is correctly treated as an undefined
soy-peptone mixture, but this active product-specific record reuses
`FOODON:03315720` as its primary identifier even though `FOODON:03315720`
denotes the broader vegetable-protein hydrolysate parent already used by the
canonical soy-peptone record.

## Identity

- Reviewed record: `data/ingredients/mapped/Phytone.yaml`.
- Identifier and grounding: `identifier: FOODON:03315720` with
  `ontology_mapping.ontology_id: FOODON:03315720`, label
  `vegetable protein, hydrolyzed`, source `FOODON`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 1089 total occurrences across 833 recipes, copied from the full
  `FOODON:03315720` group by the #337 occurrence refresh.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `FOODON:03315720` resolves `FOODON:03315720`
  `vegetable protein, hydrolyzed`.
- The final SSSOM row was inspected directly and maps `MIM:Phytone` exactly to
  `FOODON:03315720`.
- An ignored/hidden-inclusive local search over `data/ingredients`,
  `data/curated`, `mappings`, `reports`, `scripts`, `src`, `tests`, `docs`,
  and `UNIFIED_INGREDIENT_MAPPING.tsv` found the active `Soy_Peptone`,
  `Soya_Peptone`, `Soya_Pepton`, and `Phytone` records on the same
  `FOODON:03315720` identifier and the duplicate-identifier report for that
  four-record group.

## Evidence

- The curated note that `Phytone` is BD's papaic digest of soybean meal
  supports `UNDEFINED_MIXTURE` and a soy-peptone classification.
- Major: the record is product-specific and only close-matches the broad
  FOODON parent, but making `FOODON:03315720` the primary identifier causes the
  final SSSOM to assert an exact match from `MIM:Phytone` to the parent class.
- Major: because this record reuses `FOODON:03315720`, occurrence refresh
  assigned `Phytone` the same 833/1089 occurrence counts as `Soy_Peptone`
  rather than the count for the `Phytone` surface itself.
- The raw duplicate `Phytone` synonym is filtered from final SSSOM `other`.

## Completeness

- The record needs a curator decision: either merge this surface into
  `Soy_Peptone`, or preserve it as a local product/alias record with a local
  primary identifier and `FOODON:03315720` retained only as a close parent.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phytone.yaml`, either reject/merge the
  record into `data/ingredients/mapped/Soy_Peptone.yaml` and keep `Phytone` as
  an appropriate soy-peptone synonym there, or mint a local
  `kgmicrobe.ingredient` primary identifier for the product-specific Phytone
  record and keep `FOODON:03315720` only as the `CLOSE_MATCH` parent.
- Major: after the identity decision, rerun the occurrence refresh or merge
  transfer so this row no longer carries the whole `FOODON:03315720`
  occurrence count unless it is intentionally retired into the representative
  soy-peptone record.
