# `data/ingredients/mapped/Modified_Wolfes_Minerals.yaml`

## Verdict

Pass. The local Modified Wolfe's Minerals stock identity, ten-component
CultureBotHT transcription, mineral-source role, fallback registry mapping, and
final registry row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Modified_Wolfes_Minerals.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:modified_wolfes_minerals` with
  `ontology_mapping.ontology_id:
  kgmicrobe.ingredient:modified_wolfes_minerals`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: MINERAL_STOCK`.
- Occurrences: three CultureBotHT media occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Modified_Wolfes_Minerals` through `Mono-_And_Disaccharides`: exited 0 and
  wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.ingredient` identifier is outside the OBO
  subset used for the batch.

## Evidence

- Google Sheets `Mixes!A206:C215` still lists exactly the ten components and
  gram-per-liter concentrations transcribed into `components`: nitrilotriacetic
  acid, magnesium sulfate, manganese sulfate monohydrate, sodium chloride,
  cobalt chloride hexahydrate, calcium chloride dihydrate, zinc sulfate
  heptahydrate, aluminum potassium sulfate dodecahydrate, boric acid, and
  sodium molybdate dihydrate.
- The #114/#288 fallback-registry rationale is still appropriate: this is a
  named multi-component mineral stock, not a single external ontology
  substance.
- A fresh exact EBI OLS4 lookup for `Modified Wolfe's Minerals` returned no
  same-label external class.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Modified_Wolfes_Minerals` to the local registry identifier with empty
  `other`.

## Completeness

- The local stock identity, 3/3 occurrence count, complete component assertion,
  source-backed `MINERAL_SOURCE` role, fallback registry rationale, and final
  exact row agree.
- The record does not publish unsupported roles or non-synonym final `other`
  text.

## Recommended Edits

- None.
