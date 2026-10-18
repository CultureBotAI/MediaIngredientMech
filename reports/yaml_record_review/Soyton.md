# `data/ingredients/mapped/Soyton.yaml`

## Verdict

Pass. The record keeps the misspelled `Soyton` source token on a local
`kgmicrobe.ingredient` identity after retiring the unrelated green-kidney-bean
FOODON mapping, and the final SSSOM row carries no unsafe Soytone aliases.

## Identity

- Reviewed record: `data/ingredients/mapped/Soyton.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:soyton` with
  `ontology_mapping.ontology_id: kgmicrobe.ingredient:soyton`, label `Soyton`,
  source `kgmicrobe.ingredient`, `mapping_quality: PLACEHOLDER`,
  `mapping_status: MAPPED`, and `ingredient_type: UNDEFINED_MIXTURE`.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Soyton` through `Spermidine_Trihydrochloride`: exited 0 and wrote zero ERROR
  rows.
- Engine A term validation was skipped for this local `kgmicrobe.ingredient`
  target; the non-OBO CURIE is covered by the product validator rather than
  OAK.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- The YAML curation history records the prior repair from an unrelated
  `FOODON:03302071` green-kidney-bean target to
  `kgmicrobe.ingredient:soyton`.
- Fresh exact OLS4 searches for `Soyton` and `Soytone` in FOODON both returned
  zero documents, so the local placeholder remains the bounded external
  grounding for this source spelling.
- The final SSSOM row is a local identity row with empty `other`; it does not
  publish `Soytone`, `Bacto Soytone`, or any of the canonical soy-peptone
  aliases from nearby records.

## Completeness

- A gitignore-independent `rg --no-ignore --hidden` scan across maintained
  `data`, `src`, `tests`, `mappings`, `scripts`, and
  `reports/hydrate_grounding.tsv`, excluding generated backups and prior YAML
  review reports, found the expected soy-peptone and Bacto-Soytone aliases but
  no second active `Soyton` ingredient.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
