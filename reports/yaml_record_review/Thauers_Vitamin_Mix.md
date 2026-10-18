# `data/ingredients/mapped/Thauers_Vitamin_Mix.yaml`

## Verdict

Pass. The local Thauer vitamin-stock identity, complete eleven-component
recipe transcription, source-backed vitamin role, aggregate row, and final
SSSOM row are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Thauers_Vitamin_Mix.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:thauers_vitamin_mix` with the same
  `ontology_mapping.ontology_id`, label `Thauer's vitamin mix`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, `ingredient_type: STOCK_SOLUTION`, and
  `solution_type: VITAMIN_MIX`.
- Components: complete `MIM_CATALOG` transcription of 11 CultureBotHT
  Mixes-tab constituents, including biotin and choline chloride.
- Occurrences: eight CultureBot recipe occurrences in eight media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetrodotoxin` through `Thauers_Vitamin_Mix_No_Biotin`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset
  from this batch: `Tetrodotoxin`, `Texazone`, and `Thallium_I_Acetate` all
  passed. This local `kgmicrobe.ingredient` row was skipped because its exact
  local registry CURIE is intentionally outside the OBO term-validator subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- The whole-corpus component partonomy validator passes with this record
  present: `2951` records, `83` decompositions, `505` components, and zero
  violations.

## Evidence

- `MIM curation (#114)` records why this named multi-component lab stock uses a
  local `kgmicrobe.ingredient` registry ID instead of a public ontology class:
  the reviewed preparation is a recurring CultureBotHT vitamin mix rather than
  a single substance.
- The component assertion cites the CultureBotHT media definitions Mixes tab at
  `Mixes!88:98 Thauer's vitamin mix` and transcribes 11 constituents at the
  recorded per-liter concentrations.
- Local OAK resolves the CHEBI component identifiers for pyridoxine
  hydrochloride, 4-aminobenzoic acid, lipoic acid, nicotinic acid, riboflavin,
  thiamine hydrochloride, calcium pantothenate, biotin, folic acid,
  cyanocobalamin, and choline chloride.
- The `VITAMIN_SOURCE` role is source-backed by the same CultureBotHT database
  entry that defines this subject as a 1000X vitamin solution.
- The final SSSOM has exactly one exact local registry row for
  `MIM:Thauers_Vitamin_Mix`, points at
  `kgmicrobe.ingredient:thauers_vitamin_mix`, and leaves `other` empty.

## Completeness

- The local stock identity, exact registry row, component transcription,
  aggregate copy, occurrence count, and final SSSOM row agree.
- The stock has a complete 11-component decomposition and correctly has no
  chemical formula, CAS RN, or CHEBI parent.
- A fresh exact OLS4 search for the normalized full
  `Thauers vitamin mix no Biotin` label and for the `Thauers` token returned
  zero hits; apostrophe-bearing Thauer phrases triggered a raw query error in
  OLS4.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureBotHT import, local
  fallback promotion, aggregate, and final SSSOM rows.

## Recommended Edits

- None.
