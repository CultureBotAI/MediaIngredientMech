# `data/ingredients/mapped/Synthetic_Sea_Salts_(sss).yaml`

## Verdict

Needs curation - major. The local fallback row is synchronized and absent from
OLS and PubChem, but `Synthetic Sea Salts (sss)` is a sea-salt preparation
minted under `kgmicrobe.compound`; the record and final SSSOM should use
`kgmicrobe.ingredient` for this non-chemical mixture.

## Identity

- Reviewed record: `data/ingredients/mapped/Synthetic_Sea_Salts_(sss).yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:synthetic_sea_salts_sss` with the same
  `ontology_mapping.ontology_id`, label `Synthetic Sea Salts (sss)`, source
  `kgmicrobe.compound`, `mapping_quality: FALLBACK_REGISTRY`, and
  `mapping_status: MAPPED`.
- Occurrences: zero CultureMech recipe occurrences and 1 MicrobeDecoder
  metabolite-utilization row.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Synergistin_A` through `TAPS_Sodium_Salt`: exited 0 and wrote zero ERROR
  rows.
- Direct old Engine A/OBO term validation was skipped for this local
  `kgmicrobe.compound` fallback row because that prefix is intentionally
  outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `Synthetic Sea Salts (sss)` returned zero
  results, and fresh PubChem name lookup found no CID.
- `data/custom/microbedecoder/unmapped_labels.tsv` preserves the single
  MicrobeDecoder import for `kgmicrobe.trait:synthetic_sea_salts_sss`.
- Major: the local fallback uses `kgmicrobe.compound` even though synthetic sea
  salts are a mixture or commercial preparation, not a distinct simple
  compound. The final SSSOM reproduces that namespace in the exact registry
  row and `kgm:compound` object source.

## Completeness

- The local fallback identity, aggregate row, MicrobeDecoder source occurrence,
  and final SSSOM row agree mechanically.
- The namespace is materially wrong for the subject identity, and the record
  also lacks a mixture-oriented `ingredient_type`.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder,
  no-ontology fallback, aggregate, alias, generated index, and final SSSOM
  rows; the encoded `MIM:Synthetic_Sea_Salts_~28sss~29` subject is the expected
  SSSOM subject for this parenthesized filename.

## Recommended Edits

- Major: remint this record from `kgmicrobe.compound` to
  `kgmicrobe.ingredient` in
  `data/ingredients/mapped/Synthetic_Sea_Salts_(sss).yaml` and assign the
  mixture or stock-solution classification supported by the source.
- Major: regenerate `mappings/ingredient_mappings.sssom.tsv` and generated docs
  so the final exact registry row uses `kgmicrobe.ingredient` and
  `kgm:ingredient`, not `kgmicrobe.compound` and `kgm:compound`.
