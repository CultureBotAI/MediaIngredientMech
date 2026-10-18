# `data/ingredients/mapped/Tetrakis_Hydroxymethylphosphonium_Sulfate.yaml`

## Verdict

Pass. The CAS fallback identity, PubChem structure, THPS synonym, aggregate row,
and final exact CAS registry row for tetrakis(hydroxymethyl)phosphonium sulfate
are synchronized and do not leak unsafe synonym payload.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Tetrakis_Hydroxymethylphosphonium_Sulfate.yaml`.
- Identifier and grounding: `identifier: cas:55566-30-8` with the same
  `ontology_mapping.ontology_id`, label
  `Tetrakis(hydroxymethyl)phosphonium sulfate`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `55566-30-8`, PubChem CID 41478, formula
  `C8H24O12P2S`, and matching PubChem InChI/SMILES.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tetracycline` through `Tetramethyl_Ammonium_Chloride`: exited 0 and wrote
  zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this CAS fallback row
  because registry CURIEs are intentionally outside the CHEBI-focused OBO term
  subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for
  `Tetrakis(hydroxymethyl)phosphonium sulfate` returned only the broader MeSH
  `Pyroset TKP` supplementary concept, whose related synonyms span several
  tetrakis(hydroxymethyl)phosphonium salts.
- Fresh PubChem lookup by CAS `55566-30-8` resolves CID 41478, confirms the
  stored `C8H24O12P2S` formula and InChI, and lists both CAS `55566-30-8` and
  `THPS`.
- The final SSSOM has exactly one exact CAS registry row for
  `MIM:Tetrakis_Hydroxymethylphosphonium_Sulfate`, points at
  `cas:55566-30-8`, names `registry:cas`, and publishes only `THPS` plus
  `CAS:55566-30-8` in `other`.

## Completeness

- The CAS identity, PubChem structure, THPS synonym, aggregate row, and final
  SSSOM row agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT fallback,
  PubChem backfill, aggregate, row-review, final SSSOM, and alias rows.

## Recommended Edits

- None.
